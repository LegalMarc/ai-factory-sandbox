#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

check() {
  local script=$1 input=$2 expected=$3 actual
  actual=$(printf '%s' "$input" | bash "$script" | jq -c .)
  if [[ "$actual" != "$expected" ]]; then
    printf 'mismatch: expected %s, got %s\n' "$expected" "$actual" >&2
    exit 1
  fi
}

check "$DIR/sumcsv.sh" \
  'name,qty,price
a,2,1.5
b,1,0.25
' \
  '{"rows":2,"total":3.25}'

check "$DIR/sumcsv.sh" \
  'name,qty,price

x,3,2

y,1,1
' \
  '{"rows":2,"total":7}'

check "$DIR/sumcsv.sh" \
  'name,qty,price
' \
  '{"rows":0,"total":0}'

check "$DIR/sumcsv.sh" \
  'name,qty,price
single,4,0.5
' \
  '{"rows":1,"total":2}'

printf 'ok\n'
