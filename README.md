# Twig coding challenge

This project consists of two files:
`splitter.py`, which contains the method
`split_array` to satisfy the requirements
of the challenge, and `test_splitter.py`,
which contains unit tests for this method.

### How to execute

One way to execute the code:
1. Open an interactive Python shell from 
this directory.
2. Enter `from splitter import split_array`
3. Call the above method, with a 
one-dimensional array as its first 
argument and a positive integer as its
second.

To run the unit tests:
1. Ensure Pytest is installed on your machine.
2. From a terminal in this directory, run `pytest`.

### Implementation notes

I decided to use Python for this task, as it
requires very little setup to create a working
project with concise, readable code.

For the main task, I decided to use a list
comprehension to build the list of sub-arrays,
as this seemed the clearest way to structure
the logic.

The method checks the types of the arguments provided
to it, as per the conditions given in the challenge
specification, and that the number of sub-arrays
to be created is a positive integer. 

### Edge case

When writing the solution, I came across an edge
case that produces a somewhat counter-intuitive
result for my solution, though I could not see that
it violated the conditions put forth by the
challenge.

The effect produced is that the resulting list
of sub-arrays includes 1 or more empty arrays,
i.e.

```python
split_array([1,2,3,4], 3) = [[1,2],[3,4],[]]
```

This edge case arises when the following 
condition is true for an array of length `x`
and a number of sub-arrays `y`:

```
(y / x) % 1 < 0.5
```

This is because my solution uses "ceiling division"
to find the size of a sub-array, i.e. it always 
rounds up, otherwise not every element in the
original array would be included in the list of
sub-arrays produced by the method.

Unsure of whether or not this is the desired output,
I decided to leave the solution as-is, include a
unit test to highlight the edge case and document
it here.