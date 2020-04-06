def find_path_out(the_map, x, y):
    # base case, if we get to the end, we stop.
    if the_map[x][y] == 'E':
        return [(x, y)]

    elif the_map[x][y] != '*':
        if x > 0: # go up
            the_map[x][y] = '*'  # prevents us from going backwards immediately
            path_x0 = find_path_out(the_map, x - 1, y)
            if path_x0:
                return [(x, y)] + path_x0
            the_map[x][y] = '_'
        if x < len(the_map) - 1: # go down
            the_map[x][y] = '*'
            path_x1 = find_path_out(the_map, x + 1, y)
            if path_x1:
                return [(x, y)] + path_x1
            the_map[x][y] = '_'
        if y > 0: # go left
            the_map[x][y] = '*'
            path_y0 = find_path_out(the_map, x, y - 1)
            if path_y0:
                return [(x, y)] + path_y0
            the_map[x][y] = '_'
        if y < len(the_map[0]) - 1: # go right
            the_map[x][y] = '*'
            path_y1 = find_path_out(the_map, x, y + 1)
            if path_y1:
                return [(x, y)] + path_y1
            the_map[x][y] = '_'

    return []


with open('map1.txt') as map_file:
    the_map = [list(line.strip()) for line in map_file.readlines()]
    print(the_map)
    for i in range(len(the_map)):
        for j in range(len(the_map[0])):
            if the_map[i][j] == 'S':
                print(i, j)
                print(find_path_out(the_map, i, j))
