from sowing.node import Node
import immutables

hashable_dict = immutables.Map(a=1, b=2)
set_test = set([1, 2, 3])
frozen_set = frozenset([1, 2, 3])
tuple_test = (1, 2, 3)



tree = (
 Node("Root")
 .add(Node("Left").add(Node("Leaf"), data=hashable_dict).add(Node("Leaf")))
 .add(Node("Right").add(Node("Leaf"), data=frozen_set).add(Node("Leaf")))
)

print(tree)

