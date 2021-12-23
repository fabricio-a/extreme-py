# -*- coding: utf-8 -*-

import os
import sys
import exsh

def writeLog(log):
    exsh.clicmd('create log message {}'.format(log))

def main():
    OUI = { #Objeto com o OUI (Identificador do fabricante). Sera utilizado para filtrar o mac-address e associar a porta as respectivas VLANs. 
        'D8:84:66' : 'MAC OUI EXTREME AP MODELO 3715e',
        'DC:B8:08' : 'MAC OUI EXTREME AP MODELO 3915i',
        '94:9B:2C' : 'MAC OUI EXTREME AP MODELO 3915e',
    }

    VLANS = [1000,1001,1002] #Vetor com as vlans que serao configuradas apos o evento ocorrer

    eventType = sys.argv[1].upper()
    eventPort = sys.argv[2]

    try {
        eventMAC = sys.argv[3]
        if 'EVENT.MAC' in eventMAC : raise ValueError('Nenhum MAC foi passado como argumento') 

    } except {
        eventMAC = exsh.clicmd('show fdb ports {}'.format(eventPort), capture=True)
        eventMAC = eventMAC[eventMAC.find(':')-2:eventMAC.find(':')+15]
    }

    eventOUI = eventMAC[0:8].upper()
    if eventMAC:
        try:
            eventModel = OUI[eventOUI]

            if(eventType == 'DEVICE-DETECT'):
                exsh.clicmd('disable netlogin ports {} dot1x web-based mac'.format(eventPort))
                for vlan in VLANS:
                    exsh.clicmd('configure vlan {} add port {} tagged'.format(vlan, eventPort))

            elif(eventType == 'DEVICE-UNDETECT'):
                exsh.clicmd('enable netlogin ports {} dot1x web-based mac'.format(eventPort))
                for vlan in VLANS:
                    exsh.clicmd('configure vlan {} delete ports {}'.format(vlan, eventPort))
        
        except:
            pass

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
