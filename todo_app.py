import streamlit as st

st.set_page_config(page_title="To-Do List", layout="centered")

if "todos" not in st.session_state:
    st.session_state.todos = []

st.title("📝 To-Do List")

with st.form("add_task", clear_on_submit=True):
    new_task = st.text_input("Add a task")
    submitted = st.form_submit_button("➕ Add")
    if submitted and new_task.strip():
        st.session_state.todos.append({"task": new_task.strip(), "done": False})

for i, todo in enumerate(st.session_state.todos):
    cols = st.columns([0.1, 0.8, 0.1])
    done = cols[0].checkbox("", value=todo["done"], key=f"done_{i}")
    if done != todo["done"]:
        st.session_state.todos[i]["done"] = done

    task_display = f"~~{todo['task']}~~" if todo["done"] else todo["task"]
    cols[1].markdown(task_display)

    if cols[2].button("❌", key=f"del_{i}"):
        st.session_state.todos.pop(i)
        st.experimental_rerun()

if st.session_state.todos and any(t["done"] for t in st.session_state.todos):
    if st.button("🧹 Clear Completed"):
        st.session_state.todos = [t for t in st.session_state.todos if not t["done"]]