# Ref: https://pymotw.com/2/subprocess/
# https://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/
# http://sebastianraschka.com/Articles/2014_multiprocessing.html
# https://pymotw.com/2/multiprocessing/basics.html

"""Pytest module to test sorting techniques."""
import multiprocessing
import os, sys
import subprocess
import tempfile
import time

from unittest import TestCase

'''stdout_value, stderr_value = proc.communicate()
print 'output: ', repr(stdout_value)
print 'err: ', repr(stderr_value)'''

def Logger(proc, log_file):
    # stdout_messages = sys.stdout
    # stdout_messages.write(message)
    # log_file.write(message)
    # log_file.write( sys.stdout)
    for line in iter(proc.stdout.readline,''):
        print line.rstrip()

class TestProcessLogging(TestCase):
    """Test module to test sorting techniques."""

    @classmethod
    def setup_class(cls):
        """Setup Class."""
        print("\nsetup_class class:%s" % cls.__name__)
        temp_dir = tempfile.mkdtemp()
        temp_file_path = '%s/logger_%s.txt' % (
            temp_dir, time.strftime('%Y%m%d_%H%M%S'))
        cls.log_file = open(temp_file_path, "a")
        cls.proc = subprocess.Popen('while [ 1 ]; do echo "Hello world"; done;',
                                    shell=True,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        cls.log_proc = multiprocessing.Process(
            target=Logger, args=(cls.proc, cls.log_file,))
        cls.log_proc.start()

 
    @classmethod
    def teardown_class(cls):
        """Teardown Class."""
        print("teardown_class class:%s" % cls.__name__)
        print("Process id = %d" % cls.proc.pid)
        '''while cls.proc.stdout.readline():
            print cls.proc.stdout.readline()'''
        cls.proc.kill()
        cls.log_proc.terminate()
        print('Is Logger Terminated: %s %s', cls.log_proc,
            cls.log_proc.is_alive())
        cls.log_proc.join()
        print('Is Logger Joined: %s %s', cls.log_proc, cls.log_proc.is_alive())
        cls.log_file.close()



    def test_do_nothing(self):
        """Test Bubble Sort."""
        print("\n<======================")
        list_obj = [5, 3, 4, 1, 2]
        assert list_obj[0] == 5


'''
OUTPUT:
$ py.test -s test_sub_process_example.py
'''
