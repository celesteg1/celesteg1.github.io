---
title: 'Lifecycle in Practice - Balance Check'
description: 'Details for the balance check phase of the token lifecycle.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-burning/"> 3. burning </a>  |   token lifecycle (explanation)
</span>
<hr/>

{{ include_file('snippets/snippy-lifecycle-in-practice.md') }}

---

# 4. Balance Check

| Section               | Details  |
|-----------------------|-----------|
| **What happens**       | You verify the number of tokens held in a given wallet. This is often used for reconciliation (e.g., matching on-chain holdings with off-chain records), reporting, or internal audits. |
| **Real-world analogy** | A custodian verifies that Client X holds 100 units of a particular bond in their account. |
| **API**                | [`GET /api/tokens/balance`](/mkdocs/examples/post-trade-automation/references/api/api-check-token-balance/) |
| **Code Example**       | [How to check token balances](/mkdocs/examples/post-trade-automation/how-tos/how-to-check-a-token-balance/) |

**Example Endpoint (GET):**

```bash
/api/tokens/balance?asset_id=UKGILT2030&wallet_address=0xA1B2...
```

## Common Triggers

{{ include_file('snippets/snippy-when-balance-checks-typically-occur.md') }}

---

## What comes next?

- [How to Mint (Create) a Token](/mkdocs/examples/post-trade-automation/how-tos/how-to-mint-a-token/) 

## Related Reading

{{ include_file('snippets/snippy-related-reading-token-lifecycle.md') }}

