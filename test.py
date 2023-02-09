import streamlit as st
import psutil


def check_chrome():
    for process in psutil.process_iter():
        try:
            if process.name() == "chrome.exe":
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

st.title("System Information")
if st.button("Check System Info"):
    print_system_info()
