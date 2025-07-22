import streamlit as st

st.title("Boss-Level Calculator")

# User inputs
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Cannot divide by zero!")
