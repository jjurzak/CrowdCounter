import os
import albumentations as A
import cv2

input_dir = r"F:\Programy\CrowdCounter\data\images_mirrored"
output_dir = r"F:\Programy\CrowdCounter\augumentation\augmented_output_mirrorred"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)


augmentations = [
    ("Original image", None),
    ("RGBShift", A.RGBShift(r_shift_limit=50, g_shift_limit=50, b_shift_limit=50, p=1.0)),
    ("HueSaturationValue", A.HueSaturationValue(hue_shift_limit=30, sat_shift_limit=50, val_shift_limit=50, p=1.0)),
    ("ChannelShuffle", A.ChannelShuffle(p=1.0)),
    ("CLAHE", A.CLAHE(clip_limit=2.0, tile_grid_size=(8, 8), p=1.0)),
    ("RandomContrast", A.RandomBrightnessContrast(brightness_limit=(-0.3, 0.5), contrast_limit=0, p=1.0)),
    ("RandomGamma", A.RandomGamma(gamma_limit=(80, 120), p=1.0)),
    ("RandomBrightness", A.RandomBrightnessContrast(brightness_limit=0.5, contrast_limit=0, p=1.0)),
    ("Blur", A.Blur(blur_limit=7, p=1.0)),
    ("MedianBlur", A.MedianBlur(blur_limit=7, p=1.0)),
    ("ToGray", A.ToGray(p=1.0)),
    ("ImageCompression", A.ImageCompression(quality_lower=30, quality_upper=50, p=1.0)),
]

for idx, filename in enumerate(os.listdir(input_dir)):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_dir, filename)

        image = cv2.imread(image_path)
        if image is None:
            print(f"Skipping {filename}, unable to load image.")
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        for title, aug in augmentations:
            if aug is None:
                transformed_image = image
            else:
                transformed_image = aug(image=image)["image"]

            transformed_image_bgr = cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR)

            augmented_filename = f"frame_{idx + 1:03d}_mirrored_{title.replace(' ', '_')}.jpg"
            output_path = os.path.join(output_dir, augmented_filename)

            cv2.imwrite(output_path, transformed_image_bgr)
            print(f"Saved: {output_path}")
