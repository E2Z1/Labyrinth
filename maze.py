from random import randint

def maze(ms):
    visited_cells = []
    walls = []


    map = [['w' for _ in range(ms)]for _ in range(ms)]







    def check_neighbours(ccr, ccc):
        neighbours = [[ccr, ccc-1, ccr-1, ccc-2, ccr, ccc-2, ccr+1, ccc-2, ccr-1, ccc-1, ccr+1, ccc-1], #left
                    [ccr, ccc+1, ccr-1, ccc+2, ccr, ccc+2, ccr+1, ccc+2, ccr-1, ccc+1, ccr+1, ccc+1], #right
                    [ccr-1, ccc, ccr-2, ccc-1, ccr-2, ccc, ccr-2, ccc+1, ccr-1, ccc-1, ccr-1, ccc+1], #top
                    [ccr+1, ccc, ccr+2, ccc-1, ccr+2, ccc, ccr+2, ccc+1, ccr+1, ccc-1, ccr+1, ccc+1]] #bottom
        visitable_neighbours = []
        for i in neighbours:                                                                        #find neighbours to visit
            if i[0] > 0 and i[0] < (ms-1) and i[1] > 0 and i[1] < (ms-1):
                if map[i[2]][i[3]] == 'p' or map[i[4]][i[5]] == 'p' or map[i[6]][i[7]] == 'p' or map[i[8]][i[9]] == 'p' or map[i[10]][i[11]] == 'p':
                    walls.append(i[0:2])
                else:
                    visitable_neighbours.append(i[0:2])
        return visitable_neighbours

    #StartingPoint

    scr = randint(1, ms-1)
    scc = randint(1, ms-1)
    ccr, ccc = scr, scc
    map[scr][scc] = "p"


    finished = False
    while not finished:
        visitable_neighbours = check_neighbours(ccr, ccc)
        if len(visitable_neighbours) != 0:
            d = randint(1, len(visitable_neighbours))-1
            ncr, ncc = visitable_neighbours[d]
            map[ncr][ncc] = 'p'
            visited_cells.append([ncr, ncc])
            ccr, ccc = ncr, ncc
        if len(visitable_neighbours) == 0:
            try:
                ccr, ccc = visited_cells.pop()
            except:
                finished = True

    maze = []

    for i in range(len(map)):
        maze += map[i]





    return maze

