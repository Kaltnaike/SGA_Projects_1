#python or python3 do not work for my OS environment only py or py -3
#!/usr/bin/env py
"""
Author: Tawakal't <purpleduralumin@gmail.com>
Purpose: Say hello
"""

import argparse

def get_args():
    """Get the  command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', 
                        '--name',
                        metavar='name',
                        default='World', 
                        help='Name to greet')
    return parser.parse_args()

def main():
    """main"""

    args = get_args()
    name = args.name
    print('Hello, ' + name + '!')

if __name__ == '__main__':
    main()
    



