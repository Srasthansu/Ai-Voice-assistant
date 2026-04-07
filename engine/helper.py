import re


def extract_yt_term(command):
    
    # Define a regular expession pattern to capture a song name
    
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    
    # Use re.search to find the match in the command
    
    match = re.search(pattern, command, re.IGNORECASE)
    
    # if the match is found return the extracte song name; otherwise return none
    
    return match.group(1) if match else None