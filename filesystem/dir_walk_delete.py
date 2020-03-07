import argparse
import os


def step(path):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            step(d)

        for f in files:
            yield os.path.join(root, f)

        for d in dirs:
            yield os.path.join(root, d)


if __name__ == '__main__':
    description = r'Recursivly walk paths in a directory.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('directory', type=str,
                        help='Directory to process')
    parser.add_argument('file', type=str,
                        help='Name of file to delete')
    parser.add_argument('-n', '--dryrun', action='store_true', default=False,
                        help='Display result of command without executing')

    args = parser.parse_args()

    for p in step(args.directory):
        if args.file in p:
            print(p)

            if not args.dryrun:
                os.remove(p)
