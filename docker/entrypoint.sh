#!/bin/bash

set -e
pip install -r requirements.txt -c constraints.txt
pip install -e /util -c constraints.txt
pip install -e /fv3core -c constraints.txt
pip install -e /physics -c constraints.txt
pip install -e /stencils -c constraints.txt
pip install -e /dsl -c constraints.txt
pip install -e /driver -c constraints.txt
exec "$@"
