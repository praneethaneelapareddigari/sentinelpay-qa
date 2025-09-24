#!/usr/bin/env bash
# Usage: bash security/zap_baseline.sh https://target.example
set -euo pipefail
TARGET=${1:-https://httpbin.org}
mkdir -p reports .zap
echo "[ZAP] Running baseline scan against $TARGET"
docker run --rm -u root -v "$(pwd)":/zap/wrk -t owasp/zap2docker-stable     zap-baseline.py -t "$TARGET" -r reports/zap.html -x reports/zap.xml || true
echo "[ZAP] Done -> reports/zap.html"
