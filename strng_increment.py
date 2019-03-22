def increment_string(strng):
    alpha = "" #letters of the string
    num =  "" #numbers of the string
    for x in range(len(strng)):
        if strng[x].isdigit() == True: #if value is int
            num += strng[x] #add to num
        else:#if value is alpha
            alpha += num + strng[x]#alpha is incrementing
            num = ""
    if num == "":
        num = "0"

    return alpha + str(int(num) + 1).zfill(len(num)) #.zfill for the 0s
