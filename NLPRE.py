import re
text = "Hello there welcome to the world of natural language processing.Lets clean this."
text = text.lower()
text = re.sub(r"[^\w\s]"," ",text)
text = re.sub(r'\s+'," ",text)
print(text)