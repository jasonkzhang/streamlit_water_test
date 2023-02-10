import streamlit as st
import socket

ip = st.text_input("Enter IP address:")

try:
    hostname = socket.gethostbyaddr(ip)[0]
    st.write("Hostname:", hostname)
    pc_name = socket.gethostbyname(hostname)
    st.write("PC Name:", pc_name)
except socket.herror as e:
    st.write("Could not resolve IP address.")

