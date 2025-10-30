import streamlit as st
import requests

BACKEND_URL = "http://localhost:5000"

st.title("👥 User Management (Flask + Streamlit + Supabase)")

menu = st.sidebar.selectbox("Menu", ["View Users", "Add User"])

if menu == "View Users":
    st.subheader("All Users")
    res = requests.get(f"{BACKEND_URL}/users")
    if res.ok:
        users = res.json()
        if users:
            st.table(users)
        else:
            st.info("No users found.")
    else:
        st.error("Failed to fetch users.")

elif menu == "Add User":
    st.subheader("Add a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Add"):
        res = requests.post(f"{BACKEND_URL}/add_user", json={"name": name, "email": email})
        if res.ok:
            st.success("User added successfully!")
        else:
            st.error("Failed to add user.")
