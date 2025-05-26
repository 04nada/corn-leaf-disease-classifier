import keras
import numpy as np
import matplotlib.pyplot as plt
from natsort import natsorted
from numpy._typing._array_like import NDArray
from pathlib import Path
from PIL import Image, ImageEnhance
from typing import Any
import pickle

IMAGE_SIZE: tuple[int, int] = (64, 64)
IMAGE_SUFFIXES: set[str] = {'.jpeg', '.jpg', '.png'}

def load_image_from_path(image_path: Path) -> list[int]:
    image: Image.Image = Image.open(image_path).convert('RGB').resize(IMAGE_SIZE)
    image = ImageEnhance.Color(image).enhance(2.0)

    image_flat: NDArray[Any] = np.asarray(image, dtype="int64").flatten()

    ret: list[int] = [int(i) for i in image_flat]
    return ret

MODEL_PATH: Path = Path.cwd() / 'model.keras'
model = keras.saving.load_model(MODEL_PATH)

def predict_image(image_path: Path) -> str:
    image_raw: list[int] = load_image_from_path(image_path)
    image: NDArray[Any] = np.array(image_raw).reshape(1, IMAGE_SIZE[0], IMAGE_SIZE[1], 3)

    pred = model.predict(image)
    pred_class = np.argmax(pred, axis = 1) 
    prediction: list[str] = [['Blight', 'Common_Rust', 'Gray_Leaf_Spot', 'Healthy'][i] for i in pred_class]

    return prediction[0]

print(predict_image('0.jpeg'))

