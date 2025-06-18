---
title: 'Lifecycle in Practice - Transferring'
description: 'Details for the transferring phase of the token lifecycle.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-minting/"> 1. minting </a>  |   token lifecycle (explanation)
</span>
<hr/>

{{ include_file('snippets/snippy-lifecycle-in-practice.md') }}

---

# 2. Transfer

| Section               | Details  |
|-----------------------|-----------|
| **What happens**       | Ownership of the token changes, typically during trade settlement. The seller sends the token to the buyer, while cash changes hands off-chain or via stablecoins. |
| **Real-world analogy** | A broker confirms delivery of a bond to a buyer’s custody account once payment is received. |
| **API**                | [`POST /api/tokens/transfer`](/mkdocs/examples/post-trade-automation/references/api/api-transfer-token/) |
| **Code Example**       | [How to Transfer Tokens](/mkdocs/examples/post-trade-automation/how-tos/how-to-transfer-tokens/) |

**Example JSON Payload:**

```json
{
  "asset_id": "UKGILT2030",
  "amount": 100,
  "from_wallet": "0xABC123...",
  "to_wallet": "0xDEF456..."
}
```

---

## What comes next?

- [Token Lifecycle in Practice: 3. Burning](/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-burning/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-token-lifecycle.md') }}

