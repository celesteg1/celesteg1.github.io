---
title: 'API Overview'
description: 'High-level guide to ABC-Labs Tokenisation API.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/how-tos/how-to-check-a-token-balance/"> how to check a token balance </a>  |   api reference
</span>
<hr/>

# API Overview

Welcome to the ABC-Labs Tokenisation API. This guide introduces the structure and logic of the API documentation, helping you quickly locate what you need.

---

## API Versions

- Latest API version: `v1.1.0`
- See our **Release Notes** for latest updates.

---

## What You Can Do with the API

- [Mint](/mkdocs/examples/post-trade-automation/references/api/api-mint-token/) tokens to represent real-world assets
- [Transfer](/mkdocs/examples/post-trade-automation/references/api/api-transfer-token/) tokens between wallets
- [Burn](/mkdocs/examples/post-trade-automation/references/api/api-burn-token/) tokens once assets are settled or redeemed
- [Check](/mkdocs/examples/post-trade-automation/references/api/api-check-token-balance/) wallet balances

---

## How the Documentation is Structured

Each API endpoint is described in its own dedicated page, following a consistent structure:

### 1. **Header Summary**

Quick summary of:

- **Brief Description**
- **Method** (e.g., `POST`, `GET`)
- **Endpoint** path
- **Relevant How-To Links**

### 2. **Request Parameters**

A table outlining:

- Parameter name
- Type (`String`, `Number`, etc.)
- Whether it's required
- What it does

```markdown
Example:

| Field         | Type   | Required | Description           |
|---------------|--------|----------|-----------------------|
| `asset_id`    | String | ✅       | Token identifier      |
| `amount`      | Number | ✅       | Number of tokens      |
```

### 3. Example Requests & Responses

Code blocks to show:

- Example request payload or query
- Example success response (JSON)
- Format varies (json, bash, etc.)

### 4. Error Handling

A table of known error responses including:

- Status code
- Error code (machine-friendly)
- Message (human-readable)

```markdown
Example:
| Status Code | Error Code        | Message                       |
|-------------|-------------------|-------------------------------|
| 400         | INVALID_INPUT     | Missing required parameters   |
```

## Navigation Tips

- **Start with Examples:** See the [How-To Guides](/mkdocs/examples/post-trade-automation/how-tos/how-to-mint-a-token/) if you prefer learning by doing.
- **Use Search:** Look up keywords like "mint", "burn", or "balance".
- **Understand the Lifecycle:** Read [Token Lifecycle](/mkdocs/examples/post-trade-automation/token-lifecycle/what-is-a-token-lifecycle/) for full context.
- **Understand Post-Trade Automation:** Read the [explanation guide](/mkdocs/examples/post-trade-automation/pt-auto/introduction/) on what post-trade automation is and how it fits in with traditional post-trade workflows. 

## Base URL

All API requests use the following base URL:

```html
https://api.abc-labs.com
```

---


## What comes next?

- [API Reference: Burn Token](/mkdocs/examples/post-trade-automation/references/api/api-burn-token/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-api-references.md') }}

