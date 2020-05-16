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

XML_DIR = HOME + "\\appdata\\Roaming\\Avell\\WMI"
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

@dataclass
class Registry:
    component_name: str
    component_property: str
    qry: str
    data_list: list
    serial_number: str
    
    def query(self, qry):
        lista = []
        if qry != None:
            teste = wmi.WMI().query(qry)
            string = qry.replace(",", "").split(" ")
            for n in teste:
                lista.append(getattr(n, string[1]))
        else:
            lista = None
        return lista

    def get_value(self):
        lista = self.query(self.qry)
        # print(lista, self.qry, type(self.qry))
        return lista

    def insert_data_list(self):
        value_list = self.get_value()
        if value_list != None:
            i = 0
            for value in value_list:
                serial_number = self.serial_number
                attribute = self.component_property
                component = self.component_name
                i+=1
                if value == None:
                    value = False
                self.data_list.append({"SN":serial_number, "Componente":component, "Atributo":attribute, "Valor_Atributo":value})

@dataclass
class Payload:
    data_list: list
    endpoint: str
    xml_dir: str
    
    def get_data_list(self):
        from wmi_dict import WMI_DICT
        sn = get_serial_number()
        for key in WMI_DICT:
            j = 0
            for prop in WMI_DICT[key]:
                registry = Registry(key, prop["propriedade"], prop["query"], self.data_list, sn)
                print(j)
                registry.insert_data_list()
                j += 1
    
    def generate_xml(self):
        print(self.send_payload())
        create_xml_file(name = "Payload", dicio= self.data_list)

    def send_to_odoo(self, data_list):
        url = self.endpoint
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        common.version()
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        auth = ["avell-oca-db", 6, "p8W1UmTRz#q$", "wmi.data"]
        response = models.execute_kw(auth[0], auth[1], auth[2], auth[3], 'get_wmi_data', [data_list])
        return response

    def send_payload(self):
        payload = []
        for n in self.data_list:
            payload.append({"name":n["SN"], "age_attribute":n["Componente"] + " " + n["Atributo"], "age_attribute_value":n["Valor_Atributo"]})
        return self.send_to_odoo(payload)

data_list = []
payload = Payload(data_list, "https://odoo-oca.avell.com", XML_DIR)
payload.get_data_list()
payload.generate_xml()