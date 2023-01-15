import pytest
from fastapi.testclient import TestClient
from app import app
from img_preprocess import img_transform
from cnn import model
import torch
from PIL import Image


client = TestClient(app)
fpath = "./chest_xray/test/NORMAL/IM-0013-0001.jpeg"


def test_responsiveness():
    with open(fpath, "rb") as f:
        file = {'img': ('IM-0013-0001.jpeg', f, 'image/jpeg')}

        response = client.post("/upload_image", files=file, headers={"Accept": "application/json"})
    # print(response.content)
    assert response.status_code == 200
    assert "Answer" in response.json()


def test_img_transform():
    img = Image.new('RGB', (100, 100), color=(73, 109, 137))
    preprocessed_img = img_transform(img)
    assert preprocessed_img.shape == (1, 128, 128)


def test_cnn():
    input_tensor = torch.rand(1, 1, 128, 128)
    output = model(input_tensor)
    assert output.shape == (1, 2)
