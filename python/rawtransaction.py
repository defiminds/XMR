from monero.wallet import Wallet
import json

# Connect to the Monero wallet
wallet = Wallet(port=18082)

# Specify the transaction inputs, outputs, and fees
inputs = [{"txid": "0000000000000000000000000000000000000000000000000000000000000000", "vout": 0}]
outputs = [{"address": "ADDRESS_1", "amount": 100000000000}, {"address": "ADDRESS_2", "amount": 50000000000}]
fees = 10000000000

# Create the raw transaction
raw_tx = wallet.transfer_split(inputs=inputs, outputs=outputs, fee=fees, relay=False)

# Save the raw transaction as a file
with open("raw_tx.json", "w") as f:
    json.dump(raw_tx, f)

print("Raw transaction saved to raw_tx.json")
