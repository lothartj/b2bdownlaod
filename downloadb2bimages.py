import requests
import os

def download_images(item_numbers, base_url, save_directory):
    for item_number in item_numbers:
        image_url = f"{base_url}{item_number}-1.jpg"
        response = requests.get(image_url)

        if response.status_code == 200:
            # Ensure the directory exists
            os.makedirs(save_directory, exist_ok=True)

            # Save the image
            with open(os.path.join(save_directory, f"{item_number}-1.jpg"), 'wb') as f:
                f.write(response.content)
            print(f"Image for item {item_number} downloaded successfully.")
        else:
            print(f"Failed to download image for item {item_number}. Status code: {response.status_code}")

# Example usage
item_numbers_to_download = ["24ICE83183", 
"ABAMA500", 
"ABDWOTA318", 
"ALAB000120", 
"ALAB004918", 
"ALAB005120", 
"ALAB005137", 


]
base_url = "https://seapridefoodsdata.blob.core.windows.net/photos/"
save_directory = r"C:\downloadb2bimages\images"

download_images(item_numbers_to_download, base_url, save_directory)
