#!/bin/sh

key_filter=`python -c 'import random; print random.randint(1,7);'`
key_title=`python -c 'import random; print random.randint(1,7);'`
echo STARTING
convert image-$1.jpg -resize 500x500^ -crop 400x400+0+0 gen-$1.jpg
echo DONE


echo PAST IT

if [ $key_filter -eq 0 ]; then
    convert gen-$1.jpg  input_blur.jpg \
              -compose Blur -set option:compose:args 10 -composite \
              gen-$1.jpg
elif [ $key_filter -eq 1 ]; then
    convert -colorspace gray gen-$1.jpg gen-$1.jpg
elif [ "$key_filter" -eq 2 ]; then
    convert gen-$1.jpg -fill yellow -colorize 50% gen-$1.jpg
elif [ "$key_filter" -eq 3 ]; then
    convert gen-$1.jpg -modulate 190,60 gen-$1.jpg
elif [ "$key_filter" -eq 4 ]; then
    convert gen-$1.jpg \( +clone -blur 0x3 \) \
          -compose Lighten -composite  gen-$1.jpg
elif [ "$key_filter" -eq 5 ]; then
    convert gen-$1.jpg  -sigmoidal-contrast 4,0% gen-$1.jpg
else
    convert gen-$1.jpg -sigmoidal-contrast 15x70% gen-$1.jpg
fi


if [ "$key_title" -eq 0 ]; then
    convert gen-$1.jpg  -fill black  -undercolor white \
                    -gravity Center -font Courier -pointsize 30\
                    -annotate -0-100 " $2 " \
                    -gravity North -font Courier -pointsize 20\
                    -annotate +0+5 " $3 " gen-$1.jpg
elif [ "$key_title" -eq 1 ]; then
     convert gen-$1.jpg  -fill black  -undercolor white \
                    -gravity SouthWest -font Helvetica -pointsize 30\
                    -annotate +0+5 " $2 " \
                    -gravity SouthEast -font Century-Schoolbook-Bold -pointsize 15\
                    -annotate +0+10 " $3 " gen-$1.jpg
elif [ "$key_title" -eq 2 ]; then
     convert gen-$1.jpg  -fill black  -undercolor white \
                    -gravity Center -font Courier -pointsize 30\
                    -annotate 25x25-0+100 " $2 " \
                    -gravity Center -font Courier -pointsize 20\
                    -annotate 20x20+0+5 " $3 " gen-$1.jpg
elif [ "$key_title" -eq 3 ]; then
     convert gen-$1.jpg  -fill white  -undercolor black \
                    -gravity East -font Courier -pointsize 15\
                    -annotate 180+180+0+20 " $2                                " \
                    -gravity SouthWest -font Courier -pointsize 20\
                    -annotate +0+5 " $3                                        " gen-$1.jpg
elif [ "$key_title" -eq 4 ]; then
     convert gen-$1.jpg -gravity North \
          -fill white \
          -font Helvetica -pointsize 40\
          -annotate +0+30 "$2" \
          -fill Black \
          -annotate +1+31 "$2" \
          -gravity South \
          -fill white \
          -font Helvetica -pointsize 25\
          -annotate +0+20 "$3" \
          -fill black \
          -annotate +1+21 "$3" \
          gen-$1.jpg
elif [ "$key_title" -eq 5 ]; then
     convert gen-$1.jpg -gravity Center \
          -fill white \
          -font Helvetica -pointsize 40\
          -annotate +30+30 " $2 " \
          -fill black \
          -annotate +31+31 " $2 " \
          -gravity SouthWest \
          -font Gill-Sans-Bold-Italic -pointsize 20\
          -fill white \
          -annotate +30+0 "$3" \
          -fill black \
          -annotate +31+1 "$3" \
          gen-$1.jpg
else
    convert gen-$1.jpg -gravity NorthWest \
          -fill Black \
          -font Century-Schoolbook-Bold -pointsize 60\
          -annotate +35+35 "$2" \
          -fill White \
          -annotate +34+34 "$2" \
          -gravity SouthWest \
          -fill white \
          -font Century-Schoolbook-Bold -pointsize 25\
          -annotate +15+15 "$3" \
          -fill black \
          -annotate +16+16 "$3" \
          gen-$1.jpg
fi















