---
title: 'How to Mint a Token'
description: 'Step-by-step guide on how to mint a token using ABC-Lab/''s API.'
pubDate: 'Jun 12 2025'
---

{{ include_file('snippets/example-disclaimer.md') }}

<hr/>
<span style="font-variant: small-caps; font-size: 0.8rem; color: grey; "> 
    ← <a href="/mkdocs/examples/post-trade-automation/token-lifecycle/lifecycle-in-practice/lip-balance-check/"> token lifecycle in practice: 4. balance check</a>  |   how-to's 
</span>
<hr/>

# How to Mint a Token

## Scenario

In this how-to, you’ll learn how to mint (create) digital tokens representing a real-world asset; in this case, a UK government bond. Once minted, the tokens will be assigned to a wallet address, representing ownership of that asset in the digital system.

---

## Prerequisites

Before you begin, make sure you have:

- Node.js and npm installed on your system  
- A basic working knowledge of JavaScript or Node.js  
- Access to the ABC-Labs API base URL: `https://api.abc-labs.com`  
- A test or real wallet address (e.g., `0xA1B2C3D4E5F6...`)  

> Refer to our **Getting Started Guide** if you don’t have access to our testing system.

---

## Steps

### 1. Create a new Node.js project (if needed)

Open your terminal and run:

```bash
mkdir labs-demo
cd labs-demo
npm init -y
npm install axios
```

### 2. Create a file called `mint-token.js`

Inside that file, add the following code:

```javascript
const axios = require('axios');

const mintToken = async () => {
  try {
    const response = await axios.post('https://api.abc-labs.com/api/tokens/mint', {
      asset_id: 'GOVT-BOND-UK-2025',
      amount: 1000,
      recipient_wallet_address: '0xA1B2C3D4E5F6A7B8C9D0' // replace with the address you're using
    });

    console.log('Token minted successfully:', response.data);
  } catch (error) {
    if (error.response) {
      console.error('Minting failed with error:', error.response.data);
    } else {
      console.error('Network or unknown error:', error.message);
    }
  }
};

mintToken();
```

### 3. Run the script

In your terminal, run:

```bash
node mint-token.js
```

If successful, you’ll see a response like:

```json
{
  "status": "success",
  "token_id": "TOKEN-12345",
  "asset_id": "GOVT-BOND-UK-2025",
  "amount": 1000,
  "assigned_to": "0xA1B2C3D4E5F6A7B8C9D0"
}
```

This confirms that the digital tokens were created and allocated.

---

### Common Errors & Troubleshooting

| Error Code | Meaning       | Likely Cause              | Solution                                                   |
|------------|---------------|---------------------------|------------------------------------------------------------|
| 400        | Bad Request   | Invalid input             | Double-check `asset_id`, `amount`, and `wallet_address`    |
| 401        | Unauthorised  | Not allowed               | Missing or invalid API key                                |
| 409        | Conflict      | Token already minted      | Check if you’ve already minted this asset                 |

Still having issues? Contact our **Support** team.

---

## What comes next?

- [How to Transfer Tokens](/mkdocs/examples/post-trade-automation/how-tos/how-to-transfer-tokens/)

## Related Reading

{{ include_file('snippets/snippy-related-reading-how-tos.md') }}

