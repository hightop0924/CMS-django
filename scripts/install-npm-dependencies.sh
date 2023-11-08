#!/bin/bash

set -e

SHRINKWRAP_FILE=npm-shrinkwrap.json
SHRINKWRAP_CACHED_FILE=node_modules/npm-shrinkwrap.cached.json

if diff -q $SHRINKWRAP_FILE $SHRINKWRAP_CACHED_FILE; then
  echo 'No shrinkwrap changes detected. npm install will be skipped...';
else
