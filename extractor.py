import subprocess
import json
import sys

def extract_metadata(file_path):
    try:
        result = subprocess.run(['exiftool', '-json', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        metadata = json.loads(result.stdout)
        for key, value in metadata[0].items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extractor.py <image_file>")
    else:
        extract_metadata(sys.argv[1])
