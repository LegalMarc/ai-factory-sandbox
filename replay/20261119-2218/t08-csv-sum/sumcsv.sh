#!/bin/bash
result=$(awk -F, '
NR == 1 { next }
{
    line = $0
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", line)
    if (line == "") next
    rows++
    total += $2 * $3
}
END { printf "%d %.10g", rows, total }
')
rows=${result%% *}
total=${result##* }
if [ -z "$rows" ]; then rows=0; fi
if [ -z "$total" ]; then total=0; fi
jq -cn --argjson rows "$rows" --argjson total "$total" '{rows: $rows, total: $total}'
