from pytube import YouTube
from pytube import Playlist
import re
import os
import time

class Audio:
    def __init__(self,url=None,path=None):
        self.__url=url
        self.__path=path
        
    @property
    def url(self):
        return self.__url 
    
    @property
    def path(self):
        return self.__path
        
    def download_audio(self):
        try:
            time_now = int(time.time())
            yt = YouTube(self.url)
            ys = yt.streams.filter(only_audio=True).first()
            ys.download(output_path=self.path, filename=f'{time_now}{ys.default_filename}')
            return True, 'Download Completo do Audio'
        except:
            return False, 'Falha no Download do Audio'