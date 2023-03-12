def palindrome(s):
    s = s.replace(" ", "").lower()
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return "Не палиндром"
    return "Палиндром"


print(palindrome("А роза упала на лапу Азора"))
print(palindrome("Палиндром"))
