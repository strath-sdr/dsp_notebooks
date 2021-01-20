import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

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

<<<<<<< Updated upstream
def tripleSubplots(fft1, fft2, fft3, samples, freqs, fs, title1, title2, title3):
    fig, axes = plt.subplots(1,3, figsize = (12,4))
    size = np.arange(1,11)
    axes[0].plot(freqs[int(fs/2):], fft1[int(fs/2):])
    axes[0].grid(True)
    axes[0].set_title(title1)
    axes[0].set_xlabel('Frequency, Hz')
    axes[0].set_ylabel('Amplitude, dB')
    axes[1].plot(freqs[int(fs/2):], fft2[int(fs/2):])
    axes[1].grid(True)
    axes[1].set_title(title2)
    axes[1].set_xlabel('Frequency, Hz')
    axes[1].set_ylabel('Amplitude, dB')
    axes[2].plot(freqs[int(fs/2):], fft3[int(fs/2):])
    axes[2].grid(True)
    axes[2].set_title(title3)
    axes[2].set_xlabel('Frequency, Hz')
    axes[2].set_ylabel('Amplitude, dB')
    fig.tight_layout()
    plt.show()
    
    return

=======
# Function to calculate Power Spectral Density (PSD)
# Uses Welch's average periodogram method

# Input: signal of interest, fft size, window type 
# and overlap ratio. 

# Output: PSD estimate linear scale 

def psd(sig,nfft,wtype,overlap):

    # Input checking 
    if (wtype != 'Hamming') and (wtype != 'Bartlett') \
        and (wtype != 'Blackman') and (wtype != 'Hann')\
        and (wtype != 'Rectangle'):  
        
        raise Exception('Window must be: Hamming, Bartlett, Blackman, Hann or Rectangle.')   
        
    if (overlap < 0) or (overlap > 1):
        
        raise Exception('Overlap ratio must be between 0 and 1.')
        
    # Compute window coefficients 
    if wtype == 'Hamming':
        window = signal.windows.hamming(nfft,0)
    elif wtype == 'Bartlett':
        window = signal.windows.bartlett(nfft,0)
    elif wtype ==  'Blackman':
        window = signal.windows.blackman(nfft,0)
    elif wtype ==  'Hann':
        window = signal.windows.hann(nfft,0)
    elif wtype == 'Rectangle':
        window = signal.windows.boxcar(nfft)
        
    # Calculate no. of overlap samples
    noverlap = math.floor(nfft*overlap)
    
    # No. of FFTs to evaluate 
    length = sig.size
    num_fft = (length - noverlap) // (nfft - noverlap)
    
    # Initialise vector to hold periodograms 
    pgram_vec = np.zeros(num_fft*nfft)
    j = 0 
    k = 0 
    
    for i in range(num_fft):
        
        # Compute periodogram using sliding window  
        pgram_vec[j:j+nfft] = np.abs(np.fft.fft(sig[k:k+nfft],nfft) * window) ** 2
        
        # Increment j & k 
        j = j + nfft
        k = k + (nfft - noverlap)
       
    # Reshape periodogram vector 
    pgram_res = pgram_vec.reshape(num_fft,nfft)
    
    # Average over 1st dimension to get PSD estimate   
    psd_est = np.sum(pgram_res,0,np.float64)/num_fft
    
    return psd_est
	
def awgn(signal,SNR):
    # Measure signal power 
    s_p = np.mean(abs(signal)**2)
    
    # Calculate noise power 
    n_p = s_p/(10 **(SNR/10))
    
    # Generate complex noise 
    noise = np.random.normal(0,np.sqrt(n_p/2),len(signal)) + \
        np.random.normal(0,np.sqrt(n_p/2),len(signal))
    
    # Add signal and noise 
    signal_noisy = signal + noise 
    
    return signal_noisy   
	
# Function to generate a block of BPSK, QPSK or 16-QAM symbols
def symbol_gen(nsym,mod_scheme):
    
    if mod_scheme == 'BPSK':
        # 1 bit per symbol for BPSK 
        m = 1  
        M = 2 ** m 
    
        # BPSK symbol values
        bpsk = [-1+0j, 1+0j]
        
        # Generate random integers 
        ints = np.random.randint(0,M,nsym)
        
        # Generate BPSK symbols 
        data = [bpsk[i] for i in ints]
        data = np.array(data,np.complex64)

    elif mod_scheme == 'QPSK': 
        # 2 bits per symbol for QPSK 
        m = 2
        M = 2 ** m 
    
        # QPSK symbol values 
        qpsk = [1+1j, -1+1j, 1-1j, -1-1j] / np.sqrt(2)
        
        # Generate random integers 
        ints = np.random.randint(0,M,nsym)
    
        # Map to QPSK symbols 
        data = [qpsk[i] for i in ints]
        data = np.array(data,np.complex64)
        
    elif mod_scheme == '16-QAM': 
        # 4 bits per symbol for 16-QAM 
        m = 4 
        M = 2 ** m 
        
        # 16-QAM symbol values  
        qam16 = [-3-3j, -3-1j, -3+3j, -3+1j,  \
                -1-3j, -1-1j, -1+3j, -1+1j,  \
                 3-3j,  3-1j,  3+3j,  3+1j,  \
                 1-3j,  1-1j,  1+3j,  1+1j] / np.sqrt(10)
        
        # Generate random integers 
        ints = np.random.randint(0,M,nsym)
        
        # Map to 16-QAM symbols 
        data = [qam16[i] for i in ints]
        data = np.array(data,np.complex64)
        
    else: 
        raise Exception('Modulation method must be BPSK, QPSK or 16-QAM.')
    
    return data 

def calculate_evm(symbols_tx, symbols_rx):
    evm_rms = np.sqrt(np.mean(np.abs(symbols_rx - symbols_tx )**2)) / \
              np.sqrt(np.mean(np.abs(symbols_tx)**2))
    
    return evm_rms*100
>>>>>>> Stashed changes
