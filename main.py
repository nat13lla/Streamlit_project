import streamlit as st
# streamlit run test.py

# Function to initialize counter
def initialize_counter():
    return 0

# Function to increment counter
def increment_counter(counter):
    return counter + 1

# Main function
def main():
    st.title('Button Click Counter')

    # Initialize counter
    if 'counter' not in st.session_state:
        st.session_state.counter = initialize_counter()

    # Display current count
    st.write('Number of times button clicked:', st.session_state.counter)

    # Button to increment counter
    if st.button('Click me!'):
        st.session_state.counter = increment_counter(st.session_state.counter)

# Run the app
if __name__ == '__main__':
    main()
