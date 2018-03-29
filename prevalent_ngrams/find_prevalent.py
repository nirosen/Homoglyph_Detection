#import sys
from collections import Counter


# constants
BREAKING_CHAR = '\\'
TOP_STRINGS = 10

def get_prevalent_strings(input_file):
    cnt = Counter()
    i=0
    # iterate over lines:
    for line in open(input_file, 'r'):
        # clean line whitespace character `\n` at the end of each line
        line = line.rstrip('\n')
        # split line by '\'
        for str in line.split(BREAKING_CHAR):
            cnt[str] += 1
        i += 1
    return cnt, i

def get_prevalent_ngrams(strings_counter, TOP_STRINGS):
    # get TOP_STRINGS=10
    top_strings_list = strings_counter.most_common(TOP_STRINGS)
    # find the length of the longest string
    list_str, list_cnt = zip(*top_strings_list)
    string_max_len = len(max(list_str, key=len))

    # find prevalent Ngrams (with N=string_max_len)


    a = 'hi'

if __name__ == '__main__':
    strings_counter, i = get_prevalent_strings("file_list3.txt")
    get_prevalent_ngrams(strings_counter, TOP_STRINGS)
    print('iterated: ' + str(i))