#!/bin/bash

python3 TTNAdapter/TTNAdapter.py

cd uploadSMCtoGeoNode
python3 uploadSMCtoGeoNode.py

cd ../irrigationMapCreation/irrigationMapFiles
Rscript ../irrigationMapCreation.r
