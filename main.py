import argparse
from argparse import RawTextHelpFormatter

import sys

from model.file_reader import FileReader
from model.geometry_parser.geometry_parser import GeometryParser
from model.presenter import Presenter
from model.solver import Solver


def console_mode_solve():
    file_reader = FileReader()
    geometry_present = file_reader.read(args.geometry)

    height = len(geometry_present)
    if height < 1:
        print("Incorrect geometry format. Try main.py -h or --help",
              file=sys.stderr)
        exit(1)

    width = len(geometry_present[0])

    geometry = GeometryParser().parse(geometry_present)
    words = file_reader.read(args.words)
    solution = Solver().solve(geometry, words, args.reversed)
    present = Presenter().get_present(width, height, solution,
                                      filled_grid=False)
    for line in present:
        print("".join(line))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        """Utility for crossword solve. 
        
        Load geometry from file with following format:        
        0 - cell of horizontal wordspace
        1 - cell of vertical wordspace
        2 - cell of intersection wordspace two type
        
        example: 
        ##1#1###1
        1#1#1###1
        202020002
        1#1#1###1
        1#1#1###1
        1#1#1###1
                
        Load words from file with following format:each next word take new line
        
        example:
        pineapple
        apple
        cherry
        orange
        banana""", formatter_class=RawTextHelpFormatter)

    parser.add_argument('geometry', type=str, nargs='?',
                        help="- geometry file name")

    parser.add_argument('words', nargs='?', type=str,
                        help="- words file name")

    parser.add_argument('--graphic',
                        action='store_true',
                        help="- flag can words be reversed")

    parser.add_argument('--reversed',
                        action='store_true',
                        help="- flag can words be reversed")

    args = parser.parse_args()

    if args.graphic:
        sys.argv.remove("--graphic")
        from application import CrosswordApp

        CrosswordApp(args.geometry, args.words,
                     reversed_mode=args.reversed).run()
    else:
        if args.geometry is None or args.words is None:
            print("For console mode need \"geometry\" and \"words\"" +
                  " parameters. Use --graphic for load files manually." +
                  " For more information try"
                  " main.py -h or --help", file=sys.stderr)
            exit(1)
        else:
            console_mode_solve()
