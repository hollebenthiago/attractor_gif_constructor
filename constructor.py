import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from methods import eulerstep, rk4step, euler, rk4
import matplotlib.animation as animation
from IPython.display import HTML
import os

m1   = input('First method: (Euler, rk4)     ')
m2   = input('Second method: (Euler, rk4)     ')
n    = input('Rate between both methods: (e.g. 2)     ')
args = input('Extra arguments of the function: (e.g. [10, 28, 8/3])     ')
x0   = input('Initial condition: (e.g. [8, 5, 13])     ')
name = input('Name of the file: (e.g. lorenz)     ')
tmax = input('Until when do you want to simulate the equations: (e.g. 100)     ')

X = input('dx/dt equation: (e.g. args[0]*(y - x) )')
Y = input('dy/dt equation: (e.g. x*(args[1] - z) - y )')
Z = input('dz/dt equation: (e.g. ) x*y - args[2]*z )')

f = open('function.py', 'w+')

f.write('import numpy as np                                                     \n')
f.write('import matplotlib.pyplot as plt                                        \n')
f.write('from mpl_toolkits.mplot3d import Axes3D                                \n')
f.write('import mpl_toolkits.mplot3d.axes3d as p3                               \n')
f.write('from methods import eulerstep, rk4step, euler, rk4, modn, update_lines \n')
f.write('import matplotlib.animation as animation                               \n')
f.write('from IPython.display import HTML                                       \n')

f.write('def F(t, xs, args):           \n')
f.write(f'  x = xs[0]                  \n')
f.write(f'  y = xs[1]                  \n')
f.write(f'  z = xs[2]                  \n')
f.write(f'  X = %s                     \n' %(X))
f.write(f'  Y = %s                     \n' %(Y))
f.write(f'  Z = %s                     \n' %(Z))
f.write(f'  return np.array([X, Y, Z]) \n')

f.write(f'h = 0.01   \n')
f.write(f'tmax = %s  \n' %(tmax))
f.write(f'args = %s  \n' %(args))
f.write(f'x0 = np.array(%s)    \n' %(x0))
f.write(f'n = %s     \n' %(n))
f.write(f'Xs_m1 = %s(F, np.linspace(0, tmax, tmax), x0, h, args)[0] \n'   %(m1))
f.write(f'xs_m1 = %s(F, np.linspace(0, tmax, tmax), x0, h, args)[0][0] \n' %(m1))
f.write(f'ys_m1 = %s(F, np.linspace(0, tmax, tmax), x0, h, args)[0][1] \n' %(m1))
f.write(f'zs_m1 = %s(F, np.linspace(0, tmax, tmax), x0, h, args)[0][2] \n' %(m1))
f.write(f'Xs_m2 = %s(F, np.linspace(0, tmax, tmax), x0, h, args)[0] \n'    %(m2))
f.write(f'xs_m2 = %s(F, np.linspace(0, tmax, tmax), x0, h, args)[0][0] \n' %(m2))
f.write(f'ys_m2 = %s(F, np.linspace(0, tmax, tmax), x0, h, args)[0][1] \n' %(m2))
f.write(f'zs_m2 = %s(F, np.linspace(0, tmax, tmax), x0, h, args)[0][2] \n' %(m2))
f.write(f'Xs_m3 = modn(F, np.linspace(0, tmax, tmax), x0, h, n, %sstep, %sstep, args)[0]    \n' %(m1, m2))
f.write(f'xs_m3 = modn(F, np.linspace(0, tmax, tmax), x0, h, n, %sstep, %sstep, args)[0][0] \n' %(m1, m2))
f.write(f'ys_m3 = modn(F, np.linspace(0, tmax, tmax), x0, h, n, %sstep, %sstep, args)[0][1] \n' %(m1, m2))
f.write(f'zs_m3 = modn(F, np.linspace(0, tmax, tmax), x0, h, n, %sstep, %sstep, args)[0][2] \n' %(m1, m2))

f.write('fig    = plt.figure()                                    \n')
f.write('ax     = p3.Axes3D(fig)                                  \n')
f.write('labels = [%s.__name__, %s.__name__, \'alternating\']                       \n' %(m1, m2))
f.write('colors  = [\'tab:blue\', \'tab:orange\', \'tab:purple\'] \n')
f.write('markers = [\'o\', \'D\', \'*\']                          \n')

f.write('data = [Xs_m1, Xs_m2, Xs_m3] \n')
f.write('lines = [ax.plot(dat[0][0:1], dat[1][0:1], dat[2][0:1], color = colors[i],linewidth = 0.6)[0] for i, dat in enumerate(data)] \n')
f.write('lines += [ax.plot(dat[0][0:1], dat[1][0:1], dat[2][0:1], color = colors[i],label = labels[i], marker = markers[i])[0] for i, dat in enumerate(data)] \n')
f.write('data += [Xs_m1, Xs_m2, Xs_m3] \n')

f.write('ax.set_xlim3d([min(min(Xs_m1[0]),min(Xs_m2[0])), max(max(Xs_m1[0]),max(Xs_m2[0]))]) \n')
f.write('ax.set_xlabel(\'X\') \n')
f.write('ax.set_ylim3d([min(min(Xs_m1[1]),min(Xs_m2[1])), max(max(Xs_m1[1]),max(Xs_m2[1]))]) \n')
f.write('ax.set_ylabel(\'Y\') \n')
f.write('ax.set_zlim3d([min(min(Xs_m1[2]),min(Xs_m2[2])), max(max(Xs_m1[2]),max(Xs_m2[2]))]) \n')
f.write('ax.set_zlabel(\'Z\') \n')

f.write('ax.grid(False) \n')
f.write('ax.set_xticks([]) \n')
f.write('ax.set_yticks([]) \n')
f.write('ax.set_zticks([]) \n')
f.write('ax.legend(loc=\'upper right\') \n')

f.write('line_ani = animation.FuncAnimation(fig, update_lines, np.arange(0, tmax, 2), fargs=(data, lines, ax),interval=50, blit=False) \n')
f.write('line_ani.save(\'gifs/%s.mp4\')' %(name))

f.close()

os.system('python3 function.py')




