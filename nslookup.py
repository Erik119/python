import os

def nslookup(url):
    stream = os.popen('nslookup ' + url)
    flag = False
    ip = None
    for line in stream:
        if url in line:flag = True
        if flag and 'Address' in line:
            ip = line.split()[-1]
    return(ip)

print(nslookup('ams.dslam.acc.oam.kpn.org'))


