import xmlrpc.client

serial_number = [x for x in range(3)]
component_id = [x for x in range(3)]
#print(serial_number, component_id)

payload = [
    {"type":"header", "url":"https://odoo-dev.avell.com" , "comment":"Importando dados do WMI para Odoo"}, # 1

    {"type":"database", "name": "producao12", "user": "teste_oto", "password": "teste"}, # 2

    {"type":"table", "name":"x_registros_prontuario", "operation":"create", "data": [ #"operation" vai mudar
        {"x_studio_prontuario_numero_serie": serial_number[0], "x_studio_reg_pront_id_componente": component_id[0]}, #Cada elemento de "data" é um registro
        {"x_studio_prontuario_numero_serie": serial_number[1], "x_studio_reg_pront_id_componente": component_id[1]},
        {"x_studio_prontuario_numero_serie": serial_number[2], "x_studio_reg_pront_id_componente": component_id[2]}
    ]}
]

'''
Análise do payload acima:
    1 - Cada elemento da lista especifica uma chamada de função na API que recebe o payload.
    2 - A chave "Type" especifica qual método deve ser executado com as demais chaves do dicionário como parâmetros do método.
    PERGUNTAS:
    1 - Em que formato o Odoo trata datas (string, date object, etc)? Se for string, qual a expressão (dia / mês / ano, dia - mês - ano, etc)
'''

#url = "https://odoo-dev.avell.com"

#db = "producao12"
#user = "teste_oto"
#password = "teste"

def send_to_odoo(payload):

    for element in payload:
        if element["type"] == "header":
            url = element["url"]
            print(element["comment"])

        if element["type"] == "database":
            db = element["name"]
            user = element["user"]
            password = element["password"]

        if element["type"] == "table":
            table = element["name"]
            operation = element["operation"]
            data = element["data"]

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    common.version()

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    uid = common.authenticate(db, user, password, {})

    teste = models.execute_kw(db, uid, password, table, operation, data)

    print(teste)

#insert_odoo(payload)

auth = ["producao12", 58, "teste", "x_registros_prontuario"]

models.execute.kw(auth[0], auth[1], auth[2], auth[3], 'create', [vals])