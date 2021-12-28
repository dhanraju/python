'''Serial port programming.'''
import serial


if __name__ == '__main__':
    # configure the serial connections (the parameters differs on the device you are connecting to)
    SER = serial.Serial(
        port='/dev/ttyUSB1',
        baudrate=115200,
        parity='N',
        stopbits=1,
        bytesize=8,
        timeout=3
    )

    # SER.open()
    SER.isOpen()

    print("Enter your commands below.\r\nInsert "exit" to leave the application.")

    while 1:
        # get keyboard input
        # input = raw_input(">> ")
        INPUT = raw_input()
        # Python 3 users
        # INPUT = INPUT(">> ")
        print(INPUT)
        if INPUT == 'exit':
            SER.close()
            exit()
        else:
            # send the character to the device
            # (note that I happend a \r\n carriage return and line feed
            # to the characters - this is requested by my device)
            # SER.write(INPUT + '\r\n')
            print("return of SER.write = ", SER.write(INPUT + '\r\n'))
            OUT = ''
            # let's wait one second before reading output (let's give device time to answer)
            # time.sleep(1)
            print(SER.readline())
            # print(SER.read(1))
            while SER.inWaiting() > 0:
                print("Inside while\n")
                # OUT += SER.read(1)
                OUT += SER.readline()
                if OUT != '':
                    print("CMD OUTPUT = " + OUT)
                    print(">>" + OUT)
                else:
                    print("something went wrong")
