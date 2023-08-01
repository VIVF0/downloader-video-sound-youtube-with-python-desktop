from pytube import YouTube
import os
import ffmpeg
import threading

class Video:
    def __init__(self, url=None, path=None, resolution='1080p'):
        self.__url = url
        self.__path = path
        self.__resolution = resolution

    @property
    def url(self):
        return self.__url

    @property
    def path(self):
        return self.__path

    @property
    def resolution(self):
        return self.__resolution

    def download_video(self):
        yt = YouTube(self.url)
        video_stream = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution()
        self.__resolution=video_stream.resolution

        video_stream.download(self.path)
        
        print('Download do Video Completo')