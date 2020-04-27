#!/usr/bin/env python3

import argparse
from collections import defaultdict
import numpy as np
import pandas as pd
import glob
 
def main():
    
    parser = argparse.ArgumentParser(
            description='Parse 23andMe text files for SNP data')
    
    required = parser.add_argument_group(
            'Required',
            'none')
    
    required.add_argument(
        "-p",
        "--path",
        type=str,
        help="path to files")
    
    required.add_argument(
        "-o",
        "--output",
        type=str,
        help="location to write output file")

    args = parser.parse_args()
    print (args, type(args))

    all_files = glob.glob(args.path + "/*.txt")

    tmp = defaultdict(list)

    read_file(all_files, tmp)

    #print(tmp)
    data = pd.DataFrame.from_dict(tmp, orient='index')
    print(data)


###Functions####

def read_file(all_files, tmp):
    
    for file in all_files:

        with open(file) as fin:
            for line in fin:
                li=line.strip()
                if li.startswith('#'):
                    #print(li)
                    continue
                name, chrom, pos, snp = li.split("\t")
                tmp[chrom + ':' + pos].append(snp)
                #print(type(coord))
            
            return tmp


                    
    
    

if __name__ == "__main__":
    main()