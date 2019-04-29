#The rgb() method is incomplete.
#Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned.
#The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.
# Hex color code is a 6 digits hexadecimal (base 16) number:
#RRGGBB16
#The 2 left digits represent the red color.
#The 2 middle digits represent the green color.
#The 2 right digits represent the blue color.
# hash with rgb numbers and hex numbers
# take rgb value
# for each rgb balue divide by 16 and translate itnto hash
# second number is the reaminder multiplied by 16
# bigger than 15 if the two numbers are bigger than 14 or less than 0
# bigger than 15 automatically
# (255, 255, 255) // returns FFFFFF
def rgb_hex(r,g,b):
    hex = {
    0:"0",
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
    }
    colors = [r,g,b]
    arr = []
    one = 0
    two = 0
    ans = []
    for x in colors:
        if 255 > x > 0:
            one = x// 16
            two = x % 16
        elif x < 0 :
            one = 0
            two = 0
        elif x >= 255:
            one = 15
            two = 15
        arr.append(one)
        arr.append(two)

    for key,value in hex.items():
        for n in arr:
            if n in hex:
                ans.append(hex[n])
        return ''.join(ans)

print(rgb_hex(255, 255, 255))
