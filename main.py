import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Our Edit Attempt",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://github.com/Siddhesh-Agarwal/CGPA-Calculator/discussions",
        "Report a bug": "https://github.com/Siddhesh-Agarwal/CGPA-Calculator/issues/new",
        "About": None,
    },
)

# Function to initialize counter
def initialize_counter():
    return 0

# Function to increment counter
def increment_counter(counter):
    return counter + 1

# Main function
def main():
    st.title('Click Counter')

    # Initialize counter
    if 'counter' not in st.session_state:
        st.session_state.counter = initialize_counter()

    # Display current count
    st.write('Number of times button clicked:', st.session_state.counter)

    # Button to increment counter
    if st.button('Click me!'):
        st.session_state.counter = increment_counter(st.session_state.counter)
    tasks_df = pd.DataFrame(columns=["Task", "Status", "Deadline"])

    def add_task(task):
        global tasks_df
        tasks_df = tasks_df.append({"Task": task, "Status": "Pending"}, ignore_index=True)
    
    def complete_task(index):
        global tasks_df
        tasks_df.at[index, "Status"] = "Complete"
    
    def delete_task(index):
        global tasks_df
        tasks_df.drop(index, inplace=True)

    task_input = st.text_input("Add Task:")
    deadline_input = st.date_input("Choose Deadline:")
    if st.button("Add"):
        add_task(task_input, deadline_input)
    
    st.write(tasks_df)
    
    for index, row in tasks_df.iterrows():
        if st.button(f"Complete Task {index}"):
            complete_task(index)
        if st.button(f"Delete Task {index}"):
            delete_task(index)
# Run the app
if __name__ == '__main__':
    main()
