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

def subplots(signal, fft_signal, samples, freqs, fs, title1, title2):
    #plot time and freq domain subplots
    fig, axes = plt.subplots(1,2, figsize = (12,4))
    x = np.arange(1,11)
    axes[0].plot(samples[0:500],signal[0:500])
    axes[0].grid(True)
    axes[0].set_title(title1)
    axes[0].set_xlabel('Samples')
    axes[0].set_ylabel('Amplitude')
    axes[1].plot(freqs[int(fs/2):], fft_signal[int(fs/2):])
    axes[1].grid(True)
    axes[1].set_title(title2)
    axes[1].set_xlabel('Frequency, Hz')
    axes[1].set_ylabel('Amplitude, dB')
    fig.tight_layout()
    plt.show()
    
    return

def QAM_subplots(signal_I, signal_Q, fft_signal_I, fft_signal_Q, samples, freqs, fs, title1, title2, label_I, label_Q, legend_title):
    #plot I and Q in time and freq domains
    fig, axes = plt.subplots(1,2, figsize = (12,4))
    x = np.arange(1,11)
    axes[0].plot(samples[0:500],signal_I[0:500], label = label_I)
    axes[0].plot(samples[0:500],signal_Q[0:500], label = label_Q)
    axes[0].grid(True)
    axes[0].set_title(title1)
    axes[0].set_xlabel('Samples')
    axes[0].set_ylabel('Amplitude')
    axes[0].legend(title = legend_title)
    
    axes[1].plot(freqs[int(fs/2):], fft_signal_I[int(fs/2):], label=label_I)
    axes[1].plot(freqs[int(fs/2):], fft_signal_Q[int(fs/2):], label=label_Q)
    axes[1].grid(True)
    axes[1].set_title(title2)
    axes[1].set_xlabel('Frequency, Hz')
    axes[1].set_ylabel('Amplitude, dB')
    axes[1].legend(title = legend_title)
    
    fig.tight_layout()
    plt.show()
    
    return

def complex_subplots(signal_I, signal_Q, fft_signal, samples, freqs, fs, label_I, label_Q, title1, title2, legend_title):
    #plot I and Q in time, single plot in freq
    fig, axes = plt.subplots(1,2, figsize = (12,4))
    x = np.arange(1,11)
    axes[0].plot(samples[0:500],signal_I[0:500], label = label_I)
    axes[0].plot(samples[0:500],signal_Q[0:500], label = label_Q)
    axes[0].grid(True)
    axes[0].set_title(title1)
    axes[0].set_xlabel('Samples')
    axes[0].set_ylabel('Amplitude')
    axes[0].legend(title = legend_title)
    
    axes[1].plot(freqs[int(fs/2):], fft_signal[int(fs/2):])
    axes[1].grid(True)
    axes[1].set_title(title2)
    axes[1].set_xlabel('Frequency, Hz')
    axes[1].set_ylabel('Amplitude, dB')
    fig.tight_layout()
    plt.show()
    
    return

def find_fft(signal, n_window):
    fft = np.fft.fftshift(np.fft.fft(signal, n_window))

    return 10*np.log10(abs(fft)/len(signal))

