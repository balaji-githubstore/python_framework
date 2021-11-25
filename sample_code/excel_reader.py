import pandas

# df = pandas.read_excel('D:\\OrangeHrmData.xlsx', sheet_name="VerifyValidCredentialTemplate") # can also index sheet by name or fetch all sheets
df = pandas.read_excel('../data/OrangeHrmData.xlsx', sheet_name="VerifyValidCredentialTemplate")
print(df)
print(type(df))

mylist = df['username'].tolist()
print(mylist)

# row read
print(df.loc[0].tolist())

# total index
print(df.index)

for i in df.index:
    print(df.loc[i].tolist())

# list of list
rows = []

for i in df.index:
    rows.append(df.loc[i].tolist())

print(rows)
