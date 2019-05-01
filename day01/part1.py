import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    frequency = 0
    with open(args.data_file) as f:
        for line in f:
            frequency += int(line)
    print(frequency)


if __name__ == '__main__':
    exit(main())
