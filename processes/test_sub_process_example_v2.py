# Ref: https://pymotw.com/2/subprocess/
# Ref:https://stackoverflow.com/questions/22366040/how-do-you-share-a-variable-between-two-processes-in-python
# https://pymotw.com/3/queue/
"""Pytest module to test sorting techniques."""
import multiprocessing
import os, sys
import subprocess
import tempfile
import time

from unittest import TestCase


class TestProcessLogging(TestCase):
    """Test module to test sorting techniques."""
    flag_set = False
    que_obj = multiprocessing.Queue()

    @classmethod
    def Logger(cls, que, proc, log_file):
        # time.sleep(3)
        for line in iter(proc.stdout.readline,''):
            print line.rstrip()
            set_flag_true = True
            que.put(set_flag_true)

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
            target=cls.Logger, args=(cls.que_obj, cls.proc, cls.log_file,))
        cls.log_proc.start()
        # Verify the flag is set by thread.
        while not cls.que_obj.empty():
            print("flag not yet set!")
            cls.flag_set = cls.que_obj.get()
        print("FLAG IS SET!!!")
 
    @classmethod
    def teardown_class(cls):
        """Teardown Class."""
        print("teardown_class class:%s" % cls.__name__)
        print("Process id = %d" % cls.proc.pid)
        cls.proc.kill()
        cls.log_proc.terminate()
        print('Is Logger Terminated: %s %s', cls.log_proc,
            cls.log_proc.is_alive())
        cls.log_proc.join()
        print('Is Logger Joined: %s %s', cls.log_proc, cls.log_proc.is_alive())
        cls.log_file.close()
        print("In teardown_class, flag_set = ", cls.que_obj.get())

    def test_do_nothing(self):
        """Test Bubble Sort."""
        print("\n<======================")
        list_obj = [5, 3, 4, 1, 2]
        assert list_obj[0] == 5


'''
OUTPUT:
$ py.test -s test_sub_process_example_v2.py
'''
