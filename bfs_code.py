#PATH FINDER
#You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.
def path_finder(matrix):
    #puts matrix values in string
    matrix = list(map(list, matrix.splitlines()))
    #finds length of matrix
    length = len(matrix)
    #assigns starting point
    start = (0,0)
    #assigns end point
    end = (length - 1,length - 1)
    #memoization, hash to access it
    level = {start: 0}
    parent = {start: 0}
    i = 1
    frontier = [start] #the spaces in the level
    while frontier:
        next = [] #for path
        for u in frontier: #u is the spaces, the node
        #assigns coordinates to nodes in frontier
            x,y = u
            #checks cardinal directions #down       up      left        right
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= x < length and 0 <= y < length: ##to avoid out of range index
                #if you cannot move within level
                    if (x,y) not in level and matrix[x][y] != 'W':
                       ##if can't move within level #W is wall
                        level[(x,y)] = i
                        parent[(x,y)] = u
                        next.append((x,y))
#                     if x == len(matrix)-1 and y == len(matrix)-1:
#                         return 1

                        #if new location is equal to end point, return true
                        if (x,y) == end:
                            return True
#                         if x == len(matrix)-1 and y == len(matrix)-1:
#                             return 1
        #list of past nodes
        frontier = next
        i += 1
    return False
# #create queue
# #create explored list
# #cycle until queue is empty
# #FIFO - check nodes in queue by creating path variable, which is a single node
# #if path not in explored do the following
# #add path to explored
# #find all of path's edges
# #add all edges to queue if not explored
# #clear path variable
# #repeat steps until done
# #return explored
