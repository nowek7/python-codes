#!/bin/sh

#\usepackage[cp1250]{inputenc}
#\usepackage[utf8]{inputenc}

for f in `find . | grep -v .git | grep tex`; do
    echo $f
    iconv -f cp1250 -t utf-8 $f > tmp
    if [[ $? == 0 ]]; then
        lines=`cat tmp | grep cp1250 | wc -l`
        if [[ $lines == 1 ]]; then
            cat tmp | sed 's/cp1250/utf8/g' > tmp2
            cp tmp2 $f
            echo $f
        fi
        rm tmp
        rm tmp2
    fi
done
