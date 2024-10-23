class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        print(" " * self.get_level() * 3 ,"|--",self.data)
        for child in self.children:
            child.print_tree()



def build_root_tree():
    root = TreeNode("Main")

    node1 = TreeNode("Node1")
    node2 = TreeNode("Node2")
    node3 = TreeNode("Node3")

    sub_node1 = TreeNode("sub_node1")
    sub_node2 = TreeNode("sub_node2")
    node1.add_child(sub_node1)
    node1.add_child(sub_node2)

    
    root.add_child(node1)
    node2.add_child(node3)
    root.add_child(node2)

    root.print_tree()
    
    

if __name__ == "__main__":
   build_root_tree()
   
