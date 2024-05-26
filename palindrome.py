# # isPalindrome.py

# def is_palindrome(s: str) -> bool:
#     """
#     This function checks if the given string `s` is a palindrome.
    
#     A palindrome is a word, phrase, number, or other sequence of characters 
#     that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    
#     Your task:
#     1. Remove all non-alphanumeric characters from the string `s`.
#     2. Convert the cleaned string to lowercase.
#     3. Check if the cleaned string is equal to its reverse.
#     4. Return True if it is a palindrome, otherwise return False.
    
#     Examples:
#     - is_palindrome("A man, a plan, a canal, Panama") should return True
#     - is_palindrome("racecar") should return True
#     - is_palindrome("hello") should return False
#     """
#     # Step 1: Remove all non-alphanumeric characters from the string `s`
#     # Step 2: Convert the cleaned string to lowercase
#     # Step 3: Check if the cleaned string is equal to its reverse
#     # Step 4: Return True if it is a palindrome, otherwise return False
    
#     # Implement your solution here
#     pass

# # You can test your function with print statements below
# # Example:
# # print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected output: True
# # print(is_palindrome("racecar"))  # Expected output: True
# # print(is_palindrome("hello"))  # Expected output: False

# palindrome.py

def is_palindrome(s: str) -> bool:
    """
    This function checks if the given string `s` is a palindrome.
    
    A palindrome is a word, phrase, number, or other sequence of characters 
    that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    
    Args:
    - s (str): The input string.
    
    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    
    Examples:
    - is_palindrome("A man, a plan, a canal, Panama") should return True
    - is_palindrome("racecar") should return True
    - is_palindrome("hello") should return False
    """
    # Step 1: Remove all non-alphanumeric characters from the string `s` and convert to lowercase
    cleaned = []
    for char in s:
        if char.isalnum():
            cleaned.append(char.lower())
    
    # Step 2: Check if the cleaned list is equal to its reverse
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected output: True
print(is_palindrome("racecar"))  # Expected output: True
print(is_palindrome("hello"))  # Expected output: False

# You can test your function with print statements below
# Example:
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected output: True
# print(is_palindrome("racecar"))  # Expected output: True
# print(is_palindrome("hello"))  # Expected output: False
