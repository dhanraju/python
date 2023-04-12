"""Accelerometer Test Script."""
import time
import unittest
from zip_test_fwk import ZipTestBoard

# Actuator move configs.
_SLOW_CLIMB = "slow_climb"
_SHARP_TURN = "sharp_turn"
_QUICK_DROP = "quick_drop"

# Register defintions
_ADXL345_ADDRESS = "0x_1D"
_BW_RATE = "0x2C"
_POWER_CTL = "0x2D"
_DATA_FORMAT = "0x31"
_DATA_X0 = "0x32"
_FIFO_CTL = "0x38"


class FailException(Exception):
    """Exception message for a failed test."""
    def __init__(self, fail_message):
        self.message = fail_message

    def __str__(self):
        return str(self.message)


class TestDut(unittest.TestCase):
    """Unit tests for DUT."""
    def setUp(self):
        # Assumption: The DUT is powered on and initialized.
        self.zip_test_board = ZipTestBoard()
        self.test_start_time = time.time()

    def tearDown(self):
        total_test_run_time = time.time() - self.test_start_time
        print(f'TEST PASSED in %.6f sec' % total_test_run_time)

    def _get_xyz_measured_values(self):
        """Captures and returns the avg of 10 samples of x, y and z axis.

        Puts board in measuring mode, captures the 10 samples of x, y and z
        axis values, averages them and retuns them.

        Returns: Tuple of 3 float values.
        """
        # Put the board in measuring mode.
        self.zip_test_board.i2c_cmd(_POWER_CTL, 8)
        # Set the stream mode to FIFO_CTRL
        self.zip_test_board.i2c_cmd(_FIFO_CTL, int("0x80", 16))
        # Allow sometime to settle.
        time.sleep(0.1)  # 100 msec
        # Capture at least 10 samples of x-, y- and z-axis values.
        x_out = y_out = z_out = []
        for _ in range(10):
            x_0, x_1, y_0, y_1, z_0, z_1 = self.zip_test_board.i2c_cmd(
                _DATA_X0, 6, 6)
            x_out.append((int(x_0) | int(x_1) << 8))
            y_out.append((int(y_0) | int(y_1) << 8))
            z_out.append((int(z_0) | int(z_1) << 8))
        return (sum(x_out)/len(x_out), sum(y_out)/len(y_out),
                sum(z_out)/len(z_out))

    def test_configure_acce(self):
        """Configures the accelerometer at the maximum data rate.

        Configures the accelerometer to output valid x,y,z measurements at the
        maximum data rate possible given communications and sensor constraints.

        Assumption: The orientation of board is x=0, y=0 and z=1.
        """
        # Put the board from standby mode to measuring mode.
        # To do this, set the D3 bit of POWER_CTL register 0x2D to high
        # (0x00001000 -> 8).
        self.zip_test_board.i2c_cmd(_POWER_CTL, 8)
        (x_out, y_out, z_out) = self._get_xyz_measured_values()
        try:
            self.assertEqual(x_out, 0,
                'X axis value is not Equal to 0')
            self.assertEqual(y_out, 0,
                'Y axis value is not Equal to 0')
            self.assertEqual(z_out, 1,
                'Z axis value is not Equal to 1')
        except AssertionError as err:
            fail_message = f'TEST FAILED in %.6f sec due to %s' % (
                (time.time() - self.test_start_time), str(err))
            raise FailException(fail_message)

    def test_accel_self_test(self):
        """Run accelerometer self test and check results within range.
        
        According to data sheet, the self-test change is defined as the
        difference between the acceleration output of an axis with self-test
        enabled and the acceleration output of the same axis with self-test
        disabled.

        Assumption: The sensor does not move between these two measurements.
        """
        # Capture acceleration output of x-, y- and z-axis before self-test
        # enabled.
        # Step1: Configure data rate to 100Hz and Put part in normal power
        # operation
        self.zip_test_board.i2c_cmd(_BW_RATE, int("0x0A", 16)|(1<<4))
        # Step2: Put part in full resolution, 16g mode
        self.zip_test_board.i2c_cmd(_DATA_FORMAT, int("0x03", 16))
        # Step3: Get the values of x_st_off, y_st_off and z_st_off.
        (x_st_off, y_st_off, z_st_off) = self._get_xyz_measured_values()
        # Enable self-test and capture x-, y- and z-axis values.
        # Step1: Set bit D7 of DATA_FORMAT register.
        self.zip_test_board.i2c_cmd(_DATA_FORMAT, int("0x03", 16)|(1<<7))
        # Step3: Get the values of x_st_on, y_st_on and z_st_on.
        (x_st_on, y_st_on, z_st_on) = self._get_xyz_measured_values()
        # Calculate the difference between st_on and st_off values.
        x_st = x_st_on - x_st_off
        y_st = y_st_on - y_st_off
        z_st = z_st_on - z_st_off
        # Disable self-test by clearing bit D7 of DATA_FORMAT register.
        self.zip_test_board.i2c_cmd(_DATA_FORMAT, int("0x03", 16)^(1<<7))
        # Expected min and max values of x_st, y_st and z_st are [6, 67],
        # [-67, -6] and [10, 110]
        try:
            self.assertGreater(x_st, 6, 'X axis is not greater than 6')
            self.assertLess(x_st, 67, 'X axis is not less than 67')
            self.assertGreater(y_st, -67, 'Y axis is not greater than -67')
            self.assertLess(y_st, -6, 'Y axis is not less than -6')
            self.assertGreater(z_st, 10, 'Z axis is not greater than 10')
            self.assertLess(z_st, 110, 'Z axis is not less than 110')
        except AssertionError as err:
            fail_message = f'TEST FAILED in %.6f sec due to %s' % (
                (time.time() - self.test_start_time), str(err))
            raise FailException(fail_message)

    def test_slow_climb(self):
        """Test coverage for slow climb config.

        Move actuator through “slow_climb” config and check throughout the
        motion that the yaxis is between -1g and 1g, and that the z axis is
        between 6g and 8g.
        """
        # Move actuator through slow_climb config.
        self.zip_test_board.actuator_move(_SLOW_CLIMB)
        (unused_x_out, y_out, z_out) = self._get_xyz_measured_values()
        try:
            # Check y axis is between -1g and 1g.
            self.assertGreater(y_out, -1, 'Y axis is not greater than -1g')
            self.assertLess(y_out, 1, 'Y axis is not less than 1g')
            # Check z axis is between 6g and 8g.
            self.assertGreater(z_out, 6, 'Z axis is not greater than 6g')
            self.assertLess(z_out, 8, 'Z axis is not less than 8g')
        except AssertionError as err:
            fail_message = f'TEST FAILED in %.6f sec due to %s' % (
                (time.time() - self.test_start_time), str(err))
            raise FailException(fail_message)
        # Bring the board back to standby mode by clearing the D3 bit of
        # POWER_CTL register 0x2D.

    def test_sharp_turn(self):
        """Test coverage for sharp_turn config.

        Move actuator through sharp_turn config and check throughout the
        motion that the x axis and y axis are both greater than 5g.
        """
        # Move actuator through sharp_turn config.
        self.zip_test_board.actuator_move(_SHARP_TURN)
        (x_out, y_out, unused_z_out) = self._get_xyz_measured_values()
        try:
            self.assertGreater(x_out, 5.0,
                'X axis value is not greater than 5g')
            self.assertGreater(y_out, 5.0,
                'Y axis value is not greater than 5g')
        except AssertionError as err:
            fail_message = f'TEST FAILED in %.6f sec due to %s' % (
                (time.time() - self.test_start_time), str(err))
            raise FailException(fail_message)

    def test_quick_drop(self):
        """Test coverage for quick_drop config.

        Move actuator through “quick_drop” config and check throughout the
        motion that the z axis is less than -8g.
        """
        # Move actuator through quick_drop config.
        self.zip_test_board.actuator_move(_QUICK_DROP)
        (unused_x_out, unused_y_out, z_out) = self._get_xyz_measured_values()
        try:
            self.assertLess(z_out, -8.0, 'Z axis is not less than -8g')
        except AssertionError as err:
            fail_message = f'TEST FAILED in %.6f sec due to %s' % (
                (time.time() - self.test_start_time), str(err))
            raise FailException(fail_message)


if __name__ == '__main__':
    unittest.main()
