import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
import io
import math
from PIL import Image

FRAME_WIDTH = 320
FRAME_HEIGHT = 240

file_name = input("Enter the file name: ")

with open(file_name, "rb") as file:
    data = file.read()
chunk_size = FRAME_WIDTH * FRAME_HEIGHT * 3
num_frames = math.ceil(len(data) / chunk_size)
data_chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_frames)]

frames = []
for i, chunk in enumerate(data_chunks):
    img = Image.new('RGB', (FRAME_WIDTH, FRAME_HEIGHT), (0, 0, 0))
    pixels = img.load()

    for j in range(len(chunk)):
        x = j % FRAME_WIDTH
        y = j // FRAME_WIDTH
        pixels[x, y] = (chunk[j], 0, 0)

    frames.append(img)

output_file = input("Enter the name of the output video file: ")
frames[0].save(output_file, "MP4V", fps=30, save_all=True, append_images=frames[1:])

creds = service_account.Credentials.from_service_account_file("path/to/credentials.json")
youtube = build('youtube', 'v3', credentials=creds)

try:
    body=dict(
        snippet=dict(
            title="My encoded video",
            description="Encoded video uploaded using Python"
        ),
        status=dict(
            privacyStatus="unlisted"
        )
    )

    with io.FileIO(output_file, mode="rb") as file:
        insert_request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=googleapiclient.http.MediaIoBaseUpload(file, "video/*")
        )
        insert_request.execute()

    print("Video uploaded successfully!")
except HttpError as error:
    print(f"An error occurred: {error}")
