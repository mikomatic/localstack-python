import boto3
from botocore.exceptions import ClientError
from datetime import datetime


def create_s3_client():
    """Create S3 client configured for LocalStack

    While this example configured a custom endpoint for LocalStack, this could be connected to AWS directly using a service account.
    The point is that this function can abstract the S3 client creation logic, allowing for easy switching between LocalStack and AWS.
    """
    return boto3.client(
        "s3",
        endpoint_url="http://localhost:4566",  # LocalStack endpoint - could possible by defined as a variable to point to a REAL AWS endpoint
        aws_access_key_id="test",  # Dummy credentials for LocalStack
        aws_secret_access_key="test",
        region_name="eu-west-1",
    )


def create_and_upload_file(s3_client, bucket_name, file_key, content):
    """Create a dummy file content and upload it to S3"""
    try:
        # Upload the content directly to S3
        s3_client.put_object(
            Bucket=bucket_name, Key=file_key, Body=content, ContentType="text/plain"
        )
        print(f"✓ File '{file_key}' uploaded successfully to bucket '{bucket_name}'")
    except ClientError as e:
        print(f"✗ Error uploading file: {e}")
        raise


def read_and_print_file(s3_client, bucket_name, file_key):
    """Read file from S3 and print its content"""
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        content = response["Body"].read().decode("utf-8")

        print(f"\n📄 Content of '{file_key}' from S3:")
        print("=" * 50)
        print(content)
        print("=" * 50)

        return content
    except ClientError as e:
        print(f"✗ Error reading file: {e}")
        raise


def list_bucket_objects(s3_client, bucket_name):
    """List all objects in the bucket"""
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        if "Contents" in response:
            print(f"\n📁 Files in bucket '{bucket_name}':")
            for obj in response["Contents"]:
                print(
                    f"  - {obj['Key']} (Size: {obj['Size']} bytes, Modified: {obj['LastModified']})"
                )
        else:
            print(f"📁 Bucket '{bucket_name}' is empty")

    except ClientError as e:
        print(f"✗ Error listing bucket objects: {e}")


def main():
    # Configuration
    file_key = "dummy-file.txt"
    # Bucket expected to exist
    bucket_name = "demo-bucket"

    # Create dummy file content
    dummy_content = f"""Hello from LocalStack S3!

This is a dummy text file created for testing purposes.

Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Bucket: {bucket_name}
File: {file_key}

Some sample data:
- Line 1: This is the first line of dummy data
- Line 2: Here's some more text content
- Line 3: LocalStack makes AWS development easier!

End of dummy file.
"""

    print("🚀 Starting S3 LocalStack Test")
    print("=" * 50)

    try:
        # Create S3 client
        s3_client = create_s3_client()
        print("✓ S3 client created successfully")

        # Upload file
        create_and_upload_file(s3_client, bucket_name, file_key, dummy_content)

        # List bucket contents
        list_bucket_objects(s3_client, bucket_name)

        # Read and print file content
        read_and_print_file(s3_client, bucket_name, file_key)

        print("\n✅ All operations completed successfully!")

    except Exception as e:
        print(f"\n❌ Script failed with error: {e}")


if __name__ == "__main__":
    main()
