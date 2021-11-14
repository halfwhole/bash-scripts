import json
import os
import requests
import sys

DEST_DIR = '~/Downloads'
INDEX_URL = 'https://yt1s.com/api/ajaxSearch/index'
CONVERT_URL = 'https://yt1s.com/api/ajaxConvert/convert'

# Get user input (arg #1)
try:
    INPUT_URL = sys.argv[1]
    VIDEO_ID = INPUT_URL.split('?v=')[1]
except Exception:
    print("Usage: youtube-download URL")
    sys.exit()

# Get download URLs and specs
s = requests.Session()

resp = s.post(INDEX_URL,
              data={'q': INPUT_URL, 'vt': 'home'})
content = json.loads(resp.content)

mp4_links = content['links']['mp4']
mp3_links = content['links']['mp3']
del mp4_links['auto']  # Ignore the auto option in mp4
mp4_vals = list(mp4_links.values())
mp3_vals = list(mp3_links.values())
len_mp4 = len(mp4_vals)
len_mp3 = len(mp3_vals)

if not mp4_vals and not mp3_vals:
    print("No video nor audio found, is your given URL '%s' correct?" % INPUT_URL)
    sys.exit(1)

# Print download options
for i in range(len_mp4 + len_mp3):
    is_mp4 = i in range(len_mp4)
    val = mp4_vals[i] if is_mp4 else mp3_vals[i-len_mp4]
    print('[%d] %s (%s, %s)' % (i+1, val['f'], val['q'], val['size']))

# User chooses download option
print('Select your option: ', end='')
chosen_option = int(input())-1

is_mp4 = chosen_option in range(len_mp4)
val = mp4_vals[chosen_option] if is_mp4 else mp3_vals[chosen_option-len_mp4]

# Retrieve download URL
print('Retrieving download URL... ', end='', flush=True)
resp2 = s.post(CONVERT_URL,
               data={'vid': VIDEO_ID, 'k': val['k']})
content2 = json.loads(resp2.content)
file_name = content2['title']
download_url = content2['dlink']
print('done!')

# Download video/audio
extension = '.' + val['f']
file_name += extension
file_name = file_name.replace('/', '')  # remove '/'s which are not allowed
path_file_name = os.path.join(os.path.expanduser(DEST_DIR), file_name)
print('Downloading %s to %s... ' % (file_name, DEST_DIR), end='', flush=True)
blob = s.get(download_url).content
with open(path_file_name, 'wb') as f:
    f.write(blob)
print('done!')
