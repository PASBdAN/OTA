import wmi

WMI_DICT = {
    "Processador": {"queries":[]},
    "Tela": {"queries":[]},
    "Memória": {"queries":[]},
    "Placa de Vídeo": {"queries":[]},
    "Armazenamento": {"queries":[]},
    "Teclado": {"queries":[]},
    "Mouses": {"queries":[]},
    "Bateria": {"queries":[]},
    "Placa Mãe": {"queries":[]},
    "Bios": {"queries":[]},
    "Sistema Operacional": {"queries":[]},
    "Adaptador de Rede": {"queries":[]},
}

list_of_classes = ["Win32_Processor", "Win32_DesktopMonitor", "Win32_PhysicalMemory", "Win32_VideoController", "Win32_DiskDrive", "Win32_Keyboard", "Win32_PointingDevice", "Win32_Battery", "Win32_BaseBoard", "Win32_BIOS", "Win32_OperatingSystem", "Win32_NetworkAdapter"]
i = 0
for device in WMI_DICT:
    n = wmi.WMI().query("Select * From " + list_of_classes[i])[0]
    #for n in wmi.WMI().query("Select * From " + list_of_classes[i]):
    properties_string = ""
    property_list = list(n._properties)
    j = 0
    while j < len(property_list):
        if j == len(property_list) - 1:
            properties_string += "{}".format(property_list[j])
        else:
            properties_string += "{}, ".format(property_list[j])
        j += 1
    # print(device ,properties_string.split(", "))
    WMI_DICT[device]["properties"] = properties_string
    WMI_DICT[device]["queries"].append("Select {} From {}".format(properties_string, list_of_classes[i]))
    i += 1
# print(WMI_DICT)

WMI_DICT["Chipset"] = {"queries":[]}
n = wmi.WMI().query("Select * From Win32_PnPEntity")[0]
properties_string = ""
property_list = list(n._properties)
j = 0
while j < len(property_list):
    if j == len(property_list) - 1:
        properties_string += "{}".format(property_list[j])
    else:
        properties_string += "{}, ".format(property_list[j])
    j += 1
WMI_DICT["Chipset"]["properties"] = properties_string
WMI_DICT["Chipset"]["queries"].append("Select {} From Win32_PnPEntity WHERE Caption LIKE '%Series Chipset Family%' OR Caption LIKE '%HM470%' OR Caption LIKE '%AMD%SMBus%'".format(properties_string))

#WMI_DICT["PNP System"] = {"queries":[]}
#n = wmi.WMI().query("Select * From Win32_PnPEntity Where PNPClass Like '%System%'")[0]
#properties_string = ""
#property_list = list(n._properties)
#j = 0
#while j < len(property_list):
#    if j == len(property_list) - 1:
#        properties_string += "{}".format(property_list[j])
#    else:
#        properties_string += "{}, ".format(property_list[j])
#    j += 1
#WMI_DICT["PNP System"]["properties"] = properties_string
#WMI_DICT["PNP System"]["queries"].append("Select {} From Win32_PnPEntity Where PNPClass Like '%System%'".format(properties_string))


WMI_DICT["Camera"] = {"queries":[]}
n = wmi.WMI().query("Select * From Win32_PnPEntity")[0]
properties_string = ""
property_list = list(n._properties)
j = 0
while j < len(property_list):
    if j == len(property_list) - 1:
        properties_string += "{}".format(property_list[j])
    else:
        properties_string += "{}, ".format(property_list[j])
    j += 1
WMI_DICT["Camera"]["properties"] = properties_string
WMI_DICT["Camera"]["queries"].append("Select {} From Win32_PnPEntity Where PNPClass Like '%Camera%'".format(properties_string))

'''
# print(WMI_DICT)
for n in WMI_DICT:
    for m in WMI_DICT[n]:
        if type(WMI_DICT[n][m]) == str:
            print(WMI_DICT[n][m])
            print("\n")
        for o in WMI_DICT[n][m]:
            if type(WMI_DICT[n][m]) != str:
                print(o)
'''


