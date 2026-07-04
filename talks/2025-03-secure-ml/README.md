---
title: "Secure ML: A Checklist for Skeptical Engineers"
date: 2025-03-12
event: KubeCon + CloudNativeCon Europe
location: London, UK
slides_link: https://speakerdeck.com/gadsosa/secure-ml-checklist
recording_link: https://www.youtube.com/watch?v=example-secure-ml
tags: [ml-security, supply-chain, kubernetes, adversarial-ml]
---

# Secure ML: A Checklist for Skeptical Engineers

**KubeCon + CloudNativeCon Europe — March 12, 2025**

## Abstract

Machine learning systems inherit every risk of traditional software and add a few of their own: training data can be poisoned, model weights can be extracted through APIs, and serialized artifacts can execute arbitrary code during deserialization. Security teams often don't know where models live, and ML teams often don't know what questions security is asking.

This talk presents a pragmatic checklist that bridges the gap. It covers data pipeline integrity, model provenance and signing, inference API abuse patterns, and the surprisingly subtle risks of third-party model hubs. Each control is mapped to a team that can own it, so the conversation moves from "is our ML secure?" to "these five gaps are owned by these three people."

## Key takeaways

- Model serialization formats are execution surfaces; scan and pin them like dependencies.
- API rate limits stop naive extraction, but adaptive defenses are needed for model stealing.
- Treat training data as a supply chain: know the source, version, and transformation lineage.
- Security and ML teams need a shared risk register, not a shared ticket queue.

## Resources

- [Slides](https://speakerdeck.com/gadsosa/secure-ml-checklist)
- [Recording](https://www.youtube.com/watch?v=example-secure-ml)
