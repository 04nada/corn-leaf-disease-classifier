import numpy as np
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2hsv, hsv2rgb
from skimage.feature import hog
import joblib
import os
from tqdm import tqdm

# Settings
IMAGE_SIZE = (128, 128)    # resize images

model = joblib.load('svm_model.pkl')
le = joblib.load('label_encoder.pkl')

def preprocess_image(image_path, saturate=True, saturation_factor=2.0):
    img = imread(image_path)
    img = resize(img, IMAGE_SIZE, anti_aliasing=True)

    # convert B/W to RGB
    if img.ndim == 2:
        img = np.stack([img] * 3, axis=-1)

    # convert RGBA to RGB
    elif img.ndim == 3 and img.shape[-1] == 4:
        img = img[..., :3]


    if saturate:
        img_hsv = rgb2hsv(img)
        img_hsv[:, :, 1] = np.clip(img_hsv[:, :, 1] * saturation_factor, 0, 1)
        img = hsv2rgb(img_hsv)

    return img

def extract_hog_features(img):
    hog_feats = []
    for c in range(3):  # RGB
        feat = hog(img[..., c], orientations=9, pixels_per_cell=(8, 8),
                   cells_per_block=(2, 2), block_norm='L2-Hys')
        hog_feats.append(feat)
    return np.concatenate(hog_feats)

def predict_image(image_path):
    img = preprocess_image(image_path)
    features = extract_hog_features(img).reshape(1, -1)
    pred = model.predict(features)
    label = le.inverse_transform(pred)
    return label[0]

print(predict_image('0.jpeg'))