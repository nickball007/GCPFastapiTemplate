# SalesService-backend

## Install
```
git clone {bitbucket repo}
poetry install
```
## Install new package
```
poetry add {package_name}
```

## Environment Variables

The following environment variables are required:


You can set these variables in a `.env` file in the root directory of the project.

## poetry - generate requirements.txt without hashes
```
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

## local test
To run the FastAPI application:
```
poetry run start
```

## Set GCP account
Login your GCP account

### Deploy
```
gcloud run deploy {your cloud run name} --port 8080 --source .
```

Allow unauthenticated invocations to [mis-nick-test] (y/N)?  y