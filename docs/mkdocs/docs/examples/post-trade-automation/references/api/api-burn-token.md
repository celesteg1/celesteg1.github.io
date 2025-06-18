---
title: 'API Reference: Burn Token'
description: 'ABC-Labs API Reference for burning tokens.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/references/api/api-overview/"> api overview </a> |   api reference
</span>
<hr/>

# API Reference: Burn Token

- **Description:** Destroys tokens from a holder's wallet. Typically used on maturity, cancellation, or redemption.
- **Method:** `POST`  
- **Endpoint:** `/api/tokens/burn`  
- **How-To:** [How to Burn a Token](/mkdocs/examples/post-trade-automation/how-tos/how-to-burn-tokens/)
- **Explanation:** [Token Lifecycle in Practice: Burning](/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-burning/)

## Request Body Parameters

| Field                  | Type   | Required | Description                          |
|------------------------|--------|----------|--------------------------------------|
| `asset_id`             | String | ✅       | ID of the asset to burn              |
| `amount`               | Number | ✅       | Number of tokens to destroy          |
| `holder_wallet_address`| String | ✅       | Wallet address where tokens are held |

---

## Example Request

```json
{
  "asset_id": "UKGILT2030",
  "amount": 500,
  "holder_wallet_address": "0xFEDCBA9876543210ABCD"
}
```

---

## Success Response

```json
{
  "status": "success",
  "asset_id": "UKGILT2030",
  "amount_burned": 500,
  "holder_wallet_address": "0xFEDCBA9876543210ABCD",
  "transaction_id": "TX-90002"
}
```

---

## Error Responses

| Status Code | Error Code                    | Message                        |
| ----------- | ----------------------------- | ------------------------------ |
| 400         | INVALID\_BURN\_AMOUNT         | Amount exceeds token holdings  |
| 404         | ASSET\_OR\_WALLET\_NOT\_FOUND | Asset or wallet does not exist |
| 409         | BURN\_CONFLICT                | Conflict during burn operation |
| 500         | INTERNAL\_ERROR               | Unexpected server error        |

---


## What comes next?

- [API Reference: Check Token Balance](/mkdocs/examples/post-trade-automation/references/api/api-check-token-balance/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-api-references.md') }}

