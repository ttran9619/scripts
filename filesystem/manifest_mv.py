import argparse
import os
import shutil


description = r'Moves files from one directory to another, based on a manifest'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('manifest', type=str,
                    help='Manifest: relative paths, on separate lines')
parser.add_argument('source', type=str,
                    help='Source Directory')
parser.add_argument('destination', type=str,
                    help='Destination Directory')
parser.add_argument('-n', '--dryrun', action='store_true', default=False,
                    help='Display result of command without executing')
parser.add_argument('-v', '--verbose', action='store_true', default=False,
                    help='Enable verbose logging')

args = parser.parse_args()

src_dir = args.source
dest_dir = args.destination
manifest = args.manifest
dryrun = args.dryrun
verbose = args.verbose

with open(manifest, 'r', encoding='utf-8') as file_handle:
    for line in file_handle:
        trimmed = line.rstrip()

        src_path = os.path.join(src_dir, trimmed)
        dest_path = os.path.join(dest_dir, trimmed)

        # Notify if a file in the manifest is missing
        if not os.path.isdir(src_path) and not os.path.isfile(src_path):
            print('Error '+str(src_path)+' not found.')

        # Move file found in manifest if it exists
        if os.path.isfile(src_path):
            if verbose or dryrun:
                print(src_path+' -> '+dest_path)

            if not dryrun:
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.move(src_path, dest_path)

# Cleanup
for path in os.listdir(src_dir):
    relative_path = os.path.join(src_dir, path)
    if os.path.isdir(relative_path) and not os.listdir(relative_path):
        if verbose or dryrun:
            print(relative_path+' empty, removing')

        if not dryrun:
            os.rmdir(relative_path)
