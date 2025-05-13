import pyaudio
import time
import math
import numpy as np
import librosa

from utils import logger

WINDOW_SIZE = 1024

HOP_SIZE = 370  # = total / fps

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
    
    def get(self):
        if self.index + WINDOW_SIZE > self.total:
            return None
        a = self.index
        b = self.index + WINDOW_SIZE
        data = self.data[a:b]
        self.index = a + HOP_SIZE
        return np.array(data)
    
    def available(self):
        samples = self.total - self.index
        samples -= WINDOW_SIZE
        available = math.ceil(samples/HOP_SIZE)
        return max(0,available)
    
SAMPLE_RATE = 22050
BUFFER_SIZE = 1024

class File(Source):
    
    def init(self,filename):
        self.data,_ = librosa.load(filename,sr=SAMPLE_RATE)
        self.steam = self.audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=SAMPLE_RATE,
            output=True,
            frames_per_buffer=BUFFER_SIZE,
            stream_callback=self.callback)
        
    def callback(self,in_data,frame_count, time_info,status):
        a = self.total
        b = self.total + BUFFER_SIZE
        data = self.data[a:b]
        self.total = b
        if self.total >= len(self.data):
            self.complete = True
        return (data,pyaudio.paContinue)
    

class Microphone(Source):
    def init(self):
        # create audio stream
        self.stream = self.audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=SAMPLE_RATE,
            input=True,
            frames_per_buffer=BUFFER_SIZE,
            stream_callback=self.callback
        )
    def callback(self,data,frame_count,time_info,status):
        data = np.frombuffer(data,dtype=np.float32)
        data = data.tolist()
        self.data.extend(data)
        self.total = len(self.data)
        return None, pyaudio.paContinue


if __name__ == '__main__':
    filename = './audio/aphex_test.mp3'

    source = File(filename)

    time.sleep(5)
