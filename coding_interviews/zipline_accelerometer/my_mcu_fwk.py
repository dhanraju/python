"""Board that interfaces with Accelerometer and DUT."""

class MyMCUBoard(object):
    def __init__(self):
        """Finds and connects to a board. Raises exception if fails."""
        # Find the DUT board
        # Connect to the board and raise ConnectionError exception if it fails
        print('**** in __init__ ****')

    def turn_on_ps(self, supply):
        """Turns on power supply for provided string arg.
        
        Args:
          supply: (string) valid values are 1V8, 2V5, 3V3, 5V

        Returns:
          status: (bool) True for success; otherwise False
        """
        print('*** The supply value is ', supply)
    
    def turn_off_ps(self, supply):
        """Turns off power supply for provided string arg.
        
        Args:
          supply: (string) valid values are 1V8, 2V5, 3V3, 5V

        Returns:
          status: (bool) True for success; otherwise False
        """
        print('*** The supply value is ', supply)
    
    def i2c_setup(self, sda, scl, freq):
        """Sets up a I2C bus with sda and scl pins and integer frequency.
        
        Args:
          sda: (string) Serial data
          scl: (string) Serial communications clock
          freq: (int) Serial clock frequency
        """
        print('*** The sda value = ', sda)
        print('*** The scl value = ', scl)
        print('*** The frequency value = ', freq)

    def i2c_cmd(self, addr, data, resp_len=0):
        """Writes data to the provided addr.
        
        And waits for response from the device of byte length resp_len. Returns
        list of read bytes of length specified. Raise I2CError exception if it
        fails.

        Args:
          addr: (string) Address of the device
          data: (list) Data to write to the provided address.
          resp_len: (int) Response from device of byte length.
        Returns:
          read_bytes_len: (list of ints) List of read bytes of length specified.
        Raises:
          I2CError: Exception if the commands fails.
        """
        print('*** The addr value = ', addr)
        print('*** The data value = ', data)
        print('*** The resp_len value = ', resp_len)
        if addr == "0x34":
            return [0, 0, 0, 7]
        if addr == "0x32":
            return [0, 5, 0, 5]
        if addr == "0x36":
            return [0, -9]

    def actuator_move(self, config):
        """Moves actuator according to config.

        This function is blockin during motion. So it returns only after it is
        completed (~10 sec).

        Args:
          config: (string) config options are slow_climb, sharp_turn and
                  quick_drop
        Raises:
          AcutatorError: Exception if config operation fails.
        """
        print('*** The config operation = ', config)


if __name__ == '__main__':
    mcu_board = MyMCUBoard()
    mcu_board.turn_on_ps("1V8")