#!/usr/bin/env python3
# Tool to remove the corresponding RAW files for deleted JPG files.

from send2trash import send2trash
import argparse
import os
import glob

def parse_arguments():
    parser = argparse.ArgumentParser(description=
      'Remove RAW image files with no corresponding JPG file in a directory')
    parser.add_argument('image_dir', type=dir_path)
    return parser.parse_args()

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

def main():
  parsed_args = parse_arguments()
  print("trashing RAW files in ", parsed_args.image_dir)
  raw_filenames = glob.glob(parsed_args.image_dir + "*.ARW")
  jpg_filenames = glob.glob(parsed_args.image_dir + "*.JPG")

  print("trashing RAWs:")
  for raw in raw_filenames:
    jpg_name = os.path.splitext(raw)[0] + ".JPG"
    if jpg_name not in jpg_filenames:
      print(raw)
      send2trash(raw)

if __name__ == "__main__":
  main()