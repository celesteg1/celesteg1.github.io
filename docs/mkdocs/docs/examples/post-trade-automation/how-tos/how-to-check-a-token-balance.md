---
title: 'How to Check a Token Balance'
description: 'Step-by-step guide on how to check a token balance using ABC-Lab/''s API.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/how-tos/how-to-burn-tokens"> how to burn tokens </a>  |   how-to's 
</span>
<hr/>

# How to Check a Token Balance

## Scenario

You want to confirm how many tokens a wallet currently holds for a specific asset. This might be useful before transferring, burning, or reconciling positions.

## Prerequisites

Before you begin, make sure you have:

- Node.js and npm installed on your system  
- A basic working knowledge of JavaScript or Node.js  
- Access to the ABC-Labs API base URL: `https://api.abc-labs.com`  
- A valid `asset_id`  
- A valid `wallet_address` to check  

> Refer to our **Getting Started Guide** if you don’t have access to our testing system.

---

## Steps

### 1. Create a file called `check-balance.js`

Inside that file, add the following code:

```javascript
const axios = require('axios');

const checkBalance = async () => {
  const asset_id = 'GOVT-BOND-UK-2025';
  const wallet_address = '0xFEDCBA9876543210ABCD';  // replace with the wallet_address you're using

  try {
    const response = await axios.get('https://api.abc-labs.com/api/tokens/balance', {
      params: {
        asset_id: asset_id,
        wallet_address: wallet_address
      }
    });

    console.log(`Balance for wallet ${wallet_address}:`, response.data);
  } catch (error) {
    if (error.response) {
      console.error('Error fetching balance:', error.response.data);
    } else {
      console.error('Network or unknown error:', error.message);
    }
  }
};

checkBalance();
```

### 2. Run the script

In your terminal, run:

```bash
node check-balance.js
```

If successful, you’ll see a response like:

```json
{
  "asset_id": "GOVT-BOND-UK-2025",
  "wallet_address": "0xFEDCBA9876543210ABCD",
  "balance": 500
}
```
This confirms that you’ve successfully retrieved the balance.

---

## Common Errors & Troubleshooting

| Error Code | Meaning     | Likely Cause                       | Solution                                                       |
|------------|-------------|------------------------------------|----------------------------------------------------------------|
| 400        | Bad Request | Invalid input                      | Missing or malformed query parameters. Double-check `asset_id` and `wallet_address`. |
| 403        | Forbidden   | Access denied                      | API key/token missing or unauthorised. Check auth headers or permissions. |
| 404        | Not Found   | No tokens found                    | Wallet never received tokens for this asset. Confirm that tokens were minted or transferred. |

Still having issues? Contact our **Support** team.

---

## What comes next?

- [API Overview](/mkdocs/examples/post-trade-automation/references/api/api-overview/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-how-tos.md') }}

