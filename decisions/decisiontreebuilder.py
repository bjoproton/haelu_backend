from decisions.enums import NODE_TYPE_NON_LEAF, NODE_TYPE_LEAF
from haelu.enums import VALUE_TYPE_INTEGER, VALUE_TYPE_FLOAT, VALUE_TYPE_BOOLEAN, OPERATOR_GREATER_THAN, OPERATOR_LESS_THAN, OPERATOR_EQUAL_TO
import matplotlib.pyplot as plt
import io
import base64


class Node:
    def __init__(self, layer, tree, model_instance, x=0):
        self.tree = tree
        self.layer = layer
        self.model_instance = model_instance
        self.name = self.model_instance.name
        self.node_type = self.model_instance.node_type
        self.condition = self.model_instance.condition
        self.x = x
        self.y = -self.layer*5

        if self.node_type == NODE_TYPE_NON_LEAF:
            layer = self.layer + 1
            self.pos_node = Node(layer, self.tree, self.tree.model_instance.nodes_m2m.get(node=self.model_instance).pos_node, x=self.x + 2.5)
            self.neg_node = Node(layer, self.tree, self.tree.model_instance.nodes_m2m.get(node=self.model_instance).neg_node, x=self.x - 2.5)

        self.plot()

    def evaluate(self, data):
        interest_var = data[self.condition.value_name]
        condition_value = self.condition.value

        if self.condition.value_type == VALUE_TYPE_BOOLEAN:
            condition_value = condition_value == 'True'
        elif self.condition.value_type == VALUE_TYPE_INTEGER:
            condition_value = int(condition_value)
        elif self.condition.value_type == VALUE_TYPE_FLOAT:
            condition_value = float(condition_value)

        if self.condition.operator == OPERATOR_EQUAL_TO:
            return self.return_pos_node() if condition_value == interest_var else self.return_neg_node()
        elif self.condition.operator == OPERATOR_LESS_THAN:
            return self.return_pos_node() if interest_var < condition_value else self.return_neg_node()
        elif self.condition.operator == OPERATOR_GREATER_THAN:
            return self.return_pos_node() if interest_var > condition_value else self.return_neg_node()

    def return_pos_node(self):
        return self.pos_node

    def return_neg_node(self):
        return self.neg_node

    def plot(self):
        self.tree.ax.text(self.x, self.y, f'{self.name}', size=10, rotation=0.,
                          ha="center", va="center",
                          bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8)),
                          )

        if self.node_type == NODE_TYPE_LEAF:
            return

        x_center_neg = self.x - 1.5
        y_center_neg = self.y - 2.5

        self.tree.ax.text(x_center_neg, y_center_neg, "Negative",
                          ha="center", va="center", rotation=45, size=10,
                          bbox=dict(boxstyle="larrow,pad=0.3",
                                    fc="lightblue", ec="steelblue", lw=2))

        x_center_pos = self.x + 1.5
        y_center_pos = self.y - 2.5
        self.tree.ax.text(x_center_pos, y_center_pos, "Positive",
                          ha="center", va="center", rotation=-45, size=10,
                          bbox=dict(boxstyle="rarrow,pad=0.3",
                                    fc="lightblue", ec="steelblue", lw=2))


class DecisionTree:
    def __init__(self, model_instance):
        self.model_instance = model_instance

        # Plot output
        self.fig = None
        self.ax = None
        self.fig, self.ax = plt.subplots()
        self.ax.set_axis_off()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-20, 0)

        # Nodes node
        self.model_nodes = self.model_instance.nodes_m2m.all()
        self.root_node = Node(0, self, self.model_nodes.first().node)

    def plot(self):
        my_stringIObytes = io.BytesIO()
        self.fig.savefig(my_stringIObytes, format='png')
        my_stringIObytes.seek(0)
        my_base64_pngData = base64.b64encode(my_stringIObytes.read()).decode()
        print (my_base64_pngData)
        return my_base64_pngData

    def evaluate(self, data):
        # Start with root node and traverse until completed
        n = self.root_node
        while True:
            if n.node_type == NODE_TYPE_LEAF:
                return n.name

            n = n.evaluate(data)
