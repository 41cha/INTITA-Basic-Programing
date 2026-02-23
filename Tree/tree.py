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

    def find_node(self, value):
        curr_root = self.root
        while curr_root:
            match curr_root.compare(value):
                case 1:
                    curr_root = curr_root.more
                case -1:
                    curr_root = curr_root.less
                case 0:
                    return True
        return False

    def __str__(self):
        padding = ''
        def recursive_str(node, padding):
            result = padding + str(node.val) + '\n'
            padding += '.'
            if node.less:
                result += recursive_str(node.less, padding)

            if node.more:
                result += recursive_str(node.more, padding)

            return result

        return recursive_str(self.root, padding)



tree = Tree()

tree.add_node(5)
tree.add_node(3)
tree.add_node(7)
tree.add_node(2)
tree.add_node(1)
print(tree)
print(tree.find_node(8))
print(tree.find_node(5))