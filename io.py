def __open_close_explicitly():

    # How to open a file
    f = open("family.txt")

    '''
        How to read a file
    '''

    # Reads all files all of the file into a list
    s = f.readlines()
    print(s)

    # read file one line at a time
    f.readline()

    # takes cursor to the first line of the file
    f.seek(0)

    # reads the whole file
    f.read()

    # Close the file
    f.close()


'''
    This is a private method.

    If the name of a Python function, class method, or attribute starts with (but doesn't end with) two underscores, it's private; everything else is public.
    https://linux.die.net/diveintopython/html/object_oriented_framework/private_functions.html
'''


def __open_file(file_name, custom_mode='r'):
    '''
        Using WITH, you do not have to explicitly close the file.

        Modes:
        'r': read only
        'r+': read and write
    '''

    import time

    # Reads the file
    if custom_mode == 'r':

        print(f"Reading file {file_name}\n")

        with open(file_name, mode='r') as f:
            print(f"{f.read()}")

    # Writes to the file. It creates a new file
    if custom_mode == 'w':

        print(f"Writing file {file_name}\n")

        with open(file_name, mode='w') as f:
            text = f.write(f"Write (w) at {time.time()}\n")

    # Writes to the file starting from position 0
    if custom_mode == 'r+':

        print(f"Reading/Writing file {file_name}\n")

        with open("family.txt", mode='r+') as f:
            text = f.write(f"Read/Write (r+) at {time.time()}\n")

        # Prints number of number of characters written to the file
        print(text)

    # append to the end of the file
    if custom_mode == "a":

        print(f"Appending file {file_name}\n")

        with open(file_name, mode='a') as f:
            f.write(f"Appending at {time.time()}\n")

    return True


'''
    This function is used to validate if the folder/file exist
    The IO file operations are handled in open_file() once it has confirmed
    the file exists

    This is a wrapper function around open_file()
'''

def open_close_implicitly(file_name, custom_mode='r'):

    try:

        modes = ['r', 'r+', 'a']

        if custom_mode in modes:
            # Checks if [folder]/file exists
            with open(file_name, mode='r') as _:
                pass

    except FileNotFoundError:
        print(f"Filename--> {file_name} does not exist. Select a new filename")
        return False

    except IOError:
        pass

    return __open_file(file_name, custom_mode)


'''
    https://docs.python.org/3/library/pathlib.html
'''
file_name = "files/family.txt"
file_name = "family.txt1"
if open_close_implicitly(file_name, "a"):
    open_close_implicitly(file_name, "r")

