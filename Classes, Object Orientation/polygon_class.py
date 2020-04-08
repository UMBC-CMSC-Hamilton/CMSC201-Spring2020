import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print('i am being added!')
        copy = Vector(self.x, self.y)
        copy.x += other.x
        copy.y += other.y
        return copy

    # something else * us
    def __rmul__(self, coefficient):
        copy = Vector(self.x, self.y)
        copy.x *= coefficient
        copy.y *= coefficient
        return copy

    # us * something else
    def __mul__(self, coefficient):
        copy = Vector(self.x, self.y)
        copy.x *= coefficient
        copy.y *= coefficient
        return copy

    def __getitem__(self, index):
        print('i am called here')
        if index == 0 or index == 'x':
            return self.x
        if index == 1 or index == 'y':
            return self.y

        return 0

    # have to implement __repr__ if you want something to print, "printable representation"
    def __repr__(self):
        return '(%f, %f)' % (self.x, self.y)

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def draw(self, grid, center, size, symbol='*'):
        vertices = [center + Vector(math.cos(2 * math.pi * i / self.sides), math.sin(2 * math.pi * i / self.sides)) * size for i in range(self.sides)]
        print(vertices)
        for i in range(self.sides):
            self.draw_segment(grid, vertices[i - 1], vertices[i], symbol)

    def draw_segment(self, grid, p1, p2, symbol='*'):
        dist = int(self.distance(p1, p2))
        vec = Vector((p2[0] - p1[0]) / (2 * dist), (p2[1] - p1[1]) / (2 * dist))
        current = p1
        for t in range(2 * dist):
            current += vec
            i = round(current.x)
            j = round(current.y)
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                grid[i][j] = symbol

    @staticmethod
    def distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2)


if False:
    # v_1 = <1, 2> v_2 = <2, 5> you're allowed to add vectors.  v_1 + v_2 = <3, 7>
    v1 = Vector(1, 2)
    v2 = Vector(2, 5)
    v3 = v1 + v2
    # v1 would be changed, if we didn't make the copy
    print(v1, v2, v3)

    print(v1[1], v3[0], v1['x'], v1['y'])

    class RandoClass:
        def __repr__(self):
            print(' i am a random class, you dont need to know more')

    p = RandoClass()
    print(p)
else:
    SIZE = 100
    grid = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
    pentagon = Polygon(5)
    pentagon.draw(grid, Vector(10, 10), 5)
    print('\n'.join([''.join(grid[i]) for i in range(SIZE)]))
    diamond = Polygon(4)
    diamond.draw(grid, Vector(12, 12), 7, '-')
    print('\n'.join([''.join(grid[i]) for i in range(SIZE)]))
    answer = 3 * Vector(2, 2)
    gauss_gon = Polygon(8)
    gauss_gon.draw(grid, Vector(30, 30), 15, 'g')
    print(answer)
    print('\n'.join([''.join(grid[i]) for i in range(SIZE)]))
    triangle = Polygon(3)
    triangle.draw(grid, Vector(30, 30), 7, 'g')
    print('\n'.join([''.join(grid[i]) for i in range(SIZE)]))
