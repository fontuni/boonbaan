#! /usr/bin/env sh

fontforge ./sfd2ttf.py boonhome-master.sfd BoonHome ttf

unhinted=./fonts-unhinted/ttf

for ttf in $unhinted/*.ttf
  do ttfautohint -D latn -f latn -w gGD -l 8 -r 60 -G 240 -x 12 -s -v $ttf ./ttf/$(basename $ttf)
done

for ttf in ./ttf/*.ttf 
  do fontforge -script any2woff.pe $ttf &&
     mv ./ttf/$(basename $ttf .ttf).woff ./woff/. &&
     woff2_compress $ttf &&
     mv ./ttf/$(basename $ttf .ttf).woff2 ./woff2/.
done
