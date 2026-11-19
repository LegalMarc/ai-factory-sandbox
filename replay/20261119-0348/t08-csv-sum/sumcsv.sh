#!/usr/bin/env bash
set -euo pipefail

read -r rows total < <(
  awk -F, '
    NR == 1 { next }
    /^[[:space:]]*$/ { next }
    {
      sub(/\r$/, "", $3)
      rows++
      total += $2 * $3
    }
    END { printf "%d %.10g\n", rows, total }
  '
)

jq -n --argjson rows "$rows" --argjson total "$total" '{rows: $rows, total: $total}'
