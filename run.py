import numpy as np
import random
import sys


REPETITION = 10
DEPTH_START = 10
DEPTH_END = 15


class BinaryTree:
    def __init__(self, depth):
        self.n = 2 ** depth - 1
        self.nodes = [0] * self.n
        self.unmarked_indices = list(range(self.n))

    @staticmethod
    def get_sibling_index(index):
        if index % 2 == 0:
            return index - 1
        else:
            return index + 1

    @staticmethod
    def get_parent_index(index):
        return int((index - 1) / 2)

    @staticmethod
    def get_children_indices(index):
        return 2 * index, 2 * index + 1

    def mark_node(self, index):
        self.nodes[index] = 1
        self.unmarked_indices.remove(index)
        if index > 0:  # not first row i.e. root
            parent_index = BinaryTree.get_parent_index(index)
            sibling_index = BinaryTree.get_sibling_index(index)
            if self.nodes[parent_index] and not self.nodes[sibling_index]:
                self.mark_node(sibling_index)
            elif not self.nodes[parent_index] and self.nodes[sibling_index]:
                self.mark_node(parent_index)
        if index < (self.n - 1) / 2:  # not last row
            left_child_index, right_child_index = BinaryTree.get_children_indices(index)
            if self.nodes[left_child_index] and not self.nodes[right_child_index]:
                self.mark_node(right_child_index)
            elif not self.nodes[left_child_index] and self.nodes[right_child_index]:
                self.mark_node(left_child_index)

    def all_marked(self):
        for node in self.nodes:
            if not node:
                return False
        return True


def process_1(depth):
    binary_tree = BinaryTree(depth)
    count = 0
    while not binary_tree.all_marked():
        count += 1
        random_index = random.randint(0, binary_tree.n - 1)
        binary_tree.mark_node(random_index)
    return count


def process_2(depth):
    binary_tree = BinaryTree(depth)
    random_permutation = np.random.permutation(binary_tree.n)
    count = 0
    while not binary_tree.all_marked():
        random_index = random_permutation[count]
        count += 1
        binary_tree.mark_node(random_index)
    return count


def process_3(depth):
    binary_tree = BinaryTree(depth)
    count = 0
    while not binary_tree.all_marked():
        count += 1
        random_index = random.choice(binary_tree.unmarked_indices)
        binary_tree.mark_node(random_index)
    return count


def run(process_function):
    for i in range(DEPTH_START, DEPTH_END + 1):
        print('### depth %d' % i)
        for j in range(REPETITION):
            count = process_function(i)
            print(count)


if __name__ == '__main__':
    process = int(sys.argv[1])
    if process == 1:
        run(process_1)
    elif process == 2:
        run(process_2)
    elif process == 3:
        run(process_3)
