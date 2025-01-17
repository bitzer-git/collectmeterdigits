import argparse
import sys
from collectmeterdigits.collect import collect
from collectmeterdigits.labeling import label


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--collect', help='collect all images. The edgeAI meter server name must be set')
    parser.add_argument('--days', type=int, default=3, help='count of days back to read. (default: 3)')
    parser.add_argument('--labeling', default='', help='labelpath if you want label the images')
    parser.add_argument('--keepdownloads', action='store_true', help='Normally all downloaded data will be deleted. If set it keeps the images.')
    parser.add_argument('--nodownload', action='store_true', help='Do not download pictures. Only remove duplicates and labeling.')
    parser.add_argument('--startlabel', type=int, default=0, help='only images >= startlabel. (default: all)')

    # print help message if no argument is given
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()
    
    if (args.labeling==''):
        collect(args.collect, args.days, keepolddata=args.keepdownloads, download=not args.nodownload, startlabel=args.startlabel)
    else:
        label(args.labeling, args.startlabel)    

if __name__ == '__main__':
    main()