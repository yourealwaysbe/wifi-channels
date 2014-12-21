#!/usr/bin/python

from wifi import Cell
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys


def get_color(address):
    r = 0
    g = 0
    b = 0

    for c in address:
        i = ord(c)
        pick = i % 3
        if pick == 0:
            r = 2*r + i 
        elif pick == 1:
            g = 2*g + i
        else:
            b = 2*b + i

    rs = hex(r % 256)[2:].zfill(2)
    gs = hex(g % 256)[2:].zfill(2)
    bs = hex(b % 256)[2:].zfill(2)

    return '#' + rs + gs + bs

def plot_channel_data(frame):
    plt.cla()
    for c in Cell.all(interface):
        ch = c.channel
        s = 100 + c.signal

        x = np.linspace(ch-2, ch+2, 50)
        y = s * np.sin((x - ch + 2) / 4 * np.pi)

        col = get_color(c.ssid + c.address)

        plt.fill(x, y, col, alpha=0.3)
        plt.annotate(c.ssid, (ch, s))


if len(sys.argv) != 2:
    print("Usage: wifi-channels <interface>")
    print("Needs root access.")
else:
    interface = sys.argv[1]
    fig, ax = plt.subplots()
    plt.grid(True)
    animation.FuncAnimation(fig, plot_channel_data, interval=5000)
    plt.show()
