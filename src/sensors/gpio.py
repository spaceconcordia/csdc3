import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/logs/config_setup')
from ablib_python3 import Pin
from sensor_constants import *
from sensor_manager import SensorManager
import argparse

def main():
    parser = argparse.ArgumentParser(description="Script to toggle switches", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-d", "--deploy", action="store_true", help="Switch to deploy antenna")
    parser.add_argument("-r", "--radio", action="store_true", help="Turn on radio")
    parser.add_argument("-p", "--payload", action="store_true", help="Turn on payload")
    parser.add_argument("-s", "--sensors", action="store_false", help="Turn off sensors")

    args = parser.parse_args()
    deploy = args.deploy
    radio = args.radio
    payload = args.payload
    sensors = args.sensors

    SensorManager.gpio_output(DEPLOYMENT_SW_B_GPIO, OFF)
    SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, OFF)
    SensorManager.gpio_output(PAYLOAD_HTR_B_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_1_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_2_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_3_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_4_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_1_GPIO, OFF)

    SensorManager.gpio_output(RADIO_EN_GPIO, radio)
    SensorManager.gpio_output(SENSORS_EN_GPIO, sensors)
    SensorManager.gpio_output(PAYLOAD_EN_GPIO, payload)
    SensorManager.gpio_output(DEPLOYMENT_SW_A_GPIO, deploy)
    """
    time.sleep(2)
    SensorManager.gpio_output(SENSORS_EN_GPIO, ON)
    SensorManager.gpio_output(RADIO_EN_GPIO, OFF)
    """
if __name__ == "__main__":
    main()
