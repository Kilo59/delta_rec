# coding: utf-8
"""
append_deltas.py
~~~~~~~~~~~~~~~~
Compares 2 files and creates new merged file.
New file contains additions from 2nd file appended to original file's contents.
"""
import difflib


def get_text_ls(filename):
    """Returns text of file as a list of strings"""
    with open(filename, 'r') as f_in:
        return f_in.readlines()


def find_diffs(file1, file2):
    """Returns tuple of added and removed lines between 2 files."""
    diff_results = list(difflib.Differ().compare(
        get_text_ls(file1),
        get_text_ls(file2)))
    added = [ln.lstrip('+ ') for ln in diff_results if ln[0] is '+']
    removed = [ln.lstrip('- ') for ln in diff_results if ln[0] is '-']
    return added, removed


def merge_additions(file1, file2):
    """Compares 2 files and creates new file containing additions
    from `diffed` files. Returns deletions as a list."""
    adds, dels = find_diffs(file1, file2)
    text1 = get_text_ls(file1)
    text1.extend(adds)
    merged_filename = 'MERGED_{}'.format(file1)
    print(len(text1))
    with open(merged_filename, 'w') as f_out:
        f_out.writelines(text1)
    print('\t*ADDITIONS MERGED*\n->', merged_filename)
    print('\nAdds\t| Subs\n{}'.format('=' * 18))
    print('{}\t| {}'.format(len(adds), len(dels)))
    return dels


if __name__ == '__main__':
    print(__doc__)
    print('Enter filenames to compare:')
    file1 = input('\n\tFilename 1: ...')
    file2 = input('\n\tFilename 2: ...')
    print('\nCOMPARING: {} AND {}\n'.format(file1, file2))
