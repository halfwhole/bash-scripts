import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlretrieve

URL = "https://twittervideodownloader.com/"
DOWNLOAD_URL = "https://twittervideodownloader.com/download"

## Get user input (arg #1)
INPUT_URL = sys.argv[1]

## Get download URLs and specs
s = requests.Session()

resp = s.get(URL)
soup = BeautifulSoup(resp.content, features='lxml')
csrf_middleware_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')

resp2 = s.post(DOWNLOAD_URL,
               headers={'referer': URL},
               data={'csrfmiddlewaretoken': csrf_middleware_token, 'tweet': INPUT_URL})
soup2 = BeautifulSoup(resp2.content, features='lxml')
download_buttons_and_descriptions = soup2.find_all('div', {'class': 'small-6 columns'})
download_buttons = download_buttons_and_descriptions[::2]
download_descriptions = download_buttons_and_descriptions[1::2]
download_urls = [btn.find('a').get('href') for btn in download_buttons]
download_specs = [desc.find('p').text for desc in download_descriptions]

if not download_urls:
    print("No videos found, is your given URL '%s' correct?" % INPUT_URL)
    sys.exit()

## Display download specs to choose from
for i in range(len(download_specs)):
    print('[%d] %s' % (i+1, download_specs[i]))

## User chooses download option
print('Select your option: ', end='')
chosen_option = int(input())-1

## Downloads video
download_url = download_urls[chosen_option]
video_name = urlparse(download_url).path.split('/')[-1]
print('Downloading %s... ' % video_name, end='')
urlretrieve(download_url, video_name)
print('done!')
