#import sys
from collections import Counter
from nltk.util import ngrams


# constants
BREAKING_CHAR = '\\'
TOP_STRINGS = 100
INPUT_PATHES_FILE = "file_list_win.txt"
OUTPUT_NGRAMS_FILE = "output_ngrams.txt"


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

def ngrams_py(input, n):
    input = input.split(' ')
    output = {}
    for i in list(range(len(input)-n+1)):
        g = ' '.join(input[i:i+n])
        output.setdefault(g, 0)
        output[g] += 1
    return output


def get_prevalent_ngrams(strings_counter, TOP_STRINGS):
    # get TOP_STRINGS=10
    top_strings_list = strings_counter.most_common(TOP_STRINGS)
    # find the length of the longest string
    list_str, list_cnt = zip(*top_strings_list)
    string_max_len = len(max(list_str, key=len))
    # find prevalent Ngrams (with N=string_max_len)
    total_ngrams_counter = Counter()
    for str in list_str:
        for i in range(1, min(len(str), string_max_len)):
            # ngrams_counter = ngrams(str, i)
            ngrams_counter = ngrams(str, i)
            total_ngrams_counter = total_ngrams_counter + Counter(ngrams_counter)
    return total_ngrams_counter

if __name__ == '__main__':
    strings_counter, i = get_prevalent_strings(INPUT_PATHES_FILE)
    total_ngrams_counter = get_prevalent_ngrams(strings_counter, TOP_STRINGS)

    print('number of pathes rows: ' + str(i))
    print('number of ngrams counter values: ' + str(sum(total_ngrams_counter.values())))
    print('number of ngrams counter different values: ' + str(len(total_ngrams_counter)))
    print('## TOP 100 most common ngrams:')
    print(total_ngrams_counter.most_common(100))

    with open(OUTPUT_NGRAMS_FILE, 'w') as output_file:
        for k,v in total_ngrams_counter.most_common(100):
            output_file.write("{}\t{}\t{}\n".format(k, BREAKING_CHAR, v))
