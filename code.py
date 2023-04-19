import streamlit as st

def find_largest_num(a, b, c):
    largest_num = a
    if b > largest_num:
        largest_num = b
    if c > largest_num:
        largest_num = c
    return largest_num

def main():
    st.title("Find the largest number")
    st.write("Enter three numbers below to find the largest one.")

    # Create three number input fields
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Display the largest number
    if st.button("Find largest number"):
        largest_num = find_largest_num(num1, num2, num3)
        st.write(f"The largest number is {largest_num}.")

if __name__ == '__main__':
    main()
