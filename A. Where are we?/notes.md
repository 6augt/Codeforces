# UTPC Contest 9-16-2026 Div. 2 (Beginner); A — Where Are We?

![Div](https://img.shields.io/badge/Div-2-green)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topic-2DGrid-orange](https://img.shields.io/badge/Topic-2DGrid-orange)
![Topic-Implementation-orange](https://img.shields.io/badge/Topic-Implementation-orange)

> You can find problem A [here](https://codeforces.com/gym/106711/problem/A)

## Instructions


> The University of Texas Programming Club has lost track of where it is after staring at grid diagrams for too long. Fortunately, the club remembers one essential fact: Texas is shaped exactly like a size-1 plus sign. In this problem, a size-1 plus sign consists of five cells: a center cell and the four cells that share a side with it.
>
>You are given an 𝑛×𝑚 map describing UTPC and its surroundings. Every cell is either open or blocked off. Count the number of ways to place a size-1 plus sign on the grid, lying on only open cells. Two placements are considered different if their center cells are different.
>
>**Input**
>The first line contains two integers 𝑛 and 𝑚 (1≤𝑛,𝑚≤100), the number of rows and columns of the map.
>
>Each of the next 𝑛 lines contains a string of 𝑚 characters. A character "." represents an open cell, and a character "#" represents a blocked cell.
>
>**Output**
>Print one integer: the number of valid placements of Texas.

## Steps To Solve it
When it comes to Codeforces problems, I always try to understand what is being said first and then try to code it.

If someone were to ask me what steps they should take to solve any problem, I'd say:

1. Read through the instructions carefully. Take your time if needed.
2. Once you understand the majority of the problem, start by writing the required input from the problem.
3. Use logic and reasoning to go from the input to the required output.

## My Reasoning
### Input

> The first line contains two integers 𝑛 and 𝑚 (1≤𝑛,𝑚≤100), the number of rows and columns of the map.

This means that `n` and `m` are both provided on the **same line**, with `n` representing the number of rows and `m` representing the number of columns.

At first, we might think we can simply do:

```python
n, m = input(), input()
```

However, this would expect `n` and `m` to be entered on **separate lines**. Since the problem provides them on the same line, we instead use:

```python
n, m = map(int, input().split())
```

#### Breakdown

* `input()` reads the entire line.
* `.split()` separates the two values.
* `map(int, ...)` converts both values from strings into integers.
* `n, m` assigns the two integers to their respective variables.

Also, there's another hidden input that might be easy to miss:

> Each of the next 𝑛 lines contains a string of 𝑚 characters.

This means that after declaring `n` and `m`, we also need to read the map itself. Each of the next `n` lines represents one row of the grid, containing `m` characters.

We can store these rows inside a list:

```python
grid = []

for row in range(n):
    grid.append(input())
```

Here, `grid` will contain all the rows of the map, allowing us to access individual cells later using `grid[row][column]`.

## My Mistakes

## Conclusion
