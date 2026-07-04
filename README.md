# Publications and Talks

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![CI](https://github.com/gadsosa/publications-and-talks/actions/workflows/ci.yml/badge.svg)](https://github.com/gadsosa/publications-and-talks/actions/workflows/ci.yml)

A curated professional portfolio of papers, patents, talks, and media appearances.

<!-- INDEX_START -->

## Papers

| Year | Title | Authors | Venue | Links |
|------|-------|---------|-------|-------|
| YYYY | [Title of your paper](papers/template.md) | [Your Name], [Co-author Name] | [Venue or journal name] | [Paper](papers/template.md), [DOI](https://doi.org/[DOI or leave blank]), [Link]([URL to paper or preprint]) |

## Patents

| Filing Date | Title | Inventors | Number | Links |
|-------------|-------|-----------|--------|-------|
| YYYY-MM-DD | [Title of your patent](patents/template.md) | [Your Name], [Co-inventor Name] | [Patent number or application number] | [Details](patents/template.md), [Record]([URL to patent office record]) |

## Talks

| Date | Title | Event | Location | Resources |
|------|-------|-------|----------|-----------|
| 2024-09-XX | [Title of your talk on ML platforms](talks/2024-09-ml-platforms/README.md) | [Conference or meetup name] | [City, Country or virtual] | [Slides]([URL to slides]), [Recording]([URL to recording]) |
| 2025-03-XX | [Title of your talk on secure ML](talks/2025-03-secure-ml/README.md) | [Conference or meetup name] | [City, Country or virtual] | [Slides]([URL to slides]), [Recording]([URL to recording]) |
<!-- INDEX_END -->

## About this repository

This repository is a living record of public work. Entries are organized into:

- [`papers/`](./papers/) — Peer-reviewed papers, preprints, and technical publications.
- [`patents/`](./patents/) — Patents and patent applications.
- [`talks/`](./talks/) — Conference talks, keynotes, workshops, and meetup presentations.
- [`media/`](./media/) — Podcasts, panels, interviews, and other media appearances.

## Adding a new entry

1. Use the template in the relevant directory:
   - [`papers/template.md`](./papers/template.md)
   - [`patents/template.md`](./patents/template.md)
   - An existing talk entry under [`talks/`](./talks/)
2. Fill in the YAML frontmatter and any supporting details.
3. Run `make index` to regenerate this README.
4. Review the diff before committing.

## License

Content in this repository is licensed under [CC-BY-4.0](./LICENSE), unless otherwise noted.
