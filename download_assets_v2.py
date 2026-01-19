
import subprocess
import os

def download_asset():
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    
    urls = [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Axel_Watertoren_4843.JPG/800px-Axel_Watertoren_4843.JPG", "src/assets/images/watertoren_axel.jpg"),
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Polder_near_Oostburg.jpg/800px-Polder_near_Oostburg.jpg", "src/assets/images/polder_zeeland.jpg")
    ]
    
    for url, output in urls:
        try:
            subprocess.run(['curl', '-L', '-A', ua, '-o', output, url], check=True)
            size = os.path.getsize(output)
            print(f"Downloaded {output}: {size} bytes")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    download_asset()
