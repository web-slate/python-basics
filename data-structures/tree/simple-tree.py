# from testUtils import solution_title, print_and_assert_new, getTestResult
# from commonUtils import timeComplexity, spaceComplexity

print('\n >>> Simple Tree Implementation')

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def traverse_child(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print('>', current_node.value)
            nodes += current_node.children

ceo = TreeNode('CEO')
finance = TreeNode('Finance Head')
marketing = TreeNode('Marketing Head')
it = TreeNode('IT Head')

ceo.add_child(finance)
ceo.add_child(marketing)
ceo.add_child(it)

finance_lead = TreeNode('Finance Lead')
marketing_lead = TreeNode('Marketing Lead')
it_lead = TreeNode('IT Lead')

finance.add_child(finance_lead)
marketing.add_child(marketing_lead)
it.add_child(it_lead)

ceo.traverse_child()