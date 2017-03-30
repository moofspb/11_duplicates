import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Find duplicate files in a folder')
    parser.add_argument('filepath', help='The folder path to scan')
    args = parser.parse_args()
    return args


def collect_files(path):
    all_files = {}  # duplicate_files in format {(file, file_size): [file_paths]}
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
    #for file in collected_files:
     #   if len(file)
    #return {k: v for k, v in collected_files if len(v) > 1}
    return {print(k, p) for k, p in collected_files}


def print_duplicate_files(duplicates):
    print("")


if __name__ == '__main__':
    path = parse_args()
    abc = collect_files(path)
    #b = collect_files('/home/moof/test')
    print(find_duplicates(abc))
