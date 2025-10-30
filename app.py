import streamlit as st
import numpy as np

# === Import helper modules ===
from utils.helpers import get_binary_input, get_analog_input
from utils.palindrome import longest_palindrome
from utils.plotting import plot_signal

# === Encoding modules ===
from encoding.line_coding import nrz_l, nrz_i, manchester, diff_manchester, ami
from encoding.scrambling import b8zs, hdb3

# === Modulation modules ===
from modulation.pcm import pcm_encode
from modulation.delta_modulation import delta_modulation

# === Decoding modules ===
from decoding.line_decoding import (
    nrz_l_decode,
    nrz_i_decode,
    manchester_decode,
    diff_manchester_decode,
    ami_decode,
)

# ------------------- Streamlit UI -------------------
st.set_page_config(page_title="Digital Signal Generator", layout="wide")

st.title("⚡ DIGITAL SIGNAL GENERATOR")
st.write("Developed by **Hamza (2023BITE048)** and **Ommer (2023BITE002)** and **Deepanshu(2023BITE052)**, NIT Srinagar, Department of IT")

# Initialize session state for persistence
if "encoded_signal" not in st.session_state:
    st.session_state.encoded_signal = None
if "encoded_scheme" not in st.session_state:
    st.session_state.encoded_scheme = None
if "encoded_data" not in st.session_state:
    st.session_state.encoded_data = None

# ------------------- INPUT TYPE -------------------
input_type = st.radio("Select Input Type:", ["Digital", "Analog"])

# ------------------- DIGITAL INPUT -------------------
if input_type == "Digital":
    data = st.text_input("Enter binary data stream (e.g. 1011001):").strip()

    if data:
        st.write(f"**Data Stream:** {data}")
        st.write(f"**Longest Palindromic Sequence:** `{longest_palindrome(data)}`")

        scheme = st.selectbox(
            "Select Line Coding Scheme:",
            ["NRZ-L", "NRZ-I", "Manchester", "Differential Manchester", "AMI"],
        )

        scramble = None
        scrambled_data = None

        # Scrambling only appears for AMI
        if scheme == "AMI":
            apply_scramble = st.radio("Apply Scrambling?", ["No", "Yes"])
            if apply_scramble == "Yes":
                scramble = st.selectbox("Choose Scrambling Scheme:", ["B8ZS", "HDB3"])

        if st.button("🔹 Generate Encoded Signal"):
            # Encode signal
            if scheme == "NRZ-L":
                signal = nrz_l(data)
            elif scheme == "NRZ-I":
                signal = nrz_i(data)
            elif scheme == "Manchester":
                signal = manchester(data)
            elif scheme == "Differential Manchester":
                signal = diff_manchester(data)
            elif scheme == "AMI":
                signal = ami(data)
            else:
                signal = []

            # Apply scrambling if selected
            if scheme == "AMI" and scramble:
                if scramble == "B8ZS":
                    scrambled_data = b8zs(data)
                    st.success(f"✅ B8ZS Scrambled Data: {scrambled_data}")
                elif scramble == "HDB3":
                    scrambled_data = hdb3(data)
                    st.success(f"✅ HDB3 Scrambled Data: {scrambled_data}")

            # Save to session
            st.session_state.encoded_signal = signal
            st.session_state.encoded_scheme = scheme
            st.session_state.encoded_data = scrambled_data if scrambled_data else data

            # Plot
            if len(signal) > 0:
                title = f"{scheme} Encoding"
                if scramble:
                    title += f" + {scramble}"
                st.pyplot(plot_signal(data, signal, title))

    # ------------------- DECODING SECTION -------------------
    if st.session_state.encoded_signal is not None:
        if st.button("🔁 Decode Last Encoded Signal"):
            scheme = st.session_state.encoded_scheme
            signal = st.session_state.encoded_signal

            try:
                if scheme == "NRZ-L":
                    decoded = nrz_l_decode(signal)
                elif scheme == "NRZ-I":
                    decoded = nrz_i_decode(signal)
                elif scheme == "Manchester":
                    decoded = manchester_decode(signal)
                elif scheme == "Differential Manchester":
                    decoded = diff_manchester_decode(signal)
                elif scheme == "AMI":
                    decoded = ami_decode(signal)
                else:
                    decoded = "⚠️ Decoding not available for this scheme."
            except Exception as e:
                decoded = f"❌ Decoding Error: {e}"

            st.subheader("🔹 Decoded Data Stream")
            st.code(decoded)

# ------------------- ANALOG INPUT -------------------
elif input_type == "Analog":
    analog_input = st.text_input("Enter analog values separated by spaces (e.g. 0.1 0.4 0.7 1.0):")

    if analog_input:
        try:
            analog_signal = [float(x) for x in analog_input.split()]
            mod_scheme = st.selectbox("Select Modulation Technique:", ["PCM", "Delta Modulation"])

            if st.button("🔹 Generate Modulated + Encoded Signal"):
                if mod_scheme == "PCM":
                    data = pcm_encode(analog_signal)
                    st.success(f"PCM Encoded Data: {data}")
                elif mod_scheme == "Delta Modulation":
                    data = delta_modulation(analog_signal)
                    st.success(f"Delta Modulated Data: {data}")
                else:
                    st.error("Invalid modulation scheme.")
                    data = ""

                if data:
                    signal = nrz_l(data)
                    st.session_state.encoded_signal = signal
                    st.session_state.encoded_scheme = "NRZ-L"
                    st.session_state.encoded_data = data
                    st.pyplot(plot_signal(data, signal, f"{mod_scheme} + NRZ-L Encoding"))

        except ValueError:
            st.error("Please enter valid numeric analog values.")

    # Decode section for analog
    if st.session_state.encoded_signal is not None:
        if st.button("🔁 Decode Modulated Signal"):
            signal = st.session_state.encoded_signal
            decoded = nrz_l_decode(signal)
            st.subheader("🔹 Decoded Binary Stream")
            st.code(decoded)

# ------------------- FOOTER -------------------
st.markdown("---")
st.caption("🎓 Project by Hamza (2023BITE048) and Omar (2023BITE002) | NIT Srinagar | Digital Signal Generator © 2025")

