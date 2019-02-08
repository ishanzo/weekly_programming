def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    length = len(matrix)
    s = (0,0)
    t = (length - 1,length - 1)
    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            x,y = u
            # find connections
            # add connections to frontier
            # check if a connection is e
def path_finder(maze):
    return #can go to lower right corner from upper left one
    queue = [0,0]
    length = len(matrix)
    explored = []
    reach = [n-1,n-1]
    while queue:
        path = queue.pop(0)
        x = path[-1]
        if x not in explored:
            explored.append(node)
#LOGIC

# create queue
# create explored list
# cycle until queue is empty
# FIFO- check nodes in queue by creating path variable, which is a single node
# If path not in explored: do the following
# add path to explored
# find all of path's edges
# add all edges to queue if not in explored
# clear path variable
# repeat steps until done
# return explored
