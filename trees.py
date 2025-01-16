from collections import Counter

trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]

tree_counts = {}

# for tree in trees:
#     if tree in tree_counts:
#         tree_counts[tree] += 1
#     else:
#         tree_counts[tree] = 1

tree_counts = Counter(trees)

for species, count in tree_counts.items():
    print(f"{species}: {count}")
