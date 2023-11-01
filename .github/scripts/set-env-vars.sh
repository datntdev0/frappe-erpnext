#!/bin/bash

# Initialize an empty string for the environment tag
environment_tag=""

# Check the branch name and set the environment tag accordingly
if [[ "$BRANCH_NAME" == "develop" ]]; then
  # If the branch is develop, set the environment tag to dev
  environment_tag="dev"
else
  # For all other branches, set the environment tag to tst
  environment_tag="tst"
fi

# Get the current date in YYYYMMDD format
current_date=$(date -u +"%Y%m%d")

# Get the current time in HHMMSS format
current_time=$(date -u +"%H%M%S")

# Construct the version using package name, environment tag, current date and time
package_name=$REPO_NAME.$environment_tag
version_number=$current_date.$current_time

if [[ -n "$TAG_NAME" ]]; then
  package_name=$REPO_NAME
  version_number=$TAG_NAME
fi

# Check the environment then set the exposing port
expose_port=""

if [[ "$environment_tag" == "dev" ]]; then
  # If the env is dev, set the port to 8001
  expose_port="8001:8080"
elif [[ "$environment_tag" == "tst" ]]; then
  # If the env is tst, set the port to 8002
  expose_port="8002:8080"
else
  # For all other env, set the port to 8000
  expose_port="8000:8080"
fi

# Print the versio
export BASE_IMAGE=ghcr.io/datntdev0/frappe-base.$environment_tag:latest
export PACKAGE_NAME=$package_name
export VERSION_NUMBER=$version_number
export STACK_NAME=erpnext$environment_tag
export EPRNEXT_IMAGE=$REGISTRY/$PACKAGE_NAME:$VERSION_NUMBER
export STACK_ENV_VARS="[{\"name\":\"DOCKER_IMAGE_URL\",\"value\":\"${EPRNEXT_IMAGE}\"},{\"name\":\"EXPOSE_PORT\",\"value\":\"${expose_port}\"}]"