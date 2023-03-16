Python Project Euler
====================
Code for a ~~elegant, concise~~ terrible computational efficiency language.

<sub>And occasionally C/C++ for speed, Mathematica for math, etc.</sub>

*Clean Code, and Keep It Simple, Stupid!*

Some features of number.py
--------------------------

- Simple Sieve of Eratosthenes
- Miller-Rabin primality test with potential witnesses
- Euler's totient function, totient range, totient sum
- Timeit and memoization wrapper
- Prime-counting function using Meissel-Lehmer
- Others: binary search, Dijkstra's algorithm, modular multiplicative inverse, int to base conversion, etc.

Running the Code
----------------
The python code is intended to be run with PyPy3 with JIT. 
Looking at the [PyPy speed benchmarks](https://speed.pypy.org/comparison/) (benchmarks ai, crypto_pyaes, float, go, pidigits), PyPy3 support is mature enough that (at least for numerical tasks) the speed is the same as PyPy2. 
Therefore, my old code written to be Python 2.7 compatible should be modified for Python 3. 

By convention, other output is allowed, but the final result should be the last line. 
Use `time` for overall timing and the timing wrapper for code sections.

Problems Solved Milestones/Levels
---------------------------------

| Level | Problems | Date       |
|-------|----------|------------|
| 1     | 25       | 2015-05-25 |
| 2     | 50       | 2015-06-13 |
| 3     | 75       | 2015-07-14 |
| 4     | 100      | 2015-08-23 |
| 5     | 125      | 2015-10-13 |
| 6     | 150      | 2016-04-17 |
| 7     | 175      | 2017-06-28 |
| 8     | 200      | 2018-08-26 |
| 9     | 225      | 2023-02-08 |

Solution Highlights
-------------------

- 5, 12, 14, 17, 18, 21, 23, 24, 26, 32, 36, 37, 43, 51, 57, 62, 65, 66, 68, 
70, 76, 79, 82, 86, 88, 89, 96
- 100, 101, 102, 107, 108, 111, 113, 114, 122, 126, 128, 131, 137, 144, 148, 152, 154, 158, 178, 199
- 265, 297
- 317
- 401, 461, 491
- 500, 501, 504, 527, 545, 561, 581
- 605, 624, 625, 643, 663
- 804, 828
