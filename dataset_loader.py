import os
import pandas as pd
from PIL import Image

def load_xray_dataset(image_dir, labels_csv):
    images = []
    metadata = pd.read_csv(labels_csv)

    for img_name in metadata["Image"].values:
        img_path = os.path.join(image_dir, img_name)
        if os.path.exists(img_path):
            images.append(img_path)

    return images, metadata


def load_ecg_dataset(signal_dir, annotations_csv):
    signals = os.listdir(signal_dir)
    annotations = pd.read_csv(annotations_csv)
    return signals, annotations
