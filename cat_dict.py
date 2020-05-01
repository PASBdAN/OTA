
# {"propriedade": None, "query": None, "valor": None}
#import wmi
#for n in wmi.WMI().Win32_PointingDevice():
#    print(n)

CAT_DICT = {
    "Processador": [
        {"propriedade": "DeviceID", "query": "Select ProcessorId From Win32_Processor", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Modelo", "query": "Select Caption From Win32_Processor", "valor": None},
        {"propriedade": "Memória Cache", "query": "Select L3CacheSize From Win32_Processor", "valor": None},
        {"propriedade": "Frequência", "query": "Select MaxClockSpeed From Win32_Processor", "valor": None},
        {"propriedade": "Temperatura Média", "query": None, "valor": None}, #
    ],
    "Chipset": [ #Series Chipset Family
        {"propriedade": "DeviceID", "query":"Select PNPDeviceID From Win32_PNPEntity WHERE Caption LIKE '%Series Chipset Family%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Modelo", "query":"Select Caption From Win32_PNPEntity WHERE Caption LIKE '%chipset%'", "valor": None},
    ],
    "Tela": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_DesktopMonitor WHERE MonitorType LIKE '%PnP%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Marca", "query": "Select PnPDeviceID From Win32_DesktopMonitor WHERE MonitorType LIKE '%PnP%'", "valor": None},
        {"propriedade": "Polegadas", "query": None, "valor": None}, #
        {"propriedade": "Resolução", "query": None, "valor": None}, #
        {"propriedade": "Taxa de Atualização de Frame", "query": "Select RefreshRate From Win32_DisplayControllerConfiguration", "valor": None},
        {"propriedade": "IPS", "query": None, "valor": None}, #
        {"propriedade": "NTSC", "query": None, "valor": None}, #
        {"propriedade": "Papel Fotográfico", "query": None, "valor": None}, #
        {"propriedade": "Contraste", "query": None, "valor": None}, #
        {"propriedade": "Brilho", "query": None, "valor": None}, #
        {"propriedade": "Tempo de Resposta do Monitor", "query": None, "valor": None}, #
    ],
    "Memória SLT1": [
        {"propriedade": "DeviceID", "query": "Select PartNumber From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select PartNumber, SerialNumber From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None},
        {"propriedade": "Capacidade", "query": "Select Capacity From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None},
        {"propriedade": "Frequência", "query": "Select Speed From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None},
        {"propriedade": "Tipo", "query": None, "valor": None}, #
        {"propriedade": "Marca", "query": "Select Manufacturer From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None},
    ],
    #"Memória SLT2": [
    #    {"propriedade": "DeviceID", "query": "Select InstallDate From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None}, #
    #    {"propriedade": "DeviceID_SN", "query": "Select InstallDate From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None}, #
    #    {"propriedade": "Capacidade", "query": "Select InstallDate From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None}, #
    #    {"propriedade": "Frequência", "query": "Select InstallDate From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None}, #
    #    {"propriedade": "Tipo", "query": None, "valor": None}, #
    #    {"propriedade": "Marca", "query": "Select InstallDate From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelA-DIMM0%'", "valor": None}, #
    #],
    "Memória SLT2": [
        {"propriedade": "DeviceID", "query": "Select PartNumber From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelB-DIMM0%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select PartNumber, SerialNumber From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelB-DIMM0%'", "valor": None},
        {"propriedade": "Capacidade", "query": "Select Capacity From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelB-DIMM0%'", "valor": None},
        {"propriedade": "Frequência", "query": "Select Speed From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelB-DIMM0%'", "valor": None},
        {"propriedade": "Tipo", "query": None, "valor": None}, #
        {"propriedade": "Marca", "query": "Select Manufacturer From Win32_PhysicalMemory WHERE DeviceLocator LIKE '%ChannelB-DIMM0%'", "valor": None},        
    ],
    "Placa de Vídeo Nvidia": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_VideoController WHERE Caption LIKE '%nvidia%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Modelo", "query": "Select Caption From Win32_VideoController WHERE Caption LIKE '%nvidia%'", "valor": None},
        {"propriedade": "Memória Dedicada", "query": "Select Caption From Win32_VideoController WHERE Caption LIKE '%nvidia%'", "valor": None},
        {"propriedade": "Bits de Cor", "query": None, "valor": None}, #
        {"propriedade": "Tipo da Memória", "query": None, "valor": None}, #
        {"propriedade": "Temperatura Média", "query": None, "valor": None}, #
        {"propriedade": "FPS", "query": None, "valor": None}, #
    ],
    "Placa de Vídeo Intel": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_VideoController WHERE Caption LIKE '%intel%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Modelo", "query": "Select Caption From Win32_VideoController WHERE Caption LIKE '%intel%'", "valor": None},
        {"propriedade": "Memória Dedicada", "query": "Select AdapterRAM From Win32_VideoController WHERE Caption LIKE '%intel%'", "valor": None},
    ],
    "Armazenamento SSD SLT1": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '0'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select SerialNumber From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '0'", "valor": None},
        {"propriedade": "Capacidade", "query": "Select Size From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '0'", "valor": None},
        {"propriedade": "Modelo", "query": "Select Caption From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '0'", "valor": None},
        {"propriedade": "Marca", "query": None, "valor": None}, #
        {"propriedade": "Formato", "query": "Select InterfaceType From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '0'", "valor": None},
        {"propriedade": "Taxa de Leitura", "query": None, "valor": None}, #
        {"propriedade": "Taxa de Gravação", "query": None, "valor": None}, #
    ],
    "Armazenamento SSD SLT2": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '1'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select SerialNumber From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '1'", "valor": None},
        {"propriedade": "Capacidade", "query": "Select Size From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '1'", "valor": None},
        {"propriedade": "Modelo", "query": "Select Caption From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '1'", "valor": None},
        {"propriedade": "Marca", "query": None, "valor": None}, #
        {"propriedade": "Formato", "query": "Select InterfaceType From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '1'", "valor": None},
        {"propriedade": "Taxa de Leitura", "query": None, "valor": None}, #
        {"propriedade": "Taxa de Gravação", "query": None, "valor": None}, #
    ],
    "Armazenamento SSD SLT3": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '2'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select SerialNumber From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '2'", "valor": None},
        {"propriedade": "Capacidade", "query": "Select Size From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '2'", "valor": None},
        {"propriedade": "Modelo", "query": "Select Caption From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '2'", "valor": None},
        {"propriedade": "Marca", "query": None, "valor": None}, #
        {"propriedade": "Formato", "query": "Select InterfaceType From Win32_DiskDrive WHERE SCSIPort != '0' AND Index = '2'", "valor": None},
        {"propriedade": "Taxa de Leitura", "query": None, "valor": None}, #
        {"propriedade": "Taxa de Gravação", "query": None, "valor": None}, #
    ],
    "Armazenamento HD SLT1": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_DiskDrive WHERE Index = '0' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select SerialNumber From Win32_DiskDrive WHERE Index = '0' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "Capacidade", "query": "Select Size From Win32_DiskDrive WHERE Index = '0' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "Rotação", "query": None, "valor": None}, #
        {"propriedade": "Espessura", "query": None, "valor": None}, #
        {"propriedade": "Marca", "query": None, "valor": None}, #
    ],
    "Armazenamento HD SLT2": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_DiskDrive WHERE Index = '1' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select SerialNumber From Win32_DiskDrive WHERE Index = '1' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "Capacidade", "query": "Select Size From Win32_DiskDrive WHERE Index = '1' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "Rotação", "query": None, "valor": None}, #
        {"propriedade": "Espessura", "query": None, "valor": None}, #
        {"propriedade": "Marca", "query": None, "valor": None}, #
    ],
    "Armazenamento HD SLT3": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_DiskDrive WHERE Index = '2' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select SerialNumber From Win32_DiskDrive WHERE Index = '2' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "Capacidade", "query": "Select Size From Win32_DiskDrive WHERE Index = '2' AND NOT InterfaceType LIKE '%SCSI%'", "valor": None},
        {"propriedade": "Rotação", "query": None, "valor": None}, #
        {"propriedade": "Espessura", "query": None, "valor": None}, #
        {"propriedade": "Marca", "query": None, "valor": None}, #
    ],
    "Sistema de Som": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_SoundDevice WHERE Caption LIKE '%Realtek%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Marca", "query": "Select Manufacturer From Win32_SoundDevice WHERE Caption LIKE '%Realtek%'", "valor": None},
        {"propriedade": "Software de Controle", "query": None, "valor": None}, #
        {"propriedade": "Potência de Caixa", "query": None, "valor": None}, #
        {"propriedade": "Nome", "query": "Select ProductName From Win32_SoundDevice WHERE Caption LIKE '%Realtek%'", "valor": None},
    ],
    "Teclado": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID, Layout From Win32_Keyboard WHERE PNPDeviceID LIKE 'ACPI\\MSFT%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Referência", "query": "Select Layout From Win32_Keyboard WHERE PNPDeviceID LIKE 'ACPI\\MSFT%'", "valor": None},
        {"propriedade": "Tipo", "query": None, "valor": None}, #
        {"propriedade": "Iluminação", "query": None, "valor": None}, #
        {"propriedade": "Controlador de Iluminação", "query": None, "valor": None}, #
    ],
    "Touchpad": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_PointingDevice WHERE PNPDeviceID LIKE 'HID\\UNI%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Software", "query": None, "valor": None}, #
        {"propriedade": "Tecnologia", "query": None, "valor": None}, #
    ],
    "Portas e Conexões": [
        {"propriedade": "Tipos de Portas", "query": None, "valor": None}, #
        {"propriedade": "HDMI", "query": None, "valor": None}, #
        {"propriedade": "Display", "query": None, "valor": None}, #
        {"propriedade": "USB 1", "query": None, "valor": None}, #
        {"propriedade": "USB 2", "query": None, "valor": None}, #
        {"propriedade": "USB 3", "query": None, "valor": None}, #
        {"propriedade": "Conexão 1", "query": None, "valor": None}, #
        {"propriedade": "Conexão 2", "query": None, "valor": None}, #
        {"propriedade": "RJ", "query": None, "valor": None}, #
    ],
    "Leitor de Cartão": [
        {"propriedade": "DeviceID", "query": None, "valor": None}, #
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Tipo de Cartões", "query": None, "valor": None}, #
    ],
    "Wireless": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_NetworkAdapter WHERE Caption LIKE '%Wireless%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": "Select GUID From Win32_NetworkAdapter WHERE Caption LIKE '%Wireless%'", "valor": None},
        {"propriedade": "Modelo", "query": "Select Caption From Win32_NetworkAdapter WHERE Caption LIKE '%Wireless%'", "valor": None},
        #{"propriedade": "Frequência", "query": "Select MaxSpeed From Win32_NetworkAdapter WHERE Caption LIKE '%Wireless%'", "valor": None},
        {"propriedade": "Velocidade Máxima", "query": None, "valor": None}, #
        {"propriedade": "Versão Bluetooth", "query": None, "valor": None}, #
    ],
    "Webcam": [
        {"propriedade": "DeviceID", "query": "Select PnPDeviceID From Win32_PNPEntity WHERE PNPClass LIKE '%Camera%'", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Qualidade", "query": None, "valor": None}, #
    ],
    "Fonte": [
        {"propriedade": "Modelo", "query": None, "valor": None}, #
        {"propriedade": "Peso", "query": None, "valor": None}, #
        {"propriedade": "Tensão", "query": None, "valor": None}, #
        {"propriedade": "Corrente de Saída", "query": None, "valor": None}, #
        {"propriedade": "Potência", "query": None, "valor": None}, #
    ],
    "Bateria": [
        {"propriedade": "DeviceID", "query": "Select DeviceID From Win32_Battery", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
    #    {"propriedade": "Tensão", "query": "Select DesignCapacity From Win32_Battery", "valor": None},
        {"propriedade": "Consumo", "query": None, "valor": None}, #
        {"propriedade": "Modelo", "query": None, "valor": None}, #
        {"propriedade": "Peso", "query": None, "valor": None}, #
    ],
    "Dimensão": [
        {"propriedade": "Dimensões", "query": None, "valor": None}, #
        {"propriedade": "Peso", "query": None, "valor": None}, #
    ],
    "Placa Mãe": [
        {"propriedade": "Modelo", "query": "Select Product From Win32_BaseBoard", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Fabricante", "query": "Select Manufacturer From Win32_BaseBoard", "valor": None},
        {"propriedade": "Versão", "query": "Select SerialNumber From Win32_BaseBoard", "valor": None},
    ],
    "Bios": [
        {"propriedade": "DeviceID", "query": "Select SoftwareElementID From Win32_BIOS", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Data", "query": "Select ReleaseDate From Win32_BIOS", "valor": None},
    ],
    "Sistema Operacional": [
        {"propriedade": "Edição", "query": "Select Caption From Win32_OperatingSystem", "valor": None},
        {"propriedade": "DeviceID_SN", "query": None, "valor": None}, #
        {"propriedade": "Versão de compilação", "query": "Select Version From Win32_OperatingSystem", "valor": None},
    ],
}
'''
qry = CAT_DICT["Memória SLT1"][0]["query"]
print(qry)
string = qry.replace(",", "").split(" ")
print(string)
i = 1
while i < len(string):
    if string[i] == "From":
        break
    print(string[i])
    i += 1
'''