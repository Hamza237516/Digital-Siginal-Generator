def b8zs(data):
    result = ""
    zero_count = 0
    for i, bit in enumerate(data):
        result += bit
        if bit == '0':
            zero_count += 1
        else:
            zero_count = 0
        if zero_count == 8:
            result = result[:-8] + "000VB0VB"
            zero_count = 0
    return result

def hdb3(data):
    result = ""
    zero_count = 0
    pulse_count = 0
    for bit in data:
        result += bit
        if bit == '0':
            zero_count += 1
            if zero_count == 4:
                if pulse_count % 2 == 0:
                    result = result[:-4] + "B00V"
                else:
                    result = result[:-4] + "000V"
                zero_count = 0
                pulse_count = 0
        else:
            pulse_count += 1
            zero_count = 0
    return result
