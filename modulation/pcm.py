import numpy as np

def pcm_encode(analog_signal, levels=8):
    """
    Simple PCM encoding: quantization + binary conversion.
    Handles constant (flat) input gracefully.
    """
    analog_signal = np.array(analog_signal, dtype=float)
    min_val = np.min(analog_signal)
    max_val = np.max(analog_signal)

    # Handle case where all samples are the same
    if max_val == min_val:
        quantized = [levels // 2] * len(analog_signal)
    else:
        step = (max_val - min_val) / levels
        if step == 0:
            step = 1e-9  # safety net
        quantized = [int((sample - min_val) / step) for sample in analog_signal]

    # Clip values to valid range
    quantized = np.clip(quantized, 0, levels - 1)

    # Convert each quantized level to binary
    bits_per_sample = int(np.ceil(np.log2(levels)))
    binary_data = ''.join([format(q, f'0{bits_per_sample}b') for q in quantized])

    return binary_data
