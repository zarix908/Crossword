from queue import Queue


class GeometryGraph:
    def __init__(self, nodes):
        self.__nodes = nodes
        self.__current_node = None
        self.__visited_nodes = []
        self.__current_node_index = -1
        self.__queue = Queue()
        self.__queue.put(self.__nodes[0])

    def next_node(self):
        self.__current_node_index += 1

        if self.__current_node_index <= -1:
            return self.__visited_nodes[self.__current_node_index]

        if self.__current_node_index > -1:
            self.__current_node_index = -1

        if len(self.__queue.queue) > 0:
            self.__current_node = self.__queue.get()
            self.__visited_nodes.append(self.__current_node)

            for node in self.__current_node.incident_nodes:
                if node not in self.__visited_nodes:
                    self.__queue.put(node)

            return self.__current_node

    def previous_node(self):
        self.__current_node_index -= 1
        return self.__visited_nodes[self.__current_node_index] if abs(
            self.__current_node_index) <= len(self.__visited_nodes) else None
