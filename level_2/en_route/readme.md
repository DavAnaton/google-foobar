En Route Salute
===============

Commander Lambda loves efficiency and hates anything that wastes time. She's a busy lamb, after all! She generously rewards henchmen who identify sources of inefficiency and come up with ways to remove them. You've spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other - one at a time - before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could save several collective hours of employee time per day. But first, you need to show her how bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
`"--->-><-><-->-"`

Each hallway string will contain three different types of characters: `'>'`, an employee walking to the right; `'<'`, an employee walking to the left; and `'-'`, an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function `answer(s)` which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. `s` will contain at least 1 and at most 100 characters, each one of `-`, `>`, or `<`.

Languages
=========

To provide a Python solution, edit `solution.py`

To provide a Java solution, edit `solution.java`

Test cases
==========

Inputs:
:`(string) s = ">----<"`

Output:
:`(int) 2`


Inputs:
:`(string) s = "<<>><"`

Output:
:`(int) 4`
    
Solution
========

For this problem, we just need to count the number of interaction between people walking right and people walking left. If we take the hallway from left to right, we just have to keep a count of the people walking right, and add this number to the total interactions number when we encounter someone walking left. The number of times the employees will salute will be twice the number of interactions.

## Correctness
Let's assume that the number we get is wrong. There is someone, let's assume walking right, for whome the count is not right. This means that he will interact with someone walking left that is not on the right of the hallway (since we already counted those). This is absurd because they can't meet someone behind them.

By symetry of the problem, we don't need to examine the case where the error would be for someone walking left.

**Therefore, the algorithm is correct.**

## Time and space complexity

We just keep track of the number of interaction, which is **`o(1)`** (space complexity).

For the time complexity, we just go through the list and execute an operation that requires a constant time. The time complexity is **`o(n)`**. 
