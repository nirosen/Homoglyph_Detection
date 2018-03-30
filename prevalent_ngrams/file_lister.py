import os

# root_folder_path = 'C:\\'
root_folder_path = 'C:\\Windows\\'

# The result file can't be in a subfoldr of the root folder, but it may be in the root folder itself.
result_file = 'file_list3.txt'
forbiden_substrings = {'$'}
max_dirs_to_scan = 10000

def save_filenames(folder_path, filenames, result_file, forbiden_substrings='', write_method='a', line_break='\n'):
    with open(result_file, write_method) as file_:
        for filename in filenames:
            file_path = ''.join((folder_path, os.sep, filename, line_break))
            file_path = file_path.replace(':\\\\',':\\')  # A hardcoded fix to a bug in os.walk, it doesn't add \ after C:
            # yielding path like C:subflder\file.txt.
            file_.write(file_path)
    return

def check_validity(input_str, forbiden_substrings):
    return not any((substr in input_str for substr in forbiden_substrings))

def handle_folder(folder_item, result_file, forbiden_substrings='', write_method='a', line_break='\n'):
    folder_path = folder_item[0]
    # subfolders = folder_item[1] #  unused, placed here for clarity
    filenames = folder_item[2]
    if check_validity(folder_path, forbiden_substrings):
        filenames = [filename for filename in filenames if check_validity(filename, forbiden_substrings)]
        save_filenames(folder_path, filenames, result_file, forbiden_substrings, write_method)
    return

if __name__ == '__main__':
    folder_walker = os.walk(root_folder_path, followlinks=True)
    #initialization loop, getting the files from C: so I can write a file there without it affecting the results
    for folder_item in folder_walker:
        handle_folder(folder_item, result_file, forbiden_substrings, write_method='w')
        break
    
    if max_dirs_to_scan > 0:
        for folder_num, folder_item in enumerate(folder_walker):
            if folder_num >= max_dirs_to_scan:
                break
            else:
                handle_folder(folder_item, result_file, forbiden_substrings)
    else:
        for folder_item in folder_walker:
            handle_folder(folder_item, result_file, forbiden_substrings)
        