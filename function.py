import numpy as np                                                     
import matplotlib.pyplot as plt                                        
from mpl_toolkits.mplot3d import Axes3D                                
import mpl_toolkits.mplot3d.axes3d as p3                               
from methods import eulerstep, rk4step, euler, rk4, modn, update_lines 
import matplotlib.animation as animation                               
from IPython.display import HTML                                       
def F(t, xs, args):           
  x = xs[0]                  
  y = xs[1]                  
  z = xs[2]                  
  X = np.sin(6*y) -np.cos(-0.3*z)                     
  Y = -np.sin(3*x) + np.cos(16*z)                     
  Z = np.cos(2*x) - np.sin(3*y)                     
  return np.array([X, Y, Z]) 
h = 0.01   
tmax = 2004  
args = []  
x0 = np.array([0.5, 0.5, 0.5])    
n = 3     
Xs_m1 = euler(F, np.linspace(0, tmax, tmax), x0, h, args)[0] 
xs_m1 = euler(F, np.linspace(0, tmax, tmax), x0, h, args)[0][0] 
ys_m1 = euler(F, np.linspace(0, tmax, tmax), x0, h, args)[0][1] 
zs_m1 = euler(F, np.linspace(0, tmax, tmax), x0, h, args)[0][2] 
Xs_m2 = rk4(F, np.linspace(0, tmax, tmax), x0, h, args)[0] 
xs_m2 = rk4(F, np.linspace(0, tmax, tmax), x0, h, args)[0][0] 
ys_m2 = rk4(F, np.linspace(0, tmax, tmax), x0, h, args)[0][1] 
zs_m2 = rk4(F, np.linspace(0, tmax, tmax), x0, h, args)[0][2] 
Xs_m3 = modn(F, np.linspace(0, tmax, tmax), x0, h, n, eulerstep, rk4step, args)[0]    
xs_m3 = modn(F, np.linspace(0, tmax, tmax), x0, h, n, eulerstep, rk4step, args)[0][0] 
ys_m3 = modn(F, np.linspace(0, tmax, tmax), x0, h, n, eulerstep, rk4step, args)[0][1] 
zs_m3 = modn(F, np.linspace(0, tmax, tmax), x0, h, n, eulerstep, rk4step, args)[0][2] 
fig    = plt.figure()                                    
ax     = p3.Axes3D(fig)                                  
labels = [euler.__name__, rk4.__name__, 'alternating']                       
colors  = ['tab:blue', 'tab:orange', 'tab:purple'] 
markers = ['o', 'D', '*']                          
data = [Xs_m1, Xs_m2, Xs_m3] 
lines = [ax.plot(dat[0][0:1], dat[1][0:1], dat[2][0:1], color = colors[i],linewidth = 0.6)[0] for i, dat in enumerate(data)] 
lines += [ax.plot(dat[0][0:1], dat[1][0:1], dat[2][0:1], color = colors[i],label = labels[i], marker = markers[i])[0] for i, dat in enumerate(data)] 
data += [Xs_m1, Xs_m2, Xs_m3] 
ax.set_xlim3d([min(min(Xs_m1[0]),min(Xs_m2[0])), max(max(Xs_m1[0]),max(Xs_m2[0]))]) 
ax.set_xlabel('X') 
ax.set_ylim3d([min(min(Xs_m1[1]),min(Xs_m2[1])), max(max(Xs_m1[1]),max(Xs_m2[1]))]) 
ax.set_ylabel('Y') 
ax.set_zlim3d([min(min(Xs_m1[2]),min(Xs_m2[2])), max(max(Xs_m1[2]),max(Xs_m2[2]))]) 
ax.set_zlabel('Z') 
ax.grid(False) 
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([]) 
ax.legend(loc='upper right') 
line_ani = animation.FuncAnimation(fig, update_lines, np.arange(0, tmax, 2), fargs=(data, lines, ax),interval=50, blit=False) 
line_ani.save('gifs/clifford3.mp4')