import os
import sys
import exsh

OUI = {
    '00:08:02' : 'Compaq',
    '00:0c:29' : 'VMWare',
    '00:0d:60' : 'IBM',
    '00:12:17' : 'Cisco-Linksys',
    '00:13:e8' : 'Intel',
    '00:15:c5' : 'Dell',
    '00:1e:c9' : 'Dell',
    '84:2b:2b' : 'Dell',
    'a4:ba:db' : 'Dell',
    '02:60:8c' : '3Com',
    '00:01:30' : 'Extreme Networks',
    '00:04:96' : 'Extreme Networks',
    'D8:84:66' : 'Extreme Networks',
    '00:01:F4' : 'Enterasys Networks',
    '00:11:88' : 'Enterasys Networks',
    '00:1F:45' : 'Enterasys Networks',
    '20:B3:99' : 'Enterasys Networks',
    '00:e0:34' : 'Cisco',
    '00:e0:52' : 'Foundry Networks',
    '00:1a:a0' : 'Dell',
    '00:50:79' : 'VPC - GNS3'
}

def writeLog(log):
    exsh.clicmd('create log message "{}"'.format(log))

argv = ['','','']
for i in range(3):
    try:
        argv[0] = sys.argv[0]
    except:
        argv[0] = 'none'

def main():
    writeLog('LOG ARGS -> '+str(sys.argv))

    if(sys.argv[1] == 'DEVICE-DETECT'):
        exsh.clicmd('configure vlan '+vlans+' add port '+sys.argv[2]+' tagged')
    elif(sys.argv[1] == 'DEVICE-UNDETECT'):
        exsh.clicmd('configure vlan SW delete ports '+sys.argv[2])

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass