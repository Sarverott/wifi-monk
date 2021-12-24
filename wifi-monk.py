# Sett Sarverott
# wifi-monk.py
# 2017
import json
import os
#from colorama import init
#init()
def wfMonk_profiler():
    profiles = []
    wlan_names = []
    data = os.popen("netsh wlan show profiles").readlines()
    #print('\x1B[91m######## SSID ########\033[0;0m')
    for profileName in data:
        if profileName[4:20] == "All User Profile":
            wlan_names.append(profileName[(profileName.find(": ") + 2):(len(profileName) - 1)])
            #print('   '+profileName[(profileName.find(": ") + 2):(len(profileName) - 1)])
    #print('\x1B[91m######## GETING DATA ########\033[0;0m')
    for wName in wlan_names:
        data_tmp = os.popen('netsh wlan show profiles name="'+wName+'" key=clear').readlines()
        obj_tmp = {}
        for wLine in data_tmp:
            if wLine[0:4] == "    ":
                x = wLine.find(" : ")
                obj_tmp[wLine[0:x].strip()] = wLine[x+2:len(wLine)].strip()
        profiles.append(obj_tmp)
        #print('   '+wName+" DONE")
    #print("\x1B[91m#### ALL PROFILES CAPTURED! ####\033[0;0m")
    return profiles
print(json.dumps(wfMonk_profiler()))
