 
def detect_intent(command):

    command = command.lower().strip()

    # Search intent
    search_words = [
        "search", "google", "find", "look up"
    ]

    if any(word in command for word in search_words):
        return "search"

    # Application opening
    if command.startswith(("open ", "launch ", "start ")):
        return "open"

    # Application closing
    if command.startswith(("close ", "exit ", "quit ")):
        return "close"

    # Website navigation
    if any(site in command for site in [
        "youtube", "gmail", "github", "google account"
    ]):
        return "website"

    # General AI question
    return "ai"
 