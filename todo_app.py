import streamlit as st

st.set_page_config(page_title="To-Do List", layout="centered")
st.title("📝 To-Do List")

todos = st.session_state.setdefault("todos", [])

if st.text_input("Add a task", key="new_task"):
    task = st.session_state.pop("new_task").strip()
    if task:
        todos.append({"task": task, "done": False})

for i, todo in enumerate(todos):
    c1, c2, c3 = st.columns([0.1, 0.8, 0.1])
    todo["done"] = c1.checkbox("", todo["done"], key=f"done_{i}")
    c2.markdown(f"~~{todo['task']}~~" if todo["done"] else todo["task"])
    if c3.button("❌", key=f"del_{i}"):
        todos.pop(i)
        st.experimental_rerun()

if any(t["done"] for t in todos) and st.button("🧹 Clear Completed"):
    st.session_state.todos = [t for t in todos if not t["done"]]