import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons, RadioButtons

def lissajous(t, A, B, a, b, delta):
    x = A * np.sin(a * t + delta)
    y = B * np.cos(b * t)
    return x, y

def tangent(t_val, A, B, a, b, delta):
    dx_dt = A * a * np.cos(a * t_val + delta)
    dy_dt = -B * b * np.sin(b * t_val)
    return dx_dt, dy_dt

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.3)

t = np.linspace(0, 10, 500)
A, B, a, b, delta = 1, 1, 3, 2, 0
x, y = lissajous(t, A, B, a, b, delta)
line, = ax.plot(x, y)
point, = ax.plot([], [], marker='o', markersize=5, color='black')
tangent_line, = ax.plot([], [], linestyle='dashed', color='gray')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Lissajous Curve')

ax_slider_t = plt.axes([0.25, 0.20, 0.65, 0.03])
slider_t = Slider(ax_slider_t, 't', 1.6, 4.74, valinit=0)

show_tangent = False  

def update(val):
    global show_tangent
    t_val = slider_t.val

    x, y = lissajous(t, A, B, a, b, delta)
    line.set_data(x, y)


    x_point, y_point = lissajous(np.array([t_val]), A, B, a, b, delta) 
    point.set_data(x_point, y_point)

    if show_tangent:
        dx, dy = tangent(t_val, A, B, a, b, delta)

        tangent_x_start = x_point - 1*dx
        tangent_x_end = x_point + 1*dx

        tangent_y_start = y_point - 1*dy
        tangent_y_end = y_point + 1*dy

        tangent_line.set_data([tangent_x_start, tangent_x_end], [tangent_y_start, tangent_y_end])
    else:
        tangent_line.set_data([],[])

    fig.canvas.draw_idle()

slider_t.on_changed(update)

rax = plt.axes([0.05, 0.7, 0.15, 0.15])
check = CheckButtons(rax, ['Tangent'], [show_tangent])

def toggle_tangent(label):
    global show_tangent
    show_tangent = not show_tangent
    update(None)  
check.on_clicked(toggle_tangent)

resetax = plt.axes([0.05, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    slider_t.reset()
    update(None)
button.on_clicked(reset)

rax = plt.axes([0.3, 0.05, 0.6, 0.15])
radio = RadioButtons(rax, ('Синий - Сплошная', 'Красный - Пунктирная', 'Зелёный - Точечная'), active=0)

def color_change(label):
    if label == 'Синий - Сплошная':
        line.set_color('blue')
        line.set_linestyle('-')
    elif label == 'Красный - Пунктирная':
        line.set_color('red')
        line.set_linestyle('--')
    elif label == 'Зелёный - Точечная':
        line.set_color('green')
        line.set_linestyle(':')
    update(None)

radio.on_clicked(color_change)


plt.show()
