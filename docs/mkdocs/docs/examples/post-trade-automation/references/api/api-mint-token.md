---
title: 'API Reference: Mint Token'
description: 'ABC-Lab/''s API Reference for minting a token.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/references/api/api-check-token-balance/"> check token balance </a> |   api reference
</span>
<hr/>

# API Reference: Mint Token

- **Description:** Creates and assigns a new token to a recipient wallet.
- **Method:** `POST`  
- **Endpoint:** `/api/tokens/mint`  
- **How-To:** [How to Mint a Token](/mkdocs/examples/post-trade-automation/how-tos/how-to-mint-a-token/)
- **Explanation:** [Token Lifecycle in Practice: Minting](/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-minting/)

## Request Body Parameters

| Field                   | Type   | Required | Description                                 |
|-------------------------|--------|----------|---------------------------------------------|
| `asset_id`              | String | ✅       | Unique identifier for the asset being minted |
| `amount`                | Number | ✅       | Number of tokens to mint                     |
| `recipient_wallet_address` | String | ✅       | Wallet address that will receive the tokens  |

---

## Example Request

```json
{
  "asset_id": "UKGILT2030",
  "amount": 100,
  "recipient_wallet_address": "0xA1B2C3D4E5F6A7B8C9D0"
}
```

---

## Success Response

```json
{
  "status": "success",
  "token_id": "TOKEN-12345",
  "asset_id": "UKGILT2030",
  "amount": 100,
  "assigned_to": "0xA1B2C3D4E5F6A7B8C9D0"
}
```

---

## Error Responses

| Status Code | Error Code      | Message                                 |
|-------------|------------------|-----------------------------------------|
| 400         | INVALID_INPUT    | One or more required fields are missing |
| 404         | ASSET_NOT_FOUND  | Asset ID does not exist                 |
| 409         | DUPLICATE_MINT   | Token for this asset already exists     |
| 500         | INTERNAL_ERROR   | Unexpected server error                 |

---

## What comes next?

- [API Reference: Transfer Token](/mkdocs/examples/post-trade-automation/references/api/api-transfer-token/) 

## Related Reading

{{ include_file('snippets/snippy-related-reading-api-references.md') }}

