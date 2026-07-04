---
title: "Cost-Aware Scheduling of GPU Inference Workloads Across Heterogeneous Accelerator Pools"
inventors:
  - "gadsosa"
  - "K. S. Lee"
  - "R. M. Patel"
number: "US11,847,293 B2"
filing_date: 2022-03-14
issue_date: 2023-12-19
abstract: "A scheduling system for machine learning inference workloads that selects among heterogeneous GPU pools based on predicted latency, cost per inference, and queue depth. The system uses a lightweight performance model trained on historical traces to route requests to the cheapest accelerator that can meet a user-defined service-level objective, reducing average inference cost by up to 28% in evaluated production traces."
link: "https://patents.google.com/patent/US11847293B2/"
---

# Cost-Aware Scheduling of GPU Inference Workloads Across Heterogeneous Accelerator Pools

**US Patent 11,847,293 B2**  
**Inventors:** gadsosa, K. S. Lee, R. M. Patel  
**Filed:** March 14, 2022  
**Issued:** December 19, 2023

[Google Patents](https://patents.google.com/patent/US11847293B2/)

## Abstract

A scheduling system for machine learning inference workloads that selects among heterogeneous GPU pools based on predicted latency, cost per inference, and queue depth. The system uses a lightweight performance model trained on historical traces to route requests to the cheapest accelerator that can meet a user-defined service-level objective, reducing average inference cost by up to 28% in evaluated production traces.

## Claims overview

- Predicts per-request latency on multiple accelerator types using a lightweight surrogate model.
- Routes requests to the lowest-cost pool that satisfies the latency SLO.
- Rebalances queues dynamically based on observed error rates and cold-start behavior.
