#!/bin/bash

set -e

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "You need to activate your virtual env before running this script"
    exit 1
fi

echo "Generating Converter Swagger schema"
../src/manage.py generate_swagger \
    ../src/openpersonen/converters/swagger2.0.json \
    --overwrite \
    --format=json \
    --mock-request \
    --url https://example.com/api/v1 \
    --info openpersonen.converters.schema.info \
    --urlconf openpersonen.converters.urls

echo "Converting Swagger to OpenAPI 3.0..."
npm run generate-converters-openapi
