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
    match_num = False

    with open(args.data_file) as f:
        lines = tuple(f)
        for i in range(len(lines)):
            match = lines[i]
            for a in lines:
                if match_minus_one(a, match) and match_num is False:
                    match_num = True
                    list_a = list(a)
                    list_match = list(match)
                    for i, char in enumerate(list_a):
                        if char != list_match[i]:
                            list_a.pop(i)
                            list_match.pop(i)
                    final_ans = ''.join(list_a)
                    print(final_ans, end='')


if __name__ == '__main__':
    exit(main())