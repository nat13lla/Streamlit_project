import streamlit as st
import numpy as np
import pandas as pd

tasks_df = pd.DataFrame(columns=["Task", "Status", "Deadline"])
    
# Main function
def main():
    def add_task(task, deadline):
        global tasks_df
        new_task_df = pd.DataFrame({"Task": [task], "Status": ["Pending"], "Deadline": [deadline]})
        tasks_df = pd.concat([tasks_df, new_task_df], ignore_index=True)
    
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
