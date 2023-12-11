inp = '''.#..........#.....................#........................................................#....................................#...........
...................#........................................#......................#........................................................
...........................................#......#..................#...................................................#..................
....#......................#...............................................#.........................#.....#......#................#........
.................................................................#.......................#..................................................
..............................................................................................................................#.............
.......#........#.............#...................................................#...................................#.....................
.........................#...................................#............................................................................#.
....................#.............#.........#..........................................#...............#....................................
.....................................................#...............#.............................................................#........
...........................................................................................................................#................
..........................................................#.........................................#...............#.......................
..............................................................................................#.............................................
.#........#........................#......#..............................................#..............................#...............#...
...............#......#...............................#.......#.........#......#.............................#.................#............
...............................#..............#.............................................................................................
............................................................................................................................................
.........................#.......................................#..........................................................................
..................#........................#......................................#........................................#................
..................................................#.......#..............................................#........................#.......#.
...#........#........................#....................................#...............#.................................................
............................................................................................................................................
.......#........................#....................................................................................#......................
...............#...........#........................................................................#.......................................
.............................................#................#.........#.............................................................#.....
...........#...........................#................#...........................#.......................................................
..................................................#.......................................#.............#...................................
.....#..................#..........#..............................#.............................#........................................#..
..............................#...............................................................................................#.............
...................................................................................................................#........................
..............#..........................................#.............#...........................#..............................#.........
...#...................................#.........................................#..........................................................
..................#...................................................................#................................................#....
..........................#...................................#.........................................#...................................
............................................................................................................................................
.........#...........#..........#..........................................#....................#..............#........#.....#...........#.
....................................................#.......................................................................................
.............................................#..............................................................................................
......................................#..................#..............................#...........#.......#...............................
............................#..................................#..............#.............................................................
...............#............................................................................................................................
...........................................#............................#.......................#...........................................
.....#..............#.................................................................................#...........................#.........
............................................................................................................................................
........................................#..........#.................#..........................................#...........................
.............................................#.................................#...........#................................................
...............................#.......................#...........................................#.......#....................#...........
#........#.............#...............................................................................................#...................#
.....................................#........................#..........#.........#........................................................
.................#............................................................................#.............................................
..........................#.......................................#.................................................#.......................
.....................................................#...................................#....................................#.............
..#.........................................................................................................................................
.............#.....#.......................#.............#....................................................#........................#....
......#........................................................................................#............................................
.................................#.................................#........................................................................
.................................................................................#.......................#................................#.
#.....................................................#...................................................................#.....#...........
.........#..................................................#......................................#........................................
..............................#.............#.................................................................#.......#.....................
........................#............................................................#......#................................#..............
.............#..............................................................................................................................
.....#........................................................#............#..........................#...........................#.........
...........................#......#.................................................................................#...................#...
.........#.....................................#...............................#............................................................
..................#.......................................#.......#................................#........................................
...............................#.....................#...................................#................................#.................
..............#..........................#.............................#............#.....................#.....................#.........#.
.................................................................................................................#..........................
......#.....................................................................................................................................
...........#.............#.........#........................................................................................................
...................................................................#..............#..................#......................................
..................#...........................................................................................#.............................
........#.................................#..............#.................................................................#..........#.....
...#.....................................................................#..............#.......#...........................................
............................................................................................................................................
............................................................................................................................................
.................................#................#..........................................................#...............#.............#
..............#............................................................#................................................................
......#.....................#..........................#........#.....#............#..............#.........................................
....................#..................................................................................#..................#.................
....................................#.........#........................................................................................#....
..........................................................#..............#..................................................................
................#...............................................................................................#.............#.............
............................................................................................................................................
............................#...................#......#.............#..............................................#.......................
.............#...................................................................................#........................................#.
......................#..........................................................#.......#..................................................
#...........................................................#...............................................................................
.........#.........................#.................#....................................................#.................#...............
............................................................................................................................................
...................#.............................................#.....#....................................................................
........................#.........................#.....................................................................................#...
.....#........................................................................................................................#.............
.......................................#...............................................................#.........#..........................
............................#...........................#...........#......................#..............................#.......#.........
..#................................#...........#............................................................................................
.................#..................................#...................#...................................................................
..........#.................................................#................................................#..............................
.....................#...............................................................................#......................................
..............#..................#..............................#.............#....................................#.........#........#.....
...#.............................................................................................#..........................................
............................................#..........................................#....................................................
.........#...............................................#..............................................................#...................
................#.........#.................................................................................................................
.....#..................................#............................#..............................#........#..................#..........#
...............................#............................................................................................................
....................................................#........#..............................................................................
........#..........................#.........#...............................................................................#..............
....................................................................................................................#.......................
....................#........#......................................#.........#.....#.....#.................................................
................................................................................................................................#.....#.....
...............#..........................................#...............#...............................#.................................
...#..............................#.........................................................................................................
........................................................................................#............#....................................#.
............................................................................................................................#...............
...................................................................................#............................#...........................
#........#........#........#..........#.........#...........................................................................................
.............................................................#..............................#............................#..................
................................#.......................#...................................................................................
.......................#................................................#...............#.........#..................#................#.....
............#..................................................................#........................#...................................
............................................................................................................................................
......#.....................#.......#......#..............#......#..........................................................................
.....................#......................................................................................................................
................................#................................................#.............#...........................#.............#..
..............................................................................................................#.............................
............#............#..........................................................................#.............................#.........
.....#...........#.....................#.............................#.....#........................................#.......................
................................................#...........#..........................#....................................................
............................................................................................................................................
#..........................#.....#................................................................#......................................#..
..........................................#.................................................................#.............#.................
................#.........................................................#.................................................................
.......#..............................#..............................................#..........................................#...........
........................#...................................#...............................................................................
............................................................................................................................#...............
..............................#.....................#.............................#...........#.................#...........................
...............................................#................#.....#................................................#....................
...................#...................#.................#.................#.........................#......................................'''

import math
def distance(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

L = inp.split("\n")

EmptyColumn = []
for x in range(len(L[0])):
    empty = True
    for y in range(len(L)):
        if L[y][x] == "#":
            empty = False
            break
    if empty:
        EmptyColumn.append(x)

Galaxies = []
vertSpace = 0
for y, line in enumerate(L):
    horzSpace = 0
    HorzColumn = EmptyColumn[:]
    if line.count("#") == 0:
        vertSpace += 10 ** 6 - 1
        continue
    for x, sym in enumerate(line):
        if len(HorzColumn) > 0:
            if HorzColumn[0] == x:
                horzSpace += 10 ** 6 - 1
                HorzColumn.pop(0)
                continue
        if sym == "#":
            Galaxies.append((x + horzSpace, y + vertSpace))

total = 0
for x in range(len(Galaxies)):
    for y in range(x + 1, len(Galaxies)):
        total += distance(Galaxies[x], Galaxies[y])
print(total)


