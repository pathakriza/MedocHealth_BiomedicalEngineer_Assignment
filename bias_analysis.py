def analyze_class_distribution(metadata, condition_list):
    distribution = {}

    for condition in condition_list:
        distribution[condition] = metadata[condition].sum()

    return distribution


def detect_bias(distribution):
    max_class = max(distribution.values())
    biases = {}

    for cls, count in distribution.items():
        if count < 0.2 * max_class:
            biases[cls] = "Underrepresented"

    return biases
