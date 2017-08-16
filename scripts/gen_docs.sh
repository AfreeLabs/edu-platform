#!/bin/bash

DOCKS_DEST=./static/docs

# delete previous docs
rm -r $DOCKS_DEST

# sphinx-build -b <builder> -c <conf>       <docs_source>    <dest>
sphinx-build   -b html      -c ./docs/source  ./             $DOCKS_DEST

