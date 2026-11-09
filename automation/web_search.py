 
import webbrowser
from urllib.parse import quote_plus


def search_web(query):

    if not query.strip():
        return "Bhai, what should I search?"

    try:
        search_url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        webbrowser.open(search_url)

        return f"Searching Google for {query}."

    except Exception as e:
        print("SEARCH ERROR:", e)
        return "Unable to open Google search."
 