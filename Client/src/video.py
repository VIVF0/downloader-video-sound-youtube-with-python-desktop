from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

class Video:
    def __init__(self,url=None,path=None):
        self.__url=url
        self.__path=path
        
    @property
    def url(self):
        return self.__url 
    
    @property
    def path(self):
        return self.__path
        
    def download_video(self):
        yt = YouTube(self.url)
        ys = yt.streams.filter(only_audio=True).first().download(self.path)
        print('Download Complete')