import numpy as np

def eulerstep(F, t, y, h, args):
    return h*F(t, y, args)

def euler(F, ts, y_atual, h, args):
    t_atual = ts[0]
    ys = [y_atual]
    for i in range(len(ts)-1):
        passo = eulerstep(F, t_atual, y_atual, h, args)
        y_next = y_atual + passo
        ys.append(y_next)
        t_atual = ts[i+1]
        y_atual = y_next
    
    return np.array(ys).T, ts

def rk4step(F, t, y, h, args):
    """Passo de Runge-Kutta de ordem 4"""
    k1 = h*F(t,     y, args)
    k2 = h*F(t+h/2, y+k1/2, args)
    k3 = h*F(t+h/2, y+k2/2, args)
    k4 = h*F(t+h,   y+k3, args)
    return (k1 + 2*k2 + 2*k3 + k4)/6

def rk4(F, ts, y_atual, h, args):
    
    t_atual = ts[0]
    ys = [y_atual]
    for i in range(len(ts)-1):
        passo = rk4step(F, t_atual, y_atual, h, args)
        y_next = y_atual + passo
        ys.append(y_next)
        
        t_atual = ts[i+1]
        y_atual = y_next
        
    return np.array(ys).T, ts

def modn(F, ts, y_atual, h, n, m1, m2, args):
    t_atual = ts[0]
    ys = [y_atual]
    for i in range(len(ts)-1):
        if i%n == 0: 
            passo = m2(F, t_atual, y_atual, h, args)
        else:
            passo = m1(F, t_atual, y_atual, h, args)
        y_next = y_atual + passo
        ys.append(y_next)
        
        t_atual = ts[i+1]
        y_atual = y_next
        
    return np.array(ys).T, ts

def update_lines(num, dataLines, lines, ax):
    colors  = ['tab:blue', 'tab:orange', 'tab:purple']
    markers = ['o', 'D', '*']
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        if lines.index(line) < len(lines)//2:
            line.set_data([data[0][0:num], data[1][0:num]])
            line.set_3d_properties(data[2][:num])
            line.set_color(colors[lines.index(line)])
        else:
            line.set_data([data[0][num], data[1][num]])
            line.set_3d_properties(data[2][num])
            line.set_marker(markers[lines.index(line)-len(lines)//2])
            line.set_color(colors[lines.index(line)-len(lines)//2])
        ax.view_init(30, num)
    return lines
