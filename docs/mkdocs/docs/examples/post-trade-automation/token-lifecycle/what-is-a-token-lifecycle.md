---
title: 'What is a token lifecycle?'
description: 'An overview of the lifecycle of a token.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/token-lifecycle/introduction">introduction to a token lifecycle </a>  |   token lifecycle (explanation)
</span>
<hr/>

# What is a Token Lifecycle?

A token lifecycle describes the key events a financial asset undergoes when it is digitised and managed on-chain. In traditional finance, an asset like a bond or derivative goes through stages such as issuance, settlement, redemption, and reporting. When tokenised, each of these stages corresponds to specific on-chain actions using tokens.

## Key Stages

- **Minting**: The digital creation of a token to represent the asset.
- **Transfer**: The movement of the token between parties (e.g., trade settlement).
- **Burning**: Destruction of the token when the asset is redeemed, cancelled, or matured.
- **Balance Checking**: Verifying token holdings for reconciliation, auditing, or regulatory compliance.

<figure>
  <img src="/mkdocs/assets/images/examples/post-trade-automation/pt-auto/tokenisationLifecycle.png"  style="border-radius: 12px; width: 600px" />
  <figcaption>Figure:  The lifecycle of a tokenised asset: from issuance to redemption, each stage is executed via API and recorded on-chain for full transparency and automation. 
  </figcaption>
</figure>

---

## When Balance Checks Typically Occur

{{ include_file('snippets/snippy-when-balance-checks-typically-occur.md') }}

---

## What comes next?

- [Why Tokenisation Matters](/mkdocs/examples/post-trade-automation/token-lifecycle/why-tokenisation-matters/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-token-lifecycle.md') }}

