#!/usr/bin/env python3

import csv
import sys
import epitran

def main(fn):
    epi = epitran.Epitran('ori-Orya')
    with open(fn, encoding='utf-8') as f:
        reader = csv.reader(f, dialect='excel-tab')
        for lemma, input, props, gloss in reader:
            props = props.replace(' ', '+')
            gold_analysis = lemma + props
            phonemic_input = epi.transliterate(input)
            print('\t'.join([input, phonemic_input, lemma, gold_analysis, gloss]))

if __name__ == '__main__':
    main(sys.argv[1])
