import pandas as pd

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


#---------- Extract data from Uniswap Subgraph ----------

sample_transport=RequestsHTTPTransport(
    url='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2',
    verify=True,
    retries=3,
)
client = Client(
    transport=sample_transport
)
query = gql('''
query {
    pairs (first: 5) {
    token0 {
      symbol
    }
    token1 {
      symbol
    }
  }
}
''')
response1 = client.execute(query)
print(response1)
print(response1['pairs'])



pairs = []
for i in response1['pairs']:
    pairs.append([
        i['token0']['symbol'],
        i['token1']['symbol'],
     ])

print(pairs)

df = pd.DataFrame(pairs)
print(df)


query = gql('''
query {
      pairs (first: 10, where: {volumeUSD_gt: "100000" }) 
    {
    volumeUSD
    token0 {
      symbol
    }
    token1 {
      symbol
    }
  }
}
''')
response2 = client.execute(query)

print()
print()


pairs = []
for i in response2['pairs']:
    pairs.append([
        i['token0']['symbol'],
        i['token1']['symbol'],
        i['volumeUSD']
     ])



df = pd.DataFrame(pairs)
print(df)