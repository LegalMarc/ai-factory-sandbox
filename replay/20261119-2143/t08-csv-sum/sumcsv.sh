#!/usr/bin/env bash
read -r rows total <<< "$(awk -F, 'NR==1{next} /^[[:space:]]*$/{next} {rows++; total+=$2*$3} END{printf "%d %.10f", rows, total}')"
jq -c -n --argjson rows "$rows" --argjson total "$total" '{rows: $rows, total: $total}'
