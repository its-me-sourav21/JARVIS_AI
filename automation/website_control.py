 
import webbrowser


WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "google account": "https://myaccount.google.com",
    "chatgpt": "https://chatgpt.com"
}


def open_website(name):

    name = name.lower().strip()

    if name not in WEBSITES:
        return None

    try:
        webbrowser.open(WEBSITES[name])
        return f"Opening {name}."

    except Exception as e:
        print("WEBSITE ERROR:", e)
        return f"Could not open {name}."
 