import numpy as np

def nrz_l(data):
    return np.array([1 if bit == '1' else -1 for bit in data])

def nrz_i(data):
    signal, last = [], 1
    for bit in data:
        if bit == '1':
            last *= -1
        signal.append(last)
    return np.array(signal)

def manchester(data):
    signal = []
    for bit in data:
        if bit == '1':
            signal.extend([1, -1])
        else:
            signal.extend([-1, 1])
    return np.array(signal)

def diff_manchester(data):
    signal = []
    last = 1
    for bit in data:
        if bit == '0':
            last *= -1
        signal.extend([last, -last])
    return np.array(signal)

def ami(data):
    signal = []
    last = -1
    for bit in data:
        if bit == '1':
            last *= -1
            signal.append(last)
        else:
            signal.append(0)
    return np.array(signal)
