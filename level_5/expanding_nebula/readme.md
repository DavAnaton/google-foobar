Expanding Nebula
================

You've escaped Commander Lambda's exploding space station along with numerous escape pods full of bunnies. But - oh no! - one of the escape pods has flown into a nearby nebula, causing you to lose track of it. You start monitoring the nebula, but unfortunately, just a moment too late to find where the pod went. However, you do find that the gas of the steadily expanding nebula follows a simple pattern, meaning that you should be able to determine the previous state of the gas and narrow down where you might find the pod.

From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, so you can model it as a 2D grid. You find that the current existence of gas in a cell of the grid is determined exactly by its 4 nearby cells, specifically
1. that cell
2. the cell below it
3. the cell to the right of it
4. the cell below and to the right of it. 

If, in the current state, exactly 1 of those 4 cells in the 2x2 block has gas, then it will also have gas in the next state. Otherwise, the cell will be empty in the next state.

For example, let's say the previous state of the grid (`p`) was:
```
.O..
..O.
...O
O...
```

To see how this grid will change to become the current grid (`c`) over the next time step, consider the 2x2 blocks of cells around each cell.  Of the 2x2 block of `[p[0][0], p[0][1], p[1][0], p[1][1]]`, only `p[0][1]` has gas in it, which means this 2x2 block would become cell `c[0][0]` with gas in the next time step:
```
.O -> O
..
```

Likewise, in the next 2x2 block to the right consisting of `[p[0][1], p[0][2], p[1][1], p[1][2]]`, two of the containing cells have gas, so in the next state of the grid, `c[0][1]` will NOT have gas:
```
O. -> .
.O
```

Following this pattern to its conclusion, from the previous state `p`, the current state of the grid `c` will be:
```
O.O
.O.
O.O
```

Note that the resulting output will have 1 fewer row and column, since the bottom and rightmost cells do not have a cell below and to the right of them, respectively.

Write a function `answer(g)` where `g` is an array of array of `bools` saying whether there is gas in each cell (the current scan of the nebula), and return an `int` with the number of possible previous states that could have resulted in that grid after 1 time step.  For instance, if the function were given the current state `c` above, it would deduce that the possible previous states were `p` (given above) as well as its horizontal and vertical reflections, and would return `4`. The width of the grid will be between 3 and 50 inclusive, and the height of the grid will be between 3 and 9 inclusive.  The answer will always be less than one billion (![10^9](http://latex.codecogs.com/svg.latex?\inline&space;10^{9})).

Languages
=========

To provide a Python solution, edit `solution.py`
<br>
To provide a Java solution, edit `solution.java`

Test cases
==========

Inputs: `(boolean) g = [[true, false, true], [false, true, false], [true, false, true]]`
<br>
Output: `(int) 4`

Inputs: `(boolean) g = [[true, false, true, false, false, true, true, true], [true, false, true, false, false, false, true, false], [true, true, true, false, false, false, true, false], [true, false, true, false, false, false, true, false], [true, false, true, false, false, true, true, true]]`
<br>
Output: `(int) 254`

Inputs: `(boolean) g = [[true, true, false, true, false, true, false, true, true, false], [true, true, false, false, false, false, true, true, true, false], [true, true, false, false, false, false, false, false, false, true], [false, true, false, false, false, false, true, true, false, false]]`
<br>
Output: `(int) 11567`

Solution
========

When I started this challenge, I had no idea what Cellular Automaton was. 
<br>
I dived in the code trying to build something that would work with dynamic programming by counting the number of previous states for the one with the most choices (bottom-right) and iterates over the whole matrix.
<br>
The problem I kept facing, obviously, is that my algorithm didn't have any memory of what the possible states where made of and this information was crucial.

Stuck, I decided to Google something like "cells neighbours overtime computer science" to learn about Cellular Automaton.
<br>
I learn that the system I had to deal with was non-reversible and outer totalistic.
<br>
However, I didn't find any information that helped me to calculate the number of previous states of a non-reversible system.

I then decided to just brute-force my way to the solution.

The main idea of my algorithm is to compute for each line the ancestors that could have given this line, compare with the previous line which ones make sense, then merge the solutions for each line together with the rest.
<br>
To find the total number of solution, I just need to count them.

The algorithm worked but could be optimized.

My optimization came from the fact that each line only influence the one that is under it. Hence, once this line's ancestors are merged with the ancestors of the one under, it becomes useless and takes a lot of space in the memory. 
<br>
I then decided to get rid of them and merge the similar ancestors that remained. In order to do that I kept track of how many times each line was obtained.
<br>
The final result was, then, only the sum of occurences of last line's ancestors.

## Space and time complexity
The case where each cell has the most ancestors is when they're all without gas; that's the one we will study here.

In order to save some space, my algorithm needed the current state to be transpose before I started working on it.

### Space complexity
The width of the transposed graph is not larger than `9`.
<br>
Each cell has `12` ancestors but, once you selected an acestor for the first cell, the second cell can only have between `0` and `4` possible ancestors. The number of possible previous states is mutiplied by `4` with every cell we take into consideration and we consider at most 2 lines at the same time.
<br>
The number of previous state is inferior to ![4^(2\*w)](http://latex.codecogs.com/svg.latex?\inline&space;4^{2*w}).

The space complexity is **`o(2^w)`**.

### Time complexity
\*TODO\*