## Wed — Model catalog, deployment & evaluation basics

### Reading / Resource
- **Select, deploy, and evaluate Microsoft Foundry models** (Microsoft Learn, 8 units)
  https://learn.microsoft.com/en-us/training/modules/model-catalog-evaluate/

### Citation
> Select, deploy, and evaluate Microsoft Foundry models — https://learn.microsoft.com/en-us/training/modules/model-catalog-evaluate/
> Used for: deploying a second model into Tuesday's Foundry project, then comparing both against benchmarks.

### What I learned
Before this, "evaluate a model" was an abstract phrase to me. Actually doing it made me realize evaluation isn't one number; it's quality, safety, cost, and performance as separate concerns, and a model can win on one and lose on another. That's why you deploy more than one: picking a model isn't "which is smartest," it's "which tradeoff fits what I'm building." Benchmarks turned out to be the fast, cheap first filter, so that you use them before you burn real usage testing a model by hand.
