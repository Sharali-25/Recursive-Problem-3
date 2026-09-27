keys = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

def count_combos(digits):
    if len(digits) == 0:
        return 1
    return len(keys[digits[0]])*count_combos(digits[1:])


print(count_combos("2"))
print(count_combos("23"))
n = (input("Enter 234 or 2345 : "))
print(count_combos(n))