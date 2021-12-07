import requests
from bs4 import BeautifulSoup

youtube_trending_url = 'https://www.youtube.com/feed/trending'

response = requests.get(youtube_trending_url)

print('Status Code: ',response.status_code)

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page Title:', doc.title.text)

video_divs = doc.find_all('div', class_='ytd-video-renderer')
print(f'Found {len(video_divs)} videos')