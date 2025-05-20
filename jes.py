import os
import requests
import zipfile

# List of image URLs and corresponding filenames (JPG)
images = {
    "1_Spaghetti_Bolognese.jpg": "https://unsplash.com/photos/1.jpg",  # <-- Replace with actual direct JPG link
    "2_Kylling_Tikka_Masala.jpg": "https://unsplash.com/photos/2.jpg",
    "3_Fiskegrateng.jpg": "https://unsplash.com/photos/3.jpg",
    "4_Vegetarisk_Chili.jpg": "https://unsplash.com/photos/4.jpg",
    "5_Pannekaker.jpg": "https://unsplash.com/photos/5.jpg",
    "6_Lasagne.jpg": "https://unsplash.com/photos/6.jpg",
    "7_Tomatsuppe.jpg": "https://unsplash.com/photos/7.jpg",
    "8_Taco.jpg": "https://unsplash.com/photos/8.jpg",
    "9_Frokostsmoothie.jpg": "https://unsplash.com/photos/9.jpg",
    "10_Omelett.jpg": "https://unsplash.com/photos/10.jpg"
}

# Create a directory to store downloaded images
os.makedirs('downloaded_images', exist_ok=True)

print("Downloading images...")
for filename, url in images.items():
    response = requests.get(url, stream=True)
    response.raise_for_status()
    filepath = os.path.join('downloaded_images', filename)
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded {filename}")

# Create a ZIP file
zip_filename = 'matretter_images.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for filename in images.keys():
        filepath = os.path.join('downloaded_images', filename)
        zipf.write(filepath, arcname=filename)

print(f"\nAll images zipped into: {zip_filename}")

# Provide instructions for where the zip is located

