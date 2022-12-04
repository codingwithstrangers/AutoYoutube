import pafy
import json


def main():
    yt_url = "https://youtu.be/AqGSC7XS2Cg"
    yt_video = download_youtube_url(yt_url)
    return yt_video


def download_youtube_url(url, download: bool = True):
    with open(".env") as f:
        json_load = json.load(f)
        API_key = json_load['API_key']
        pafy.set_api_key(API_key)

    video = pafy.new(url)
    if download:
        audiostreams = video.audiostreams
        audiostreams[2].download(filepath="F:\Coding with Strangers\AutoYoutube\podcast.m4a", quiet=False)

    return video


if __name__ == "__main__":
    yt_info = main()
    print(yt_info.description, yt_info.title)
