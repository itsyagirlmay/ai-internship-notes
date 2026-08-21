## Tue — Azure basics & first Foundry deployment

### Reading / Resource
- **Get started with AI in Azure** (Microsoft Learn, 8 units)
  https://learn.microsoft.com/en-us/training/modules/get-started-with-ai-in-azure/
- **Azure free trial sign-up**
  https://azure.microsoft.com/free/

### Citation
> Get started with AI in Azure — https://learn.microsoft.com/en-us/training/modules/get-started-with-ai-in-azure/
> Used for: creating the free trial account, setting a budget alert, and the module's own exercise — creating a Foundry project, deploying a model, and exploring multi-modal assets.

### What I learned
Foundry isn't a separate product I need to go find but it's the layer that sits on top of Azure once you're inside a project, and a "deployment" is really just giving a specific model version an endpoint I can call. The budget alert mattered more than I expected going in: it's not a formality, it's the thing that stops an experiment from quietly turning into a bill. The "multi-modal assets" part clicked once I saw it wasn't just chat models in the catalog because vision and speech models sit in the same place.

