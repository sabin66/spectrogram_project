import moderngl

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import QOpenGLWidget, QApplication, QShortcut

class Window(QOpenGLWidget):
    frame_rate = 61.0
    def __init__(self):
        super().__init__()
    
        fmt = QSurfaceFormat()
        fmt.setVersion(3, 3)
        fmt.setProfile(QSurfaceFormat.CoreProfile)
        fmt.setDefaultFormat(fmt)
        fmt.setSamples(4)
        self.setFormat(fmt)

        QShortcut(Qt.Key_Escape, self,self.quit)

    #---------------------------
    #-------OpenGL logic--------

    def initializeGL(self):
        self.context = moderngl.create_context(require=330)
        

    def resizeGL(self,width,height):
        pass

    def paintGL(self):
        pass
    
    def quit(self):
        self.close()

    @classmethod
    def run(cls):
        app = QApplication([])
        window = cls()
        window.show()
        app.exit(app.exec())

if __name__ == "__main__":
    Window.run()