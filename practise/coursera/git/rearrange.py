import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\x .]*)$", name)
    if result == None:
        return result
    return "{} {}".format(result[2], result[1])


Notes:

Redirecting diff of two files to a file, which is called patch_file.
$ diff -u old_file new_file > patch_file

Apply the diff file using patch command to the old file to reflect the new changes.
$ patch old_file.py < patch_file

