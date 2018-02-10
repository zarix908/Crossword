from collections import defaultdict, namedtuple

from enums import WordType
from geometry_graph import GeometryGraph
from geometry_node import GeometryNode

Point = namedtuple("Position", ['x', 'y'])
IncidentNodeInfo = namedtuple("IncidentNodeInfo",
                              ['adj_letter_index', 'node'])


class GeometryParser:
    global current_id

    def parse(self, geometry_present):
        global current_id
        current_id = 0
        intersections = defaultdict(lambda: [])
        nodes = []

        args = [geometry_present, nodes, intersections]

        self.parse_nodes_by_type(*args, is_vertical=False)
        self.parse_nodes_by_type(*args, is_vertical=True)

        for incident_nodes_info in intersections.values():
            first_node_info = incident_nodes_info[0]
            second_node_info = incident_nodes_info[1]

            first_letter_index = first_node_info.adj_letter_index
            first_node = first_node_info.node

            second_letter_index = second_node_info.adj_letter_index
            second_node = second_node_info.node

            first_node.add_incident(second_node, first_letter_index)
            second_node.add_incident(first_node, second_letter_index)

        return GeometryGraph(nodes)

    def parse_nodes_by_type(self, geometry_present, nodes,
                            intersections, is_vertical):
        length = 0
        current_node = GeometryNode(is_vertical, Point(0, 0))
        width = len(geometry_present)
        height = len(geometry_present[0])

        first_iterable = range(width)
        second_iterable = range(height)

        if is_vertical:
            first_iterable = range(height)
            second_iterable = range(width)

        for x in first_iterable:
            for y in second_iterable:
                position = Point(x, y)

                if is_vertical:
                    position = Point(*reversed(position))

                symbol = geometry_present[position.x][position.y]

                if symbol == "2":
                    adj_letter_index = length
                    info = IncidentNodeInfo(adj_letter_index, current_node)
                    intersections[position].append(info)

                if symbol != "#":
                    length += 1
                    continue

                self.new_node(nodes, current_node, length)
                init_point = Point(x, y + 1) if is_vertical else Point(y + 1,
                                                                       x)
                current_node = GeometryNode(is_vertical, init_point)
                length = 0

            self.new_node(nodes, current_node, length)
            position = Point(0, x + 1)

            if is_vertical:
                position = Point(*reversed(position))

            current_node = GeometryNode(is_vertical, position)
            length = 0

    def new_node(self, nodes, current_node, length):
        global current_id

        if length > 1:
            current_node.id = current_id
            current_id += 1
            current_node.capacity = length
            nodes.append(current_node)
