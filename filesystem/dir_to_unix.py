import argparse
import os
import re


def rename(root, file_name, verbose, dryrun):
    new_name = file_name.replace(" ", "-").lower()
    new_name = re.sub(r'(-)\1+', r'\1', new_name)
    if new_name != file_name:
        if not dryrun:
            os.rename(root+'\\'+file_name, root+'\\'+new_name)

        if verbose or dryrun:
            print(file_name+' -> '+new_name)


def step(path, verbose, dryrun):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            step(d, verbose, dryrun)

        for f in files:
            rename(root, f, verbose, dryrun)

        for d in dirs:
            rename(root, d, verbose, dryrun)


if __name__ == '__main__':
    description = r'Recursivly "UNIX-ifies" paths in a directory.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('directory', type=str,
                        help='Directory to process')
    parser.add_argument('-n', '--dryrun', action='store_true', default=False,
                        help='Display result of command without executing')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='Enable verbose logging')

    args = parser.parse_args()

    step(args.directory, args.verbose, args.dryrun)
