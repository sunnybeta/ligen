import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", type=str, help="Name of the author", required=True)
parser.add_argument("-y", "--year", type=str, help="License Year", required=True)
parser.add_argument("-e", "--email", type=str, help="Email of the author", default="")
parser.add_argument("-t", "--type", type=str, help="License Type", default='mit')
parser.add_argument("-f", "--file", type=str, help="Output to custom filename")

args = parser.parse_args()

