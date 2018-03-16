from collections import namedtuple

Point = namedtuple("Position", ['x', 'y'])
IncidentNodeInfo = namedtuple("IncidentNodeInfo",
                              ['adj_letter_index', 'node'])