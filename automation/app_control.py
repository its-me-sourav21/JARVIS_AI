 
import subprocess


APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "google chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "vs code": "code",
    "visual studio code": "code",

    "notepad": "notepad",
    "calculator": "calc",
    "file explorer": "explorer"
}


PROCESSES = {
    "chrome": "chrome.exe",
    "google chrome": "chrome.exe",
    "vs code": "Code.exe",
    "visual studio code": "Code.exe",
    "notepad": "notepad.exe",
    "calculator": "CalculatorApp.exe"
}


def open_app(app_name):

    app_name = app_name.lower().strip()

    if app_name not in APPS:
        return f"Sorry Bhai, {app_name} is not supported yet."

    try:
        subprocess.Popen(APPS[app_name])
        return f"Opening {app_name}."

    except Exception as e:
        print("APP ERROR:", e)
        return f"Could not open {app_name}."


def close_app(app_name):

    app_name = app_name.lower().strip()

    if app_name not in PROCESSES:
        return f"Sorry Bhai, I cannot close {app_name} yet."

    try:
        result = subprocess.run(
            ["taskkill", "/IM", PROCESSES[app_name], "/T", "/F"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return f"Closing {app_name}."

        return f"{app_name} is not running."

    except Exception as e:
        print("APP ERROR:", e)
        return f"Could not close {app_name}."
 