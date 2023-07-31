from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

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
        yt = YouTube(self.url)
        ys = yt.streams.filter(only_audio=True).first().download(self.path)
        for file in os.listdir(self.path):
            if re.search('mp4', file):                                 
                mp4_path = os.path.join(self.path , file)   
                mp3_path = os.path.join(self.path, os.path.splitext(file)[0]+'.mp3') 
                new_file = mp.AudioFileClip(mp4_path)  
                new_file.write_audiofile(mp3_path)    
                os.remove(mp4_path) 
        print('Download Completo')