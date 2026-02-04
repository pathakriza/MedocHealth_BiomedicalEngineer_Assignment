DATASETS = {
    "chest_xray": {
        "name": "NIH ChestX-ray14",
        "modality": "X-ray",
        "source": "NIH",
        "image_dir": "data/chest_xray/images",
        "labels_csv": "data/chest_xray/labels.csv",
        "conditions": [
            "Pneumonia", "Cardiomegaly", "Effusion",
            "Atelectasis", "Nodule", "Pneumothorax"
        ]
    },
    "ecg": {
        "name": "MIT-BIH Arrhythmia",
        "modality": "ECG",
        "source": "PhysioNet",
        "signal_dir": "data/ecg/signals",
        "annotations": "data/ecg/annotations.csv",
        "conditions": ["Normal", "AFib", "PVC", "LBBB", "RBBB"]
    }
}

MIN_IMAGE_RESOLUTION = (224, 224)
ACCEPTABLE_VIEWS = ["PA", "AP"]
MISSING_LABEL_THRESHOLD = 0.2
