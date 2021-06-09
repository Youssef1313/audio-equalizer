from scipy import signal

freqs = [[0,170],
         [170,310],
         [310,600],
         [600,1000],
         [1000,3000],
         [3000,6000],
         [6000,12000],
         [12000,14000],
         [14000,16000]
]

def iir_filter(fs):
    n = 10
    wn = []
    irr_filters = []
    for i in range(len(freqs)):
        lis = [freqs[i][0] / fs,freqs[i][1] / fs]
        if lis[1] >= 1 and i != 0:
            wn.append(wn[i - 1])
        wn.append(lis)
    if len(wn) == 0:
        for i in range(len(freqs)):
            b, a = signal.iirfilter(n, fs / fs, btype = 'lowpass')
            irr_filters.append([b, a])
    else:
        for i in range(len(freqs)):
            b, a = signal.iirfilter(n, wn[i])
            lis = [b, a]
            irr_filters.append(lis)
    return irr_filters

