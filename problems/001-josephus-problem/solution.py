# Josephus returns de idx of the survivor of an n circle, with k jumping

# Time: O(n^2) (pop is O(n)); Space: O(n)
def josephus(n: int, k: int) -> int:
    if n < 1 or k < 1:
        return -1

    people = list(range(n))
    current = 0

    while len(people) > 1:
        current = (current + k - 1) % len(people)
        people.pop(current)

    return people[0]

# Time: O(n); Space: O(1), actually O(n) space bc of recursion, use "for" for O(1)
def josephus_rec(n: int, k: int) -> int:
    if n < 1 or k < 1: # constraint
        return -1
    
    if n == 1: # base case
        return 0

    erased_idx = (k - 1) % n # who will be erased in this n-size circle
    survivor_idx = josephus_rec(n-1, k) # the survivor_idx of an (n-1)-circle
    original_idx = (erased_idx + survivor_idx + 1) % n # translate the (n-1) to n

    return original_idx