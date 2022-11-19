import re 

def clean(content: str):
    # remove all non-alphanumeric characters except spaces, dots, and commas
    content = re.sub(r"[^a-zA-Z0-9 .,:;&*!(_•~?\"%'-]", "", content)
    # convert to lowercase
    content = content.lower()
    return content