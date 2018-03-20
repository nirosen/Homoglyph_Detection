#################################
########### imports #############
#################################
from data_file_parser import DataFileDir
from char_manager import CharacterManager
from output_char_codes import OutputCharCodes
from output_chars import OutputChars
from output_js import OutputJS
from output_js_tests import OutputJSTests
import os
import subprocess


#################################
########### globals #############
#################################
TEMPLATES_DIR = 'templates'
DATA_DIR      = 'source_data'
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
HOMOGLYPHS = []


#################################
####### helper functions ########
#################################

## currently prints to file + creates images
# setting range of homoglyphs to 2
# (since there are too many permutations: M^N)
def permute(a, l, r, cm, f):
    if l == r+1:
        #HOMOGLYPHS.append(''.join(a))
        f.write(''.join(a))
        f.write('\n')
        f.flush()
        str_to_png(a)
    else:
        set_of_homoglyps_for_char = cm.get_set_for_char(a[l])
        len_of_cur_set = len(set_of_homoglyps_for_char)
        # setting range to 2
        # (since there are too many permutations: M^N)
        for i in range(0, 2):
            temp = a[l]
            #a[l] = set_of_homoglyps[l][i]
            a[l] = list(set_of_homoglyps_for_char)[i]
            permute(a, l + 1, r, cm, f)
            a[l] = temp  # backtrack


def str_to_png(str):
    cmd = ['str_to_png.exe', ''.join(str), "Arial"]
    #  in order to create image with font file:
    # cmd = ['str_to_png.exe', ''.join(str), "C:\Temp\L_10646.TTF", "C:\Temp\L_10646.TTF from_python.png"]
    process_str_to_png = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = process_str_to_png.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        process_str_to_png.kill()
        outs, errs = process_str_to_png.communicate()



#################################
############# Main ##############
#################################


if __name__ == '__main__':
    ## initialization of the homoglyph generator classes
    cm = CharacterManager()
    dfd = DataFileDir(DATA_DIR)
    dfd.parse_all(cm)

    ## call to the recursive function
    ## to find Homoglyphs-Permutations of a string (e.g, 'abc' or 'C:\\Windows\\System32\\ntdll.dll')
    string = "calc"
    n = len(string)
    a = list(string)
    with open("test_homoglyph_permutations.txt", encoding='utf-8', mode='w') as f:
        permute(a, 0, n - 1, cm, f)







#################################
######## commented out ##########
#################################
    ## test purposes:
    # set_of_homoglyps = [['1', '2', 'A'],
    #                    ['3', '4', 'B'],
    #                    ['5', '6', 'C']]


        # env = os.environ
    # os.chdir(os.path.dirname(__file__))
    # env["PATH"] = os.getcwd() + ';' + env["PATH"]
    ##process_str_to_png = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)


        #char = 'a'
    #set = cm.get_set_for_char(char)
    ##set_without_orig = list(filter(lambda c: c != char, set))
    #str_to_png(set)
    #for c in CHARS:
    #    set = cm.get_set_for_char(c)
    #    #set_without_orig = list(filter(lambda c: c != char, set))
    #    str_to_png(set)

        #def write_to_file:
    #write the replaced_string to file
    #with open("test_homoglyph2.txt", encoding='utf-8', mode='w') as f:
    #lines = ["this is a test file, in order to write homoglyphs of the char a:\n"]
    #lines.append(''.join(set))
    #lines.append(''.join("\nSPACE\n"))
    #for c in set_for_a:
    #    lines.append(''.join(c))
    #f.write('\n'.join(lines))
    #set_without_orig = list(filter(lambda c: c != char, set))

    #OutputCharCodes('raw_data', TEMPLATES_DIR).create(cm)
    #OutputChars('raw_data', TEMPLATES_DIR).create(cm)
    #OutputJS('homoglyph.js', 'javascript/src', TEMPLATES_DIR).create(cm, CHARS)
    #OutputJS('index.js','node', TEMPLATES_DIR).create(cm, CHARS)
    #OutputJSTests('DataTests.js','javascript/tests/js/tests', TEMPLATES_DIR).create(cm, CHARS)