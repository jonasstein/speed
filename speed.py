#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:01:16 2017

@author: Jonas Stein
"""

import datetime

def CreateLogfile():
    MyLogTime = datetime.datetime.now()
    MyFileName = MyLogTime.strftime("protokoll_%Y-%m-%dT%H_%M_%S.csv")
    f = open(MyFileName, 'w')
    f.write('"Nr.","Datum Uhrzeit","Dauer (s)","Geschwindigkeit (km/h)"\n')
    f.close
    return(MyFileName)

def LogThis(MyFileName, Text):
    f = open(MyFileName, 'a')
    f.write(Text + '\n')
    f.close


def measure(Distance_meter, FzID, MyFileName):
    Tstart = datetime.datetime.now()
    input("# (Messung läuft...)                              Stopp mit Return")
    Tstop = datetime.datetime.now()
    
    TdifferenceSeconds = (Tstop-Tstart).total_seconds()
    
    Speed_m_s = Distance_meter / TdifferenceSeconds
    Speed_km_h = Speed_m_s /1000 * 3600
    StrTimeStamp = Tstart.strftime("%Y-%m-%d %H:%M:%S")
 
    print('%03d, %s, %.6f,   %.1f'%(FzID,StrTimeStamp,TdifferenceSeconds,Speed_km_h))
    LogThis(MyFileName,'%03d,%s,%.6f,%.1f'%(FzID,StrTimeStamp,TdifferenceSeconds,Speed_km_h))

def main():
    FzID = 0

    MyLogFile = CreateLogfile()

    Distance_meter = 86.5
    print('Geschwindigkeitsmessung.\n Distanz zwischen Start- und Stoppsignal: %f (m)\n\n'%Distance_meter)
    print('Nr., Datum       Uhrzeit, Dauer (s),  Geschwindigkeit (km/h)')
    while True:
        KeyByUser = input("# (Standby)                                       Start mit Return, Quit mit q")
        if KeyByUser != '':
            print('Ende der Messserie.\n')
            print('Protokoll öffnen mit')
            print('libreoffice %s'%(MyLogFile))
            break
        elif KeyByUser == '':
            FzID = FzID + 1
            measure(Distance_meter, FzID, MyLogFile)
       

if __name__ == '__main__':
    main()
