import scrapetube
import re

vid_url = scrapetube.get_channel("UCSJ4gkVC6NrvII8umztf0Ow", sort_by="newest", content_type="streams")
vid_url2 = scrapetube.get_channel(channel_username="LofiGirl", sort_by="newest", content_type="streams")

for videos in vid_url2:
    try:
        status = videos['thumbnailOverlays'][0]['thumbnailOverlayTimeStatusRenderer']['text']['runs'][0]['text']
        title = videos['title']['runs'][0]['text']
        check = bool(re.search(".*study.*", title))
        if (status == "LIVE"):
            if (check):
                url = "https://www.youtube.com/watch?v=" + videos['videoId']
                print(url)
    except:
        a = 1
