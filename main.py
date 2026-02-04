from config import DATASETS, MIN_IMAGE_RESOLUTION
from dataset_loader import load_xray_dataset
from authenticity_assessment import assess_dataset_authenticity
from labeling_schema import chest_xray_label_schema
from quality_control import filter_xray_images
from bias_analysis import analyze_class_distribution, detect_bias

def run_pipeline():
    print("=== Biomedical Dataset Pipeline ===\n")

    xray_config = DATASETS["chest_xray"]

    # Simulate data creation for demonstration since we don't have actual files
    # In a real scenario, these directories and files would exist.
    import os
    os.makedirs(xray_config["image_dir"], exist_ok=True)

    import pandas as pd
    from PIL import Image

    # Create a dummy labels.csv
    dummy_labels_data = {
        "Image": [f"image{i}.png" for i in range(10)],
        "Pneumonia": [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
        "Cardiomegaly": [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        "Effusion": [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        "Atelectasis": [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        "Nodule": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        "Pneumothorax": [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        "View Position": ["PA", "AP", "PA", "LAT", "AP", "PA", "PA", "AP", "LAT", "PA"],
        "Age": [30, 45, 60, 55, 70, 40, 50, 65, 35, 25],
        "Sex": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"]
    }
    dummy_labels_df = pd.DataFrame(dummy_labels_data)
    dummy_labels_df.to_csv(xray_config["labels_csv"], index=False)

    # Create dummy image files
    for i in range(10):
        # Create a blank image with resolution (224, 224) for the first 8, then smaller for the last 2
        if i < 8:
            img = Image.new('RGB', (224, 224), color = 'red')
        else:
            img = Image.new('RGB', (100, 100), color = 'blue')
        img.save(os.path.join(xray_config["image_dir"], f"image{i}.png"))

    images, metadata = load_xray_dataset(
        xray_config["image_dir"],
        xray_config["labels_csv"]
    )

    print("Authenticity Assessment:")
    print(assess_dataset_authenticity(xray_config, metadata), "\n")

    print("Labeling Framework:")
    print(chest_xray_label_schema(), "\n")

    usable, rejected = filter_xray_images(
        images, metadata,
        {
            "ACCEPTABLE_VIEWS": ["PA", "AP"],
            "MIN_IMAGE_RESOLUTION": MIN_IMAGE_RESOLUTION
        }
    )

    print(f"Usable samples: {len(usable)}")
    print(f"Rejected samples: {len(rejected)}\n")

    distribution = analyze_class_distribution(
        metadata, xray_config["conditions"]
    )

    print("Class Distribution:")
    print(distribution)

    print("\nBias Detection:")
    print(detect_bias(distribution))


if __name__ == "__main__":
    run_pipeline()



import subprocess

# Run the main.py script
result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)

# Print the standard output and error
print(result.stdout)
print(result.stderr)
