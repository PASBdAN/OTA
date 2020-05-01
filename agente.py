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

HOME = os.path.expanduser("~")
XML_DIR = HOME + "\\appdata\\Roaming\\Avell"
try:
    os.chdir(XML_DIR)
except:
    os.mkdir(XML_DIR)
    os.chdir(XML_DIR)

def get_serial_number():
    return str(wmi.WMI().Win32_Bios()[0].SerialNumber)

def create_xml_file(name = get_serial_number(), dicio = {}):
    xml = dicttoxml(dicio)
    dom = parseString(xml)
    with open(name + ".xml", "w+") as f:
        dom.writexml(writer = f, encoding = "iso-8859-1")

def create_json_file(name = get_serial_number(), dicio = {}): #cria uma pasta chamada JSON/ + SerialNumber da máquina caso não exista e muda de diretório. Ir para linha 19.
    with open(name + ".txt", "w+") as f:
        dump(dicio, f)
    with open(name + "_PrettyPrinting.txt", "w+") as f:
        dump(dicio, f, indent=4)

def time_stamp():
    obj = datetime.datetime.now()
    # 02/03/2020 16:55:03 -> exemplo do Odoo
    # \'%Y-%m-%d %H:%M:%S\'
    obj_str = obj.strftime("%Y-%m-%d %H:%M:%S")
    return obj_str

@dataclass
class Registry:
    component_name: str
    component_property: str
    qry: str
    data_list: list
    serial_number: str
    id_qry: str
    sn_qry: str
    
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
        return lista

    def get_devicesn(self):
        lista = self.query(self.sn_qry)
        return lista

    def get_value(self):
        lista = self.query(self.qry)
        return lista

    def insert_data_list(self):
        value_list = self.get_value()
        if value_list != None:
            i = 0
            for value in value_list:
                serial_number = self.serial_number
                attribute = self.component_property
                component = self.component_name
                try:
                    device_id = self.get_deviceid()[i]
                except:
                    device_id = False
                try:
                    device_sn = self.get_devicesn()[i]
                except:
                    device_sn = False
                if device_id == None:
                    device_id = False
                if device_sn == None:
                    device_sn = False
                i+=1
                if value == None:
                    value = False
                self.data_list.append({"SN":serial_number, "ID_Device":device_id, "ID_SerialNumber_Device":device_sn, "Componente":component, "Atributo":attribute, "Valor_Atributo":value})

@dataclass
class Payload:
    data_list: list
    endpoint: str
    xml_dir: str
    date_register: list

    def get_data_list(self):
        from cat_dict import CAT_DICT
        sn = get_serial_number()
        for key in CAT_DICT:
            id_query = CAT_DICT[key][0]["query"]
            sn_query = CAT_DICT[key][1]["query"]
            for prop in CAT_DICT[key]:
                registry = Registry(key, prop["propriedade"], prop["query"], self.data_list, sn, id_query, sn_query)
                registry.insert_data_list()
    
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
            #obj = datetime.datetime.now()
            #obj_str = obj.strftime("%Y%m%d%H%M%S")
            #file_name = obj_str + ".xml"
            #os.rename("Payload.xml", obj_str + ".xml")
            os.remove("Payload.xml")
            os.rename("Payload2.xml", "Payload.xml")
            return False

    def generate_old_xml(self, flag):
        #if flag == False:
        #    i = 1
        #    aux = 0
        #    while aux == 0:
        #        if os.path.isfile("Old_Payload" + str(i) + ".xml"):
        #            i += 1
        #        else:
        #            file_name = "Old_Payload" + str(i) + ".xml"
        #            aux += 1
        #    for attr in self.data_list:
        #        attr["date"] = time_stamp()
        #    create_xml_file(name = file_name.split(".")[0], dicio = self.data_list) 
            obj = datetime.datetime.now()
            obj_str = obj.strftime("%Y%m%d%H%M%S")
            file_name = obj_str + ".xml"
            create_xml_file(name = file_name.split(".")[0], dicio = self.data_list)

    def generate_xml(self):
        if os.path.isfile("Payload.xml"):
            create_xml_file(name = "Payload2", dicio = self.data_list)
            flag = self.compare_hash(["Payload.xml", "Payload2.xml"])
            self.generate_old_xml(flag)
        else:
            self.send_payload()
            create_xml_file(name = "Payload", dicio= self.data_list)
            self.generate_old_xml(False)

    def send_to_odoo(self, data_list):
        url = self.endpoint
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        common.version()
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        auth = ["avell-oca-db", 6, "p8W1UmTRz#q$", "agent.data"]
        response = models.execute_kw(auth[0], auth[1], auth[2], auth[3], 'get_agent_data', [data_list])
        return response

    def send_payload(self):
        payload = []
        for n in self.data_list:
            tempo = time_stamp()
            payload.append({"name":n["SN"], "age_deviceid":n["ID_Device"], "age_devicesn":n["ID_SerialNumber_Device"], "age_attribute":n["Componente"] + " " + n["Atributo"], "age_attribute_value":n["Valor_Atributo"], "age_register_date": tempo})
        return self.send_to_odoo(payload)

#odoo v13
data_list = []
date_list = []
payload = Payload(data_list, "https://odoo-oca.avell.com", XML_DIR, date_list)
payload.get_data_list()
payload.generate_xml()


