#!/usr/bin/env python3
"""Generate the main README.md index from essays, influential papers, and talks."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_START = "<!-- INDEX_START -->"
INDEX_END = "<!-- INDEX_END -->"


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        return value[1:-1]
    return value


def _parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1]
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

        list_match = re.match(r"^[ \t]+-\s+(.*)$", line)
        if list_match and key is not None and not value_lines:
            in_list = True
            list_items.append(_strip_quotes(list_match.group(1).strip()))
            continue

        if key is not None and not in_list:
            value_lines.append(line)

    flush()
    return data


def collect_entries(directory: Path) -> list[tuple[Path, dict]]:
    """Collect markdown files with YAML frontmatter, skipping templates and READMEs."""
    entries = []
    if not directory.exists():
        return entries
    for path in sorted(directory.rglob("*.md")):
        if path.name.lower() in ("template.md", "readme.md"):
            continue
        fm = parse_frontmatter(path)
        if fm:
            entries.append((path, fm))
    return entries


def collect_essays(directory: Path) -> list[Path]:
    """Collect essay markdown files without requiring YAML frontmatter."""
    essays = []
    if not directory.exists():
        return essays
    for path in sorted(directory.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        essays.append(path)
    return essays


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def _normalize_title(title: str) -> str:
    title = title.strip()
    if title.startswith("[") and title.endswith("]"):
        title = title[1:-1]
    return title


def build_influential_papers_section(entries: list[tuple[Path, dict]]) -> str:
    lines = [
        "## Influential Papers",
        "",
        "Papers by others that shaped how I think about production ML, platform engineering, and ML security.",
        "",
        "| Year | Title | Authors | Why it matters |",
        "|------|-------|---------|----------------|",
    ]
    if not entries:
        lines.append("| - | - | - | - |")
    for path, fm in entries:
        title = _normalize_title(fm.get("title", "[Title]"))
        year = fm.get("year", "YYYY")
        authors = ", ".join(fm["authors"]) if isinstance(fm.get("authors"), list) else fm.get("authors", "[Authors]")
        why = fm.get("why_it_matters", "")
        if len(why) > 120:
            why = why[:117] + "..."
        lines.append(f"| {year} | [{title}]({rel(path)}) | {authors} | {why} |")
    lines.append("")
    return "\n".join(lines)


def build_influential_talks_section(entries: list[tuple[Path, dict]]) -> str:
    lines = [
        "## Influential Talks",
        "",
        "Talks, courses, and lectures by others that I return to regularly.",
        "",
        "| Year | Title | Speaker | Why it matters |",
        "|------|-------|---------|----------------|",
    ]
    if not entries:
        lines.append("| - | - | - | - |")
    for path, fm in entries:
        title = _normalize_title(fm.get("title", "[Title]"))
        year = fm.get("year", "YYYY")
        speaker = fm.get("speaker", "[Speaker]")
        why = fm.get("why_it_matters", "")
        if len(why) > 120:
            why = why[:117] + "..."
        lines.append(f"| {year} | [{title}]({rel(path)}) | {speaker} | {why} |")
    lines.append("")
    return "\n".join(lines)


def _essay_title(path: Path) -> str:
    """Use the first Markdown H1 heading as the essay title, if available."""
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def build_essays_section(essays: list[Path]) -> str:
    lines = [
        "## Essays",
        "",
        "Original thought leadership on production ML, ML leadership, and startup R&D.",
        "",
        "| Title |",
        "|-------|",
    ]
    if not essays:
        lines.append("| - |")
    for path in essays:
        title = _essay_title(path)
        lines.append(f"| [{title}]({rel(path)}) |")
    lines.append("")
    return "\n".join(lines)


def _abstract_focus(path: Path) -> str:
    """Extract the focus line from a talk abstract, if present."""
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## Focus\s*\n+(.+?)$", text, re.MULTILINE | re.DOTALL)
    if match:
        focus = " ".join(match.group(1).split())
        if len(focus) > 100:
            focus = focus[:97] + "..."
        return focus
    return ""


def build_talk_abstracts_section(abstracts: list[Path]) -> str:
    lines = [
        "## Talk Abstracts",
        "",
        "Ready-to-submit abstracts for conference talks and keynotes.",
        "",
        "| Title | Focus |",
        "|-------|-------|",
    ]
    if not abstracts:
        lines.append("| - | - |")
    for path in abstracts:
        title = _essay_title(path)
        focus = _abstract_focus(path)
        lines.append(f"| [{title}]({rel(path)}) | {focus} |")
    lines.append("")
    return "\n".join(lines)


def generate_index() -> str:
    essays = collect_essays(ROOT / "essays")
    abstracts = collect_essays(ROOT / "talks" / "abstracts")
    papers = collect_entries(ROOT / "influential-papers")
    talks = collect_entries(ROOT / "influential-talks")

    sections = []
    if essays:
        sections.append(build_essays_section(essays))
    if abstracts:
        sections.append(build_talk_abstracts_section(abstracts))
    if papers:
        sections.append(build_influential_papers_section(papers))
    if talks:
        sections.append(build_influential_talks_section(talks))

    if not sections:
        return f"{INDEX_START}\n\n_No entries yet._\n\n{INDEX_END}"

    return f"{INDEX_START}\n\n" + "\n".join(sections) + f"{INDEX_END}"


def update_readme() -> None:
    readme_path = ROOT / "README.md"
    new_index = generate_index()

    content = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

    pattern = re.compile(re.escape(INDEX_START) + ".*?" + re.escape(INDEX_END), re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(new_index, content)
    else:
        if content and not content.endswith("\n"):
            content += "\n"
        content += new_index + "\n"

    readme_path.write_text(content, encoding="utf-8")
    print("README.md index regenerated.")


if __name__ == "__main__":
    update_readme()
