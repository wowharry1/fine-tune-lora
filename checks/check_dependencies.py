import torch
import transformers
import peft
import datasets
import accelerate
import numpy


print("Torch version:", torch.__version__)
print("Transformers version:", transformers.__version__)
print("PEFT version:", peft.__version__)
print("Datasets version:", datasets.__version__)
print("Accelerate version:", accelerate.__version__)
print("Numpy version:", numpy.__version__)