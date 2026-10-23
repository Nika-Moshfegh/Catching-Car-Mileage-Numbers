def is_interesting(number, awesome_phrases):
    def interesting(n):
        if n < 100:
            return False
        s = str(n)
        return (all_zeros(n) or same_number(n) or
                sequential_incementing(n) or sequential_decrementing(n) or
                palindrome(n) or n in awesome_phrases)

    if interesting(number):      return 2
    if interesting(number + 1):  return 1
    if interesting(number + 2):  return 1
    return 0
    

def all_zeros(n):
    return set(str(n)[1:]) == {"0"}

def same_number(n):
    return len(set(str(n)))==1

def sequential_incementing(n):
    return str(n) in "1234567890"

def sequential_decrementing (n):
    return str(n) in "9876543210"

def palindrome(n):
    s = str(n)
    return s[:len(s)//2] == s[(len(s)+1)//2:][::-1]

def exist_awesome_phrases (n,awesome_phrases):
    return n in awesome_phrases

print(
    sequential_incementing(1234)
    )
    