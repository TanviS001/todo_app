import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List App")

new_task = st.text_input("Add a new task:", placeholder="Enter your task here...")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task.strip(), "completed": False})
        st.success("Task added successfully!")
    else:
        st.error("Task cannot be empty!")

st.write("## Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([1, 4, 1])

        with col1:
            is_completed = st.checkbox("", value=task["completed"], key=f"check_{i}")
            st.session_state.tasks[i]["completed"] = is_completed

        with col2:
            task_text = f"~~{task['task']}~~" if task["completed"] else task["task"]
            st.write(task_text)

        with col3:
            if st.button("❌", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.success("Task deleted successfully!")
                st.experimental_rerun()
else:
    st.info("No tasks yet! Add your first task.")

st.sidebar.write("Developed by Tan 🎨💻")
