import streamlit as st
import paramiko
import getpass

ip = st.text_input("Enter IP address:")
username = st.text_input("Enter username:")
password = st.text_input("Enter password:", type="password")
program = st.text_input("Enter program name:")

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(f"ps aux | grep {program}")
    output = stdout.read().decode()
    if output:
        st.write(f"{program} is running on {ip}")
    else:
        st.write(f"{program} is not running on {ip}")
    ssh.close()
except Exception as e:
    st.write("Could not establish connection:", e)
