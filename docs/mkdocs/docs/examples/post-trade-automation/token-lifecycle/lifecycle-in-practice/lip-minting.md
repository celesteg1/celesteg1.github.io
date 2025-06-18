---
title: 'Lifecycle in Practice - Minting'
description: 'Details for the minting phase of the token lifecycle.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/token-lifecycle/token-lifecycle-stages-and-api-mapping">token lifecycle stages & api mapping </a>  |   token lifecycle (explanation)
</span>
<hr/>

{{ include_file('snippets/snippy-lifecycle-in-practice.md') }}

---

# 1. Minting


| Section               | Details  |
|-----------------------|-----------|
| **What happens**       | A new token is created to represent the financial asset. This happens at the point of asset issuance or contract creation.                  |
| **Real-world analogy** | Issuing a bond certificate and recording it in a central ledger. Here, you're issuing a digital version on a blockchain.                   |
| **API**                | [`POST /api/tokens/mint`](/mkdocs/examples/post-trade-automation/references/api/api-mint-token/) |
| **Code Example**       | [How to mint a token](/mkdocs/examples/post-trade-automation/how-tos/how-to-mint-a-token/) |



**Example JSON Payload:**

```json
{
  "asset_id": "UKGILT2030",
  "amount": 100,
  "recipient_wallet_address": "0xABC123..."
}
```

---

## What comes next?

- [Token Lifecycle in Practice: 2. Transfer](/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-transfer/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-token-lifecycle.md') }}

