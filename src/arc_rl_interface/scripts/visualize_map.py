#!/usr/bin/env python3

import matplotlib.pyplot as plt
import yaml
import os
import cv2
import numpy as np

# Load the map.yaml file
script_dir = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.normpath(
    os.path.join(script_dir, "..", "src" ,"arc_rl_interface" ,"arc_rl_interface", "maps", "map_minicity_v3_cleaned.yaml")
)
with open(yaml_path, 'r') as f:
    map_metadata = yaml.safe_load(f)

image_path = os.path.join(os.path.dirname(yaml_path), map_metadata['image'])
resolution = map_metadata["resolution"]
origin = map_metadata["origin"] # [x, y, theta]

# Load the PGM image
map_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if map_img is None:
    raise FileNotFoundError(f"Could not load image at: {image_path}")

# Debug info
height, width = map_img.shape
print(f"Image dimensions (pixels): {width}w x {height}h")
print(f"Expected real-world size: {width*resolution:.2f}m x {height*resolution:.2f}m")
print(f"Pixel intensity range: min={np.min(map_img)}, max={np.max(map_img)}")
non_bg = np.count_nonzero(map_img < 254)
print(f"Non-background pixel count (<254): {non_bg} out of {width * height}")

# Show pixel intensity histogram
plt.figure()
plt.hist(map_img.ravel(), bins=256, range=(0, 256))
plt.title("Pixel Intensity Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

# Threshold to find non-background area
threshold = 254 # background assumed near white
mask = map_img < threshold
ys, xs = np.where(mask)

# Compute crop bounds
x_min_px, x_max_px = np.min(xs), np.max(xs)
y_min_px, y_max_px = np.min(ys), np.max(ys)

# Crop the image
cropped_img = map_img[y_min_px:y_max_px+1, x_min_px:x_max_px+1]

# Compute the corresponding real-world coordinates
x0_m = origin[0] + x_min_px * resolution
x1_m = origin[0] + x_max_px * resolution
y0_m = origin[1] + y_min_px * resolution
y1_m = origin[1] + y_max_px * resolution
# Display map with proper scale and orientation
plt.figure(figsize=(10, 10))
plt.imshow(map_img, cmap='gray', origin='upper', extent=[x0_m, x1_m, y1_m, y0_m])
plt.xlabel("x [meters]")
plt.ylabel("y [meters]")
plt.title("Cropped Minicity Map Visualization")
plt.grid(True)
plt.gca().set_aspect('equal')
plt.show()
