#!/bin/bash

DOCKS_BUILD=./docs/build
DOCKS_DEST=./static/docs

# delete previous docs
rm -r $DOCKS_BUILD
rm -r $DOCKS_DEST

# sphinx-build -b <builder> -c <conf>       <docs_source>    <dest>
sphinx-build   -b html      -c ./docs/source  ./             $DOCKS_BUILD

# copy docs to web folder
cp -r $DOCKS_BUILD $DOCKS_DEST
