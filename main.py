# main.py
from utils.helpers import get_binary_input, get_analog_input
from utils.palindrome import longest_palindrome
from utils.plotting import plot_signal
from encoding.line_coding import nrz_l, nrz_i, manchester, diff_manchester, ami
from encoding.scrambling import b8zs, hdb3
from modulation.pcm import pcm_encode
from modulation.delta_modulation import delta_modulation
from decoding.line_decoding import (
    decode_nrz_l, decode_nrz_i, decode_manchester, decode_diff_manchester, decode_ami
)
import numpy as np

def main():
    print("=== DIGITAL SIGNAL GENERATOR ===")
    input_type = input("Enter input type (analog/digital): ").strip().lower()

    # -------------------- DIGITAL INPUT --------------------
    if input_type == "digital":
        data = get_binary_input()
        print(f"Data stream: {data}")
        print(f"Longest palindrome: {longest_palindrome(data)}")

        print("\nChoose Line Coding Scheme:")
        print("1. NRZ-L\n2. NRZ-I\n3. Manchester\n4. Differential Manchester\n5. AMI")
        choice = input("Enter choice: ").strip()

        signal = None
        if choice == '1':
            signal = nrz_l(data)
            plot_signal(data, signal, "NRZ-L Encoding")

        elif choice == '2':
            signal = nrz_i(data)
            plot_signal(data, signal, "NRZ-I Encoding")

        elif choice == '3':
            signal = manchester(data)
            plot_signal(data, signal, "Manchester Encoding")

        elif choice == '4':
            signal = diff_manchester(data)
            plot_signal(data, signal, "Differential Manchester Encoding")

        elif choice == '5':
            signal = ami(data)
            scramble = input("Do you want to apply scrambling? (y/n): ").strip().lower()
            if scramble == 'y':
                print("Choose Scrambling: 1. B8ZS  2. HDB3")
                s_type = input("Enter choice: ").strip()
                if s_type == '1':
                    scrambled = b8zs(data)
                    print("Scrambled (B8ZS):", scrambled)
                elif s_type == '2':
                    scrambled = hdb3(data)
                    print("Scrambled (HDB3):", scrambled)
            plot_signal(data, signal, "AMI Encoding")

        else:
            print("Invalid choice.")
            return

        # -------------------- DECODING OPTION --------------------
        decode_choice = input("Do you want to decode this signal? (y/n): ").strip().lower()
        if decode_choice == 'y':
            decoded = None
            if choice == '1':
                decoded = decode_nrz_l(signal)
            elif choice == '2':
                decoded = decode_nrz_i(signal)
            elif choice == '3':
                decoded = decode_manchester(signal)
            elif choice == '4':
                decoded = decode_diff_manchester(signal)
            elif choice == '5':
                decoded = decode_ami(signal)

            if decoded:
                print("Decoded data stream:", decoded)
            else:
                print("Decoding failed or not implemented for this scheme.")

    # -------------------- ANALOG INPUT --------------------
    elif input_type == "analog":
        analog_signal = get_analog_input()
        print("\nChoose Modulation Technique:")
        print("1. PCM\n2. Delta Modulation")
        mod_choice = input("Enter choice (1/2): ").strip()

        if mod_choice == '1':
            data = pcm_encode(analog_signal)
            print("PCM Encoded Data:", data)
            signal = nrz_l(data)
            plot_signal(data, signal, "PCM + NRZ-L Encoding")

        elif mod_choice == '2':
            data = delta_modulation(analog_signal)
            print("Delta Modulated Data:", data)
            signal = nrz_l(data)
            plot_signal(data, signal, "DM + NRZ-L Encoding")

        else:
            print("Invalid modulation choice.")
            return

    else:
        print("Invalid input type.")

if __name__ == "__main__":
    main()
