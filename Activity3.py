def paths(m, n):
    if m == 1 or n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)


print("  paths(3, 3) =", paths(3, 3))
print("  paths(4, 4) =", paths(4, 4))
n = int(input("Enter grid size for both rows and cols (try 5 or 6): "))

print("each call branches into two — move down or move right — the tree grows fast")
print( paths(n, n))