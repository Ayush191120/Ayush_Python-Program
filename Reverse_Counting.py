# This program demonstrates clean recursion. Let me know if you want it to write to a file instead of printing!

import sys
sys.setrecursionlimit(1100)  # Set a bit higher than 1000 to allow safe execution

def reverse_count(n):
    if n == 0:
        return
    print(n)
    reverse_count(n - 1)

reverse_count(1000)
