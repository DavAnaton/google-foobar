Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function `answer(m)` that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in `state 0`. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
```json
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
```
So, we can consider different paths to terminal states, such as:
```
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
```
Tracing the probabilities of each, we find that
- s2 has probability 0
- s3 has probability 3/14
- s4 has probability 1/7
- s5 has probability 9/14

So, putting that together, and making a common denominator, gives an answer in the form of
`[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator]` which is
`[0, 3, 2, 9, 14]`.

Languages
=========

To provide a Python solution, edit `solution.py`

To provide a Java solution, edit `solution.java`

Test cases
==========

Inputs:
:`(int) m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]`

Output:
:`(int list) [7, 6, 8, 21]`

Inputs:
:`(int) m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]`

Output:
:`(int list) [0, 3, 2, 9, 14]`

Solution
========
I didn't think about Absorbing Markov Chains right away, so I started to try implementing something using Johnson to find all the cycles in the graph and reduce them to a simple edge.

I spent so much time on this solution, that I felt bad deleting it. It fails some of the test cases, but you can take a look if you had time to spend. :)

The real solution implements Absorbing Markov Chains, as I said.

The way this works is that we will receive a graph that looks like this:
```
|q(0, 0)   ...   q(0, n)   r(0, 0)   ...   r(0, m)|
|  :::     ...     :::       :::     ...     :::  |
|q(n, 0)   ...   q(n, n)   r(n, 0)   ...   r(n, m)|
|   0      ...      0         1      ...      0   |
|  :::     ...     :::       :::     ...     :::  |
|   0      ...      0         0      ...      1   |
```
 and that represent the probability of a state to desintegrate in an another state (in the challenge, when a state doesn't desintegrate, they replace the self loop with no exiting edge).
 
 In order to solve the probabilities of a non-absorbing state to end up in an absorbing state, we need to compute `P = invert(I - Q) * R` where `I` is the matrix identity of size `n x n`.
 
 Since we start only with `state 0`, after we append the denominator the the end of `P[0]`, we will have the right answer.
 
 ## Time complexity
 My algorithm is **not** optimized. 
 
 I just followed the basic formulas to calculate a determinant (complexity `o(n!)`), inverse a matrix (complexity `o(n^3)`)... for readability and to ensure that the code was actually written by me.  
 
 By using `numpy` or any other optimized matrix computation librairy, the time complexity could have been more or less `o(m * n^2)` where `n` is the number of non-absorbing states and `m` the numver of absorbing states (`o(n^2.373)` to inverse `Q` and `o(m * n^2)` for the product of the result by `R`).
 
 Instead, my time complexity is **`o(n! + m * n^2)`**.
 
 