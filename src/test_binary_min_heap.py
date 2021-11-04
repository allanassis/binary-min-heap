from unittest import TestCase
import unittest

from binary_min_heap import BinaryMinHeap


class TestBinaryMinHeap(TestCase):
    def setUp(self):
        self.root_value = 10

    def test_instance(self):
        # arrange/act
        tree = BinaryMinHeap()
        # assert
        self.assertIsInstance(tree, BinaryMinHeap)
    
    def test_insert_root(self):
        # arrange
        tree = BinaryMinHeap()
        # act
        tree.insert(self.root_value)
        # assert
        self.assertEqual(tree._list[0], self.root_value)

    def test_insert_many_root(self):
        # arrange
        tree = BinaryMinHeap()
        expected = [1, 2, 3, 7, 4, 11, 5, 14, 10, 12, 6]
        # act
        tree.insert(self.root_value)
        tree.insert(4)
        tree.insert(5)
        tree.insert(1)
        tree.insert(2)
        tree.insert(11)
        tree.insert(3)
        tree.insert(14)
        tree.insert(7)
        tree.insert(12)
        tree.insert(6)
        # assert
        self.assertListEqual(expected , tree._list)

    def test_pop_root(self):
        # arrange
        tree = BinaryMinHeap()
        tree.insert(self.root_value)
        # act
        node = tree.pop()
        # assert
        self.assertEqual(node, self.root_value)
        self.assertListEqual([], tree._list)

    def test_pop(self):
        # arrange
        tree = BinaryMinHeap()
        tree.insert(self.root_value)
        tree.insert(4)
        tree.insert(5)
        tree.insert(1)
        tree.insert(2)
        tree.insert(11)
        tree.insert(3)
        tree.insert(14)
        tree.insert(7)
        tree.insert(12)
        tree.insert(6)
        expected = [2, 4, 3, 7, 6, 11, 5, 14, 10, 12]
        # act
        node = tree.pop()
        # assert
        self.assertEqual(node, 1)
        self.assertListEqual(expected, tree._list)
    

if __name__ == "__main__":
    unittest.main()