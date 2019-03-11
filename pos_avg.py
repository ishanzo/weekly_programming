s = "466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"
def pos_average(s):
    arr = s.split(", ") #split the array
    pos = 0 #position variable
    total = 0 #total variable
    for i in range(len(arr)-1): #iterating over the index values
        for j in range(i+1, len(arr)): #iterating over the next values
            for k in range(len(arr[i])): # iterating over the columns
                if arr[i][k] == arr[j][k]: # if the numbers are equal to each other
                    pos = pos + 1 # number of positions increase by 1
                total = total + 1 # total number of positions, outside if statement
    return(100 * pos/ total) # average position
print(pos_average(s))
