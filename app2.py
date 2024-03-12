import streamlit as st
from datetime import datetime

def main():
    st.title("Task Manager App")

    task_name = st.text_input("Enter task name:")
    due_date = st.date_input("Enter due date:")
    importance_input = st.selectbox("Importance:", ["Low", "Medium", "High"])
    category_input = st.selectbox("Category:", ["Work", "Personal", "Study", "Other"])

    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    if st.button("Add Task"):
        if task_name:
            task_due_date = due_date.strftime("%Y-%m-%d")
            st.session_state.tasks.append({"task": task_name, "due_date": task_due_date, "importance": importance_input, "category": category_input, "completed": False})
            st.success("Task added successfully!")
        else:
            st.error("Please enter a task name.")

    if st.session_state.tasks:
        st.header("Task List")
        for i, task in enumerate(st.session_state.tasks, start=1):
            importance_color = {"Low": "yellow", "Medium": "orange", "High": "red"}
            importance_style = f"color: {importance_color[task['importance']]}"
            category_color = {"Work": "blue", "Personal": "green", "Study": "orange", "Other": "gray"}
            category_style = f"color: {category_color[task['category']]}"

            task_complete = st.checkbox("", value=task['completed'], key=f"task_{i}")
            if task_complete != task['completed']:
                st.session_state.tasks[i-1]["completed"] = task_complete

            st.markdown(f"{i}. {task['task']} (Due: {task['due_date']}), (Importance: <span style='{importance_style}'>{task['importance']}</span>), (Category: <span style='{category_style}'>{task['category']}</span>)", unsafe_allow_html=True)


if __name__ == "__main__":
    main()