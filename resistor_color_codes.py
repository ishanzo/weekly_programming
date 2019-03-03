def encode_resistor_colors(ohms_string):
    color_codes = { #color codes hash
    '0': 'black',
    '1': 'brown',
    '2': 'red',
    '3': 'orange',
    '4': 'yellow',
    '5': 'green',
    '6': 'blue',
    '7': 'violet',
    '8': 'gray',
    '9': 'white'
    }
    string = str.split(ohms_string) # split string
    convert = string[0] # convert is the first value of the string
    if 'k' in convert: # replace k by 000
        replaced_one = [t.replace('k', '000') for t in convert]
         # [1,000]
    elif 'M' in convert: # replace M by 000000
        replaced_one= [m.replace('M','000000') for m in convert]
    else:
        replaced_one = convert
    arr = list(replaced_one)
    print(arr)
    if arr[1]=='.' and arr[-1] == '000' in replaced_one:
        replaced_one.remove('.')
        arr = replaced_one
        values = 2
    elif '.' in replaced_one:
        replaced = replaced_one
        replaced.remove('.')
        values = 5
        arr = list(replaced) #split the new arr
    elif '000'in arr and arr[0] != '1':
        if len(arr) == 4:
            values = len(arr)
        else:
            values = 3
        arr.remove(arr[-1])
        # arr = list(map(str, str(arr[0])))
    elif arr[0] == '1' and arr[-1] =='000' in arr:
        values = len(arr)
        arr[0] = arr[0] +'0'
        arr = list(map(str, str(arr[0])))
    elif '0000' in arr and len(arr) ==2:
        arr.remove('.')
        arr = arr[:-1]
        values = len(arr)
    elif '000000'in arr:
        print(arr,'m')
        if arr[1] == '0':
            arr[0] = arr[0] +'0'
            arr = list(map(str, str(arr[0])))
        print(arr,'ll')
        values = 5
    elif len(arr) > 2: # if the length of the arr is greater than 2
        print('----')
        values = len(arr[2:]) # values is the length of the array minus the first two elements
        arr = arr[:-1]
    elif len(arr) == 1: # if the length of the arr is 1
        print(arr,'p')
        values = 2 # values is equal to 2
    elif len(arr) ==2:
        values = 0
    ans = [] # empty array for output
    values = str(values)
    print(values)
    if arr[1] == '000' or '000000':
        arr[1] = '0'
    if len(arr) >2:
        arr = arr[:-1]
        if len(arr) > 2:
            arr = arr[:-1]
    for key, value in color_codes.items():
        for x in arr:
            ans.append(color_codes[x])
        ans.append(color_codes[values])
        ans.append('gold')
        output = " ".join(ans)
        return output

print(encode_resistor_colors('1M ohms'))# brown black green gold")
