class DecisionTree:
    def __init__(self, root_node, vals):
        self.root_node = root_node
        self.vals = vals

    def evaluate(self):
        # Start with root node and traverse until completed
        n = self.root_node
        while True:
            if n.leaf:
                print(f'Final result {n._class}')
                break
            
            _name = n.name
            (l, n) = n.evaluate(self.vals)
            print (f'{l} from {_name}, {n.name}')

    def draw(self):
        print("")
        n = self.root_node
        pos = n.pos_node
        neg = n.neg_node
        print(n.draw())



GREATER_THAN = 0
LESS_THAN = 1
BOOL = 2

choices = {GREATER_THAN: ">",
           LESS_THAN: "<",
           BOOL: "="}
class Node:
    def __init__(self, name=None, _type=None, threshold=None, leaf=False, _class=None):
        self.name = name if name else ""
        self.leaf = leaf
        self._type = _type
        self.threshold = threshold
        self._class = _class if _class else ""

    def evaluate(self, data):
        print(f'{self.name} evaluate')
        interest_var = data[self.name]
        if self._type == BOOL and isinstance(interest_var, bool):
            if interest_var:
                return self.passed()
            return self.failed()

        if self._type in (GREATER_THAN, LESS_THAN) and (isinstance(interest_var, int) or isinstance(interest_var, float)) and (isinstance(self.threshold, int) or isinstance(self.threshold, float)):
            if self._type == GREATER_THAN:
                if interest_var > self.threshold:
                    return self.passed()
                return self.failed()
            elif self._type == LESS_THAN:
                if interest_var < self.threshold:
                    return self.passed()
                return self.failed()

    def passed(self):
        return ("Positive", self.pos_node)

    def failed(self):
        return ("Negative", self.neg_node)

    def set_pos_node(self, pos_node):
        self.pos_node = pos_node

    def set_neg_node(self, neg_node):
        self.neg_node = neg_node

    def draw(self):
        expression = f'{self.name} {choices[self._type]} {self.threshold}'
        repr = "      --------      \n"
        num_spaces = int((20 - len(expression)) / 2)
        repr += " " * num_spaces + f'{expression}' + " " * num_spaces + "\n"
        repr += "      --------      \n"
        repr += "       /    \       \n"
        repr += "      /      \      \n"
        repr += "     /        \     \n"
        repr += "    /          \    \n"
        return repr

vals = {'age': 76,
        'respiratory infection': True,
        'bp': 60,
        'mental': True}

n = Node(name="age", _type=GREATER_THAN, threshold=75, leaf=False)
n.set_neg_node(Node(leaf=True, _class="Negative"))
n.set_pos_node(Node(name="respiratory infection", _type=BOOL))
t = DecisionTree(n, vals)

n = n.pos_node
n.set_neg_node(Node(leaf=True, _class="Negative"))
n.set_pos_node(Node(name="bp", _type=LESS_THAN, threshold=90))

n = n.pos_node
n.set_pos_node(Node(leaf=True, _class="Red Flag"))
n.set_neg_node(Node(name="mental", _type=BOOL))

n = n.neg_node
n.set_pos_node(Node(leaf=True, _class="Red Flag"))
n.set_neg_node(Node(leaf=True, _class="Negative"))






