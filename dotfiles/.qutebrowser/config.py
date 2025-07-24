# CONFIG FILE #

#Userscript directory
#/Users/canberkdemir/Library/'Application Support'/qutebrowser

#====== KEEPASSXC userscript (qute-keepassxc) ======#
key = "mDMEaF/UpRYJKwYBBAHaRw8BAQdAd0RC9F/TTZRxVF5UW6SUDejiJs2D7Ju2XELdUvJrraW0MENhbmJlcmsgKEtlZXBhc3MgS2V5KSA8Y2FuYmVya2RlbWlyMDNAZ21haWwuY29tPoiTBBMWCgA7FiEE9UEixUbJCdsjPlMOy+usrK/yGB8FAmhf1KUCGwMFCwkIBwICIgIGFQoJCAsCBBYCAwECHgcCF4AACgkQy+usrK/yGB8KHQD+Kjpr18MiN/EPw5uPJCA62Gy8cCq73hXuR/DM7WhF2xkA/jN8mj4WJ5k3jx0uoAkvGMrleHlUbLe0w2wNxMVRZgkNuDgEaF/UpRIKKwYBBAGXVQEFAQEHQPU8vdDAlrVh8IkaxoHNRwCEoaBhqpyTNIwQs3TP1SQxAwEIB4h4BBgWCgAgFiEE9UEixUbJCdsjPlMOy+usrK/yGB8FAmhf1KUCGwwACgkQy+usrK/yGB/NNQEAyqL1B2UnoF9DlFSrp9dhHQ5r45hjmz0sKQGISD0VoCEBAM1c5gUKwTjMyRcjMwNljPb1PjKnxgt1DvQ2n5Cj4lYE=pUPr"
config.bind('<Alt-Shift-u>', 'spawn --userscript qute-keepassxc --key mDMEaF/UpRYJKwYBBAHaRw8BAQdAd0RC9F/TTZRxVF5UW6SUDejiJs2D7Ju2XELdUvJrraW0MENhbmJlcmsgKEtlZXBhc3MgS2V5KSA8Y2FuYmVya2RlbWlyMDNAZ21haWwuY29tPoiTBBMWCgA7FiEE9UEixUbJCdsjPlMOy+usrK/yGB8FAmhf1KUCGwMFCwkIBwICIgIGFQoJCAsCBBYCAwECHgcCF4AACgkQy+usrK/yGB8KHQD+Kjpr18MiN/EPw5uPJCA62Gy8cCq73hXuR/DM7WhF2xkA/jN8mj4WJ5k3jx0uoAkvGMrleHlUbLe0w2wNxMVRZgkNuDgEaF/UpRIKKwYBBAGXVQEFAQEHQPU8vdDAlrVh8IkaxoHNRwCEoaBhqpyTNIwQs3TP1SQxAwEIB4h4BBgWCgAgFiEE9UEixUbJCdsjPlMOy+usrK/yGB8FAmhf1KUCGwwACgkQy+usrK/yGB/NNQEAyqL1B2UnoF9DlFSrp9dhHQ5r45hjmz0sKQGISD0VoCEBAM1c5gUKwTjMyRcjMwNljPb1PjKnxgt1DvQ2n5Cj4lYE=pUPr', mode='insert')
config.bind(f'pw', 'spawn --userscript qute-keepassxc --key mDMEaF/UpRYJKwYBBAHaRw8BAQdAd0RC9F/TTZRxVF5UW6SUDejiJs2D7Ju2XELdUvJrraW0MENhbmJlcmsgKEtlZXBhc3MgS2V5KSA8Y2FuYmVya2RlbWlyMDNAZ21haWwuY29tPoiTBBMWCgA7FiEE9UEixUbJCdsjPlMOy+usrK/yGB8FAmhf1KUCGwMFCwkIBwICIgIGFQoJCAsCBBYCAwECHgcCF4AACgkQy+usrK/yGB8KHQD+Kjpr18MiN/EPw5uPJCA62Gy8cCq73hXuR/DM7WhF2xkA/jN8mj4WJ5k3jx0uoAkvGMrleHlUbLe0w2wNxMVRZgkNuDgEaF/UpRIKKwYBBAGXVQEFAQEHQPU8vdDAlrVh8IkaxoHNRwCEoaBhqpyTNIwQs3TP1SQxAwEIB4h4BBgWCgAgFiEE9UEixUbJCdsjPlMOy+usrK/yGB8FAmhf1KUCGwwACgkQy+usrK/yGB/NNQEAyqL1B2UnoF9DlFSrp9dhHQ5r45hjmz0sKQGISD0VoCEBAM1c5gUKwTjMyRcjMwNljPb1PjKnxgt1DvQ2n5Cj4lYE=pUPr', mode='normal')

#====== Save Temp Changes ======#
config.load_autoconfig()


#====== PDF Reader ======#
config.set('content.pdfjs', True)


#====== Browser Setings ======#
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'ddg': 'https://duckduckgo.com/?q={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'g': 'https://www.google.com/search?q={}',
}


#====== YT and Google JS, Cookie Setting ======#
# Javascript setting
config.set('content.javascript.enabled', True, 'https://www.youtube.com/*')
config.set('content.javascript.enabled', True, 'https://accounts.google.com/*')
# Cookie Setting
config.set('content.cookies.accept', 'all', 'https://www.youtube.com')
config.set('content.cookies.accept', 'all', 'https://accounts.google.com')
# Trick youtube to think chrome is used
# Enable popup windows
config.set('content.autoplay', True, 'https://www.youtube.com')


#====== MPV support and keybindings ======#
config.bind('<Ctrl-shift-m>','spawn mpv {url}')
config.bind('<shift-m>','hint links spawn /opt/homebrew/bin/mpv {hint-url}')


#====== Spellcheck ======#
# Could not get it to work, look at this later
c.spellcheck.languages = ['en-US']


#====== Catpuccin Theme ======#
import catppuccin

# load your autoconfig, use this, if the rest of your config is empty!
config.load_autoconfig()

# set the flavor you'd like to use
# valid options are 'mocha', 'macchiato', 'frappe', and 'latte'
# last argument (optional, default is False): enable the plain look for the menu rows
catppuccin.setup(c, 'mocha', True)

import os
import ssl
from urllib.request import urlopen

# load your autoconfig, use this, if the rest of your config is empty!
config.load_autoconfig()

# if not os.path.exists(config.configdir / "theme.py"):
#     theme = "https://raw.githubusercontent.com/catppuccin/qutebrowser/main/setup.py"
#     with urlopen(theme) as themehtml:
#         with open(config.configdir / "theme.py", "a") as file:
#             file.writelines(themehtml.read().decode("utf-8"))

if os.path.exists(config.configdir / "theme.py"):
    import theme
    theme.setup(c, 'mocha', True)


#====== Shortcut to External Browsers ======#
# I currently only have librewolf
config.bind(',l', 'spawn /opt/homebrew/bin/librewolf {url}')


#====== Google Translate Userscript (Qute-Translate) ======#
config.bind(';t', 'hint userscript link translate')
config.bind(';T', 'hint userscript all translate --text')
config.bind('<Ctrl+T>', 'spawn --userscript translate')
config.bind('<Ctrl+Shift+T>', 'spawn --userscript translate --text')



