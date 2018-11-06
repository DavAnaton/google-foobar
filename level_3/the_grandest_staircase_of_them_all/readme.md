The Grandest Staircase Of Them All
==================================

With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when `N = 3`, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (`#` indicates a brick)
```
#
##
21
```
When `N = 4`, you still only have 1 staircase choice:
```
#
#
##
31
 ```
But when `N = 5`, there are two ways you can build a staircase from the given bricks. The two staircases can have heights `(4, 1)` or `(3, 2)`, as shown below:
```
#
#
#
##
41
```
```
#
##
##
32
```
Write a function called `answer(n)`  that takes a positive integer `n` and returns the number of different staircases that can be built from exactly `n` bricks. `n` will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

Languages
=========

To provide a Python solution, edit `solution.py`
<br>
To provide a Java solution, edit `solution.java`

Test cases
==========

Inputs: `(int) n = 3`
<br>
Output: `(int) 1`

Inputs: `(int) n = 200`
<br>
Output: `(int) 487067745`

Solution
========

This problem is a typical problem of dynamic programming. Each solution depends on the solutions you had in the previous steps.

To solve this, we will solve the problem when we have 0 brick, and then iterate until `n` and store the results in a matrix.
<br>
In my solution, each cell `(i, j)` holds the number of staircase we can make from `j` bricks knowing that the largest step uses `i` bricks.

## Correctness
### Initial step
For `n=0`, a 0 brick staircase is valid. 
<br>
Any other staircase can't be built because we don't have enough bricks. Hence the total number of staircases: `1 + 0 + .... + 0 = 1`. 
<br>
To this number, we take out `1` to get the number of staircase with more than 1 step and get the answer we were expecting: `0`.

*The algorithm is verified for the initial step.*

### Induction step
Let's assume that the algorithm is verified under a given state `n` included.
<br>
Now, we have `n + 1` bricks.

If we start using `i > 0` bricks (starting a staircase with the biggest step that has 0 brick is not interesting), we will be left with `n + 1 - i <= n` bricks.
<br>
Now, the inductive step says that we already solved the problem with `n + 1 - i` bricks. We just can't start the staircase above the first step with more than `i - 1` bricks, so we just have to sum all the solutions `S[n + 1 - i][j]` for `j` between `0` and `i`. This is the value that we stored in the algorithm.

*The algorithm is verified for the inductive step.*


## Time and space complexity

### Space complexity
The space complexity is obviously **`o(n^2)`** because of the size of the matrix we use to store the previous steps.

### Time complexity
To improve readability and ease the process of development, I accepted to have a time complexity of `o(n^3)` instead of `o(n^2)`. In my code, each cell `(i, j)` holds the number of staircase we can make from `j` bricks knowing that the largest step uses `i` bricks. This implies that for each cell, I have to compute the sum of a line between `0` and `i - 1`, which is a `o(n)` operation. Hence the time complexity **`o(n^3)`**. 

To get the optimal time complexity that this problem can get, each cell `(i, j)` must hold the number of staircase we can make from `j` bricks knowing that the largest step uses **at most** `i` bricks. Then, we would not have to compute a sum for each cell. 