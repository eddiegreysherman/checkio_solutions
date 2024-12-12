def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    if begin in text and end not in text:
        return(text.split(begin)[1])
    
    elif end in text and begin not in text:
        return(text.split(end)[0])
    
    elif begin and end in text:
        # figure out if end comes before begin in the text
        if text.index(end) < text.index(begin):
            return ""
        
        return(text.split(begin)[1].split(end)[0])
    
    elif begin and end not in text:
        return text
    
    else:
        return ""


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
