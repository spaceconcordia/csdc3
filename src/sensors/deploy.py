from time import sleep
from sensor_constants import *
from sensor_manager import SensorManager
import argparse

def main():
    parser = argparse.ArgumentParser(description="Deployment script", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--time", type=int, default=5, help="Time deployment switch is on")
    args = parser.parse_args()
    deploy_time = args.time
    SensorManager.gpio_output(DEPLOYMENT_SW_A_GPIO, ON)
    sleep(deploy_time)
    SensorManager.gpio_output(DEPLOYMENT_SW_A_GPIO, OFF)

if __name__ == "__main__":
    main()
