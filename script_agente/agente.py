import wmi
from dataclasses import dataclass, field
from typing import Any
import datetime
import os
from dicttoxml import dicttoxml
from json import load, loads, dump, dumps
from xml.dom.minidom import parseString
import xmlrpc.client
import hashlib
import subprocess

'''
import psutil
# PID = os.getpid()
# print(PID)
# print(psutil.Process(PID).name())
PID = os.getpid()
i = 0
for process in wmi.WMI().Win32_Process ():
    if psutil.Process(PID).name() == process.Name:
        i += 1
    if i > 2:
        os._exit(0)

#HOME = os.path.expanduser("~")
#XML_DIR = HOME + "\\appdata\\Roaming\\Avell"
XML_DIR = "C:\\ProgramData\\Avell"
INSTALL_DIR = "C:\\Program Files (x86)\\Avell Support Application"

try:
    os.chdir(XML_DIR)
except:
    os.mkdir(XML_DIR)
    os.chdir(XML_DIR)
'''
XML_DIR = "C:\\ProgramData\\Avell"
def get_serial_number():
    sn = str(wmi.WMI().Win32_Bios()[0].SerialNumber)
    return sn

def create_xml_file(name = get_serial_number(), dicio = {}):
    xml = dicttoxml(dicio)
    dom = parseString(xml)
    with open(name + ".xml", "w+") as f:
        dom.writexml(writer = f, encoding = "iso-8859-1")

def time_stamp():
    obj = datetime.datetime.now()
    # 02/03/2020 16:55:03 -> exemplo do Odoo
    # \'%Y-%m-%d %H:%M:%S\'
    obj_str = obj.strftime("%Y-%m-%d %H:%M:%S")
    return obj_str

'''
from cryptography.fernet import Fernet
import configparser

def decrypt_odoo_auth(userb:str, passwdb:str, dbb:str):
    user_key = b'fQq1raRWvH8-qAh5AMPwAIRh8BlVgy48ZMKEKo5nXKs='
    f = Fernet(user_key)
    user = userb.encode()
    decrypted_user = f.decrypt(user)

    passwd_key = b'i3qW9jz-mE0nwyLTgjNPkCSBhjeWyrvjZWGU-TJCJOA='
    f = Fernet(passwd_key)
    passwd = passwdb.encode()
    decrypted_passwd = f.decrypt(passwd)

    db_key = b'fFjSP0AQ3D_ZE7O3vOOPE1QtzlytT6S5nvRIG-Z2tKw='
    f = Fernet(db_key)
    db = dbb.encode()
    decrypted_db = f.decrypt(db)

    return decrypted_user, decrypted_passwd, decrypted_db

def decrypt_file(filename:str, key):
    cat_dict_key = key
    with open(filename, "rb") as fl:
        data = fl.read()
    f = Fernet(cat_dict_key)
    decrypted_file = f.decrypt(data)
    # with open("{}.ini".format(name), "wb") as fl:
    #     fl.write(decrypted_file)
    return decrypted_file.decode("utf-8")
'''

