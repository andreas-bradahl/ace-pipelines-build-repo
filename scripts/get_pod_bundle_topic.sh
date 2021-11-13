apk add jq curl > /dev/null

curl \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/$1/$2 |
    jq -r '.topics[] | select(. | startswith("pod"))'