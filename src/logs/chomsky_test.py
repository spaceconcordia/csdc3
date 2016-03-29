import sys
sys.path.append("/root/csdc3/src/sensors/")
from sensor_constants import *
from chomsky import *
# selectPayloadData(0, 1459144191, TEMP_PAYLOAD_A)
print(selectPayloadData(0, 1459144191, TEMP_PAYLOAD_A))
