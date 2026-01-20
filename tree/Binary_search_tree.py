class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearch:
    def __init__(self):
        self.root = None

    def insert(self,data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        break
                    else:
                        current_node = current_node.right

    def contains(self,data):
        current_node = self.root
        while current_node is not None:
            if data<current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right
            else:
                return True
        return False


    def remove(self, data):
        self.remove_helper(data, self.root, None)


    def remove_helper(self,data, current_node, parent_node):
        while current_node is not None:
            if data < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            elif data > current_node.data:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.data = self.get_min_value(current_node.right)
                    self.remove_helper(current_node.data, current_node.right, current_node)
                else:
                    if parent_node is None:
                        if current_node.right is None:
                            self.root = current_node.left
                        else:
                            self.root = current_node.right
                    else:
                        if parent_node.left == current_node:
                            if current_node.right is None:
                                parent_node.left = current_node.left
                            else:
                                parent_node.left = current_node.right
                        else:
                            if current_node.right is None:
                                parent_node.right = current_node.left
                            else:
                                parent_node.right = current_node.right
                break
    def get_min_value(self, current_node):
        if current_node.left is None:
            return current_node.data
        else:
            return self.get_min_value(current_node.left)



    def in_order(self):
        self.in_order_helper(self.root)
    def in_order_helper(self, node):
        if node is not None:
            self.in_order_helper(node.left)
            print(node.data)
            self.in_order_helper(node.right)

    def pre_order(self):
        self.pre_order_helper(self.root)
    def pre_order_helper(self, node):
        if node is not None:
            print(node.data)
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def post_order(self):
        self.post_order_helper(self.root)
    def post_order_helper(self, node):
        if node is not None:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.data)

    def find_closest(self, target):
        current_node = self.root
        closest = current_node.data
        while current_node is not None:
            if abs(target - closest) > abs(target - current_node.data):
                closest = current_node.data
            if target < current_node.data:
                current_node = current_node.left
            elif target > current_node.data:
                current_node = current_node.right
            else:
                break
        return closest




def main():
    bs = BinarySearch()
    bs.insert(10)
    bs.insert(8)
    bs.insert(14)
    bs.insert(17)
    bs.insert(13)

    bs.in_order()
    #bs.pre_order()
    #bs.post_order()

    #print(bs.find_closest(12))


if __name__ == "__main__":
    main()

