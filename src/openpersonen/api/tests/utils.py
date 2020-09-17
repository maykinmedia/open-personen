import itertools


def get_bsn():

    for n in itertools.count():

        eight_first_digits = [int(x) for x in str(n + 10**7).zfill(8)]

        total = sum((9 - i) * digit
                    for i, digit
                    in enumerate(eight_first_digits))

        check_digit = total % 11
        if check_digit == 10:
            continue

        rsin = ''.join(str(x) for x in eight_first_digits + [check_digit])

        yield rsin


def get_a_nummer():

    for n in itertools.count():

        ten_digits = [int(x) for x in str(n + 10**7).zfill(10)]

        a_nummer = ''.join(str(x) for x in ten_digits)

        yield a_nummer
