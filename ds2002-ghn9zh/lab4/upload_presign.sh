#!/usr/bin/bash

# Check if all three arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <file> <bucket> <expiration>"
    exit 1
fi

FILE=$1
BUCKET=$2
EXPIRATION=$3

# Upload the file to the S3 bucket
aws s3 cp "$FILE" "s3://$BUCKET/"

# Generate a presigned URL
PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET/$FILE" --expires-in "$EXPIRATION")

echo "File uploaded successfully!"
echo "Presigned URL (Expires in $EXPIRATION seconds): $PRESIGNED_URL"
