---
title: "Building ML Platforms That Don't Fall Over at 3 AM"
date: 2024-09-18
event: QCon San Francisco
location: San Francisco, CA
slides_link: https://speakerdeck.com/gadsosa/ml-platforms-3am
recording_link: https://www.infoq.com/presentations/ml-platforms-reliability/
tags: [ml-platforms, reliability, kubernetes, observability]
---

# Building ML Platforms That Don't Fall Over at 3 AM

**QCon San Francisco — September 18, 2024**

## Abstract

Most production ML failures look nothing like the papers. They look like a silent feature store lag, a model artifact that vanished from object storage, or a GPU node pool that scaled to zero during a traffic spike. This talk distills a decade of building and operating ML platforms into a set of practical defaults: small serving surfaces, deterministic rollouts, observability that treats models as software artifacts, and on-call runbooks that assume the model is the symptom, not the root cause.

I walk through three real incident archetypes — training-serving skew, cascading inference latency, and poisoned batch inputs — and show how platform design choices (feature stores, canary deployments, request/response logging, and model cards) either prevented or amplified each one. The goal is not to sell a specific tool, but to give teams a rubric for deciding what belongs in their own platform layer.

## Key takeaways

- Treat models as versioned artifacts with the same lifecycle expectations as services.
- Separate the control plane (scheduling, routing, rollback) from the inference plane.
- Invest in request/response logging before you invest in a model monitoring dashboard.
- Build runbooks that start with "which model version?" not "which model?".

## Resources

- [Slides](https://speakerdeck.com/gadsosa/ml-platforms-3am)
- [Recording](https://www.infoq.com/presentations/ml-platforms-reliability/)
