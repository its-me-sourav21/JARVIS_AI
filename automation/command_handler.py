 
import re
import time
import pyautogui
import pygetwindow as gw

from automation.app_control import open_app, close_app
from automation.web_search import search_web
from automation.website_control import open_website


# Previous search context
last_search = {
    "platform": None,
    "query": None
}


# --------------------------------
# YOUTUBE SEARCH
# --------------------------------

def search_youtube(query):

    if not query.strip():
        return "What should I search on YouTube?"

    try:
        windows = gw.getAllWindows()

        browser = next(
            (
                window for window in windows
                if "avast secure browser" in window.title.lower()
            ),
            None
        )

        if browser is None:
            return "Avast Secure Browser not found."

        if browser.isMinimized:
            browser.restore()

        browser.activate()
        time.sleep(1)

        # Focus YouTube search box
        pyautogui.write("/")
        time.sleep(0.5)

        # Replace existing search text
        pyautogui.hotkey("ctrl", "a")
        pyautogui.write(query, interval=0.04)
        pyautogui.press("enter")

        last_search["platform"] = "youtube"
        last_search["query"] = query

        return f"Searching YouTube for {query}."

    except Exception as e:
        print("YOUTUBE SEARCH ERROR:", e)
        return "Could not search YouTube."


# --------------------------------
# GOOGLE SEARCH
# --------------------------------

def search_google(query):

    if not query.strip():
        return "What should I search?"

    result = search_web(query)

    last_search["platform"] = "google"
    last_search["query"] = query

    return result


# --------------------------------
# SEARCH INTENT DETECTION
# --------------------------------

def extract_search_query(command):

    text = command.strip()

    # Remove common search prefixes
    prefixes = [
        "search for ",
        "search ",
        "find ",
        "look up ",
        "find on google "
    ]

    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
            break

    # YouTube search: supports both natural and explicit commands
    youtube_match = re.match(
        r"^(.+?)\s+(?:on|in)\s+youtube$",
        text
    )

    if youtube_match:
        query = youtube_match.group(1).strip()

        if query:
            return "youtube", query

    # Hinglish YouTube search
    youtube_hinglish = re.match(
        r"^youtube\s+par\s+(.+?)(?:\s+search\s+karo)?$",
        text
    )

    if youtube_hinglish:
        return "youtube", youtube_hinglish.group(1).strip()

    # Google search
    google_match = re.match(
        r"^(.+?)\s+(?:on|in)\s+google$",
        text
    )

    if google_match:
        return "google", google_match.group(1).strip()

    # Explicit Google search
    if text.startswith("google "):
        query = text[len("google "):].strip()

        if query:
            return "google", query

    # Normal search without platform defaults to Google
    if any(command.startswith(prefix) for prefix in [
        "search for ",
        "search ",
        "find ",
        "look up "
    ]):
        if text:
            return "google", text

    return None, None


# --------------------------------
# WEBSITE CONTROL
# --------------------------------

def handle_website(command):

    command = re.sub(
        r"\b(again|please|now)\b",
        "",
        command
    ).strip()

    websites = {
        "google": "google",
        "open google": "google",
        "youtube": "youtube",
        "open youtube": "youtube",
        "gmail": "gmail",
        "open gmail": "gmail",
        "gmail kholo": "gmail",
        "github": "github",
        "open github": "github",
        "open google account": "google account",
        "open my google account": "google account",
        "chatgpt": "chatgpt",
        "open chatgpt": "chatgpt"
    }

    if command in websites:
        return open_website(websites[command])

    return None


# --------------------------------
# APPLICATION CONTROL
# --------------------------------

def handle_application(command):

    open_commands = {
        "chrome": "chrome",
        "google chrome": "chrome",
        "vs code": "vs code",
        "visual studio code": "vs code",
        "notepad": "notepad",
        "calculator": "calculator",
        "file explorer": "file explorer"
    }

    close_commands = {
        "chrome": "chrome",
        "google chrome": "chrome",
        "vs code": "vs code",
        "notepad": "notepad",
        "calculator": "calculator"
    }

    for prefix in ["open ", "launch ", "start "]:

        if command.startswith(prefix):

            app = command[len(prefix):].strip()

            app = re.sub(
                r"\b(again|please|now)\b",
                "",
                app
            ).strip()

            if app in open_commands:
                return open_app(open_commands[app])

    for prefix in ["close ", "exit ", "quit "]:

        if command.startswith(prefix):

            app = command[len(prefix):].strip()

            if app in close_commands:
                return close_app(close_commands[app])

    return None


# --------------------------------
# MAIN COMMAND HANDLER
# --------------------------------

def handle_command(command):

    command = command.lower().strip()

    if not command:
        return None

    # 1. Repeat previous search
    repeat_commands = [
        "do the search",
        "search again",
        "repeat the search",
        "do that search",
        "search it again"
    ]

    if command in repeat_commands:

        if last_search["query"]:

            if last_search["platform"] == "youtube":
                return search_youtube(last_search["query"])

            if last_search["platform"] == "google":
                return search_google(last_search["query"])

        return "There is no previous search to repeat."

    # 2. Website commands
    website_result = handle_website(command)

    if website_result:
        return website_result

    # 3. Application commands
    app_result = handle_application(command)

    if app_result:
        return app_result

    # 4. Search commands
    platform, query = extract_search_query(command)

    if platform == "youtube":
        return search_youtube(query)

    if platform == "google":
        return search_google(query)

    # 5. Unknown commands go to Gemini
    return None
 