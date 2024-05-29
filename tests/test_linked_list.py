import unittest
from io import StringIO
import sys
from src.linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    # Tests for append method
    def test_append_single_node(self):
        n1 = Node(1)
        self.ll.append(n1)
        self.assertEqual(self.ll.head.data, 1)
        self.assertIsNone(self.ll.head.next)

    def test_append_multiple_nodes(self):
        n1 = Node(1)
        n2 = Node(2)
        self.ll.append(n1)
        self.ll.append(n2)
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.head.next.data, 2)

    # Tests for print_list method
    def test_print_list(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        self.ll.append(n1)
        self.ll.append(n2)
        self.ll.append(n3)
        
        captured_output = StringIO()
        sys.stdout = captured_output
        self.ll.print_list()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "1 -> 2 -> 3 -> None")

    # Tests for is_there_cycle method
    def test_is_there_cycle_no_cycle(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        self.ll.append(n1)
        self.ll.append(n2)
        self.ll.append(n3)
        self.assertFalse(self.ll.is_there_cycle())

    def test_is_there_cycle_with_cycle(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        self.ll.append(n1)
        self.ll.append(n2)
        self.ll.append(n3)
        n3.next = n1  # Create a cycle
        self.assertTrue(self.ll.is_there_cycle())

if __name__ == '__main__':
    unittest.main()