class Node:
    def __init__(self,val):
        self.val = val
        self.less = None
        self.more = None

    def compare(self, num):
        if num < self.val:
            return -1

        elif num > self.val:
            return 1

        return 0




class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, val):
        if not self.root:
            self.root = Node(val)
            return
        curr_root = self.root

        while True:
            curr_val = curr_root.compare(val)
            if curr_val == 0:
                return
            elif curr_val == 1:
                if not curr_root.more:
                    curr_root.more = Node(val)
                    return
                else:
                    curr_root = curr_root.more
            else:
                if not curr_root.less:
                    curr_root.less = Node(val)
                    return
                else:
                    curr_root = curr_root.less


    def __str__(self):
        queue = [self.root]
        result = []
        while len(queue) > 0:
            current = queue.pop(0)
            if not current:
                continue
            result.append(str(current.val))
            queue.append(current.less)
            queue.append(current.more)

        return ' '.join(result)


tree = Tree()

tree.add_node(5)
tree.add_node(3)
tree.add_node(7)
tree.add_node(2)
print(tree)