@dataclass
class Registry:
    component_name: str
    component_property: str
    qry: str # query para buscar o valor referente a aquele registro
    data_list: list # variável que recebe o resultado das queries
    serial_number: str # define o serial number da máquina
    id_qry: str # define a query de busca no WMI do identificador geral do componente/software (DeviceID)
    sn_qry: str # define a query de busca no WMI do identificador único do componente/software (SerialNumberID)
    reg_type: str # define se o registro é de software ou hardware
    
    def query(self, qry):
        lista = []
        if qry != None:
            string = qry.replace(",", "").split(" ")
            for n in wmi.WMI().query(qry):
                #lista.append(getattr(n, string[1]))
                value = getattr(n, string[1])
                i = 2
                while i < len(string):
                    if string[i] == "From":
                        break
                    value = value + "_" + getattr(n, string[i])
                    i += 1
                lista.append(value)
        else:
            lista = None
        return lista

    def get_deviceid(self):
        lista = self.query(self.id_qry)
        if (lista != None and lista != []) and (self.id_qry != None and self.id_qry != []):
            if self.id_qry.split()[3] == "Win32_NetworkAdapter":
                i = 0
                while(i < len(lista)):
                    if lista[i] != None:
                        if lista[i].split('\\')[0] != 'PCI':
                            lista.pop(i)
                            i -= 1
                    i += 1
            print("\n PEGOU O {} DO {}: {}".format(self.id_qry.split()[1], self.id_qry.split()[3], lista))
        else:
            lista = []
            print("\n NÃO PEGOU DADOS")
        # print(lista, "getting deviceid")
        if lista != None and lista != []:
            if self.id_qry.split()[1] == "PNPDeviceID" or self.id_qry.split()[1] == "PnPDeviceID" or self.id_qry.split()[1] == "PnPDeviceId" or self.id_qry.split()[1] == "PnPDeviceID," or self.id_qry.split()[1] == "PNPDeviceID,":
                if self.id_qry.split()[4] == "Win32_Keyboard":
                    valor = lista[0].split("_")
                    print(valor)
                    valor2 = valor[0].split("\\")
                    print(valor2)
                    del valor2[-1]
                    valor3 = "\\".join(valor2)
                    print(valor3)
                    lista[0] = valor3 + "_" + valor[1]
                    print("\n PEGOU O DEVICEID DO {}: {}".format(self.id_qry.split()[3], lista[0]))

                elif type(lista[0]) == str:
                    aux = lista[0].split("\\")
                    del aux[-1]
                    aux2 = "\\".join(aux)
                    lista[0] = aux2
                    print("\n PEGOU O DEVICEID DO {}: {}".format(self.id_qry.split()[3], lista[0]))
        return lista

    def get_devicesn(self):
        lista = self.query(self.sn_qry)
        print("\n PEGOU O DEVICESN DO {}".format(self.sn_qry.split()[3]))
        return lista

    def get_value(self):
        '''
        aux = self.get_deviceid()
        print(aux, self.qry)
        if (aux != None and aux != []) and (self.qry != None and self.qry != []):
            if aux[0] != None:
                if self.qry.split()[3] == "Win32_NetworkAdapter" and aux[0].split("\\")[0] == "PCI":
                    lista = self.query(self.qry)
                elif self.qry.split()[3] != "Win32_NetworkAdapter":
                    lista = self.query(self.qry)
                else:
                    lista = []
                print("\n PEGOU O {} DO {}: {}".format(self.qry.split()[1], self.qry.split()[3], lista))
            else:
                lista = []
        else:
            lista = []
            print("\n NÃO PEGOU DADOS")
        '''
        lista = self.query(self.qry)
        # print(lista, "getting registry value"
        if lista != None and lista != []:
            aux = self.qry.split()
            if self.qry != None and (aux[1] == "PNPDeviceID" or aux[1] == "PnPDeviceID" or aux[1] == "PnPDeviceId" or aux[1] == "PnPDeviceID," or aux[1] == "PNPDeviceID,"):
                try:
                    if aux[4] == "Win32_Keyboard":
                        print("\n INICIOU A COLETA DE {} DO {}".format(self.qry.split()[1],self.qry.split()[3]))
                        valor = lista[0].split("_")
                        print(valor)
                        valor2 = valor[0].split("\\")
                        print(valor2)
                        del valor2[-1]
                        valor3 = "\\".join(valor2)
                        print(valor3)
                        lista[0] = valor3 + "_" + valor[1]
                        print("\n PEGOU O {} DO {}: {}".format(self.qry.split()[1],self.qry.split()[4], lista[0]))
                    elif type(lista[0]) == str:
                        print("\n INICIOU A COLETA DE {} DO {}".format(self.qry.split()[1],self.qry.split()[3]))
                        aux = lista[0].split("\\")
                        del aux[-1]
                        aux2 = "\\".join(aux)
                        lista[0] = aux2
                        print("\n PEGOU O {} DO {}: {}".format(self.qry.split()[1],self.qry.split()[3], lista[0]))
                except:
                    pass
        return lista

    def insert_data_list(self):
        value_list = self.get_value()
        if value_list != None:
            i = 0
            for value in value_list:
                serial_number = self.serial_number
                attribute = self.component_property
                registry_type = self.reg_type
                component = self.component_name
                try:
                    device_id = self.get_deviceid()[i]
                    if device_id == None:
                        device_id = False
                except:
                    device_id = False
                try:
                    device_sn = self.get_devicesn()[i]
                    if device_sn == None:
                        device_sn = False
                except:
                    device_sn = False
                i+=1
                if value == None:
                    value = False
                self.data_list.append({"SN":serial_number, "ID_Device":device_id, "Registry_type": registry_type, "ID_SerialNumber_Device":device_sn, "Componente":component, "Atributo":attribute, "Valor_Atributo":value})
                if component == "Wireless" and device_id == False:
                    self.data_list.pop(-1)

