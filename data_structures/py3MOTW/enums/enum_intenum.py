"""Use of IntEnum class for enums where the members need to behave more like
numbers. For example, to support comparisons.
"""

import enum


class BugStatus(enum.IntEnum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


if __name__ == '__main__':
    print ('Ordered by value:')
    print ('\n'.join(' ' + s.name for s in sorted(BugStatus)))


'''
OUTPUT:
Ordered by value:
 fix_released
 fix_committed
 in_progress
 wont_fix
 invalid
 incomplete
 new
'''