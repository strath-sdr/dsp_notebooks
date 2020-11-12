import numpy as np
import matplotlib.pyplot as plt

def plot_iq_timeseries(x, ax=None, **kwargs):
    if ax is None:
        ax = plt.gca()
    ax.plot(np.real(x), **kwargs)
    ax.plot(np.imag(x), **kwargs)
    ax.set_title('Time series plot')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Magnitude')
    ax.legend(('Real', 'Imaginary'))
    return ax

def frequency_plot(freqs, signal_db, ax=None):
    if ax is None:
        ax = plt.gca()
    plt.plot(freqs, signal_db)
    plt.title('FFT plot')
    plt.xlabel('Frequency, Hz')
    plt.ylabel('Amplitude, dB')
    return ax

def scatterplot(x, y, ax=None):
    if ax is None:
        plt.figure(figsize=(5,5))
        ax = plt.gca()
    ax.scatter(x,y)
    ax.set_title('Constellation plot')
    ax.set_xlabel('Channel 1 amplitude')
    ax.set_ylabel('Channel 2 amplitude')
    return ax

def scatterplot_with_ref(x, x_ref, ax=None):
    if ax is None:
        plt.figure(figsize=(5,5))
        ax = plt.gca()
    ax.scatter(np.real(x), np.imag(x))
    ax.scatter(np.real(x_ref), np.imag(x_ref), s=120, c='red', marker='x')
    ax.set_title('Constellation plot')
    ax.set_xlabel('Channel 1 amplitude')
    ax.set_ylabel('Channel 2 amplitude')
    ax.legend(('Received symbols', 'Reference points'), \
           bbox_to_anchor=(1, 1), loc='upper left')
    return ax