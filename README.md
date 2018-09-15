[![Build Status](https://travis-ci.org/DD5HT/image_downloader.svg?branch=master)](https://travis-ci.org/DD5HT/image_downloader)
### How I would normally solve this problem:

This solution is super fast, handles errors and malformated entries without a problem and ignores duplicates.

```bash
#! /usr/bin/env bash
file="$1"
while read p; do
  wget -nv -N "$p"
done <$file
```

Usage: `$ ./download.sh samplefile.txt`

### Now the python3.6 program

Usage:   `$ ./image_downloader.py samplefile.txt`

Testing: `$ pytest `

### Comments

This type of program can easily be parallelized by splitting the input file into multiple smaller files
and iterating over each separately.
