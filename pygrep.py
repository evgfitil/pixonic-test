from argparse import ArgumentParser

MAN_DICT = {
    '-n': 'prints out each line number in the file with the specified patterns',
    '-f': 'prints out files names with the specified patterns',
    '-i': 'ignore case',
    '-v': 'selected lines are those not matching any of the specified patterns'
}


def get_parser():
    """Initializes a parser and available args"""

    parser = ArgumentParser()
    parser.add_argument('pattern', type=str)
    parser.add_argument('file_name', nargs='*')
    parser.add_argument('-n', '--numbers', action='store_true',
                        help=MAN_DICT.get('-n'))
    parser.add_argument('-f', '--files', action='store_true',
                        help=MAN_DICT.get('-f'))
    parser.add_argument('-i', '--ignore_case', action='store_true',
                        help=MAN_DICT.get('-i'))
    parser.add_argument('-v', '--invert_match', action='store_true',
                        help=MAN_DICT.get('-v'))

    return parser


def get_files_names(file):
    """Returns files names"""

    for line in file:
        if args.pattern in line and args.invert_match:
            return print(file.name)
        if args.pattern in line and not args.invert_match:
            return print(file.name)
    return


def get_matches(file):
    """Returns matches"""

    pattern = args.pattern
    for line_num, line in enumerate(file):
        if args.ignore_case:
            if args.invert_match:
                if pattern.lower() not in line.lower():
                    if multiple_files:
                        print(f'{file.name}:', end='')
                    print(f'{line_num + 1} {"" if args.numbers else line.rstrip()}')
            if not args.invert_match:
                if pattern.lower() in line.lower():
                    if multiple_files:
                        print(f'{file.name}:', end='')
                    print(f'{line_num + 1} {"" if args.numbers else line.rstrip()}')
        else:
            if args.invert_match:
                if pattern not in line:
                    if multiple_files:
                        print(f'{file.name}:', end='')
                    print(f'{line_num + 1} {"" if args.numbers else line.rstrip()}')
            if not args.invert_match:
                if pattern in line:
                    if multiple_files:
                        print(f'{file.name}:', end='')
                    print(f'{line_num + 1} {"" if args.numbers else line.rstrip()}')


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    multiple_files = True if len(args.file_name) > 1 else False

    if args.pattern:
        for file in args.file_name:
            with open(file) as origin_file:
                if args.files:
                    get_files_names(origin_file)
                else:
                    get_matches(origin_file)
