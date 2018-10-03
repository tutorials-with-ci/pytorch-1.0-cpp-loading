# Copy from PyTorch Tutorial: https://pytorch.org/tutorials/advanced/cpp_export.html
# Copyright 2017, PyTorch.

import torch
import torchvision

# An instance of your model.
model = torchvision.models.resnet18()

# An example input you would normally provide to your model's forward() method.
example = torch.rand(1, 3, 224, 224)

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)

traced_script_module.save('model.pt')
