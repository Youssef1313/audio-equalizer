from scipy import signal
from pzmap import pzmap
import matplotlib.pyplot as plt
import numpy as np


def get_bands():
    return [[0, 170],
            [170, 310],
            [310, 600],
            [600, 1000],
            [1000, 3000],
            [3000, 6000],
            [6000, 12000],
            [12000, 14000],
            [14000, 16000]]


def iir_filter(order, fs):
    iir_filters = []
    bands = get_bands()
    for i in range(len(bands)):
        lis = [bands[i][0]*2 / fs, bands[i][1]*2 / fs]
        if lis[1] >= 1:
            return iir_filters
        if lis[0] == 0:
            current_filter = signal.iirfilter(order, lis[1], btype='lowpass')
        else:
            current_filter = signal.iirfilter(order, lis)
        iir_filters.append([current_filter])

    return iir_filters


def plot_zeros_poles(p_z):
    for ele in (p_z):
        z = signal.TransferFunction(ele[0], ele[1])
        pzmap(z.zeros, z.poles)


def plot_mag_phase(filters):
    # i = 0
    for fi in filters:
        w, h = signal.freqz(fi[0][0], fi[0][1])
        fig, ax1 = plt.subplots()
        ax1.set_title('Digital filter frequency response ')
        ax1.plot(w, 20 * np.log10(abs(h)), 'b')
        ax1.set_ylabel('Amplitude [dB]', color='b')
        ax1.set_xlabel('Frequency [rad/sample]')

        ax2 = ax1.twinx()
        angles = np.unwrap(np.angle(h))
        ax2.plot(w, angles, 'g')
        ax2.set_ylabel('Angle (radians)', color='g')
        ax2.grid()
        ax2.axis('tight')
    plt.show()


# def plot_impl_unitstep(filters):
#     for filter in filters:
#         impz(filter[0], filter[1])
