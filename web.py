import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my Todo App')
st.write('this app is to increase your productivity')


for index, a in enumerate(todos):
    checkbox = st.checkbox(a, key=a)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[a]
        st.rerun()

st.text_input(label=" ",
              placeholder="Add a todo...",
              on_change=add_todo, key= 'new_todo')
