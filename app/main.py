from window import Window
from source import File, Microphone
from wave import Wave



class App(Window):
    def init(self):
        #self.source = File('./audio/aphex_test.mp3')
        self.source = Microphone()

        self.wave = Wave(self.ctx,0,0,1280,720)

    def size(self,width,height):
        self.wave.size(width,height)

    def draw(self,dt):
        available = self.source.available()
        window = self.source.get()
        print(available,window.shape if window is not None else None)

        self.wave.add(window)
        self.wave.update()
        self.wave.draw()


    
if __name__ == '__main__':
    App.run()
