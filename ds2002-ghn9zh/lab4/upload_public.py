import boto3

# Set variables
bucket_name = "ds2002-ghn9zh"
file_name = "puppy.jpg"

# Create S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# Upload file without ACLs
s3.upload_file(file_name, bucket_name, file_name)

print(f"Uploaded {file_name} to s3://{bucket_name}/{file_name}")
print(f"Public URL (if bucket policy allows it): https://s3.amazonaws.com/{bucket_name}/{file_name}")
