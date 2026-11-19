#!/usr/bin/env bash
result=$(awk -F, '
NR==1 {next}
{
  line=$0
  gsub(/^[ \t]+|[ \t]+$/, "", line)
  if (line == "") next
}
{
  rows++
  total += $2 * $3
}
END { printf "%d %s", rows+0, total+0 }
')
read -r rows total <<< "$result"
rows=${rows:-0}
total=${total:-0}
jq -n --argjson rows "$rows" --argjson total "$total" '{rows: $rows, total: $total}'
