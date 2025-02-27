import boto3

# Create S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# List all buckets
response = s3.list_buckets()

# Print bucket names
for bucket in response['Buckets']:
    print(bucket['Name'])
