#!/bin/bash

set -o errexit  # exit on error
set -o nounset  # don't allow unset variables

export LOCALSTACK_HOST=localhost # When not defined, CI fails as awslocal try to communicate with the wrong IP

echo "########### Setting region as env variable ##########"

export AWS_REGION=eu-west-1

echo "########### Setting S3 env variables ###########"

export BUCKET_NAME=demo-bucket

echo "########### Creating bucket ##########"
awslocal s3 mb s3://$BUCKET_NAME

echo "########### READY TO GO ! ##########"