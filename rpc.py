import requests
import urllib3
import json

'''
urllib3.disable_warnings()

headers = {'Content-Type': 'application/json'}
url = "https://localhost:8555/get_blockchain_state"
data = '{}'

# cert = ('C:/Users/Mark/.chia/standalone_wallet/config/ssl/full_node/private_full_node.crt', 'C:/Users/Mark/.chia/standalone_wallet/config/ssl/full_node/private_full_node.key')

# Change this to point to your keys
cert = ('C:/Users/Mark/.chia/mainnet/config/ssl/full_node/private_full_node.crt', 'C:/Users/Mark/.chia/mainnet/config/ssl/full_node/private_full_node.key')
# cert = ('ssl/full_node/private_full_node.crt', 'ssl/full_node/private_full_node.key')
# response = json.loads(requests.post(url, data=data, headers=headers, cert=cert, verify=False).text)
# print(json.dumps(response, indent=4, sort_keys=True))

url = "https://localhost:8555/get_network_space"

response = json.loads(requests.post(url, data=data, headers=headers, cert=cert, verify=False).text)
print(json.dumps(response, indent=4, sort_keys=True))

'''
