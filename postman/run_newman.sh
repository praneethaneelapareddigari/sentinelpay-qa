#!/usr/bin/env bash
set -euo pipefail
mkdir -p reports
newman run postman/SentinelPay.postman_collection.json   -e postman/env/SentinelPay.postman_environment.json   --reporters cli,htmlextra   --reporter-htmlextra-export reports/newman.html   --env-var run_id=$(date +%s)
echo 'Newman run complete -> reports/newman.html'
