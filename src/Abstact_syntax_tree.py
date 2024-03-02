class Number():
    """Class for number processing"""
    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        return int(self.value)
    
class BinaryOp():
    """Binary operations"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    """Addition"""
    def evaluate(self):
        return self.left.eval() + self.right.eval()
    
class Sub(BinaryOp):
    """Subtraction"""
    def evaluate(self):
        return self.left.eval() - self.right.eval()
    
class Mul(BinaryOp):
    """Multipulcation"""
    def evaluate(self):
        return self.left.eval() * self.right.eval()
    
class Comment():
    pass

class Print():
    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        print(self.value.eval())