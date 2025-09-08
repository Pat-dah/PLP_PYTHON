import os
import requests
from urllib.parse import urlparse
import uuid

def download_images():
    # Prompt user for multiple URLs (comma-separated)
    urls = input("Enter image URLs (comma-separated): ").strip().split(",")

    # Directory for saving images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    for url in urls:
        url = url.strip()
        if not url:
            continue

        try:
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise error for bad HTTP status

            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename:  # If no filename in URL, generate one
                filename = f"image_{uuid.uuid4().hex}.jpg"

            filepath = os.path.join(save_dir, filename)

            # Save image in binary mode
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✅ Image saved successfully as: {filepath}")

        except requests.exceptions.HTTPError as http_err:
            print(f"❌ HTTP error for {url}: {http_err}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection error for {url}.")
        except requests.exceptions.Timeout:
            print(f"❌ Request timed out for {url}.")
        except Exception as e:
            print(f"❌ An error occurred for {url}: {e}")

if __name__ == "__main__":
    download_images()
