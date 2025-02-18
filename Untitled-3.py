def is_vowel(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return False

# Example usage
char = 'a'
if is_vowel(char):
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")
