from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

Name = "{filename}"
L = instaloader.Instaloader(filename_pattern=Name)

PROFILE = "demijmering"

posts = instaloader.Profile.from_username(L.context, "demijmering").get_posts()
profile = instaloader.Profile.from_username(L.context, PROFILE)

SINCE = datetime(2023, 12, 1)
UNTIL = datetime(2023, 1, 1)

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    L.download_post(post, "demijmering")
    filename = profile.username + '/' + L.format_filename(post, target=profile.username)