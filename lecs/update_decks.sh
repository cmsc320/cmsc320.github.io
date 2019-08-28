#!/usr/bin/env bash

set -o nounset
set -o errexit

# Copy all CMSC320 lectures (pptx and pdf) from private into public repo
privatedir=~/code/cmsc320-fall2019-private/lecs/
publicdir=~/code/cmsc320-fall2019-website/lecs/
cp -v ${privatedir}/cmsc320_f2019_lec*pptx ${publicdir}/
cp -v ${privatedir}/cmsc320_f2019_lec*pdf ${publicdir}/


