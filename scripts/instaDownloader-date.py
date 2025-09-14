from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

PROFILE = "demijmering"
Name = "{shortcode}"

L = instaloader.Instaloader(filename_pattern=Name)

posts = instaloader.Profile.from_username(L.context, PROFILE).get_posts()
profile = instaloader.Profile.from_username(L.context, PROFILE)


SINCE = datetime(2025, 12, 31)
UNTIL = datetime(2025, 9, 7)

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    L.download_post(post, PROFILE)
    filename = profile.username + '/' + L.format_filename(post, target=profile.username)