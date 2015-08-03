#!/usr/bin/env fontforge

# Copyright (c) 2014, Sungsit Sawaiwan
#
# argv[1] = sfd file
# argv[2] = font family name
# argv[3] = desired font extentsion (otf, ttf, woff, svg)
#
# Usage: fontforge ./sfd2ttf.py <sdf file> <font family name> <font extention>

import sys,os
from datetime import datetime
import fontforge

fontfile = sys.argv[1]
font = fontforge.open(fontfile)

# Change copyright text here
font.copyright = 'Copyright (c) 2014-2015, Sungsit Sawaiwan (https://sungsit.com | gibbozer [at] gmail [dot] com).'
font.version = '0.3-alpha1'

fontdir = './fonts-unhinted/' + sys.argv[3] + '/'
feadir = './features/'
dirs = [fontdir, feadir]
for d in dirs:
  if not os.path.exists(d):
    os.makedirs(d)

# save full feature file
font.generateFeatureFile(feadir + sys.argv[2] + '.fea')


cnt = font.layer_cnt

i = 0
while (i < cnt):
  if i > 1: # Exclude first two layers (Back & Fore)
    layername = font.layers[i].name

    fullname = sys.argv[2] + ' ' + layername.replace('-',' ')

    psname = fullname.replace(' ','-')
    font.fontname = psname
    font.fullname = fullname
    filename = psname

    if layername.startswith('700'):
      font.weight = '700'
      font.os2_weight = 700
    else:
      font.weight = '400'
      font.os2_weight = 400

    if layername.endswith('Oblique'):
      subfamily = layername.strip('Oblique')
      font.italicangle = -12.0
      # import italic .fea
    else:
      subfamily = layername
      font.italicangle = 0.0

    font.familyname = sys.argv[2]

    newname = filename + '.' + sys.argv[3]

    # gen layer to font file
    font.generate(fontdir + newname, flags = ('round','opentype'), layer = layername)

  i += 1

font.save()
font.close()
