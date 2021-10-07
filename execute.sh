#!/bin/bash
source /home/cloud9-ubuntu/anaconda3/etc/profile.d/conda.sh
conda init bash
conda activate movingpandas
python /home/cloud9-ubuntu/Documents/backend/scripts/main_script.py
