import sys
tree_dict = {}
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree: break
    if tree not in tree_dict:
        tree_dict[tree] = 1
    else:
        tree_dict[tree] += 1
total_tree = sum(tree_dict.values())
for t in sorted(tree_dict.keys()):
    print(f"{t} {tree_dict[t]/total_tree * 100:.4f}")
