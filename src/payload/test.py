import argparse

parser = argparse.ArgumentParser(description="Payload experiment to perform a 3-point bending test on a self-healing material",
                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-b", "--runb", action="store_true", help="Select second experiment to run")
args = parser.parse_args()

print args.runb
