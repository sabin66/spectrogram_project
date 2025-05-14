import moderngl
import numpy as np
from utils import ortrographic

class Wave:

    VERTEX = '''
        #version 330 core
        uniform mat4 P;
        uniform float x,y,h;
        in float sample;
        void main(){
            int x_interp = gl_VertexID / 2;
            float h = (h/2) + sample * (h/2);
            gl_Position = P * vec4(x+x_interp,y + h,0,1.0);
        }
    '''
    FRAGMENT = '''
        #version 330 core
        out vec4 out_color;
        void main(){
            out_color = vec4(0.1,1.0,0.6,1.0);
        }
    '''

    def __init__(self,ctx,x,y,w,h):
        self.ctx = ctx
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.prog = self.ctx.program(
            vertex_shader = self.VERTEX,
            fragment_shader = self.FRAGMENT
        )
        self.samples = np.zeros(int(w*2),dtype='f4')
        self.buffer = self.ctx.buffer(
            reserve = self.samples.nbytes,dynamic = True
        )
        self.vao = self.ctx.vertex_array(self.prog,self.buffer,'sample')
        self.prog['x'] = x
        self.prog['y'] = y
        self.prog['h'] = h
        self.update()

    def add(self,window):
        if window is not None:
            sample = np.abs(window[:100]).max()
        else:
            sample = 0.002

        self.samples[:-2] = self.samples[2:]
        self.samples[-2:] = [-sample,sample]

    def update(self):
        self.buffer.write(self.samples)

    def size(self,w,h):
        P = ortrographic(w,h)
        self.prog['P'].write(P)

    def draw(self):
        self.vao.render(moderngl.LINES)