from PIL import Image

def check_image_quality(image_path, min_resolution):
    try:
        img = Image.open(image_path)
        return img.size[0] >= min_resolution[0] and img.size[1] >= min_resolution[1]
    except:
        return False


def filter_xray_images(images, metadata, config):
    usable = []
    rejected = []

    for img_path in images:
        image_name = img_path.split("/")[-1]
        row = metadata[metadata["Image"] == image_name]

        if row.empty:
            rejected.append((img_path, "Missing metadata"))
            continue

        if row["View Position"].values[0] not in config["ACCEPTABLE_VIEWS"]:
            rejected.append((img_path, "Invalid view"))
            continue

        if not check_image_quality(img_path, config["MIN_IMAGE_RESOLUTION"]):
            rejected.append((img_path, "Low image quality"))
            continue

        usable.append(img_path)

    return usable, rejected
