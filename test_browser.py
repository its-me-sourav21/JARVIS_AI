import pygetwindow as gw

windows = gw.getAllWindows()

print("\n--- DETECTED BROWSERS ---")

for window in windows:
    title = window.title.lower()

    if "chrome" in title or "avast" in title:
        print("Browser:", window.title)