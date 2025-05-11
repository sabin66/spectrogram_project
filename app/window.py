import moderngl
import time
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import QOpenGLWidget, QApplication, QShortcut

from utils import logger

class Window(QOpenGLWidget):
    frame_rate = 61.0
    def __init__(self):
        super().__init__()
    
        self.setFixedSize(1280,720)
        fmt = QSurfaceFormat()
        fmt.setVersion(3, 3)
        fmt.setProfile(QSurfaceFormat.CoreProfile)
        fmt.setDefaultFormat(fmt)
        fmt.setSamples(4)
        self.setFormat(fmt)

        self.t = None

        QShortcut(Qt.Key_Escape, self,self.quit)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(int(1000/self.frame_rate))

    #---------------------------
    #-------OpenGL logic--------

    def initializeGL(self):
        self.context = moderngl.create_context(require=330)
        self.context.clear(0.2,0.6,0.5)
        self.context.multisample = True
        self.init()


    def resizeGL(self,width,height):
        self.size(width,height)

    def paintGL(self):
        now = time.time()
        dt = now - self.t if self.t else 1.0 / self.frame_rate
        self.draw(dt)
    
    def quit(self):
        self.exit()
        self.close()

    @classmethod
    def run(cls):
        app = QApplication([])
        window = cls()
        window.show()
        app.exit(app.exec())

    #---------------------------
    #--------Interface----------
 
    def init(self):
        logger.info('init')

    def size(self,width,height):
        logger.info(f"size {width} {height}")

    def draw(self,dt):
        logger.info(f"draw {dt:.4f}")

    def exit(self):
        logger.info("exit")



if __name__ == "__main__":
    Window.run()