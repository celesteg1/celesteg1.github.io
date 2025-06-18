---
title: 'API Reference: Check Token Balance'
description: 'ABC-Labs API Reference for checking token balance.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/references/api/api-burn-token/"> burn token </a> |   api reference
</span>
<hr/>

# API Reference: Check Token Balance

- **Description:** Retrieves the token balance of a specific wallet for a given asset.
- **Method:** `GET`  
- **Endpoint:** `/api/tokens/balance`  
- **How-To:** [How to Check Token Balance](/mkdocs/examples/post-trade-automation/how-tos/how-to-check-a-token-balance/)
- **Explanation:** [Token Lifecycle in Practice: Balance Check](/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-balance-check/)

## Query Parameters

| Field            | Type   | Required | Description                      |
|------------------|--------|----------|----------------------------------|
| `asset_id`       | String | ✅       | ID of the asset to query         |
| `wallet_address` | String | ✅       | Wallet to check balance for      |

---

## Example Request

```bash
GET /api/tokens/balance?asset_id=UKGILT2030&wallet_address=0xDEF456...
```

---

## Success Response

```json
{
  "asset_id": "UKGILT2030",
  "wallet_address": "0xDEF456...",
  "balance": 100
}
```

---

## Error Responses

| Status Code | Error Code            | Message                            |
| ----------- | --------------------- | ---------------------------------- |
| 400         | MISSING\_QUERY\_PARAM | Asset ID or wallet address missing |
| 404         | WALLET\_NOT\_FOUND    | Wallet address does not exist      |
| 500         | INTERNAL\_ERROR       | Unexpected server error            |

---


## What comes next?

- [API Reference: Mint Token](/mkdocs/examples/post-trade-automation/references/api/api-mint-token/) 

## Related Reading

{{ include_file('snippets/snippy-related-reading-api-references.md') }}
