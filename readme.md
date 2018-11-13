# Foobar

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

I was researching [Google Charts](https://developers.google.com/chart) when I saw a pink bubble at the top of the screen. After clicking it, I arrived on a black screen looking like a console saying something along the line of "You're speaking our language. Up for a challenge?".
After a few clicks, Google started sending me my first foobar coding challenge.

Amongst the different skills and knowledge that were tested, you can find:
  - Atbash cipher
  - Basic Mathematical Knowledge (Fibonacci sequence, Combinations & Permutations,...)
  - Deeper Mathematical Knowledge (Linear Algebra, Absorbing Markov Chains, ...)
  - Greedy algorithms
  - Basic Algorithms understanding (Ability to write a few lines of code to solve a simple problem)
  - Common Algorithms (BFS, DFS, Kosaraju, Johnson, ...)
  - Deeper Algorithms understanding (Ability to divide complex problems in many small problem, and to combine well-known algorithms with personal algorithm knowledge, like augmenting paths, to solve them)
  - Dynamic Programming
  - [Cellular Automaton](http://www.cs.tau.ac.il/~nachumd/models/CA.pdf)
  - Brute force optimization

In order to work with a Test Driven Development, I created a ```create_check_function.py``` with a general function to verify test cases. By importing this module, I get a ```check_function``` that is called with the following parameters ```[any] test_cases, [any] expected, (function) answer_function``` and gives another function. When called with no parameter, this last one checks all the test cases and by passing in an index, we can check just one relevant test case, for easier development. 
Each folder will then have a ```test.py``` file that will implement the test for each challenge. Each folder will also have a ```readme.txt``` that describes the problem as Google gave it to me, and a ```solution.py``` that solves the problem. 

## To Do
  - Maybe ```level_4/free_the_bunny_prisoners``` needs a proof of correctness. The algorithm uses combinations and is very simple and straight forward but the proof is harder to write down. 
  - ```level_5/expanding_nebula``` needs to have its time complexity calculated.
  - If you also took the foobar challenge and had a challenge that is not on the list, I would love it if you could send me the ```readme.txt``` so I can have one more.