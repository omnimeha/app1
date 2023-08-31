import streamlit as st

def find_largest(n1, n2, n3):
    return max(n1, n2, n3)

def main():
    st.title("Find the Largest Number")
    
    n1 = st.number_input("Enter the first number:")
    n2 = st.number_input("Enter the second number:")
    n3 = st.number_input("Enter the third number:")
    
    if st.button("Find Largest"):
        largest = find_largest(n1, n2, n3)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()

