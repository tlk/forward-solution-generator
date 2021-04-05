↻ There and Back Again ↺
========================

The [Nintendo game](challenge/hello.cpp) takes a 32-byte input value and returns a 16-byte output value. The objective of the game is to find out how to reverse this process.

In the following, input values are referred to as solutions and an output value is referred to as a target.

Here is an example of a solution (in hex) to the target value "Hello, World!":
```
$ make solution
a728ecdd3663964c88884c193636f2967d074c19dd88dd3688ddf2ddb9c3eca7 Hello, World!   
```

This solution was generated in constant time.


SP-network
----------
The game algorithm takes a solution and applies substitution and permutation operations to it repeatedly (256 times). The substitution table maps each of the 32 bytes from a set of 256 values to a set of 240 values and it has an interesting – almost magic – property that shall not be revealed here.
The permutation is done by XOR'ing bytes in a specific pattern that is illustrated below.

![Pbox](./assets/pbox.svg)

Animation of a single solution
------------------------------
 The first line in this animation represents a 32-byte solution. Each pixel in the line corresponds to a bit in the 32 bytes.
 
 The following lines (rows of pixels) represents temporary values being passed through the SP-network in 256 steps.
 
 The last line represents the last 32-byte value before it is reduced to the final 16-byte target.

![Steps](./assets/steps.gif)

Solution generator
------------------
The solution generator works its way [backwards](game/nreverse.py) up through the SP-network and computes all valid solutions for any given target.

In this example, the solution generator is configured to return 8 solutions. The solutions are passed over (piped) to the forward program which runs the game algorithm on the solutions and prints their corresponding target values:

```
$ tools/reverse.py 8 'Hello there!!!!!' | tools/forward.py | uniq | cat -n
    1	338dd8a345b898fc66c0ccbabdc12b68fd7321f4d5f0c6fd50ba1ef4b97aa2bd Hello there!!!!!
    2	338dd8a345cf98fc66c0ccbabdc12b68fd7321f4d5f0c6fd50ba1ef4b97aa2bd Hello there!!!!!
    3	24150ff7d529334b45a8ea13cb2a997bef2b2cb72b179fda52cc7a85492b3fbc Hello there!!!!!
    4	24150ff7d5b5334b45a8ea13cb2a997bef2b2cb72b179fda52cc7a85492b3fbc Hello there!!!!!
    5	24970ff7d529334b45a8ea13cb2a997bef2b2cb72b179fda52cc7a85492b3fbc Hello there!!!!!
    6	24970ff7d5b5334b45a8ea13cb2a997bef2b2cb72b179fda52cc7a85492b3fbc Hello there!!!!!
    7	7c150ff7d529334b45a8ea13cb2a997bef2b2cb72b179fda52cc7a85492b3fbc Hello there!!!!!
    8	7c150ff7d5b5334b45a8ea13cb2a997bef2b2cb72b179fda52cc7a85492b3fbc Hello there!!!!!
```

The solution generator is single-threaded and implemented with Python generators. It takes a little while before it discovers the first solution:

```
$ make perftest-level3
8192 solutions found in 5.62s, on average 0.69ms per solution.
8192 solutions found in 4.18s, on average 0.51ms per solution.
8192 solutions found in 4.39s, on average 0.54ms per solution.
8192 solutions found in 3.61s, on average 0.44ms per solution.
```

Animation of multiple solutions
-------------------------------
This animation is similar to the previous animation, but here each frame represents all 256 steps of a unique solution. The animation contains only a tiny subset of all solutions for this particular target. Notice how the bottom-part does not change because all solutions in this animation leads to the same target.

![Solutions](./assets/solutions.gif)


See also
--------

This page contains a note with related tables and graphs that may be of interest: https://tlk.github.io/nsg/
