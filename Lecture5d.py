import pandas as pd
import plotly.express as px

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


#---------- Extract data from Uniswap Subgraph ----------

sample_transport=RequestsHTTPTransport(
    url='https://api.thegraph.com/subgraphs/name/aragon/aragon-tokens-xdai',
    verify=True,
    retries=3,
)
client = Client(
    transport=sample_transport
)
query = gql('''
query {
    miniMeTokens(where:{name: "morphosis"}) {
        name
        totalSupply
        holders {
            address
            balance
        }
    }
}
''')
response = client.execute(query)
print(response)

print(response['miniMeTokens'][0]['holders'])



holders = []
for i in response['miniMeTokens'][0]['holders']:
    holders.append([
        i['address'],
        i['balance'],
     ])

print(holders)
print()
print()
df = pd.DataFrame(holders)
print(df)

df[1] = df[1].astype(float)/1000000000000000000
df.columns=['Holder', 'Amount']
print()
print()
print(df)

fig = px.bar(df, x='Holder', y='Amount')
fig.show()


