import pyaudio
import time
import math
import numpy as np

from utils import logger

class Source:
    def __init__(self,*args,**kwargs):
        self.audio = pyaudio.PyAudio()
        self.complete = False
        self.data = []
        self.index = 0
        self.total = 0
        self.init(*args,**kwargs)

    def init(*args,**kwargs):
        raise NotImplementedError("source.init")
    
    def callback(self,data,frame_count,time_info,status):
        raise NotImplementedError("source.callback")
    

class File(Source):
    pass

class Microphone(Source):
    pass