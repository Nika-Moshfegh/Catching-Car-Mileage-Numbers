def is_interesting(number, awesome_phrases):
    res=0
    if 99>number or  number<1_000_000_000:
        return 0

    if same_number(number):
        res=2
        
    return res


def same_number(n):
    return len(set(str(n)))==1

def sequential_incementing (n):
    return sorted(str(n))==[i for i in str(n)]

def palindrome(n):
    s = str(n)
    return s[:len(s)//2] == s[(len(s)+1)//2:][::-1]


print(
    palindrome(1238121)
    )
    