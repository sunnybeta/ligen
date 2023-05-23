import argparse
from ligen import templates


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", type=str, help="Name of the author", required=True)
    parser.add_argument("-y", "--year", type=str, help="License Year", required=True)
    parser.add_argument("-e", "--email", type=str, help="Email of the author", default="")
    parser.add_argument("-t", "--type", type=str, help="License Type", default='mit')
    parser.add_argument("-f", "--file", type=str, help="Output to custom filename")
    args = parser.parse_args()

    args.email = f"<{args.email}>" if args.email else ""
    license_text = templates.mit.format(name=args.name, year=args.year, email=args.email)
    if args.file:
        with open(args.file,'w') as f:
            f.write(license_text)
    else:
        print(license_text)
