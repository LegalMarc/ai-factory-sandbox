#!/usr/bin/env bash
# The repo's single source-of-truth check command. Runs fully OFFLINE (no network, no secrets) and
# exits non-zero on any failure.
#
# This file is the repo's control surface. Tickets must be satisfiable WITHOUT editing it — if a
# change looks like it needs check.sh relaxed, the change is wrong.
set -euo pipefail
cd "$(dirname "$0")/.."

PY="${PY:-.venv/bin/python}"
[ -x "$PY" ] || PY="$(command -v python3)"

echo "== ruff check =="
"$PY" -m ruff check wordstats tests

echo "== ruff format --check =="
"$PY" -m ruff format --check wordstats tests

echo "== pytest =="
"$PY" -m pytest
