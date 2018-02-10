from file_reader import FileReader
from geometry_parser.geometry_parser import GeometryParser
from presenter import Presenter
from solver import Solver

geometry_present = FileReader.read("examples/exp3/geometry.txt")
geometry_graph = GeometryParser().parse(geometry_present)

words = FileReader.read("examples/exp3/words.txt")

solution = Solver().solve(geometry_graph, words)

for node, word in solution.items():
    print(node, word, sep="")

print("""
###################
###############################################
##############################################
###########################
""")

height = len(geometry_present)
width = len(geometry_present[0])

present = Presenter().get_present(width, height, solution)

for i in present:
    print(i)
