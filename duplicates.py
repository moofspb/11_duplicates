import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Find duplicate files in a folder')
    parser.add_argument('filepath', help='The folder path to scan')
    args = parser.parse_args()
    return args


def collect_files(path):
    all_files = {}  # in format {(file, file_size): [file_paths]}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if (file, file_size) in all_files:
                all_files[(file, file_size)].append(file_path)
            else:
                all_files[(file, file_size)] = [file_path]
    return all_files


def find_duplicates(collected_files):
    return list(filter(lambda x: len(x) > 1, collected_files.values()))


def print_duplicate_files(duplicates):
    if duplicates:
        print('Dublicates files:')
        for paths in duplicates:
            print('--------------------------')
            for path in paths:
                print(path)
    else:
        print('No duplicates files found!')


if __name__ == '__main__':
    args = parse_args()
    parsed_files = collect_files(args.filepath)
    duplicate_files = find_duplicates(parsed_files)
    print_duplicate_files(duplicate_files)
