def assess_dataset_authenticity(dataset_config, metadata=None):
    assessment = {}

    assessment["Source Credibility"] = dataset_config["source"]
    assessment["Modality"] = dataset_config["modality"]

    if metadata is not None:
        assessment["Dataset Size"] = len(metadata)
        assessment["Missing Labels (%)"] = (
            metadata.isnull().mean().mean() * 100
        )
    else:
        assessment["Dataset Size"] = "Signal-based dataset"

    assessment["Ethics"] = {
        "De-identified": True,
        "Consent": "Public research dataset",
        "HIPAA/GDPR Risk": "Low"
    }

    assessment["Known Limitations"] = [
        "Class imbalance",
        "Single-center bias",
        "Label uncertainty"
    ]

    return assessment
