"""This module demonstrates file operations."""


def get_f_obj_attrs(f_obj):
    '''Get File attributes.'''
    print("Name of the file : ", f_obj.name)
    print("File closed or not : ", f_obj.closed)
    print("Opening mode : ", f_obj.mode)
    print("Softspace flag : ", f_obj.softspace)

def f_mode_wb(f_obj):
    '''File operation wb mode.'''
    print()
    print("Enter some data")
    f_obj.write("Python is a great language.\nYeah its great!!!\n")

def f_mode_rplus(f_obj):
    '''File operation rplus mode.'''
    print()
    print("Read data")
    print f_obj.read(10)
    print()
    print("Current file position : ", f_obj.tell()
    print()
    print("Repositioning file pointer at the beginning of file.")
    f_obj.seek(0, 0)
    print()
    print("Again Read data")
    print f_obj.read(10)
    print()


DICT_FILE_MODES = {
    "wb" : f_mode_wb,
    "r+" : f_mode_rplus
}

def file_ops(op_type):
    '''File operations.'''
    f_obj = open("demo_file.txt", "%s" % op_type)
    print()
    print("***** File attributes *****")
    get_f_obj_attrs(f_obj)
    DICT_FILE_MODES[op_type](f_obj)
    print("***** Closing file *****")
    f_obj.close()



if __name__ == "__main__":
    print()
    print("Performing \"wb\" (write in Binary format) operation on file.")
    file_ops("wb")
    print()
    print("Performing \"r+\" read/write operation on file.")
    file_ops("r+")

