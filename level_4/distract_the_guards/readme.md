Distract the Guards
===================

The time for the mass escape has come, and you need to distract the guards so that the bunny prisoners can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the guards are fond of bananas. And gambling. And thumb wrestling.

The guards, being bored, readily accept your suggestion to play the Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two guards will pair off to thumb wrestle. The guard with fewer bananas will bet all their bananas, and the other guard will match the bet. The winner will receive all of the bet bananas. You don't pair off guards with the same number of bananas (you will see why, shortly). You know enough guard psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of guards will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to guarding the prisoners, and you don't want THAT to happen!

For example, if the two guards that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to guarding.

How is all this useful to distract the guards? Notice that if the guards had started with 1 and 4 bananas, then they keep thumb wrestling! `1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4` and so on.

Now your plan is clear. You must pair up the guards in such a way that the maximum number of guards go into an infinite thumb wrestling loop!

Write a function `answer(banana_list)` which, given a list of positive integers depicting the amount of bananas the each guard starts with, returns the fewest possible number of guards that will be left to watch the prisoners. Element `i` of the list will be the number of bananas that guard `i` (counting from 0) starts with.

The number of guards will be at least 1 and not more than 100, and the number of bananas each guard starts with will be a positive integer no more than 1073741823 (i.e. ![2^30](http://latex.codecogs.com/svg.latex?\inline&space;2^{30}) -1). Some of them stockpile a LOT of bananas.

Languages
=========

To provide a Python solution, edit `solution.py`
<br>
To provide a Java solution, edit `solution.java`

Test cases
==========

Inputs: `(int list) banana_list = [1, 1]`
<br>
Output: `(int) 2`

Inputs: `(int list) banana_list = [1, 7, 3, 21, 13, 19]`
<br>
Output: `(int) 0`

Solution
========

Once again, I offered 2 solutions to this problem.

I first wanted to go with a greedy solution but wasn't able to prove the correctness of the algorithm. I went with a different solution that had a slightly larger time complexity. When I proved the second one, I had the missing part to prove the greedy algorithm and submitted the later instead.

The greedy algorithm works like so:
1. Transform the `banana_list` into a adjacency matrix, with an edge between 2 guards only if they can get stuck in a loop.
2. Order the guards from the one that can get stuck playing with the least other guards to the one that get get stuck with the most people.
3. Pair the guards with the closest following in the list.

## Correctness

### Required properties of the graphs we work with
- First, we can prove that 2 guards can be stuck in a game *if and only if* the sum of their bananas is not a power of 2 and they are different to begin with.
  <br>
  Let `A(k)` and `B(k)` be the number of banana of the guards after `k` rounds of the game.

  `A(0) > B(0)` and 
  ![There exists t](http://latex.codecogs.com/svg.latex?\inline&space;\exists&space;t) such as `A(0) + B(0)` = ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t)
  <br>
  `<=>` `A(0) =` ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t) `- B(0)`
  <br>
  `<=>` `B(k) =` ![2^k](http://latex.codecogs.com/svg.latex?\inline&space;2^k) `B(0) mod ` ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t) 
  and `A(k) =` ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t) `-` ![2^k](http://latex.codecogs.com/svg.latex?\inline&space;2^k) `B(0) mod ` ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t)
  <br>
  `<=>` `B(k) =` ![2^k](http://latex.codecogs.com/svg.latex?\inline&space;2^k) `B(0) mod ` ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t) 
  and `A(k) =` ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t) `B(0) -` ![2^k](http://latex.codecogs.com/svg.latex?\inline&space;2^k) `B(0) mod ` ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t)
  <br>
  _because every multiple of ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t) modulo ![2^t](http://latex.codecogs.com/svg.latex?\inline&space;2^t) is equal to 0_

  This last line, evaluated on `k = t - 1`, gives:
  <br>
  `A(k) = B(k) =` ![2^t-1](http://latex.codecogs.com/svg.latex?\inline&space;2^{t&space;-&space;1}) `B(0)`

  **2 guards can be stuck in a game `<=>` the sum of their bananas is not a power of 2 and they are different to begin with**

- Then, we can prove that every 4 non-isolated vertices in `G` are connected.
  <br>
  Let's assume that we have a non-connected graph with 2 non-connected components that aren't isolated vertices:
  ```
  A----B        C----D
  ```
  In the rest of the proof, the number of banana associated to the guard `A` will be noted `a`.
  
  For this graph to exist, 
  ```
      |a > b
      |c > d
      |a + c = 2^k
      |a + d = 2^l
      |b + c = 2^m
      |b + d = 2^n
  ```
  ```
  <=> |k > m
      |l > n
      |a = 2^k - c
      |a = 2^l - d
      |b = 2^m - c
      |b = 2^n - d
  ```
  ```
   => |k > m
      |l > n
      |2^k - c = 2^l - d
      |2^m - c = 2^n - d
  ``` 
  ```
   => |k > m
      |l > n
      |2^m - 2^k = 2^l - 2^n
  ```
  ```
   => |k > m
      |l > n
      |2^m - 2^k = 2^l - 2^n
  ```
  ```
   => |2^k - 2^m > 2^m
      |2^l - 2^n > 2^n
      |2^k - 2^m + 2^l - 2^n = 0
  ```
  _which is absurd_.

  **So, if the graph `G` is not connected, his non-connected components are isolated vertices.**

### Initial state, with 3 vertices
Obviously, we don't have any problem proving it; 
- If the graph is connected, there will be only 1 guard left to be paired, no matter what is the pairing we choose.
- If the graph is made of 3 non-connected component, the 3 guards can't be paired in any way.

**The algorithm is verified with in its initial state**.

### Next state, where it gets a little crazier
Let's assume that the algorithm when given a graph with `n` vertices.
<br>
Let `G` be a graph with `n + 1` connected vertices (if there weren't connected, the problem would be trivial with the induction hypothesis).
<br>
Now, let's call `S` the solution found by the algorithm and `S'` the optimal solution.
<br>
Let `v` be the vertex in `G` with the least edges, the one with which the algorithm will start.

1. `v` is paired with the same vertex in `S` and in `S'`:
   By induction, we can assume that `S = S'` and that the algorithm would be correct
2. `v` is paired with different neighbours in the 2 solutions:
   - If `v` just has 1 neighbour:
     `v` is paired in `S` and not in `S'`. Obviously, `v` would have to be connected to a paired vertex for this solution to be possible (otherwise we would be able to improve it), let `w` be that vertex and `x` the vertex it's paired with. 
     <br>
     The induction hypothesis ensures that the algorithm run on `G - {v, w, x}` gives the best solution.
     <br>
     So the differences between `S` and `S'` are only on those 3 vertices. However, the number of vertices left unpaired in those 2 sets in the 2 solutions is the same.

     **The solution `S` is optimal**.

   - If `v` has more than 1 neighbour (`deg(v) > 1`):
     <br>
     We just need to prove that `G - {v, u}` is still a connected graph. If we can prove that, the induction hypothesis will do the rest.

     - First of all, removing those 2 vertices can't leave the graph with 2 not connected components that have more than 1 vertex because we showed in the [Required properties of the graphs we work with](#Required-properties-of-the-graphs-we-work-with) that these graphs can't exist with the way they are built.

     - Let's suppose that the removing these 2 vertices leaves a single vertex not connected to the graph and let `w` be that vertex.
       <br>
       In `G - {v, u}`, `deg(w) = 0`, so, in `G`, `deg(w) <= 2` .
       <br>
       In `G`, `deg(w) >= deg(v) >= 2` and `deg(u) >= deg(v) >= 2` because `v` has the least neighbours in `G`.
       <br>
       Now, `v` was paired with `u` instead of `w` so `deg(u) >= deg(w)`

       All of the above suggest that `{u, v, w}` is a complete non-connected component of `G` (these vertices are all linked to each other and only each other), with doesn't make sense since `G` was connected.

       Hence the **removing `{u, v}` can't leave a single vertex not connected to `G`**.

    Now, since `G - {v, u}` is connected, the induction hypothesis ensures that the algorithm will run and give us an optimal solution on this graph. Adding 2 paired vertices (`{u, v}`) to this solution will keep this solution optimality.

    So `S` and `S'` are equivalent solutions.

All of this to prove that `S` is optimal, so **The algoritm correctness is established for `n + 1` vertices**.

## Time and space complexity

### Space complexity

We transform the `banana_list` array of size `n` into a square matrix of size `n * n`. Then, each line in this matrix is paired with one of its lines and this is stored in an array of size `n`.

The final space complexity is **`o(n^2)`**.

### Time complexity

Filling the adjency matrix is `o(n^2)`. Counting the neighbours of a vertex is `o(n)`, so `o(n^2)` for all the vertices. Ordering them accordingly is `o(n * log(n))`.
<br>
Finally, assigning them to the next possible in the list is also `o(n^2)`


Hence the final time complexity is **`o(n^2)`**.