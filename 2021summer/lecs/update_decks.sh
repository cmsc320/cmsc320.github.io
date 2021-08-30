#!/usr/bin/env bash

set -o nounset
set -o errexit

# Copy all CMSC320 lectures (pptx and pdf) from private into public repo
privatedir=~/code/cmsc320-fall2020-private/lecs/
publicdir=~/code/cmsc320-website/lecs/
cp -v ${privatedir}/cmsc320_f2020_lec*pptx ${publicdir}/
cp -v ${privatedir}/cmsc320_f2020_lec*pdf ${publicdir}/


