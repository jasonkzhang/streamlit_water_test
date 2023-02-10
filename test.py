import streamlit as st
import paramiko
import getpass

ip = st.text_input("Enter IP address:")
username = st.text_input("Enter username:")
password = st.text_input("Enter password:", type="password")

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command("whoami")
    current_user = stdout.read().decode().strip()
    st.write("Current User:", current_user)
    ssh.close()
except Exception as e:
    st.write("Could not establish connection:", e)
