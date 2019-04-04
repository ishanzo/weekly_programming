def increment_string(strng):
    # strng = list(strng)
    letters = ''
    nums = ''
    print(strng)
    # last = len(strng)
    for x in range(len(strng)):
        if strng[x].isdigit() == True: #if value is int
            nums += strng[x] #add to num
        else:#if value is alpha
            letters += nums + strng[x]#alpha is incrementing
            num = ""
    if nums == "":
        nums = "0"
    return letters + str(int(nums) + 1).zfill(len(num)) #zfill is for the zeros. leading zeros
print(increment_string('foo1'))
