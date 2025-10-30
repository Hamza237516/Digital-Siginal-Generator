def decode_nrz_l(signal):
    return ''.join(['1' if level == 1 else '0' for level in signal])

def decode_nrz_i(signal):
    result, last = [], 1
    for level in signal:
        bit = '1' if level != last else '0'
        result.append(bit)
        last = level
    return ''.join(result)

def decode_manchester(signal):
    bits = []
    for i in range(0, len(signal), 2):
        bits.append('1' if signal[i] == 1 else '0')
    return ''.join(bits)
