
import subprocess

def download_asset():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Axel_Watertoren_4843.JPG/800px-Axel_Watertoren_4843.JPG"
    output = "src/assets/images/watertoren_axel.jpg"
    try:
        subprocess.run(['curl', '-L', '-o', output, url], check=True)
        print(f"Downloaded {output}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    download_asset()
