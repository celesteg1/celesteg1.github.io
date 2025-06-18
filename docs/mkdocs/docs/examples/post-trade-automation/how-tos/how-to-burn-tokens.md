---
title: 'How to Burn Tokens'
description: 'Step-by-step guide on how to burn tokens using ABC-Lab/''s API.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/how-tos/how-to-transfer-tokens"> how to transfer tokens </a>  |   how-to's 
</span>
<hr/>

# How to Burn Tokens

## Scenario

You’ve transferred tokens to a holder, and now the real-world asset they represent has matured, been redeemed, or otherwise settled. You need to burn (i.e., destroy) the tokens to reflect that they no longer represent an active or valid claim on the underlying asset.

---

## Prerequisites

Before you begin, make sure you have:

- Node.js and npm installed on your system  
- A basic working knowledge of JavaScript or Node.js  
- Access to the ABC-Labs API base URL: `https://api.abc-labs.com`  
- The `wallet_address` holding the tokens to be burned  
- Sufficient token balance in that wallet  

> Refer to our **Getting Started Guide** if you don’t have access to our testing system.

---

## Steps

### 1. Create a file called `burn-token.js`

Inside that file, add the following code:

```javascript
const axios = require('axios');

const burnToken = async () => {
  try {
    const response = await axios.post('https://api.abc-labs.com/api/tokens/burn', {
      asset_id: 'GOVT-BOND-UK-2025',
      amount: 500,
      holder_wallet_address: '0xFEDCBA9876543210ABCD' // replace with the holder_wallet_address you're using
    });

    console.log('Burn successful:', response.data);
  } catch (error) {
    if (error.response) {
      console.error('Burn failed with error:', error.response.data);
    } else {
      console.error('Network or unknown error:', error.message);
    }
  }
};

burnToken();
```

### 2. Run the script

In your terminal, run:

```bash
node burn-token.js
```

If successful, you’ll see a response like:

```json
{
  "status": "success",
  "asset_id": "GOVT-BOND-UK-2025",
  "amount_burned": 500,
  "holder_wallet_address": "0xFEDCBA9876543210ABCD",
  "transaction_id": "TX-90002"
}
```

This confirms that the digital tokens were successfully burned.

---

## Common Errors & Troubleshooting

| Error Code | Meaning     | Likely Cause                             | Solution                                                          |
|------------|-------------|------------------------------------------|-------------------------------------------------------------------|
| 400        | Bad Request | Invalid input                            | Incorrect or missing parameters. Verify `asset_id`, `holder_wallet_address`, or `amount`. |
| 403        | Forbidden   | Not allowed                              | Wallet doesn’t own or control the tokens. Confirm ownership or permissions. |
| 409        | Conflict    | Insufficient balance                     | Holder wallet doesn’t have enough tokens. Check balance first.    |
| 404        | Not Found   | Token doesn’t exist                      | Token may already have been burned or never minted. Double check `asset_id`. |

Still having issues? Contact our **Support** team.

---

## What comes next?

- [How to Check a Token Balance](/mkdocs/examples/post-trade-automation/how-tos/how-to-check-a-token-balance/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-how-tos.md') }}

