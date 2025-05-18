"""
Problem 8: You have a string that contains a bad word, and you want to censor it using *. Replace the word with "***".
"""
import re
text = "You are such bad person with bad attitude."
result = re.sub(r'bad', '***', text, flags=re.IGNORECASE)
print(result)
