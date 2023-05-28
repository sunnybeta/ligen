import sys
import argparse
from ligen import templates


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", type=str, help="Name of the author", default="")
    parser.add_argument("-y", "--year", type=str, help="License Year", default="")
    parser.add_argument("-e", "--email", type=str, help="Email of the author", default="")
    parser.add_argument("-t", "--type", type=str, help="License Type; Available Options ['apache_2','mit','unliecnse','ggpl2']", default='mit')
    parser.add_argument("-f", "--file", type=str, help="Output to custom filename")
    
    arguments = parser.parse_args()

    try:
        license_type = getattr(getattr(templates, arguments.type), arguments.type)
    except AttributeError:
        print(f"\n[ERROR] The template {arguments.type} you are looking for does not exist ;_; ... yet! :O\n")
        sys.exit(0)

    license_text = license_type.format(
        name=arguments.name,
        year=arguments.year,
        email=arguments.email,
    )
    
    if arguments.file:
        with open(arguments.file,'w') as f:
            f.write(license_text)
    else:
        print(license_text)


if __name__ == '__main__':
    main()
