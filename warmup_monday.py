# Create a function that takes in a string and replaces vowels as such.
# A = @
# E = 3
# I = !
# O = 0 (zero)
# U = )

def replace(strng):
    vowels = {
    'A':'@',
    'E':'3',
    'I':'!',
    'O':'0',
    'U':')'
    }
    ans = []
    for key, value in vowels.items():
        for x in strng:
            if key == x:
                x = value
                ans.append(value)
        return ans
strng = input('input string ')
print(replace(strng))
#______________________________________________________
def reverse(user_string): #cat --> tac
    last = len(user_string)
    output = []
    # for x in user_string:
    for i in range(last, 0,-1):
        print(i)
        output += user_string[i-1]
    return output
user_string = input('input string to reverse ')
print(reverse(user_string))