@dataclass
class Payload:
    data_list: list
    # xml_dir: str

    def get_data_list(self):
        print("\n\nINICIALIZANDO COLETA DOS DADOS...")
        with open("cat_dict.json", encoding="UTF-8") as f:
            CAT_DICT = load(f)
        # CAT_DICT = loads(decrypt_file("C:\\Program Files (x86)\\Avell Support Application\\cat_dict", b'qFIrLCHqw4X_9kq_0XkHQ9kGdGWW93ArTyTPonOLwyc='))
        with open("driver_dict.json", encoding='utf-8') as f:
            DRIVER_DICT = load(f)
        # DRIVER_DICT = loads(decrypt_file("C:\\Program Files (x86)\\Avell Support Application\\driver_dict", b'bcoCpMZdi25K0IgJCLe8pkY1o4MYH7A1kJaXmgv8fI0='))
        sn = get_serial_number()
        for key in CAT_DICT:
            print("\n\nCOLETANDO: {}".format(key))
            id_query = CAT_DICT[key][0]["query"]
            # print("got id query of {}: {}".format(key, id_query))
            sn_query = CAT_DICT[key][1]["query"]
            for prop in CAT_DICT[key]:
                registry = Registry(key, prop["propriedade"], prop["query"], self.data_list, sn, id_query, sn_query, "Hardware")
                registry.insert_data_list()
            aux = registry.get_deviceid()
            if aux != None and aux != []:
                HardWareID = aux[0]
            else:
                HardWareID = None
            for prop in DRIVER_DICT[key]:
                if HardWareID != None:
                    registry = Registry("{} Driver".format(key), prop, "Select {} From Win32_PnPSignedDriver Where HardWareID LIKE '%{}%'".format(prop, HardWareID), self.data_list, sn, id_query, "Select DriverVersion From Win32_PnPSignedDriver Where HardWareID LIKE '%{}%'".format(HardWareID), "Driver")
                    registry.insert_data_list()
                # for n in DRIVER_DICT:
                #     print(n)

    def hash_bytestr_iter(self, bytesiter, hasher, ashexstr=False):
        for block in bytesiter:
            hasher.update(block)
        return hasher.hexdigest() if ashexstr else hasher.digest()

    def file_as_blockiter(self, afile, blocksize=65536):
        with afile:
            block = afile.read(blocksize)
            while len(block) > 0:
                yield block
                block = afile.read(blocksize)

    def compare_hash(self, fnametuple):
        if (self.hash_bytestr_iter(self.file_as_blockiter(open(fnametuple[0], "rb")), hashlib.md5()) == self.hash_bytestr_iter(self.file_as_blockiter(open(fnametuple[1], "rb")), hashlib.md5())):
            os.remove("Payload.xml")
            os.rename("Payload2.xml", "Payload.xml")
            return True
        else:
            self.send_payload()
            os.remove("Payload.xml")
            os.rename("Payload2.xml", "Payload.xml")
            return False

    def generate_old_xml(self, flag):
        if not(flag):
            obj = datetime.datetime.now()
            obj_str = obj.strftime("%Y%m%d%H%M%S")
            file_name = obj_str + ".xml"
            create_xml_file(name = file_name.split(".")[0], dicio = self.data_list)

    # É POSSÍVEL FAZER UMA ÚNICA FUNÇÃO
    def generate_xml(self):
        print("\n\nGERANDO O XML DO PAYLOAD\n")
        if os.path.isfile("Payload.xml"):
            create_xml_file(name = "Payload2", dicio = self.data_list)
            flag = self.compare_hash(["Payload.xml", "Payload2.xml"])
            self.generate_old_xml(flag)
            response = [True, [], True]
        else:
            # response = self.send_payload()
            response = [True, [], True]
            create_xml_file(name = "Payload", dicio= self.data_list)
            self.generate_old_xml(False)
        return response

    def send_to_odoo(self, data_list):
        # config = configparser.ConfigParser()
        # configfilename = "{}\\config".format(INSTALL_DIR)
        # config.read_string(decrypt_file(configfilename, b'RyDXGlrqcgqwlxxpxlP7-Ut3i4bi0_xJs2x43nFg_3s='))
        # user, passwd, db = decrypt_odoo_auth(config["params"]["param1"], config["params"]["param2"], config["params"]["param3"])

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format("https://helpdesk.avell.com"))
        common.version()
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format("https://helpdesk.avell.com"))
        auth = ["helpdesk", 7, "p8W1UmTRz#q$", "agent.data"]
        print("\n\nENVIANDO REQUISIÇÃO AO ODOO\n\n")
        response = models.execute_kw(auth[0], auth[1], auth[2], auth[3], "get_agent_data", [data_list])
        return response

    def send_payload(self):
        payload = []
        for n in self.data_list:
            payload.append({"name":str(n["SN"]).strip(), "age_type": n["Registry_type"], "age_deviceid":str(n["ID_Device"]).strip(), "age_devicesn":str(n["ID_SerialNumber_Device"]).strip(), "age_component":n["Componente"], "age_property":n["Atributo"], "age_property_value":str(n["Valor_Atributo"]).strip()})
        #try:
        #    r = self.send_to_odoo(payload)
        #except:
        #    r = False
        # return r
        return self.send_to_odoo(payload)

