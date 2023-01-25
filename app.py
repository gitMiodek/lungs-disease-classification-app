from cnn import model
from img_preprocess import img_transform
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
import torch.nn.functional as F
import torch

app = FastAPI()

@app.get("/")
async def index():
    html = """
           <!DOCTYPE html>
           <html>
           <head>
               <title>Upload Image</title>
           </head>
           <body>
               <h1>Upload Image</h1>
               <form method="post" enctype="multipart/form-data" action="/upload_image">
                   <input type="file" name="img" id="img">
                   <input type="submit" value="Upload">
               </form>
           </body>
           </html>
       """
    return HTMLResponse(content=html)

@app.post('/upload_image')
async def predict_image(img: UploadFile = File(...)):
    loaded_img = Image.open(img.file)
    preprocessed_img = img_transform(loaded_img)
    output = model(preprocessed_img.unsqueeze(0))
    y = F.softmax(output, dim=1)
    probability, label = torch.max(y, dim=1)
    if label.item() == 0:
        statement = f" I am {probability.item() * 100:.1f}% sure that your lungs are healthy!"
    else:
        statement = f"I am {probability.item() * 100:.1f}% sure that you have pneumonia :("
    return {
            'Answer': statement
    }
