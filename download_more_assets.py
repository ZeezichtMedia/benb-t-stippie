
import subprocess

def download_asset():
    urls = [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Polder_near_Oostburg.jpg/800px-Polder_near_Oostburg.jpg", "src/assets/images/polder_zeeland.jpg")
    ]
    for url, output in urls:
        try:
            subprocess.run(['curl', '-L', '-o', output, url], check=True)
            print(f"Downloaded {output}")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    download_asset()
