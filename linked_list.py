class LinkedList:
    def __init__(self, nodes=None):
        if nodes is None:
            self.head = None 
        else:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next 
    
    def __repr__(self):
        node = self.head 
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
    def __iter__(self):
        node = self.head 
        while node is not None:
            yield node
            node = node.next
            
    def add_first(self, node):
        node.next = self.head 
        self.head = node 
        
    def add_last(self, node):
        if self.head is None:
            self.head = node 
            return
        for current_node in self:
            pass
        current_node.next = node 
        
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('The list is empty')
        
        for node in self:
            if target_node_data == node.data:
                new_node.next = node.next 
                node.next = new_node
                return
        
        raise Exception('Node with data %s is not found', target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if self.head is Node:
            return self.add_first(new_node)
        
        prev_node = self.head 
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node 
                new_node.next = node 
                return 
            prev_node = node 
        
        raise Exception('Node with data %s is not found', target_node_data)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception('The list is empty')
        if self.head.data == target_node_data:
            self.head = self.head.next
            return         
        
        prev_node = self.head 
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next 
                return 
            prev_node = node 
        
        raise Exception('Node with data %s is not found', target_node_data)
    
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
    
    def __repr__(self):
        return str(self.data)
    
if __name__ == '__main__':
    # llist initialization
    llist = LinkedList(['a', 'b', 'c', 'd', 2])
    print('initializing:\t', llist) 
    
    # traversing (iterating) through llist
    print('iterating:\t ', end='')
    for node in llist:
        print(node, end=' -> ')
    print(None)
    
    # operations on the elements of the llist
    llist.add_first(Node('Boom!'))
    llist.add_last(Node('Bam!'))
    llist.add_after('b', Node('Bimbim!'))
    llist.add_before('c', Node('Bambom!'))
    llist.remove_node('d')
    print('operations:\t', llist)