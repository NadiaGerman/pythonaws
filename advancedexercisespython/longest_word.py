
def longest_word(words):
    """Find the longest word in a list of words."""
    if not words:
        return None
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Testing the function
word_list = ["apple", "banana", "cherry", "watermelon", "grape"]
print("Longest word:", longest_word(word_list))

word_list = ["hi", "hello", "hey", "hola"]
print("Longest word:", longest_word(word_list))

word_list = ["same", "size", "word"]
print("Longest word:", longest_word(word_list))

word_list = []
print("Longest word:", longest_word(word_list))  # return None
