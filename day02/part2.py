import argparse


def match_minus_one(a: str, match: str) -> bool:
    skip = 0
    for j, k in zip(a, match):
        if j == k and skip <= 1:
            continue
        elif j != k and skip < 1:
            skip += 1
        else:
            return False
    return skip == 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        lines = tuple(f)
        for i, match in enumerate(lines):
            for a in lines[i + 1:]:
                if match_minus_one(a, match):
                    for c, d in zip(a, match):
                        if c == d:
                            print(c, end='')
                    print('')
                    return 0


if __name__ == '__main__':
    exit(main())
