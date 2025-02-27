import boto3

# Set variables
bucket_name = "ds2002-ghn9zh"  # Replace with your bucket name
file_name = "puppy.jpg"  # Replace with your local file

# Create S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# Upload file to S3 (PRIVATE by default)
s3.upload_file(file_name, bucket_name, file_name)

print(f"Uploaded {file_name} to s3://{bucket_name}/{file_name}")

