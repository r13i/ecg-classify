
from scipy.signal import butter, lfilter, filtfilt


def butter_lowpass (cutoff_freq, sampling_freq, order) :
    nyquist_freq = sampling_freq / 2
    normalized_cutoff = cutoff_freq / nyquist_freq
    b, a = butter (order, normalized_cutoff, "lowpass", analog=False)    # 'b' is the numerator, 'a' the denominator
    return b, a

def butter_highpass (cutoff_freq, sampling_freq, order) :
    nyquist_freq = sampling_freq / 2
    normalized_cutoff = cutoff_freq / nyquist_freq
    b, a = butter (order, normalized_cutoff, "highpass", analog=False)    # 'b' is the numerator, 'a' the denominator
    return b, a

def butter_bandpass (low_cutoff_freq, high_cutoff_freq, sampling_freq, order) :
    nyquist_freq = sampling_freq / 2
    normalized_low = low_cutoff_freq / nyquist_freq
    normalized_high = high_cutoff_freq / nyquist_freq
    b, a = butter (order, [normalized_low, normalized_high], "bandpass", analog=False)    # 'b' is the numerator, 'a' the denominator
    return b, a

def butter_bandstop (low_cutoff_freq, high_cutoff_freq, sampling_freq, order) :
    nyquist_freq = sampling_freq / 2
    normalized_low = low_cutoff_freq / nyquist_freq
    normalized_high = high_cutoff_freq / nyquist_freq
    b, a = butter (order, [normalized_low, normalized_high], "bandstop", analog=False)    # 'b' is the numerator, 'a' the denominator
    return b, a

def apply_butter (x, b, a, linear_phase=False):
    if linear_phase:
        return filtfilt (b, a, x)    # See the doc for hint on performance improvement
    else:
        return lfilter (b, a, x)


def butter_filter (x, filter_type, cutoff_freqs, sampling_freq=360, order=3, linear_phase=False):
    assert(isinstance(cutoff_freqs, list))
    assert(cutoff_freqs[0] <= cutoff_freqs[-1])

    if filter_type == "highpass":
        b, a = butter_highpass (cutoff_freqs[0], sampling_freq, order)
    elif filter_type == "lowpass":
        b, a = butter_lowpass (cutoff_freqs[0], sampling_freq, order)
    elif filter_type == "bandpass":
        b, a = butter_bandpass (cutoff_freqs[0], cutoff_freqs[-1], sampling_freq, order)
    elif filter_type == "bandstop":
        b, a = butter_bandstop (cutoff_freqs[0], cutoff_freqs[-1], sampling_freq, order)
    else:
        raise ValueError("Non-recognized filter type !")

    return apply_butter (x, b, a, linear_phase)