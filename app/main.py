from window import Window
from source import File, Microphone
from wave import Wave
from spec import Spec
import config



class App(Window):
    def init(self):
        self.source = File('./audio/windowlicker.mp3')
        #self.source = Microphone()

        self.wave = Wave(self.ctx,0,0,config.WINDOW_WIDTH,200)
        self.spec = Spec(self.ctx,0,self.wave.h,config.WINDOW_WIDTH,520)

    def size(self,w,h):
        self.wave.size(w,h)
        self.spec.size(w,h)

    def draw(self,dt):
        available = self.source.available()
        window = self.source.get()
        print(available,window.shape if window is not None else None)

        self.wave.add(window)
        self.spec.add(window)
        self.wave.update()
        self.spec.update()
        self.wave.draw()
        self.spec.draw()


    
if __name__ == '__main__':
    App.run()
