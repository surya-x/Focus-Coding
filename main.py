import os
import random

import pafy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    exec_file_path = r"/Users/vsuryakumar/CodeBase/chromedriver"
    options = Options().add_argument("--headless")
    driver = webdriver.Chrome(executable_path=exec_file_path, options=options)
    return driver


def play_song(driver, url):
    # Playing the song by
    #   opening the url on the driver
    if driver.get(url):
        return True
    return False


def get_random(url_list, exception_list):
    # To get a random element from url_list except for
    #   elements appeared in exception_list
    selection_list = [url for url in url_list
                      if not exception_list.count(url)]
    return random.choice(selection_list)


def create_streams(urls):
    # To create PAFY stream objects from YT urls
    stream_objects = []
    for each in url:
        video = pafy.new(each)
        # print(video.author)
        if video.getbestaudio() is not None:
            stream_objects.append(video)
        else:
            print("LOG: audio stream not found for object ", video.author)
    return stream_objects


def close_project(driver):
    print("CONSOLE: ", "Closing Project")
    print("CONSOLE: ", "Thank You!!!")
    driver.close()


def load_urls(path=""):     # if not passed path Assumes it in working directory
    url_list = []
    with open(os.path.join(path, "ytlinks.txt")) as f:
        for line in f:
            li = line.strip(" \n")
            if not li.startswith("//") and li != "":
                url_list.append(li)
        return url_list


if __name__ == '__main__':
    url = load_urls()

    print("CONSOLE: ", "Setting up the environment")
    stream_objects = create_streams(url)

    video_played = []  # To Store all the video objects already played/playing
    video_played.append(get_random(stream_objects, video_played))
    now_playing = video_played[-1]
    print("CONSOLE: ", now_playing.author)
    print(now_playing.getbestaudio().url)

    # Opening chrome window to play the song
    driver = get_driver()
    play_song(driver, now_playing.getbestaudio().url)

    input()
    driver.execute_script('videos = document.querySelectorAll("video"); for(video of videos) {video.pause()}')
    input()
    driver.execute_script('videos = document.querySelectorAll("video"); for(video of videos) {video.play()}')

    print("CONSOLE: ", "Done setting\nPlease wait...")
    # close_project(driver)
