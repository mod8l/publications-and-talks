# Publications and Talks

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![CI](https://github.com/gadsosa/publications-and-talks/actions/workflows/ci.yml/badge.svg)](https://github.com/gadsosa/publications-and-talks/actions/workflows/ci.yml)

A curated professional portfolio of papers, patents, talks, and media appearances.

<!-- INDEX_START -->

## Papers

| Year | Title | Authors | Venue | Links |
|------|-------|---------|-------|-------|
| 2021 | [Streaming Feature Stores for Real-Time Recommendation Systems](papers/2021-recsys/README.md) | gadsosa, A. R. Chen, M. J. Okafor | Proceedings of the 15th ACM Conference on Recommender Systems (RecSys 2021) | [Paper](papers/2021-recsys/README.md), [DOI](https://doi.org/10.1145/3460231.3474233), [Link](https://dl.acm.org/doi/10.1145/3460231.3474233) |
| 2023 | [Adversarial Robustness of Production Computer Vision Pipelines](papers/2023-neurips-mlsys/README.md) | gadsosa, L. Petrov, S. Nakamura | NeurIPS 2023 Workshop on Machine Learning Systems | [Paper](papers/2023-neurips-mlsys/README.md), [Link](https://arxiv.org/abs/2312.04567) |

## Patents

| Filing Date | Title | Inventors | Number | Links |
|-------------|-------|-----------|--------|-------|
| 2022-03-14 | [Cost-Aware Scheduling of GPU Inference Workloads Across Heterogeneous Accelerator Pools](patents/2022-gpu-scheduling/README.md) | gadsosa, K. S. Lee, R. M. Patel | US11,847,293 B2 | [Details](patents/2022-gpu-scheduling/README.md), [Record](https://patents.google.com/patent/US11847293B2/) |

## Talks

| Date | Title | Event | Location | Resources |
|------|-------|-------|----------|-----------|
| 2023-11-08 | [From Notebook to Kubernetes: A Field Guide for ML Engineers](talks/2023-11-notebook-to-kubernetes/README.md) | MLOps World | Austin, TX | [Slides](https://speakerdeck.com/gadsosa/notebook-to-kubernetes) |
| 2024-09-18 | [Building ML Platforms That Don't Fall Over at 3 AM](talks/2024-09-ml-platforms/README.md) | QCon San Francisco | San Francisco, CA | [Slides](https://speakerdeck.com/gadsosa/ml-platforms-3am), [Recording](https://www.infoq.com/presentations/ml-platforms-reliability/) |
| 2025-03-12 | [Secure ML: A Checklist for Skeptical Engineers](talks/2025-03-secure-ml/README.md) | KubeCon + CloudNativeCon Europe | London, UK | [Slides](https://speakerdeck.com/gadsosa/secure-ml-checklist), [Recording](https://www.youtube.com/watch?v=example-secure-ml) |
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
