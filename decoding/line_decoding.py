# decoding/line_decoding.py
"""
Line Decoding Schemes for Digital Signal Generator
Author: Hamza Mehmood
"""

def nrz_l_decode(signal):
    """NRZ-L decoding: 1 = High, 0 = Low"""
    return ''.join(['1' if x == 1 else '0' for x in signal])


def nrz_i_decode(signal):
    """NRZ-I decoding: change = 1, no change = 0"""
    if not signal:
        return ''
    decoded = '0'
    last = signal[0]
    for i in range(1, len(signal)):
        decoded += '1' if signal[i] != last else '0'
        last = signal[i]
    return decoded


def manchester_decode(signal):
    """Manchester decoding: low→high = 1, high→low = 0"""
    decoded = ''
    for i in range(0, len(signal), 2):
        if i + 1 >= len(signal):
            break
        if signal[i] < signal[i + 1]:
            decoded += '1'
        else:
            decoded += '0'
    return decoded


def diff_manchester_decode(signal):
    """Differential Manchester decoding"""
    decoded = ''
    if len(signal) < 2:
        return decoded
    last_mid = signal[1]
    for i in range(2, len(signal) - 1, 2):
        mid = signal[i + 1]
        decoded += '1' if mid == last_mid else '0'
        last_mid = mid
    return decoded


def ami_decode(signal):
    """AMI decoding: polarity alternates for 1s"""
    decoded = ''
    for v in signal:
        decoded += '1' if v != 0 else '0'
    return decoded
