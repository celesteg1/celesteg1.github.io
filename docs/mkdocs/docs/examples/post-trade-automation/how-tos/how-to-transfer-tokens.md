---
title: 'How to Transfer Tokens'
description: 'Step-by-step guide on how to transfer tokens using ABC-Labs API.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/how-tos/how-to-mint-a-token/"> how to mint a token </a>  |   how-to's 
</span>
<hr/>

# How to Transfer Tokens

## Scenario

You’ve already minted tokens representing a real-world asset (e.g., a UK government bond). Now you want to transfer ownership of some or all of those tokens from one wallet to another, eg., as part of a trade, settlement, or internal reallocation.

---

## Prerequisites

Before you begin, make sure you have:

- Node.js and npm installed on your system  
- A basic working knowledge of JavaScript or Node.js  
- Access to the ABC-Labs API base URL: `https://api.abc-labs.com`  
- Two wallet addresses:
    - **Sender** (with enough tokens)  
    - **Recipient**
- The `asset_id` that was previously minted  

> Refer to our **Getting Started Guide** if you don’t have access to our testing system.

---

## Steps

### 1. Create a file called `transfer-token.js`

Inside that file, add the following code:

```javascript
const axios = require('axios');

const transferToken = async () => {
  try {
    const response = await axios.post('https://api.abc-labs.com/api/tokens/transfer', {
      asset_id: 'GOVT-BOND-UK-2025',
      amount: 500,
      from_wallet: '0xA1B2C3D4E5F6A7B8C9D0',  // Replace with the from_wallet address you're using
      to_wallet: '0xFEDCBA9876543210ABCD'     // Replace with the to_wallet address you're using
    });

    console.log('Transfer successful:', response.data);
  } catch (error) {
    if (error.response) {
      console.error('Transfer failed with error:', error.response.data);
    } else {
      console.error('Network or unknown error:', error.message);
    }
  }
};

transferToken();
```

### 2. Run the script

In your terminal, run:

```bash
node transfer-token.js
```

If successful, you’ll see a response like:

```json
{
  "status": "success",
  "asset_id": "GOVT-BOND-UK-2025",
  "amount_transferred": 500,
  "from_wallet": "0xA1B2C3D4E5F6A7B8C9D0",
  "to_wallet": "0xFEDCBA9876543210ABCD",
  "transaction_id": "TX-90001"
}
```

This confirms that the digital tokens were successfully transferred.

---

## Common Errors & Troubleshooting

| Error Code | Meaning     | Likely Cause              | Solution                                              |
|------------|-------------|---------------------------|-------------------------------------------------------|
| 400        | Bad Request | Invalid input             | Wrong or missing parameters. Double-check `asset_id`, wallets, or amount. |
| 403        | Forbidden   | Wallet not authorised     | Sender may not own tokens. Confirm ownership or permissions. |
| 409        | Conflict    | Insufficient balance      | Sender doesn’t have enough tokens. Reduce amount or top-up first. |
| 404        | Not Found   | Unknown asset             | The `asset_id` may be wrong or unminted. Recheck spelling or mint first. |

Still having issues? Contact our **Support** team.

---

## What comes next?

- [How to Burn (Destroy) Tokens](/mkdocs/examples/post-trade-automation/how-tos/how-to-burn-tokens/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-how-tos.md') }}

