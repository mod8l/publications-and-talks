# Publications and Talks

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![CI](https://github.com/gadsosa/publications-and-talks/actions/workflows/ci.yml/badge.svg)](https://github.com/gadsosa/publications-and-talks/actions/workflows/ci.yml)

A reading list of the papers, talks, and resources that shaped how I think about production ML, platform engineering, and ML security — plus a template area for my own future publications and talks.

> **Note:** The influential papers and talks listed here are by other people. They are included with attribution because I reference them constantly in my work. My own publications and talks live (when they exist) in [`my-work/`](./my-work/).

<!-- INDEX_START -->

## Influential Papers

Papers by others that shaped how I think about production ML, platform engineering, and ML security.

| Year | Title | Authors | Why it matters |
|------|-------|---------|----------------|
| 2015 | [Hidden Technical Debt in Machine Learning Systems](influential-papers/2015-sculley-ml-technical-debt.md) | D. Sculley, G. Holt, D. Golovin, E. Davydov, T. Phillips, D. Ebner, V. Chaudhary, M. Young, J.-F. Crespo, D. Dennison | This is the paper I hand to engineers who think shipping a model is the finish line. It names the boundary erosion, e... |
| 2017 | [The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction](influential-papers/2017-breck-ml-test-score.md) | E. Breck, S. Cai, E. Nielsen, M. Salib, D. Sculley | The closest thing ML has to a production readiness checklist. I use its scoring logic as a starting point when I buil... |
| 2019 | [Software Engineering for Machine Learning: A Case Study](influential-papers/2019-amershi-se4ml.md) | S. Amershi, A. Begel, C. Bird, R. DeLine, H. Gall, E. Kamar, N. Nagappan, B. Nushi, T. Zimmermann | It captures the day-to-day reality of ML teams: version control, data management, and collaboration are harder than m... |
| 2021 | [OWASP Machine Learning Security Top 10](influential-papers/2021-owasp-ml-top-10.md) | OWASP Foundation | The most practical starting point for ML security conversations. It gives non-technical leaders a vocabulary and give... |

## Influential Talks

Talks, courses, and lectures by others that I return to regularly.

| Year | Title | Speaker | Why it matters |
|------|-------|---------|----------------|
| 2019 | [Machine Learning Systems Design](influential-talks/2019-huyen-ml-systems-design.md) | Chip Huyen | Chip Huyen is one of the clearest writers on the gap between research ML and production ML. Her framing of data, mode... |
| 2021 | [Designing Machine Learning Systems](influential-talks/2021-jordan-ml-infrastructure.md) | Jeremy Jordan | Jordan’s writing distills the invisible work of ML infrastructure: monitoring, feature platforms, and the feedback lo... |
| 2022 | [The Missing Link in AI: Production-Ready Machine Learning](influential-talks/2022-catanzaro-missing-link.md) | Sarah Catanzaro | Catanzaro makes the business case for ML infrastructure with unusual clarity. Her argument that model performance dec... |

## My Work

A place for my own papers, patents, and talks. Templates are provided in [`my-work/`](./my-work/); I will replace them with real entries as I publish them.

| Type | Status | Template |
|------|--------|----------|
| Papers | Empty | [`my-work/papers/template.md`](./my-work/papers/template.md) |
| Patents | Empty | [`my-work/patents/template.md`](./my-work/patents/template.md) |
| Talks | Empty | [`my-work/talks/template.md`](./my-work/talks/template.md) |
<!-- INDEX_END -->

## How to use this repo

- **Looking for what I read:** Browse [`influential-papers/`](./influential-papers/) and [`influential-talks/`](./influential-talks/).
- **Looking for my own work:** Check [`my-work/`](./my-work/) — it will be empty until I add real entries.
- **Media I follow:** See [`media/README.md`](./media/README.md).

## Adding an entry

1. For influential work: add a Markdown file with YAML frontmatter to `influential-papers/` or `influential-talks/`.
2. For my own work: copy a template from `my-work/` and fill it in.
3. Run `make index` to regenerate this README.
4. Review the diff before committing.

## License

Content in this repository is licensed under [CC-BY-4.0](./LICENSE), unless otherwise noted.
