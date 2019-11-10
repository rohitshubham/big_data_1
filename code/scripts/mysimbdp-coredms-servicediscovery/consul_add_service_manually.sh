curl \
    --request PUT \
    --data @payload.json \
    http://127.0.0.1:8500/v1/agent/service/register?replace-existing-checks=1