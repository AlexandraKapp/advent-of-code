class tree_node:
    children = []

    def __init__(self, file_path, parent, which_type, size):
        self.file_path = file_path
        self.parent = parent
        self.which_type = which_type
        self.size = size
    
    def add_child(self, child):
        new_children = self.children + [child]
        self.children = list(set(new_children))

def recursive_update_size(node):
    if len(node.children) > 0:
        for child in node.children:
            node.size += recursive_update_size(tree[child])
    return node.size

if __name__ == "__main__":
    lines = [str.strip(l, "\n") for l in open("input_day7.txt","r").readlines()]

    # create tree #
    tree = dict()

    # create start node
    current_node = "/"
    tree[current_node] = tree_node("/", "", "dir", 0) 

    for command in lines:
        # is instruction?
        if str.startswith(command, "$"):
            instr = str.split(command, "$ ")[1]
            # change directory
            if str.startswith(instr, "cd"):
                move_to_dir = str.split(instr, "cd ")[1]
                # move to root
                if move_to_dir == "/":
                    current_node = "/"
                # move up
                elif move_to_dir == "..":
                    current_node = tree[current_node].parent
                # move down to
                else:
                    current_node = current_node + "/" + move_to_dir
        else:
            # add dir to tree
            if str.startswith(command, "dir"):
                item = str.split(command, "dir ")[1]
                size = 0
                which_type = "dir"
            # add leaf to tree
            else:
                size, item = str.split(command, " ")
                which_type = "file"

            item_path = current_node + "/" + item
            tree[item_path] = tree_node(item_path, current_node, which_type, int(size))
            tree[current_node].add_child(item_path)

    # count file sizes #
    recursive_update_size(tree["/"])

    ############ Part 1 ###########
    print(sum([n.size for n in tree.values() if (n.size < 100000) & (n.which_type == "dir")]))

    ############ Part 2 ###########
    unused_space = 70000000 - tree["/"].size
    needed_space = 30000000 - unused_space

    node_as_list = list(tree.values())
    diff_to_needed_space = [n.size - needed_space for n in node_as_list]
    closest_value = min([diff for diff in diff_to_needed_space if diff > 0])
    print(node_as_list[diff_to_needed_space.index(closest_value)].size)