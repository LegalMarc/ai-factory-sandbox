#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if ! printf 'name,qty,price\na,2,1.5\nb,1,0.25\n' | bash "$DIR/sumcsv.sh" | jq -e '.rows == 2 and .total == 3.25' >/dev/null; then
  echo "mismatch: sumcsv.sh case 1" >&2
  exit 1
fi
if ! printf 'name,qty,price\n\nx,3,2\n\ny,1,1\n' | bash "$DIR/sumcsv.sh" | jq -e '.rows == 2 and .total == 7' >/dev/null; then
  echo "mismatch: sumcsv.sh case 2" >&2
  exit 1
fi
if ! printf 'name,qty,price\n' | bash "$DIR/sumcsv.sh" | jq -e '.rows == 0 and .total == 0' >/dev/null; then
  echo "mismatch: sumcsv.sh case 3" >&2
  exit 1
fi
echo ok
exit 0
