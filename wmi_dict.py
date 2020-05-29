import wmi

WMI_DICT = {
    "Processador": [],
    "Tela": [],
    "Memória": [],
    "Placa de Vídeo": [],
    "Armazenamento": [],
    "Teclado": [],
    "Mouses": [],
    "Bateria": [],
    "Placa Mãe": [],
    "Bios": [],
    "Sistema Operacional": [],
}

list_of_classes = ["Win32_Processor", "Win32_DesktopMonitor", "Win32_PhysicalMemory", "Win32_VideoController", "Win32_DiskDrive", "Win32_Keyboard", "Win32_PointingDevice", "Win32_Battery", "Win32_BaseBoard", "Win32_BIOS", "Win32_OperatingSystem"]
i = 0
for device in WMI_DICT:
    for n in wmi.WMI().query("Select * From " + list_of_classes[i]):
        for m in n._properties:
            WMI_DICT[device].append({"propriedade": m, "query": "Select " + m + " From " + list_of_classes[i], "value": None})

    i += 1

WMI_DICT["Chipset"] = []
for n in wmi.WMI().query("Select * From Win32_PnPEntity Where Caption Like '%Chipset%'"):
    for m in n._properties:
        WMI_DICT["Chipset"].append({"propriedade": m, "query": "Select " + m + " From Win32_PNPEntity Where Caption Like '%Chipset%'", "value": None})

for n in wmi.WMI().query("Select * From Win32_DisplayControllerConfiguration"):
    for m in n._properties:
        WMI_DICT["Tela"].append({"propriedade": m, "query": "Select " + m + " From Win32_DisplayControllerConfiguration", "value": None})

# print(WMI_DICT)
