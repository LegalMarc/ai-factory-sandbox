#!/bin/bash
result=$(awk -F, '
NR==1 {next}
/^[[:space:]]*$/ {next}
{ rows++; total += $2 * $3 }
END { printf "%d %.10f\n", rows+0, total+0 }
')
rows=$(printf '%s' "$result" | cut -d' ' -f1)
total=$(printf '%s' "$result" | cut -d' ' -f2)
rows=${rows:-0}
total=${total:-0}
total=$(printf '%s' "$total" | sed -e 's/\.\?0*$//')
case "$total" in
""|"-") total=0 ;;
esac
jq -n --argjson rows "$rows" --argjson total "$total" '{rows: $rows, total: $total}'
