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
    parser.add_argument('--nosort', action='store_true', default=False,
                        help='Do not sort output')
    args = parser.parse_args()

    if args.nosort:
        for p in step(args.directory):
            print(p)
    else:
        paths = list(step(args.directory))
        paths.sort()
        for p in paths:
            print(p)
