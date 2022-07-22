#!/usr/bin/env python
"""
Author : Awonaike Tawakalitu <purpleduralumin@gmail.com>
Date   : 2022-07-22
Purpose: Print items on picnic
"""
import argparse
from pydoc import pager
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print items on picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('items',
                        metavar='item',
                        type=str,
                        nargs='+',
                        help='Items we are bringing')
   
    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')
    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num = len(items)

    if args.sorted:
        items.sort()

    bringing  = ''
    if  num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)
        
    
    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
