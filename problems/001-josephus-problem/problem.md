# Josephus Problem

n people stand in a circle, numbered 0 to n-1. Starting at position 0,
you count k people (inclusive of the starting point) and eliminate the
k-th one. Counting continues from the next person. Repeat until one
person remains.

Given n and k, return the index (0-based, in the original circle) of
the last remaining person.

## Signature
def josephus(n: int, k: int) -> int:

## Constraints
- 1 <= n <= 10^6
- 1 <= k <= 10^9

## Example
josephus(5, 2) -> 2
josephus(1, 5) -> 0