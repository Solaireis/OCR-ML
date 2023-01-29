import httpx
import pathlib

image_path = pathlib.Path("dhcp.png") # change this accordingly
image_bytes = image_path.read_bytes()

url = "http://172.27.190.249:8080" # change this accordingly
req = httpx.post(url, files={"image": image_bytes})
print(req.json())

image_path = pathlib.Path("Passport.jpg") # change this accordingly
image_bytes = image_path.read_bytes()

url = "http://172.27.190.249:8080" # change this accordingly
req = httpx.post(url, files={"image": image_bytes})
print(req.json())