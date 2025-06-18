---
title: 'Glossary of Terms'
description: 'A glossary of common blockchain terminology'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/references/api/api-transfer-token/"> api reference: transfer token </a>  |   glossary of key concepts (reference)
</span>
<hr/>

# Glossary of Key Concepts in Blockchain and Tokenisation

---

## Atomic Settlement
Atomic settlement means that the exchange of assets (e.g., payment for securities) occurs simultaneously and irreversibly. Either both sides of the transaction succeed, or neither does, eliminating settlement risk.

---

## Blockchain
A blockchain is a distributed ledger maintained across a network of nodes. Each transaction is validated, timestamped, and linked to previous ones via cryptographic hashes, creating an immutable and transparent record.

---

## Burning
Burning refers to the permanent removal of a token from circulation, typically when an asset is redeemed, expires, or is otherwise retired.

---

## Common Domain Model (CDM)
The CDM is a standardised, machine-readable model developed by ISDA, ISLA, and ICMA. It defines how financial instruments behave and how lifecycle events (like trade confirmation or margin calls) should be represented and processed.

---

## Distributed Validation
Instead of relying on a central authority (like a clearinghouse), blockchain transactions are validated by multiple nodes in the network. This decentralised model improves resilience and trust.

---

## Immutability
Once written to the blockchain, data cannot be changed without redoing the entire chain. This provides a tamper-proof audit trail, which is especially valuable in regulated financial environments.

---

## Minting
Minting is the process of creating new tokens and registering them on the blockchain. This typically occurs when an asset is issued or when a new financial product is brought on-chain.

---

## On-Chain vs. Off-Chain

**On-chain** refers to data and logic that are executed and stored directly on the blockchain (e.g., smart contracts, token balances).

**Off-chain** refers to data or processes managed outside the blockchain, such as user authentication or high-volume analytics, but that may still reference or interact with on-chain activity.

---

## Smart Contracts
Smart contracts are self-executing pieces of code stored on the blockchain. They encode rules and workflows, for example, automatically settling a trade, sending margin calls, or executing interest payments. At ABC-Labs, smart contracts align with the Common Domain Model (CDM) to ensure standardisation and interoperability.

---

## Tokenisation
Tokenisation is the process of digitally representing real-world assets (RWAs), such as bonds, derivatives, or commodities, on a blockchain. Each token reflects rights or ownership tied to the underlying asset and can be governed by programmable logic.

---


## What comes next?

- [Official Docs: Overview](/mkdocs/official-docs/overview/)


## Related Reading

{{ include_file('snippets/snippy-related-reading-glossary-of-terms.md') }}
