from pprint import pprint


def filter_file_lines(filename, substring):
    result = []
    with open(filename) as f:
        for line in f:
            if substring in line:
                result.append(line)
    return result


if __name__ == "__main__":
    pprint(filter_file_lines("config_r1.txt", "ip address"))

"""
Example:

[' ip address 10.1.1.1 255.255.255.255\n',
 ' ip address 10.0.13.1 255.255.255.0\n',
 ' no ip address\n',
 ' ip address 10.0.19.1 255.255.255.0\n',
 ' no ip address\n',
 ' no ip address\n']

"""