import threading
from tracemalloc import stop
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/JCNCAmqFfaWQ9WQrW143reOVrnRg1YfY"))
private_key = "ee9cec01ff03c0adea731d7c5a84f7b412bfd062b9ff35126520b3eb3d5ff258"
pub_key ="0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3"

recipient_pub_key = "0xeBDff495c36a451022b6EC69FDa0fbC1627966f5"
def loop():
    while True:
        balance = w3.eth.get_balance(pub_key)
        print()
        print(balance)
        gasPrice = w3.toWei('1100', 'gwei')
        gasLimit = 21000
        nonce = w3.eth.getTransactionCount(pub_key)
        tx = {
            'chainId': 3,
            'nonce': nonce,
            'to': recipient_pub_key,
            'value': balance-gasLimit*gasPrice,
            'gas': gasLimit,
            'gasPrice': gasPrice
        }

        try:
         if balance > 0:
            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(w3.toHex(tx_hash))
        except:
            print("insufficient funds")

threading.Thread(target=loop, daemon=True).start()
input('Press Enter to exit.')
