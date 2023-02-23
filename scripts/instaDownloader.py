import instaloader

from instaloader import Profile

L = instaloader.Instaloader()

PROFILE = "demijmering"

profile = Profile.from_username(L.context, PROFILE)

posts_sorted_by_likes = sorted(profile.get_posts(), key = lambda post: post.likes, reverse = True)

for post in posts_sorted_by_likes:
    L.download_post(post, PROFILE)
    filename = L.format_filename(post)