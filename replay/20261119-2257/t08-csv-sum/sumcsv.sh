#!/bin/bash
awk -F, '
NR == 1 { next }
$0 ~ /^[[:space:]]*$/ { next }
{ rows++; total += $2 * $3 }
END { printf "%d %.10g", rows, total }
' | { read -r rows total; jq -cn --argjson rows "${rows:-0}" --argjson total "${total:-0}" '{rows: $rows, total: $total}'; }
