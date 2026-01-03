import os
from PIL import Image


def process_images():
    # Create the 'new_images' folder if it doesn't already exist
    if not os.path.exists('new_images'):
        os.mkdir('new_images')

    # Get the list of all files in the 'images' folder
    image_files = os.listdir('images')

    # Loop through each image file and process it
    for i, filename in enumerate(image_files):
        # Open the image using PIL
        with Image.open(f'images/{filename}') as img:
            # Convert to PNG format
            img = img.convert('RGBA')
            # Crop the edges to be a square
            width, height = img.size
            if width != height:
                if width > height:
                    left = (width - height) // 2
                    right = left + height
                    top, bottom = 0, height
                else:
                    top = (height - width) // 2
                    bottom = top + width
                    left, right = 0, width
                img = img.crop((left, top, right, bottom))
            # Rotate so the faces of the people are oriented correctly
            img = img.rotate(90, expand=True)
            # Resize to 75x75 pixels
            img = img.resize((75, 75), resample=Image.BICUBIC)
            # Convert to grayscale
            img = img.convert('L')
            # Save the new image
            new_filename = f'pic{i+1:04}.png'
            img.save(f'new_images/{new_filename}')
            print(f'Processed {filename} -> {new_filename}')


if __name__ == '__main__':
    process_images()
