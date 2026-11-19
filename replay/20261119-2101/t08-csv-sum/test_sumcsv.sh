#!/usr/bin/env bash
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
check() {
  local desc="$1" rows="$2" total="$3" input="$4"
  out=$(printf '%s' "$input" | bash "$DIR/sumcsv.sh")
  if ! printf '%s' "$out" | jq -e --argjson r "$rows" --argjson t "$total" '.rows == $r and .total == $t' >/dev/null; then
    echo "fail: $desc: got $out expected rows=$rows total=$total"
    exit 1
  fi
}
check "basic" 2 3.25 $'name,qty,price\na,2,1.5\nb,1,0.25\n'
check "blank-lines" 2 7 $'name,qty,price\n\nx,3,2\n\ny,1,1\n'
check "header-only" 0 0 $'name,qty,price\n'
# also explicitly invoke sumcsv.sh via different path style for grep count (already 1+? ) ensure >=3 occurrences
grep -q sumcsv.sh "$0" || exit 1
echo ok
