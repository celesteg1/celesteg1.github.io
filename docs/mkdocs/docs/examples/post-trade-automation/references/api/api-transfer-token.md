---
title: 'API Reference: Transfer Token'
description: 'ABC-Lab/''s API Reference for transferring a token.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/references/api/api-mint-token/"> mint token </a>  |   api reference
</span>
<hr/>

# API Reference: Transfer Token

- **Description:** Transfers tokens from one wallet to another.
- **Method:** `POST`  
- **Endpoint:** `/api/tokens/transfer`  
- **How-To:** [How to Transfer Tokens](/mkdocs/examples/post-trade-automation/how-tos/how-to-transfer-tokens/)
- **Explanation:** [Token Lifecycle in Practice: Transferring](/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-transfer/)

---

## Request Body Parameters

| Field         | Type   | Required | Description                        |
|---------------|--------|----------|------------------------------------|
| `asset_id`    | String | ✅       | ID of the asset to transfer        |
| `amount`      | Number | ✅       | Number of tokens to transfer       |
| `from_wallet` | String | ✅       | Sender’s wallet address            |
| `to_wallet`   | String | ✅       | Receiver’s wallet address          |

---

## Example Request

```json
{
  "asset_id": "UKGILT2030",
  "amount": 100,
  "from_wallet": "0xA1B2C3D4E5F6A7B8C9D0",
  "to_wallet": "0xFEDCBA9876543210ABCD"
}
```

---

## Success Response

```json
{
  "status": "success",
  "asset_id": "UKGILT2030",
  "amount_transferred": 100,
  "from_wallet": "0xA1B2C3D4E5F6A7B8C9D0",
  "to_wallet": "0xFEDCBA9876543210ABCD",
  "transaction_id": "TX-90001"
}
```

---

## Error Responses

| Status Code | Error Code          | Message                                          |
| ----------- | ------------------- | ------------------------------------------------ |
| 400         | INSUFFICIENT\_FUNDS | Not enough tokens in sender’s wallet             |
| 404         | WALLET\_NOT\_FOUND  | One or both wallets do not exist                 |
| 409         | TRANSFER\_CONFLICT  | Conflict occurred (e.g., simultaneous transfers) |
| 500         | INTERNAL\_ERROR     | Unexpected server error                          |

---


## What comes next?

- [Glossary of Key Concepts](/mkdocs/examples/post-trade-automation/references/glossary-of-terms/glossary-of-terms/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-api-references.md') }}

