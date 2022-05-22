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
    print(ipcheck)


if __name__ == '__main__':
    iptocheck = lookup()
    check(iptocheck)
