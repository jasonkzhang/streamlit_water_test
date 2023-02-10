import streamlit as st
import getpass
import socket

ip = st.text_input("Enter IP address:")

try:
    hostname = socket.gethostbyaddr(ip)[0]
    st.write("Hostname:", hostname)
    st.write("Current User:", getpass.getuser())
except socket.herror as e:
    st.write("Could not resolve IP address.")

