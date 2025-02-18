# Get your playlist link ( https://d.lalal.ai/media/split/HASH/(no_)vocals_playlist ) from lalal.ai when uploading your audio

# fast written tool for instant using

from requests import get
import os
link = input("Enter the link to the playlist: ")
file_name_segment = "segment-{}.mp3"
all_files = sorted(os.listdir("segments"))
last_segment = 0

for file in all_files:
        if file.startswith("segment-"):
                last_segment = int(file[8:-4]) # from segment- to .mp3
                break

for num_segment in range(last_segment, 1000):
    segment_link = link
    if not link.endswith("/"):
        segment_link += "/"
    segment_name = file_name_segment.format(str(num_segment).zfill(3))
    segment_link += segment_name
    print(f"Downloading {segment_name}...")
    response = get(segment_link)
    if response.status_code == 200:
        with open(f"segments/{segment_name}", "wb") as file:
            file.write(response.content)
    else:
        print(f"Can't download {segment_name}. Probably doesn't exist")
        print(segment_link)
        break
