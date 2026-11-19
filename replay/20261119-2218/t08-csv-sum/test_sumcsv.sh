#!/bin/bash
set -u
script_dir=$(dirname "$0")

fail() {
    echo "FAIL: $1" >&2
    exit 1
}

out=$(printf 'name,qty,price\na,2,1.5\nb,1,0.25\n' | bash "$script_dir/sumcsv.sh") || fail "basic: sumcsv.sh failed"
printf '%s' "$out" | jq -e '.rows == 2 and .total == 3.25' >/dev/null || fail "basic: got $out"

out=$(printf 'name,qty,price\n\nx,3,2\n\ny,1,1\n' | bash "$script_dir/sumcsv.sh") || fail "blank: sumcsv.sh failed"
printf '%s' "$out" | jq -e '.rows == 2 and .total == 7' >/dev/null || fail "blank: got $out"

out=$(printf 'name,qty,price\n' | bash "$script_dir/sumcsv.sh") || fail "header only: sumcsv.sh failed"
printf '%s' "$out" | jq -e '.rows == 0 and .total == 0' >/dev/null || fail "header only: got $out"

echo ok
exit 0
