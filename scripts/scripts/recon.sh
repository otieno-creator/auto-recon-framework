#!/bin/bash
# Simple Automated Recon Engine

TARGET=$1
if [ -z "$TARGET" ]; then
    echo "Usage: ./recon.sh <target_ip_or_domain>"
    exit 1
fi

echo "[+] Starting reconnaissance on $TARGET..."
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUT_DIR="results/${TARGET}_${TIMESTAMP}"
mkdir -p "$OUT_DIR"

# Run Nmap with service discovery and default scripts
nmap -sV -sC -oX "$OUT_DIR/scan.xml" "$TARGET"

echo "[+] Scan complete. XML results saved to $OUT_DIR/scan.xml"
