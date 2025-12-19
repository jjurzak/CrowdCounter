import os
import shutil

annotations_dir = r"F:\Programy\CrowdCounter\data\labels_mirrored"  # Original annotations directory
augmented_annotations_dir = r"F:\Programy\CrowdCounter\data\labels_augmentations_mirrroed"  # Output augmented annotations directory

if not os.path.exists(augmented_annotations_dir):
    os.makedirs(augmented_annotations_dir)


augmentations = [
    ("Original image", None),
    ("RGBShift", None),
    ("HueSaturationValue", None),
    ("ChannelShuffle", None),
    ("CLAHE", None),
    ("RandomContrast", None),
    ("RandomGamma", None),
    ("RandomBrightness", None),
    ("Blur", None),
    ("MedianBlur", None),
    ("ToGray", None),
    ("ImageCompression", None),
]

for idx, filename in enumerate(os.listdir(annotations_dir)):
    if filename.lower().endswith('.txt'):
        original_annotation_file = os.path.join(annotations_dir, filename)
        base_filename = filename.split('.')[0]  

        for title, _ in augmentations:
            new_annotation_filename = f"{base_filename}_mirrored_{title.replace(' ', '_')}.txt" if title != "Original image" else f"{base_filename}_mirrored_Original_image.txt"
            new_annotation_file_path = os.path.join(augmented_annotations_dir, new_annotation_filename)
            shutil.copy(original_annotation_file, new_annotation_file_path)
            print(f"Annotation copied to: {new_annotation_file_path}")
