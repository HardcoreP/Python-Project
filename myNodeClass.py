class Node(object):

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)

    def getValue(self):
        return self.value
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getParent(self):
        return self.parent
    
    def setValue(self, value):
        self.value = value
    
    def setLeft(self, leftNode):
        assert isinstance(leftNode, Node)
        if leftNode.getParent() == None:
            self.left = leftNode
            leftNode.parent = self
        else:
            raise Exception(str(leftNode) + ' has a parent already!')

    def setRight(self, rightNode):
        assert isinstance(rightNode, Node)
        if rightNode.getParent() == None:
            self.right = rightNode
            rightNode.parent = self
        else:
            raise Exception(str(rightNode) + ' has a parent already!')
    
def DFS(root, fnc):
    stack = [root]
    
    while len(stack) != 0:
        print stack[0].getValue()
        if fnc(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            if temp.getRight() != None:
                stack.insert(0, temp.getRight())
            if temp.getLeft() != None:
                stack.insert(0, temp.getLeft())
    return False

def BFS(root, fnc):
    queue = [root]
    while len(queue) != 0:
        print queue[0].getValue()
        if fnc(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            
            if temp.getLeft() != None:
                queue.append(temp.getLeft())
            if temp.getRight() != None:       
                queue.append(temp.getRight())
    return False

def nodePath(node):
    if not node.getParent():
        return [node]
    return [node] + nodePath(node.getParent())

def find6(node):
    return node.getValue() == 6

def find10(node):
    return node.getValue() == 10

count = 0
def debugPrint(x):
    global count
    print str(count) + '.The type of object ' + str(x) + ' is: '+ str(type(x))
    count += 1

n5 = Node(5)
n2 = Node(2)
n1 = Node(1)
n4 = Node(4)
n8 = Node(8)
n6 = Node(6)
n7 = Node(7)
n3 = Node(3)

n5.setLeft(n2)
n5.setRight(n8)
n2.setLeft(n1)
n2.setRight(n4)
n8.setLeft(n6)
n6.setRight(n7)
n4.setLeft(n3)
