from __future__ import print_function
import pandas as pd
import argparse
import re
import os

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

def get_ellipse_files(file_list):
    ellipse_files = []
    for some_file in file_list:
        match = re.search('ellipseList\\.txt', some_file)
        if match:
            ellipse_files.append(some_file)

    return ellipse_files


def main():
    parser = argparse.ArgumentParser(description='Populate a data frame from all the data in the FDDB ellipses directory.' +
                                     ' The file can then be read in using pands in the following way: \n\n' +
                                     ' import pandas as pd \nfddb=pd.read_hdf(\'path/to/your/dir/fddb_ellipse.h5\', \'table\')')
    parser.add_argument('path_to_ellipses', nargs=1, type=str, help='This is the path to the ground truth ellipse files.')
    parser.add_argument('path_to_output_hdf', nargs=1, type=str, help='This is the hdf5 containing the ellipses.')
    args = parser.parse_args()
    files_path = args.path_to_ellipses[0]

    print('Reading files from ', files_path)
    ellipse_files = get_ellipse_files(os.listdir(files_path))

    if not ellipse_files:
        raise Exception('There are no ellipse files in provided directory')

    print('Found the following ellipse files: ', ellipse_files)
    df = pd.DataFrame(columns=['filename', 'ellipse'])
    for ellipse_file in ellipse_files:
        print('Processing ', ellipse_file, '...')
        with open(files_path +'/'+ ellipse_file) as f:
            df = pd.concat([df,parse_annotation(f)])


    df.to_hdf(args.path_to_output_hdf[0] + '/fddb_ellipse.h5', 'table', mode='w')



if __name__ == '__main__':
    main()

