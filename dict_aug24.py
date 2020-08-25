d=dict(joe=90,peter=80)
print(d)
d[0]='pns'
print(d)
print('peter' in d)
print(d.get('john',0))
print(d.get('joe',0))
print(d.keys())
print(list(d.keys()))
print(d.values())
print(list(d.values()))
n=dict([('lpn',10)])
print(n)
#multidimensional dictionary
m={'pns':[90,80,30],'rns':[50,70,90]}
print(m)
print(m['rns'])
print(m['rns'][2])
k={'pvv':{'maths':90,'sc':70},'gvv':{'eng':70,'hin':90}}
print(k['pvv'])
print(k['pvv']['sc'])
#defaultdictclass----it will not raise key error.It assigns default value for the key that does not exist
