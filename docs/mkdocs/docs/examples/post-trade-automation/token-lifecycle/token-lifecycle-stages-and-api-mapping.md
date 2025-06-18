---
title: 'Token Lifecycle Stages & API Mapping'
description: 'Benefits of tokenisation'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/token-lifecycle/why-tokenisation-matters">why tokenisation matters </a>  |   token lifecycle (explanation)
</span>
<hr/>

# Token Lifecycle Stages & API Mapping

The table below matches ABC-Labs' API endpoints with the different lifecycle stages of a token.

| Stage         | Real-World Equivalent             | API Endpoint                                                   | What it Does                                        | How-to Guide                |
|---------------|-----------------------------------|----------------------------------------------------------------|-----------------------------------------------------|-----------------------------|
| **Mint**      | Asset issuance / contract creation| [`POST /api/tokens/mint`](/mkdocs/examples/post-trade-automation/references/api/api-mint-token/)                                        | Creates token and assigns to a wallet               | [How to Mint a Token](/mkdocs/examples/post-trade-automation/how-tos/how-to-mint-a-token/)    |
| **Transfer**  | Trade execution & settlement      | [`POST /api/tokens/transfer`](/mkdocs/examples/post-trade-automation/references/api/api-transfer-token/)                                 | Moves token from one wallet to another              | [How to Transfer Tokens](/mkdocs/examples/post-trade-automation/how-tos/how-to-transfer-tokens/)|
| **Burn**      | Redemption, maturity, cancellation| [`POST /api/tokens/burn`](/mkdocs/examples/post-trade-automation/references/api/api-burn-token/)                                       | Destroys the token, representing position closure   | [How to Burn Tokens](/mkdocs/examples/post-trade-automation/how-tos/how-to-burn-tokens/)    |
| **Balance Check** | Reconciliation / audit / compliance | [`GET /api/tokens/balance?asset_id=...&wallet_address=...`](/mkdocs/examples/post-trade-automation/references/api/api-check-token-balance/) | Retrieves balance of a wallet for a given asset     | [How to Check a Token Balance](/mkdocs/examples/post-trade-automation/how-tos/how-to-check-a-token-balance/) |


---

## What comes next?

- [Token Lifecycle in Practice: 1. Minting](/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-minting/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-token-lifecycle.md') }}

