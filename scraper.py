from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

youtube_trending_url = 'https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)

  return driver

def get_videos(driver):
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(youtube_trending_url)
  videos = driver.find_elements(By.TAG_NAME,VIDEO_DIV_TAG)

  return videos

def parse_video(video):
  #title, url, thumbnail_url, channel, views, uploaded,description
  title = video.find_element(By.ID,'video-title').text

  url = video.find_element(By.ID,'video-title').get_attribute('href')

  thumbnail_url = video.find_element(By.TAG_NAME, 'img').get_attribute('src')

  channel_name = video.find_element(By.CLASS_NAME, 'ytd-channel-name').text

  views = video.find_elements(By.ID, 'metadata-line')[0].text

  description = video.find_element(By.ID, 'description-text').text

  return {
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel': channel_name,
    'views': views,
    'description': description
  }

if __name__ == '__main__':
  print('Creating Driver')
  driver = get_driver()

  print('Fetching trending videos')
  videos = get_videos(driver)

  print(f'Found {len(videos)} videos')

  print('Parsing top 10 videos')

  videos_data = [parse_video(video) for video in videos[:1]]
  print(videos_data)

  # print('Saving the data to a CSV')
  # videos_df = pd.DataFrame(videos_data)
  # videos_df.to_csv('trending.csv',index=None)


