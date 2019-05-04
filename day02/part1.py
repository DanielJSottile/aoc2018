import argparse
import collections


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    two_sum = 0
    three_sum = 0
    with open(args.data_file) as f:
        for line in f:
            ctr = collections.Counter(line)
            if 2 in ctr.values():
                two_sum += 1
            if 3 in ctr.values():
                three_sum += 1
    print(two_sum * three_sum)


if __name__ == '__main__':
    exit(main())
