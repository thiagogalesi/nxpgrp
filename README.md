# README #

This is a simple grep/ack like tool 

### Usage ###

usage: nxgr [-h] -e RE [--ne NRE] [--frgx FRGX] [--fx FX] [--fnrgx FNRGX]
            [file [file ...]]

positional arguments:
  file           Files to be searched

optional arguments:
  -h, --help     show this help message and exit
  -e RE (match this regex)
  --ne NRE (exclude this regex)
  --frgx FRGX (match file names containing this regex)
  --fx FX (matches files with this extension - turns FX into a regex \.FX$)
  --fnrgx FNRGX (exclude) file names containing this regexes)

