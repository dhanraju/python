#I have an array of data which is coming in periodically at 10ms; I want to check if the data coming through is the correct length and that it is valid. The first element always has an identifier, then based of the identifier we have to look up the length of data that is expected. For example ID 1 has a length of 4 elements (including the identifier element). If the data is not of correct length I want that error written to the screen with the ID and the expected and actual length received. if the data is correct just continue.

def validate_data(data, id_len):
    for i in range(len(id_len.keys())):
        print(id_len.items())
        if data[0] is id_len.get([i], None):  # and len(data) is id_len.keys()[i]:
            print('Pass')
        else:
            print('Fail')



if __name__ == '__main__':
    #Dictionary with mesage ID length
    ID_length = {
        1: 4,
        2: 7,
        3: 8
    }
    
    # create two/threys which would make your function pass or fail
    # create two/three lists which would make your function pass or fail
    data1 = [1,1,1,2]
    data2 = [1,1,2,5,4,6,8]
    data3 = [2,1,2,3,5,8,4]
    data4 = [2,9,4]
    data5 = [3,2,1,5,7,7,9,8]
    data6 = [9,7,7]
    
    validate_data(data1, ID_length)
