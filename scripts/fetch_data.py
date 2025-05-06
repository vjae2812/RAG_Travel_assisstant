import subprocess
import os

# List of Wikitravel URLs
paths = [
    "https://wikitravel.org/en/Thailand",
    "https://wikitravel.org/en/Lower_Northern_Thailand",
    "https://wikitravel.org/en/Central_Thailand",
]

# Proxy base URL
base_url = "https://r.jina.ai/"
save_dir = "./data"
os.makedirs(save_dir, exist_ok=True)

# Download content
for path in paths:
    try:
        # Construct the full URL by combining the base URL and the dynamic path
        full_url = base_url + path

        # Extract the last part of the URL (after the last '/')
        filename = path.split('/')[-1] + '.txt'
        save_path = os.path.join('/content/data', filename)
        # Use curl command to fetch the content and save it to a file
        with open(save_path, 'w', encoding='utf-8') as file:
            subprocess.run(['curl', full_url], stdout=file)

        print("Content saved to:",f"/content/data/{filename}")

    except Exception as e:
        print(f"Error while fetching {full_url}: {e}")

