import torch
import torch.nn as nn


class ModelDropoutNorm(nn.Module):
    """Adding batch_normalization and dropout to previous model to see how it influences the training"""

    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Conv2d(1, 12, kernel_size=3, padding=1, padding_mode="zeros"),

            nn.ReLU(),

            nn.Conv2d(12, 48, kernel_size=3, padding=1, padding_mode="zeros"),
            nn.BatchNorm2d(48),
            nn.ReLU(),

            nn.MaxPool2d(2, 2),

            nn.Conv2d(48, 128, kernel_size=3, padding=1, padding_mode="zeros"),

            nn.ReLU(),

            nn.Conv2d(128, 128, kernel_size=3, padding=1, padding_mode="zeros"),
            nn.BatchNorm2d(128),
            nn.ReLU(),

            nn.MaxPool2d(2, 2),

            nn.Conv2d(128, 256, kernel_size=3, padding=1, padding_mode="zeros"),

            nn.ReLU(),

            nn.Conv2d(256, 256, kernel_size=3, padding=1, padding_mode="zeros"),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.MaxPool2d(2, 2),

            nn.Flatten(),
            nn.Linear(256 * 16 * 16, 2048),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(2048, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 2))

    def forward(self, xb):
        return self.network(xb)


model = ModelDropoutNorm()
state_dict = torch.load('third-model.pt')
model.load_state_dict(state_dict)
model.eval()
