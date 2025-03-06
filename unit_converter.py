import streamlit as st 

st.write("<h1 style='text-align: center; color: black;'>⚖️Simple Unit Converter 🧮</h1>", unsafe_allow_html=True)

st.write("<h5 style='text-align: center; color: gray;'>Convert different units easily!</h5>", unsafe_allow_html=True)

# User se input lena:
number = st.number_input("🔢 Enter the value:")

# Conversion options:
units = ["Kilometer to Miles", "Miles to Kilometers", "Celsius to Fahrenheit", "Fahrenheit to Celsius"]

conversion_type = st.selectbox("📍 Select conversion type:", units)

# Conversion logic:

if conversion_type == "Kilometers to Miles":
    result = number * 0.621371
elif conversion_type == "Miles to Kilometers":
    result = number * 0.621371
elif conversion_type == "Celsius to Fahrenheit":
    result = (number * 9/5) + 32
elif conversion_type == "Fahrenheit to Celsius":
    result = (number - 32) * 5/9
else:
    result = "Invalid Selection"

st.write("Converted Value:", result)



