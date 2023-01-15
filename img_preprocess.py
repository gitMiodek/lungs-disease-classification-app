import torch
from torchvision.transforms import transforms

IMG_SIZE = 128
MEAN = [0.5]
STD = [0.5]


def standardize(img: torch.tensor):
    img -= img.mean()
    img /= img.std()
    return img


img_transform = transforms.Compose([transforms.Resize((128, 128)),
                                    transforms.Grayscale(),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=MEAN, std=STD),
                                    standardize])
