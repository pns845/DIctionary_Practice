db={'name':'Router1','IP':'1.1.1.1','username':'zframez','password':'zframez'}
print(db)
s=input("get data from user")
#print(db[s])
if s in db:
    print("key is"+str(s))
    print(db[s])
else:
    db[s]='new value'
print(db)

