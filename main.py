import argparse

geometry_file_name, words_file_name = "", ""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        """Utility for crossword solve. Load geometry from file with following format:
        
        0 - symbol of horizontal wordspace
        1 - symbol of vertical wordspace
        2 - symbol of intersection wordspace two type
        
        example: 
        ##1#1###1
        1#1#1###1
        202020002
        1#1#1###1
        1#1#1###1
        1#1#1###1
        
        Load words from file with following format: each next word take new line
        
        example:
        pineapple
        apple
        cherry
        orange
        banana""")

    parser.add_argument('geometry', type=str, nargs='?',
                        help="- geometry file name")

    parser.add_argument('words', nargs='?', type=str,
                        help="- words file name")

    parser.add_argument('--reversed',
                        action='store_true',
                        help="- flag can words be reversed")

    args = parser.parse_args()

    from application import CrosswordApp

    CrosswordApp(args.geometry, args.words, reversed_mode=args.reversed).run()
