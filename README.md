# S3 LocalStack Test

A simple Python script to test Amazon S3 operations using LocalStack for local development.

## Prerequisites

- Docker and Docker Compose
- Python 3.9+
- Poetry (for dependency management)

### Installing Poetry

If you don't have Poetry installed, you can install it using:

```bash
# On macOS/Linux
curl -sSL https://install.python-poetry.org | python3 -
```

Or using pip:
```bash
pip install poetry
```

## Setup Instructions

1. **Clone or download the project files**

2. **Start LocalStack:**

 ```bash
 docker compose -f src/docker/docker-compose.yml up -d
 ```

3. **Install dependencies using Poetry:**
   
```bash
  poetry install
```

4. **Run the Python script:**
   ```bash
   poetry run python src/localstack_demo/__init__.py
   ```

5. **Stop LocalStack when done:**
   ```bash
   docker compose -f src/docker/docker-compose.yml down
   ```

## What the script does


1. **Creates an S3 client** configured to work with LocalStack (running on localhost:4566)
3. **Generates dummy content** with timestamp and sample data
4. **Uploads the file** to S3 as 'dummy-file.txt'
5. **Lists all objects** in the bucket
6. **Downloads and prints** the file content to the console

The bucket creation is actually performed by LocalStack, so the script assumes the bucket already exists.
The localstack bucket creation is performed using localstack hooks: https://docs.localstack.cloud/aws/capabilities/config/initialization-hooks/

## Project Structure

```
.
├── src
   ├── docker
      ├───docker-compose.yml      # LocalStack docker compose file
      ├───init-aws.sh             # Localstack initialization script
   ├── localstack_demo
      ├── __init__.py             # Main Python package
├── pyproject.toml        # Poetry configuration and dependencies
└── README.md             # This file
```

## Troubleshooting

1. **Connection refused error**: Make sure LocalStack is running (`docker-compose up -d`)
2. **Port conflicts**: Ensure port 4566 is not being used by other services
3. **Docker issues**: Check that Docker is running and you have sufficient permissions