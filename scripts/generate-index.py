#!/usr/bin/env python3
"""Generate the main README.md index from publication and talk entries."""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_START = "<!-- INDEX_START -->"
INDEX_END = "<!-- INDEX_END -->"


def _strip_quotes(value: str) -> str:
    """Remove matching surrounding quotes from a scalar value."""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        return value[1:-1]
    return value


def _parse_inline_list(value: str) -> list[str]:
    """Parse a '["a", "b"]' or '[a, b]' style inline list."""
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1]
        # Split on commas not inside quotes
        items = re.split(r",\s*(?=(?:[^'\"]*['\"][^'\"]*['\"])*[^'\"]*$)", inner)
        return [_strip_quotes(item) for item in items if item.strip()]
    return []


def parse_frontmatter(path: Path) -> dict:
    """Parse a simple YAML frontmatter block from a Markdown file."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}

    fm = match.group(1)
    data: dict[str, str | list] = {}
    key = None
    value_lines: list[str] = []
    list_items: list[str] = []
    in_list = False

    def flush():
        nonlocal key, value_lines, list_items, in_list
        if key is None:
            return
        if in_list and list_items:
            data[key] = list_items
        elif value_lines:
            value = "\n".join(value_lines).strip()
            inline = _parse_inline_list(value)
            data[key] = inline if inline else _strip_quotes(value)
        else:
            data[key] = ""
        key = None
        value_lines = []
        list_items = []
        in_list = False

    for line in fm.splitlines():
        # New top-level key (no leading whitespace)
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            flush()
            key = m.group(1)
            rest = m.group(2).strip()
            if rest:
                value_lines.append(rest)
                inline = _parse_inline_list(rest)
                if inline:
                    data[key] = inline
                    key = None
                    value_lines = []
            continue

        # List item under the current key
        list_match = re.match(r"^[ \t]+-\s+(.*)$", line)
        if list_match and key is not None and not value_lines:
            in_list = True
            list_items.append(_strip_quotes(list_match.group(1).strip()))
            continue

        # Continuation of a scalar value
        if key is not None and not in_list:
            value_lines.append(line)

    flush()
    return data


def collect_entries(directory: Path) -> list[tuple[Path, dict]]:
    """Collect all markdown files with YAML frontmatter under directory."""
    entries = []
    if not directory.exists():
        return entries
    for path in sorted(directory.rglob("*.md")):
        fm = parse_frontmatter(path)
        if fm:
            entries.append((path, fm))
    return entries


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def fmt_link(text: str, url: str) -> str:
    if not text or text == "-":
        return "-"
    return f"[{text}]({url})"


def build_talks_section(entries: list[tuple[Path, dict]]) -> str:
    lines = ["## Talks", "", "| Date | Title | Event | Location | Resources |", "|------|-------|-------|----------|-----------|"]
    if not entries:
        lines.append("| - | - | - | - | - |")
    for path, fm in entries:
        title = _normalize_title(fm.get("title", "[Title]"))
        date = fm.get("date", "YYYY-MM-DD")
        event = fm.get("event", "[Event]")
        location = fm.get("location", "[Location]")
        links = []
        if fm.get("slides_link"):
            links.append(fmt_link("Slides", fm["slides_link"]))
        if fm.get("recording_link"):
            links.append(fmt_link("Recording", fm["recording_link"]))
        resources = ", ".join(links) if links else "-"
        lines.append(f"| {date} | [{title}]({rel(path)}) | {event} | {location} | {resources} |")
    lines.append("")
    return "\n".join(lines)


def _normalize_title(title: str) -> str:
    """Avoid double square brackets when the title itself is placeholder-like."""
    title = title.strip()
    if title.startswith("[") and title.endswith("]"):
        title = title[1:-1]
    return title


def build_papers_section(entries: list[tuple[Path, dict]]) -> str:
    lines = ["## Papers", "", "| Year | Title | Authors | Venue | Links |", "|------|-------|---------|-------|-------|"]
    if not entries:
        lines.append("| - | - | - | - | - |")
    for path, fm in entries:
        title = _normalize_title(fm.get("title", "[Title]"))
        year = fm.get("year", "YYYY")
        authors = ", ".join(fm["authors"]) if isinstance(fm.get("authors"), list) else fm.get("authors", "[Authors]")
        venue = fm.get("venue", "[Venue]")
        links = [fmt_link("Paper", rel(path))]
        if fm.get("doi"):
            links.append(fmt_link("DOI", f"https://doi.org/{fm['doi']}"))
        if fm.get("link"):
            links.append(fmt_link("Link", fm["link"]))
        lines.append(f"| {year} | [{title}]({rel(path)}) | {authors} | {venue} | {', '.join(links)} |")
    lines.append("")
    return "\n".join(lines)


def build_patents_section(entries: list[tuple[Path, dict]]) -> str:
    lines = ["## Patents", "", "| Filing Date | Title | Inventors | Number | Links |", "|-------------|-------|-----------|--------|-------|"]
    if not entries:
        lines.append("| - | - | - | - | - |")
    for path, fm in entries:
        title = _normalize_title(fm.get("title", "[Title]"))
        filing = fm.get("filing_date", "YYYY-MM-DD")
        inventors = ", ".join(fm["inventors"]) if isinstance(fm.get("inventors"), list) else fm.get("inventors", "[Inventors]")
        number = fm.get("number", "[Number]")
        links = [fmt_link("Details", rel(path))]
        if fm.get("link"):
            links.append(fmt_link("Record", fm["link"]))
        lines.append(f"| {filing} | [{title}]({rel(path)}) | {inventors} | {number} | {', '.join(links)} |")
    lines.append("")
    return "\n".join(lines)


def generate_index() -> str:
    talks = collect_entries(ROOT / "talks")
    papers = collect_entries(ROOT / "papers")
    patents = collect_entries(ROOT / "patents")

    sections = []
    if papers:
        sections.append(build_papers_section(papers))
    if patents:
        sections.append(build_patents_section(patents))
    if talks:
        sections.append(build_talks_section(talks))

    if not sections:
        return f"{INDEX_START}\n\n_No entries yet._\n\n{INDEX_END}"

    return f"{INDEX_START}\n\n" + "\n".join(sections) + f"{INDEX_END}"


def update_readme() -> None:
    readme_path = ROOT / "README.md"
    new_index = generate_index()

    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
    else:
        content = ""

    pattern = re.compile(re.escape(INDEX_START) + ".*?" + re.escape(INDEX_END), re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(new_index, content)
    else:
        # Append if markers are missing
        if content and not content.endswith("\n"):
            content += "\n"
        content += new_index + "\n"

    readme_path.write_text(content, encoding="utf-8")
    print("README.md index regenerated.")


if __name__ == "__main__":
    update_readme()
