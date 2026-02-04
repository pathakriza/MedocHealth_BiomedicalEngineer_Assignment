def chest_xray_label_schema():
    return {
        "Primary Labels": {
            "Pneumonia": "Infectious lung opacity",
            "Effusion": "Pleural fluid accumulation",
            "Cardiomegaly": "Enlarged cardiac silhouette",
            "Pneumothorax": "Collapsed lung"
        },
        "Severity": ["Mild", "Moderate", "Severe", "Uncertain"],
        "Metadata": [
            "Age", "Sex", "View Position",
            "Machine Vendor", "Acquisition Setting"
        ]
    }


def excluded_labels():
    return [
        "Hospital Name",
        "Patient ID",
        "Technician Notes"
    ]
