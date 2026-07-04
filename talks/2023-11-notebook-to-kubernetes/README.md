---
title: "From Notebook to Kubernetes: A Field Guide for ML Engineers"
date: 2023-11-08
event: MLOps World
location: Austin, TX
slides_link: https://speakerdeck.com/gadsosa/notebook-to-kubernetes
recording_link: ""
tags: [mlops, kubernetes, reproducibility, platform-engineering]
---

# From Notebook to Kubernetes: A Field Guide for ML Engineers

**MLOps World — November 8, 2023**

## Abstract

The hardest part of production ML is rarely the model. It is the handoff between the notebook where the model was born and the system where it will live. This talk is a field guide for that handoff, built from years of untangling experiments into services.

I discuss containerization choices that preserve reproducibility without inflating image size, how to version data and code together, and why every production model needs a retirement plan before it gets a traffic route. The talk includes a worked example of taking a PyTorch training notebook and turning it into a reproducible training job, a model registry entry, and a canaried inference deployment.

## Key takeaways

- Reproducibility starts with dependency pinning and ends with data lineage.
- A model registry is a contract between research and production, not a storage dump.
- Canary deployments for ML should compare distributions, not just error rates.
- Every model should have an owner, a deprecation date, and a rollback path.

## Resources

- [Slides](https://speakerdeck.com/gadsosa/notebook-to-kubernetes)
