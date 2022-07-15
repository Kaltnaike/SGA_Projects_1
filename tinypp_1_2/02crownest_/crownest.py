#python or python3 do not work for my OS environment only py or py -3
#!/usr/bin/env py
"""
Author : Tawakal't <purpleduralumin@gmail.com>
Date   : 15-07-2022
Purpose: Give correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Give correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = "an" if word[0].lower() in "aeiou" else "a"

    print(f"Ahoy, Captain, {article} {word.upper()} off the larboard bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
