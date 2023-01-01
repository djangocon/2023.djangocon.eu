#!/bin/bash

function skeleton {
    im=$1; shift
    echo Image: $im
    b=$(basename "$(basename "$im" .jpg)" .png)
    destpath="../../../_organisers/${b}.md"

    if [ ! -e $destpath ]; then
        echo Output: $destpath
        cat > "$destpath" << EOF
---
layout: base
name: $b
role: DjangoCon Europe Organiser
photo_url: /static/img/organisers/$im
# twitter: yourtwitterhandle_no_@
# github: yourgithub
# website: https://yourwebsite.com/
---
EOF
    else
        echo "$destpath exists."
    fi
}

function main {
    for im in $(ls *.png *.jpg); do
        skeleton "$im"
    done
}

# skeleton "padraic.jpg"

main;