import unittest

from model.file_reader import FileReader
from model.geometry_graph import GeometryGraph
from model.geometry_node import GeometryNode
from model.geometry_parser.geometry_parser import GeometryParser, Point
from model.lexicon.lexicon import Lexicon
from model.lexicon.mask import Mask
from model.solutions_saver import SolutionsSaver
from model.solver import Solver


class ModelTest(unittest.TestCase):
    def setUp(self):
        self.__geometry_present = FileReader().read(
            "examples/exp1/geometry.txt")
        self.__words = FileReader().read("examples/exp1/words.txt")

    def test_geometry_parser(self):
        geometry = GeometryParser().parse(self.__geometry_present)
        expected_geometry = self.create_expected_geometry()

        while True:
            node = geometry.next_node()
            expected_node = expected_geometry.next_node()

            if node is None:
                break

            self.assertEqual(node.id, expected_node.id)
            self.assertEqual(node.capacity, expected_node.capacity)
            self.assertEqual(node.is_vertical_orientation,
                             expected_node.is_vertical_orientation)

            incident = node.incident_nodes
            expected_incident = node.incident_nodes

            self.assertEqual(len(list(incident)), len(list(expected_incident)))

            expected_ids = list(map(lambda el: el.id, expected_incident))
            for neighbour in incident:
                self.assertTrue(neighbour.id in expected_ids)

    def test_solver(self):
        geometry = GeometryParser().parse(self.__geometry_present)
        solution = Solver().solve(geometry, self.__words, reversed_mode=False)
        check_solution = {}

        for node, word in solution.items():
            check_solution[node.id] = word

        expected_geometry = self.create_expected_geometry()
        expected_solution = {expected_geometry.next_node().id: "hello",
                             expected_geometry.next_node().id: "hunter"}

        self.assertEqual(len(check_solution), len(expected_solution))
        self.assertDictEqual(check_solution, expected_solution)

    def test_lexicon(self):
        words = ["apple", "banana", "pineapple", "cherry", "orange"]
        solution_saver = SolutionsSaver()
        node = None
        test_filter = Lexicon(words, solution_saver, reversed_enabled=True)

        mask = Mask(6, {})
        answer = sorted(list(test_filter.get_word_by(mask, node)))
        self.assertListEqual(answer,
                             ["ananab", "banana", "cherry", "egnaro", "orange",
                              "yrrehc"])

        mask = Mask(6, {2: 'n'})
        answer = sorted(list(test_filter.get_word_by(mask, node)))
        self.assertListEqual(answer, ["banana", "egnaro"])

        mask = Mask(6, {5: 'e'})
        answer = sorted(list(test_filter.get_word_by(mask, node)))
        self.assertListEqual(answer, ["orange"])

    def create_expected_geometry(self):
        node1 = GeometryNode(False, Point(0, 0))
        node1.id = 0
        node1.capacity = 5

        node2 = GeometryNode(True, Point(0, 0))
        node2.id = 1
        node2.capacity = 6

        node1.add_incident(node2, 0)
        node2.add_incident(node1, 0)

        return GeometryGraph([node1, node2])
