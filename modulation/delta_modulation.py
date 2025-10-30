def delta_modulation(analog_signal, delta=0.1):
    encoded = []
    last = analog_signal[0]
    for sample in analog_signal:
        if sample > last:
            encoded.append('1')
            last += delta
        else:
            encoded.append('0')
            last -= delta
    return ''.join(encoded)
