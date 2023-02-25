# instaDump
A Python script that scrapes the images from user "demijmering".
This is part of a workflow to automatically post Instagram posts to a Mailchimp newsletter.

## Scripts
Using instaloaders Python module https://instaloader.github.io/
Two script options. instaDownloader-date scrapes the images for a certain period, instaDownloader scrapes all the images. With the last one you will get blocked by Meta pretty quickly for going over their usage limits.

## History
### Fase 1
It used to be a simple operation of connecting Instagram to Zapier, generating an RSS feed, and connecting that feed to Mailchimp.

### Fase 2
Instagram started working with expiring image url's which meant the newsletter was filled with broken images.
I set up Airtable as an intermediary. Dumping all the Instagram info in an Airtable database through Zapier. Then generating the RSS feed from the data in Airtable through Zapier and using the excisting connection with Mailchimp.

### Fase 3
Airtable also started working with expiring links for attachments :(. Still using the data from Airtable, but using this Python script to get the images. Images are now hosted on GitHub... Everything is combined when generating the RSS feed in Zapier.