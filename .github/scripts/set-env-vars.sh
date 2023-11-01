#!/bin/bash

selected_env=$SELECTED_ENV

# Set value for environment name
if [[ -z "$selected_env" ]]; then
  if [[ -n "$TAG_NAME" ]]; then
    selected_env="prd"
  elif [[ "$BRANCH_NAME" == "develop" ]]; then
    selected_env="dev"
  else
    selected_env="tst"
  fi
fi

# Set value for export port
expose_port=""
if [[ "$selected_env" == "dev" ]]; then
  expose_port="8001:8080"
elif [[ "$selected_env" == "tst" ]]; then
  expose_port="8002:8080"
else
  expose_port="8003:8080"
fi

# Set value for build number
build_number=$(date -u +"%Y%m%d").$(date -u +"%H%M%S")
if [[ -n "$TAG_NAME" ]]; then
  build_number=$TAG_NAME
fi

# Set value for erpnext docker image
erpnext_img=$REGISTRY/$REPO_NAME.$selected_env

# Export environment vars
export SELECTED_ENV=$selected_env
export BUILD_NUMBER=$build_number
export PORTAINER_ENV_VARS="[{\"name\":\"DOCKER_IMAGE_URL\",\"value\":\"${erpnext_img}\"},{\"name\":\"EXPOSE_PORT\",\"value\":\"${expose_port}\"}]"
