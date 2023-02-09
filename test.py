import os
import psutil
import streamlit as st

def check_chrome():
    for process in psutil.process_iter():
        try:
            if process.name() == "chrome.exe":
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def check_tuflow():
    for process in psutil.process_iter():
        try:
            if process.name() == "TUFLOW_iSP_w64.exe":
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def print_system_info():
    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent()
    st.write(f'CPU usage: {cpu_percent}%')

    # Get memory usage
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    st.write(f'Memory usage: {memory_percent}%')

    # Get GPU usage percentage
    gpu_percent = psutil.virtual_memory().percent
    st.write("GPU Usage: {}%".format(gpu_percent))

    # Check if Chrome is running
    is_chrome_running = check_chrome()
    if is_chrome_running:
        st.write("Google Chrome is running.")
    else:
        st.write("Google Chrome is not running.")

    # Check if Tu-Flow is running
    is_tuflow_running = check_tuflow()
    if is_tuflow_running:
        st.write("Tu-Flow is running.")
    else:
        st.write("Tu-Flow is not running.")
    
    # Get information about users who are logged in
    result = os.popen("query user").read().strip()
    lines = result.split("\n")
    lines = lines[1:]
    users = []
    for line in lines:
        parts = line.split()
        username = parts[0]
        session = parts[2]
        id = parts[3]
        users.append((username, session, id))
    st.write("List of logged in users:")
    for user in users:
        st.write("- " + user[0] + " (Session " + user[1] + ", ID " + user[2] + ")")

st.title("Cruncher Manager Dashboard")
if st.button("Click me!"):
    print_system_info()
