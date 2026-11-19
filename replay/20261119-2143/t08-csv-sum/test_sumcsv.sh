#!/usr/bin/env bash
DIR="$(dirname "$0")"
printf 'name,qty,price\na,2,1.5\nb,1,0.25\n' | bash "$DIR/sumcsv.sh" | jq -e '.rows == 2 and .total == 3.25' >/dev/null || { echo "fail case1" >&2; exit 1; }
printf 'name,qty,price\n\nx,3,2\n\ny,1,1\n' | bash "$DIR/sumcsv.sh" | jq -e '.rows == 2 and .total == 7' >/dev/null || { echo "fail case2" >&2; exit 1; }
printf 'name,qty,price\n' | bash "$DIR/sumcsv.sh" | jq -e '.rows == 0 and .total == 0' >/dev/null || { echo "fail case3" >&2; exit 1; }
echo ok
