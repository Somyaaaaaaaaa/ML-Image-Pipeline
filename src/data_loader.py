import os
import cv2

# print("RUNNING DATA_LOADER FROM:", __file__)


def load_data(data_dir=None):
    # print("FILE LOCATION:", os.path.abspath(__file__))
    # print("CURRENT WORKING DIRECTORY:", os.getcwd())

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print("BASE DIR:", base_dir)

    if data_dir is None:
        data_dir = os.path.join(base_dir, "data", "images")

    # print("DATA DIR USED:", data_dir)

    images = []
    labels = []

    for label_name in os.listdir(data_dir):
        label_path = os.path.join(data_dir, label_name)
        # print("FOUND LABEL DIR:", label_path)

        if not os.path.isdir(label_path):
            # print("SKIPPED (not dir):", label_path)
            continue

        for file in os.listdir(label_path):
            file_path = os.path.join(label_path, file)
            # print("  TRYING FILE:", file_path)

            img = cv2.imread(file_path)

            if img is None:
                print("  FAILED TO READ:", file_path)
                continue

            # print("  READ OK:", file_path)
            images.append(img)
            labels.append(label_name)

    print(f"Loaded {len(images)} images.")
    return images, labels
