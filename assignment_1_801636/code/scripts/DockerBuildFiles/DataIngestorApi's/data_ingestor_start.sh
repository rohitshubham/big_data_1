#!/bin/sh
set -e

#to build the dockerfile, use the following command
# sudo docker build --tag mysimbdp-ingestor ../../../mysimbdp-ingestor/Data-ingestion-container/

# to run use the following command
sudo docker run --net=host  mysimbdp-ingestor

# Note: run in interactive mode for checking the output
 