from __future__ import print_function
import pandas as pd
import argparse
import re

def parse_annotation(file_handle):

    df = pd.DataFrame(columns=['filename', 'ellipse'])
    line = file_handle.readline()
    while line:
        filename = re.search(r'(.*\/.*)', line)
        if filename:
            # print('filename is: ', filename.group(1))
            pass
        else:
            line = file_handle.readline()
            continue

        data_dict ={'filename':  filename.group(1)}
        num_faces = int(file_handle.readline())
        ellipses = []
        # print('Number of faces is: ', num_faces)
        for ellipse_idx in range(0, num_faces):
            ellipse_val = file_handle.readline()
            # print ('ellipse idx', ellipse_idx, ' = ', ellipse_val)
            ellipses.append(ellipse_val)
        data_dict['ellipse'] = ellipses
        tmp = pd.DataFrame(data_dict)
        # print('tmp = ', tmp)
        df = pd.concat([df, tmp])
        line = file_handle.readline()

    return df


def main():
    parser = argparse.ArgumentParser(description='Populate a data frame for face data.')
    parser.add_argument('path_to_file', nargs=1, type=str)
    args = parser.parse_args()
    file_name = args.path_to_file[0];
    print('Creating a data from ', file_name)
    with open(file_name) as f:
        parse_annotation(f)


if __name__ == '__main__':
    main()

