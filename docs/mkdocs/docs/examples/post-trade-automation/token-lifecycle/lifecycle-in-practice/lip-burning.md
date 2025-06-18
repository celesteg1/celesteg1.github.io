---
title: 'Lifecycle in Practice - Burning'
description: 'Details for the burning phase of the token lifecycle.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-transfer/"> 2. transfer </a>  |   token lifecycle (explanation)
</span>
<hr/>

{{ include_file('snippets/snippy-lifecycle-in-practice.md') }}

---

# 3. Burning

| Section               | Details  |
|-----------------------|-----------|
| **What happens**       | A token is destroyed when the underlying asset is redeemed, matured, or cancelled. This signals the end of the asset’s lifecycle on-chain. |
| **Real-world analogy** | A bond matures and is paid back to the holder, the position is closed, and the record is archived. |
| **API**                | [`POST /api/tokens/burn`](/mkdocs/examples/post-trade-automation/references/api/api-burn-token/) |
| **Code Example**       | [How to Burn Tokens](/mkdocs/examples/post-trade-automation/how-tos/how-to-burn-tokens/) |

**Example JSON Payload:**

```json
{
  "asset_id": "UKGILT2030",
  "amount": 100,
  "holder_wallet_address": "0xDEF456..."
}
```

---

## What comes next?

- [Token Lifecycle in Practice: 4. Balance Check](/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-balance-check/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-token-lifecycle.md') }}

