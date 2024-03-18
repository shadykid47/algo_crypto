import json
import os
from base58 import b58decode
from requests import Request, Session

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from signer import Signer

live_url = 'https://api-evm.orderly.org'



base_url = "https://testnet-api-evm.orderly.org"

Wallet_Address = 'ad'
Account_ = 'dfadsf'
Orderly_API_Key = 'sdfsd'
Orderly_API_Secret = 'sdafadf'

orderly_account_id = Account_

key = b58decode(Orderly_API_Secret.split(':')[1])
orderly_key = Ed25519PrivateKey.from_private_bytes(key)

session = Session()
signer = Signer(orderly_account_id, orderly_key)

req = signer.sign_request(
    Request(
        "POST",
        "%s/v1/order" % live_url,
        json={
            "symbol": "PERP_ETH_USDC",
            "order_type": "MARKET",
            "order_quantity": 0.01,
            "side": "BUY",
        },
    )
)
res = session.send(req)
response = json.loads(res.text)

auth_data = response
print(auth_data)