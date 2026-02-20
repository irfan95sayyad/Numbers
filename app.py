import streamlit as st
import random

st.title("🎲 Random Number Generator (1–61) - With Exclusions")

# Numbers to exclude
excluded_numbers = [
    2, 9, 13, 16, 21, 22, 23, 27, 28,
    34, 35, 39, 41, 45, 46, 47,
    52, 53, 54, 55, 56, 57, 58
]

# Create allowed numbers list
allowed_numbers = [num for num in range(1, 62) if num not in excluded_numbers]

st.write("Excluded numbers:", excluded_numbers)

if st.button("Generate Random Number"):
    number = random.choice(allowed_numbers)
    st.success(f"Your random number is: {number}")