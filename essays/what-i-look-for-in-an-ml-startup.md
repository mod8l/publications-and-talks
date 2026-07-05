# What I Look for in an ML Startup

When I advise founders or join a startup as VP R&D, I do not start with the
model architecture. I start with the signal. A startup can have a beautiful
paper, a slick demo, and a Nobel laureate on the advisory board, and still die
six months later because it cannot ship, cannot keep data, or cannot tell the
difference between a research milestone and a customer outcome.

Over the years I have developed a short list of signals that predict whether an
ML startup will become a real product company or a slide deck with a GPU bill.
Here is what I look for.

## Shipping velocity beats model novelty

The first question I ask is not "What model do you use?" It is "When was the
last time a customer saw value from something you built?" The best ML teams I
have worked with ship weekly, sometimes daily. They are not shipping models;
they are shipping decisions, alerts, recommendations, and automations that make
a user better at their job.

If a team cannot point to a production change in the last two weeks, I get
suspicious. It usually means the engineering loop is broken somewhere: data
access, deployment pipelines, review processes, or a founder who keeps moving
the goalposts. Startups do not die from a lack of intelligence. They die from a
lack of feedback.

I also look at the demo-to-deployment ratio. A company that has twenty demo
videos and two paying customers is a creative studio, not a product company.
Demos are fine. Demos are necessary. But a demo that never gets deployed is a
liability. It teaches the team to optimize for applause instead of outcomes.

## Data rights are a moat, not a footnote

The next thing I dig into is data. Not the size of the corpus, but the rights
around it. Can the startup use the data to train models? Can they use it for
product improvement? Can they keep it if the customer churns? Can they
aggregate patterns across customers without violating contracts?

I have seen brilliant teams build on data they were never allowed to
commercialize. I have seen others sign enterprise deals that quietly granted the
customer ownership of every derivative work. These mistakes are expensive and
often irreversible. If the startup does not have a clear, written data-rights
framework reviewed by someone who understands ML, I treat that as a blocker.

Beyond rights, I look at data discipline. Is there lineage? Is there a process
for labeling? Is there someone who owns data quality the way an engineer owns
uptime? Data is not oil. Data is a garden. It needs weeding, tracking, and
someone who cares when it changes.

## Team composition is destiny

The composition of the early ML team tells me almost everything I need to know.
A room full of PhDs with no production engineers will build beautiful
experiments that break the first time the real world coughs. A room full of
platform engineers with no ML depth will ship fast, accurate pipelines for
models that do not matter.

What I want to see is a mix: one or two people who understand the science
deeply, and at least one person who has carried a pager for a production
system. Ideally those people respect each other. Ideally they can write code in
the same repository.

I also watch for title inflation. A team of six people with four "Heads of AI"
is usually a warning sign. It suggests politics, unclear ownership, and a
hiring process optimized for LinkedIn rather than outcomes. Startups need
owners, not ornaments.

## First SLOs reveal maturity

Finally, I ask about service-level objectives. Not SLAs. SLOs. What latency is
acceptable? What error rate? What drift threshold triggers an investigation?
How do you know the model is getting worse before the customer does?

A team that cannot answer these questions is not ready to scale. They may be
ready to experiment, but scaling experiments is how you scale your AWS bill,
not your business. The startups that impress me are the ones that treat model
behavior as a system property, not a research result. They know their p95,
their retraining cadence, and their rollback plan.

## The bottom line

A startup can fix many things: pricing, positioning, even product direction.
But it is hard to fix a culture that confuses publication with progress, or a
team that has never shipped under load. When I evaluate an ML startup, I am
looking for evidence that the founders understand the difference between a
model that works in a notebook and a system that works in a customer's life.

That difference is what separates an AI startup from an AI hobby.
