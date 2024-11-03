from collections import deque

def is_palindrome(text):

    text = ''.join(ch for ch in text.lower() if ch.isalnum())
    chars = deque(text)
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


print(is_palindrome("Steave please don't do this"))  
print(is_palindrome("Anna"))  
print(is_palindrome("Hello"))  
print(is_palindrome("Madam, I'm Adam"))  