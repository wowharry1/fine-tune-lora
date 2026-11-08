import torch

print("Torch version is", torch.__version__)

print("CUDA Available:", torch.cuda.is_available())

print("GPU Name:", torch.cuda.get_device_name(0))

x = torch.rand(3, 3, device = 'cuda')

print(x, x.device)