import argparse

geometry_file_name, words_file_name = "", ""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('geometry', type=str, nargs='?',
                        help="- geometry file name")

    parser.add_argument('words', nargs='?', type=str,
                        help='- words file name')

    args = parser.parse_args()

    from application import CrosswordApp
    CrosswordApp(args.geometry, args.words).run()
