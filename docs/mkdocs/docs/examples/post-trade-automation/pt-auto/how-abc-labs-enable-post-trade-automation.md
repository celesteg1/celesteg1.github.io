---
title: 'How ABC-Labs Enable Post-Trade Automation'
description: 'Outline of how ABC-Labs enable post-trade automation with smart contracts, legal logic and dev-focused API'
pubDate: 'Jun 12 2025'
---
{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
     ← <a href="/mkdocs/examples/post-trade-automation/pt-auto/why-tokenise-financial-assets/">why tokenise financial assets? </a>  |   post-trade automation (explanation)
</span>
<hr/>

# How ABC-Labs Enable Post-Trade Automation

## 1. Smart Contracts & Legal Logic

Every token created with ABC-Labs is powered by smart contracts. These contracts handle the logic behind:

- Coupon payments
- Redemption schedules
- Conditional ownership changes
- Event-driven asset lifecycle management

To ensure legality and interoperability, ABC-Labs aligns with [ISDA’s Common Domain Model (CDM)](https://www.isda.org/isda-solutions-infohub/cdm/), which is a machine-readable standard that captures legal and economic terms of real-world contracts.

!!! tip
     A tokenised Gilt is still a Gilt. Tokenisation doesn’t change the asset. It changes how it’s issued, managed, and settled.

---

## 2. ABC-Labs' Developer-Focused API

ABC-Labs provides an API designed for developers and institutions to automate full asset lifecycles, from issuance to redemption. All actions are recorded on-chain and integrated with operational and legal workflows.


**Token Lifecycle:**

| Endpoint            |   API Endpoint | Purpose                                          |
|---------------------|----------------|----------------------------------|
| **Mint Tokens**     | [`/api/tokens/mint`](/mkdocs/examples/post-trade-automation/references/api/api-mint-token/)    | Create a digital token representing a new asset (e.g., a bond issuance). |
| **Transfer Tokens** | [`/api/tokens/transfer`](/mkdocs/examples/post-trade-automation/references/api/api-transfer-token/)| Move tokens between wallets (e.g. investors, counterparties)       |
| **Burn Tokens**     | [`/api/tokens/burn`](/mkdocs/examples/post-trade-automation/references/api/api-burn-token/)    | Retire tokens (e.g. at maturity or cancellation)                    |
| **Check Balances**  | [`/api/tokens/balance`](/mkdocs/examples/post-trade-automation/references/api/api-check-token-balance/) | Query wallet holdings or transaction state                         |
  
<figure>
  <img src="/mkdocs/assets/images/examples/post-trade-automation/pt-auto/tokenisationLifecycle.png"  style="border-radius: 12px; width: 600px" />
  <figcaption>Figure:  The lifecycle of a tokenised asset: from issuance to redemption, each stage is executed via API and recorded on-chain for full transparency and automation. 
  </figcaption>
</figure>

---


!!! example Automating a Bond Lifecycle

    Here’s how ABC-Labs' API can be used to manage a tokenised UK government bond:

    - **Mint**  
    `/api/tokens/mint` → Create tokens to represent the bond.

    - **Primary Distribution**  
    `/api/tokens/transfer` → Allocate tokens to investors.

    - **Secondary Trading**  
    `/api/tokens/transfer` → Exchange tokens peer-to-peer in the secondary market.

    - **Maturity & Redemption**  
    `/api/tokens/burn` → Remove tokens from circulation upon bond maturity.

    - **Full Audit Trail**  
    All steps are immutably recorded on-chain and visible via explorer tools or API queries.  
    Each step is executed via API, reducing complexity, human error, and manual intervention.

---

## What comes next?

- [Why it matters](/mkdocs/examples/post-trade-automation/pt-auto/conclusion/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-post-trade-automation.md') }}