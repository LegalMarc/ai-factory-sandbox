#!/bin/bash
dir="$(dirname "$0")"
out=$(printf 'name,qty,price\na,2,1.5\nb,1,0.25\n' | bash "$dir/sumcsv.sh")
printf '%s' "$out" | jq -e '.rows == 2 and .total == 3.25' >/dev/null || exit 1
out=$(printf 'name,qty,price\n\nx,3,2\n\ny,1,1\n' | bash "$dir/sumcsv.sh")
printf '%s' "$out" | jq -e '.rows == 2 and .total == 7' >/dev/null || exit 1
out=$(printf 'name,qty,price\n' | bash "$dir/sumcsv.sh")
printf '%s' "$out" | jq -e '.rows == 0 and .total == 0' >/dev/null || exit 1
echo ok
exit 0
