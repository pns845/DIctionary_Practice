import sys
db_1 = {1: {'Interface':'Ethernet0', 'IP':'1.1.1.1' , 'Status':'up' },
        2: {'Interface':'Ethernet1', 'IP':'2.2.2.2' , 'Status': 'down'},
        3: {'Interface': 'Serial0', 'IP': '3.3.3.3', 'Status': 'up'},
        4: {'Interface': 'Serial1', 'IP': '4.4.4.4', 'Status': 'up'}}

for key in db_1:
    if db_1[key]['Status']== 'up':
        print("the interface is "+db_1[key]['Interface']+"the ip is"+db_1[key]['IP'])