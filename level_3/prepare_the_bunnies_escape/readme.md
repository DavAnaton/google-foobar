Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of `0`s and `1`s, where `0`s are passable space and `1`s are impassable walls. The door out of the prison is at the top left `(0,0)` and the door into an escape pod is at the bottom right `(w-1,h-1)`. 

Write a function `answer(map)` that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (`0`). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit `solution.py`
<br>
To provide a Java solution, edit `solution.java`

Test cases
==========

Inputs: `(int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]`
<br>
Output: `(int) 7`

Inputs: `(int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]`
<br>
Output:`(int) 11`

Solution
========

Since we are allowed to remove only one wall, we just need to have the distance from the starting point to each wall, from each wall to the ending point and minimizing the sum of these distances.
<br>
In order to achieve that, I used a BFS from the starting point, one from the ending point, and then return the minimum of the sums I've had from each algorithm.

## Correctness
The correctness of this algorithm is **ensured by the correctness of the BFS**.

## Time and space complexity
The  results of each BFS are stored in an array where each cell represents a vertex in the graph. 
Hence the space complexity: **`o(V)`**.

We just run 2 BFS and go through those 2 arrays synchronously.
<br>
Each BFS is `o(E + V)` (`E` is the number of edges, `V` the number of vertices) and finding the minimum is `o(V)`.
<br>
Hence the final time complexity: **`o(E + V)`**.