"""
You need to transfer vehicle logs through a slow datalink as fast as possible. You consider using a file archiver to compress data before sending. Output the minimal time you'll need to send the vehicle log data through the datalink, including compression and extraction time, rounded up to the nearest integer. Only round up the final answer, not intermediary calculation results.

Input

Line 1: (integer) dataSize: the size of the data to transfer, in bytes, 1 <= dataSize <= 10,000

Line 2: (integer) transferSpeed: the speed of data transfer through the link, in bytes per second, 1 <= transferSpeed <= 10

Line 3: (integer) N: the number of archivers to consider, either 1 or 2

Line 4 (if N == 1): Archiver 1

Line 5 (if N == 2): Archiver 2

Archivers 1 and 2 are described with two space-separated integers:

processingSpeed: the speed of data processing (both compressions and extraction), in bytes per second, 1 <= processingSpeed <= 99

and

compressionRate: the rate of compression achieved by the archiver (i.e. the size of compressed data divided by the size of original data), in percent, 1 <= compressionRate <= 99

You may expect all input to conform to these rules.

Example

input

1000
10
2
100 50
60 20

output

40

Sending the data uncompressed will take 1000/10 = 100 seconds.
Using first archiver will take 1000/100 + 1000*0.5/10 + 1000*0.5/100 = 65 seconds.
Using second archiver will take 1000/60 + 1000*0.2/10 + 1000*0.2/60 = 39 1/3 seconds, rounding up to 40
"""


import sys

line = sys.stdin.readline()  # Do not remove this line, mandatory for test run
# print(line)  # printed output is used to review test results
minimal_time = 0
dataSize = int(line)
transferSpeed = int(sys.stdin.readline())
N = int(sys.stdin.readline())

# print('dataSize = ', dataSize)
# print('transferSpeed = ', transferSpeed)
# print('N = ', N)

archiver1 = sys.stdin.readline()
processingSpeed1 = int(archiver1.split()[0])
compressionRate1 = int(archiver1.split()[1])
archiver2 = sys.stdin.readline()
processingSpeed2 = int(archiver2.split()[0])
compressionRate2 = int(archiver2.split()[1])

# print('firstpart = ', (dataSize/processingSpeed1))
# print('secondpart = ', (dataSize * ((compressionRate1/100)/transferSpeed)))
# print('thirdpart = ', (dataSize * ((compressionRate1/100)/processingSpeed1)))

if N == 1:
  minimal_time = (
    (dataSize/processingSpeed1) +
    (dataSize * ((compressionRate1/100)/transferSpeed)) +
    (dataSize * ((compressionRate1/100)/processingSpeed1))
  )

# print('firstpart = ', (dataSize/processingSpeed2))
# print('secondpart = ', (dataSize * ((compressionRate2/100)/transferSpeed)))
# print('thirdpart = ', (dataSize * ((compressionRate2/100)/processingSpeed2)))

if N == 2:
  minimal_time = (
    (dataSize/processingSpeed2) +
    (dataSize * ((compressionRate2/100)/transferSpeed)) +
    (dataSize * ((compressionRate2/100)/processingSpeed2))
  )

# print('minimal_time = ', int(minimal_time))
print(int(minimal_time))