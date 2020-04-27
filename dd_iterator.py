#!/usr/bin/env python3

import argparse
import os

def main():

    parser = argparse.ArgumentParser(
                description='Iterate a deep dream')
    
    required = parser.add_argument_group(
            'Required',
            'none')
    
    required.add_argument(
            "-s",
            "--source_img",
            type=str,
            help="image to dream on")
        
    required.add_argument(
            "-i",
            "--iterations",
            type=int,
            help="number of iterations to run (+1)")

    args = parser.parse_args()

    source = args.source_img

    for i in range(1,args.iterations):
	    os.system("python deep_dream.py " + source + " run" + str(i))
	    source = "run"+str(i)+".png"

if __name__ == "__main__":
    main()