import os
from PIL import Image

# Artifacts path where images were generated
brain_path = r"C:\Users\amarl\.gemini\antigravity\brain\37fa0dcc-763a-4787-b345-9bfbf650cce5"
# Destination path
dest_path = r"c:\Users\amarl\Documents\Orange farmers Market\src\images"

# Map generated prefix to final webp name
image_map = {
    "dates_hero": "blog_dates_hero.webp",
    "sunday_hero": "blog_sunday_hero.webp",
    "vendors_hero": "blog_vendors_hero.webp",
    "fresh_produce": "inline_produce.webp",
    "artisan_goods": "inline_artisan.webp"
}

os.makedirs(dest_path, exist_ok=True)

# Find generated files
for file in os.listdir(brain_path):
    if file.endswith(".png"):
        for key, webp_name in image_map.items():
            if file.startswith(key):
                src = os.path.join(brain_path, file)
                dst = os.path.join(dest_path, webp_name)
                print(f"Optimizing {src} to {dst}")
                with Image.open(src) as img:
                    img.save(dst, 'webp', quality=80)

print("Optimization complete.")
