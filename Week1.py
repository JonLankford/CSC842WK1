import os
import sys
import subprocess
import re


def lookup():
    cmd = 'nslookup'
    records = subprocess.Popen([cmd, 'amazon.com'], stdout=subprocess.PIPE)
    output = str(records.communicate())

    strings = output.split('\\n')
    iplist = strings[5:-2]
    ipstring = ' '.join(str(e) for e in iplist)
    iptocheck = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ipstring).group()
    return iptocheck


def check(ipcheck):
    cmd = '/home/kali/IP-Tracer'
    o = subprocess.Popen(['echo', 'kali'], stdout=subprocess.PIPE)
    p = subprocess.Popen(['sudo', '-S'] + [cmd, 'ip-tracer-t' + ipcheck], stdin=o.stdout, stdout=subprocess.PIPE)
    out = str(p.communicate())
    print(out)

    '''cmd2 = '/ip-trace'
    recs = subprocess.Popen([cmd2, '-t 139.167.168.255'], stdout=subprocess.PIPE)
    output = str(recs.communicate())
    print(output)
    strings = output.split('\\n')
    iplist = strings[5:-2]
    ipstring = ' '.join(str(e) for e in iplist)
    iptocheck = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ipstring).group()
    print(ipcheck)'''


if __name__ == '__main__':
    iptocheck = lookup()
    check(iptocheck)
