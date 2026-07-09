import os
import json
import time
import requests
from io import BytesIO
from PIL import Image

BASE_DIR = "/Users/shameelabid/MyWork/Guess Games/guess_games_data"

def download_image_from_itunes(app_name, save_path):
    print(f"Searching iTunes for: {app_name}")
    try:
        url = f"https://itunes.apple.com/search?term={app_name}&entity=software&limit=1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if not data.get('results'):
            print(f"  -> No results found in iTunes for {app_name}")
            return False
            
        result = data['results'][0]
        image_url = None
        
        # Prefer screenshots, but skip the first few to avoid promotional banners/logos
        if result.get('screenshotUrls') and len(result['screenshotUrls']) > 0:
            screenshots = result['screenshotUrls']
            if len(screenshots) > 2:
                # Pick the 3rd screenshot (index 2) which is usually pure UI
                image_url = screenshots[2]
            elif len(screenshots) > 1:
                # Pick the 2nd one
                image_url = screenshots[1]
            else:
                # Fallback to the first one if it's the only one
                image_url = screenshots[0]
        elif result.get('artworkUrl512'):
            image_url = result['artworkUrl512']
            
        if not image_url:
            print(f"  -> No image URLs found in iTunes result for {app_name}")
            return False
            
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        img_resp = requests.get(image_url, headers=headers, timeout=10)
        img_resp.raise_for_status()
        
        img = Image.open(BytesIO(img_resp.content))
        # Convert to WEBP
        img.save(save_path, "WEBP")
        print(f"  -> Saved: {save_path}")
        return True
    except Exception as e:
        print(f"  -> Error fetching {app_name}: {e}")
        return False

def main():
    json_file = os.path.join(BASE_DIR, "allLevelDetails_v2.json")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        if item.get("type") != "Apps":
            continue
            
        album_name = item.get("name")
        album_dir = os.path.join(BASE_DIR, album_name)
        units_file = os.path.join(album_dir, "units.json")
        img_dir = os.path.join(album_dir, "img")
        
        if not os.path.exists(units_file):
            print(f"Skipping {album_name}: units.json not found.")
            continue
            
        print(f"\n--- Processing {album_name} ---")
        with open(units_file, 'r', encoding='utf-8') as f:
            units = json.load(f)
            
        for idx, app_name in enumerate(units):
            image_num = idx + 1
            save_path = os.path.join(img_dir, f"{image_num}.webp")
            
            if os.path.exists(save_path):
                print(f"[{image_num}/{len(units)}] {app_name} image already exists. Skipping.")
                continue
                
            print(f"[{image_num}/{len(units)}] Fetching {app_name}...")
            
            success = download_image_from_itunes(app_name, save_path)
            # Small delay to respect iTunes API limits
            time.sleep(1.5)

if __name__ == "__main__":
    main()
