from pytube import YouTube
import os
import time

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
        try:
            yt = YouTube(self.url)
            video_stream = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution()
            self.__resolution=video_stream.resolution
            time_now = int(time.time())
            video_stream.download(output_path=self.path, filename=f'{time_now}{video_stream.default_filename}')
            
            return True, 'Download Completo do Video'
        except:
            return False, 'Falha no Download do Video'