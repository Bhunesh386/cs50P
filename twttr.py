a = input("Input: ")
vowels = "aeiouAEIOU"
result = ""
for char in a:
    if char not in vowels:
        result += char
print("Output:", result)
