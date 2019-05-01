import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    frequency = 0
    done = False
    seen = set()
    while not done:
        with open(args.data_file) as f:
            for line in f:
                frequency += int(line)
                if frequency in seen:
                    print(frequency)
                    done = True
                    break
                else:
                    seen.add(frequency)


if __name__ == '__main__':
    exit(main())
