hosts={}
hosts['slacrr1'] = '1.1.1.1'
hosts['slacrr2'] = '2.1.1.1'
hosts['slacrr3'] = '3.1.1.1'

for host, ip in hosts.items():
    print(host, ip)

for item in hosts.items():
    print(*item)    