
# FERET Dataset Setup

## Getting Started

### Step 1: Download the FERET Dataset

Please download the FERET Dataset into this folder. The dataset can be found at the following URL:

[Color FERET Database](https://www.nist.gov/itl/products-and-services/color-feret-database)

### Step 2: Image Alignment Using MTCNN

After downloading the dataset, apply the MTCNN function to align the images. Ensure you have the `facenet_pytorch` and `PIL` libraries installed. You can install these with pip if needed:

```bash
pip install facenet-pytorch pillow
```


### Step 3: Apply MTCNN
Use the following Python script to process the images using MTCNN for alignment:
```import os
from facenet_pytorch import MTCNN
from PIL import Image

# Initialize MTCNN
mtcnn = MTCNN(image_size=512, margin=15)

# List all files in the current directory
files = os.listdir('.')

# Process each image
for file in files:
    if file.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        img = Image.open(file)
        img_cropped = mtcnn(img, save_path=f'mtcnn_{file}')