#odoo v13
data_list = []
payload = Payload(data_list)#, XML_DIR)
payload.get_data_list()
response = payload.generate_xml()

print("\nFINALIZADO:\n{}\n\n".format(response))


with open("teste_prod.vbs", "+w") as f:
    if response[1]:
        # for n in response[1]:
            # f.write('msgbox(" ERROR: " & vbCrLf & vbCrLf & vbCrLf & "{} : {}" & vbCrLf)'.format(n[0], n[1]))
        os.system("taskkill /im Tray.exe")
        f.write('msgbox("ERROR: " & vbCrLf & vbCrLf & "{}" & vbCrLf)'.format(response[1]))     
    else:
        os.system("taskkill /im Tray.exe")
        f.write('msgbox("OK")')
subprocess.call("cmd /c teste_prod.vbs", shell=True, timeout=None)
#aux = "C:\\Program Files (x86)\\Avell Support Application\\uninstallbyname.exe"
#subprocess.Popen(aux, shell = True)
# with open("uninstallbyname.vbs", "+w") as f:
#     f.write('Set installer = CreateObject("WindowsInstaller.Installer")\nDim RunShell\nSet RunShell = WScript.CreateObject ("WScript.Shell")\nOn Error Resume Next\nFor Each product In installer.ProductsEx("", "", 7)\nproductcode = product.ProductCode\nname = product.InstallProperty("ProductName")\nif name="Avell Support Application" then\nRunShell.run "msiexec.exe /x " & productcode\nend if\nNext')
# subprocess.call("cmd /c uninstallbyname.vbs", shell=True, timeout=None)
# os.system('rd /s /q "C:\\ProgramData\\Avell"')
# \nSet installer = CreateObject("WindowsInstaller.Installer")\nDim RunShell\nSet RunShell = WScript.CreateObject ("WScript.Shell")\nOn Error Resume Next\nFor Each product In installer.ProductsEx("", "", 7)\nproductcode = product.ProductCode\nname = product.InstallProperty("ProductName")\nif name="Avell Support Application" then\nRunShell.run "msiexec.exe /x " & productcode\nend if\nNext




