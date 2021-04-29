import csv
from modules.getDataBase import GetDataBase

### Index Listas ###
#[officesubscription, power_bi_pro, projectessentials, projectprofessional, projectpremium, visioclient]

#Listas por empresa
list_tech = [0,0,0,0,0,0]
list_telecom = [0,0,0,0,0,0]
list_cscalgar = [0,0,0,0,0,0]
list_farming = [0,0,0,0,0,0]
list_granja = [0,0,0,0,0,0]
list_holding = [0,0,0,0,0,0]

#Listas por area CSC Algar
list_compras = [0,0,0,0,0,0]
list_controladoria = [0,0,0,0,0,0]
list_financeiro = [0,0,0,0,0,0]
list_fiscal = [0,0,0,0,0,0]
list_gente_gestao = [0,0,0,0,0,0]
list_juridico = [0,0,0,0,0,0]
list_superintendencia = [0,0,0,0,0,0]
list_th = [0,0,0,0,0,0]
list_ti_pmo = [0,0,0,0,0,0]
list_projeto_erp = [0,0,0,0,0,0]
list_depart=[]

base_licences_emp = open('C:/Automations/licenses/config/base_licences_emp.txt', 'r').readlines()
list_base_licences_emp = []
list_base_licences_emp_desc = []
for n in base_licences_emp:
    list_base_licences_emp_desc.append((n[:n.find('=')]).strip())
    list_base_licences_emp.append((n[n.find('=') + 1:]).rstrip().strip('[]').split(','))
list_base_licences_emp.pop(0)
list_base_licences_emp_desc.pop(0)

base_licences_csc = open('C:/Automations/licenses/config/base_licences_cscalgar.txt', 'r').readlines()
list_base_licences_csc = []
list_base_licences_csc_desc = []
for n in base_licences_csc:
    list_base_licences_csc_desc.append((n[:n.find('=')]).strip())
    list_base_licences_csc.append((n[n.find('=') + 1:]).rstrip().strip('[]').split(','))
list_base_licences_csc.pop(0)
list_base_licences_csc_desc.pop(0)

base_licences_csc_dep = open('C:/Automations/licenses/config/departments_cscalgar.txt', 'r').readlines()
list_base_licences_csc_dep = []
for n in base_licences_csc_dep:
    list_base_licences_csc_dep.append(n.strip())

base_terceiros_csc = open('C:/Automations/licenses/config/departments_terceiros.txt', 'r').readlines()
list_base_terceiros_csc = []
for n in base_terceiros_csc:
    list_base_terceiros_csc.append((n.upper()[n.find('=') + 1:]).rstrip().strip('[]').split(','))




ativos_tabelao = GetDataBase.tabelao(None)

class General():
    def __init__(self):
        pass

    def general(self):
        with open('C:/Automations/licenses/import/geral.csv', newline='', encoding='utf-16') as arquivo:
            linhas = csv.reader(arquivo, delimiter=',')
            for linha in linhas:
                valida = 0
                if linha[1].upper() == 'TRUE':

                    #Avaliar licensas Office
                    if 'OFFICESUBSCRIPTION' in linha[2].upper():
                        if 'ALGARTECH' in linha[3].upper():
                            list_tech[0] += 1
                        elif 'ALGARTELECOM' in linha[3].upper():
                            list_telecom[0] += 1
                        elif 'CSCALGAR' in linha[3].upper():
                            list_cscalgar[0] += 1
                            #verifica licencas por departamentos do CSC Algar
                            for tabelao in ativos_tabelao:
                                if linha[3].upper() == tabelao[1] or linha[0].upper() == tabelao[0]:
                                    valida = 1
                                    if tabelao[2] in list_base_licences_csc_dep[0]:
                                        list_compras[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[1]:
                                        list_controladoria[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[2]:
                                        list_financeiro[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[3]:
                                        list_fiscal[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[4]:
                                        list_gente_gestao[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[5]:
                                        list_juridico[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[6]:
                                        list_superintendencia[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[7]:
                                        list_th[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[8]:
                                        list_ti_pmo[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[9]:
                                        list_projeto_erp[0] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[10]:
                                        pass
                                    else:
                                        list_depart.append(tabelao[2])

                            #verifica licencas de terceiros por departamentos do CSC Algar
                            if linha[3].upper() in list_base_terceiros_csc[0]:
                                list_compras[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[1]:
                                list_controladoria[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[2]:
                                list_financeiro[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[3]:
                                list_fiscal[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[4]:
                                list_gente_gestao[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[5]:
                                list_juridico[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[6]:
                                list_superintendencia[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[7]:
                                list_th[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[8]:
                                list_ti_pmo[0] += 1
                                valida = 1
                            elif linha[3].upper() in list_base_terceiros_csc[9]:
                                list_projeto_erp[0] += 1
                                valida = 1
                            else:
                                pass

                            list_depart.append(linha[0].upper()) if valida == 0 else False
                        elif 'FARMING' in linha[3].upper():
                            list_farming[0] += 1
                        elif 'GRANJAMARILEUSA' in linha[3].upper() or 'SPACEEMPREENDIMENTOS' in linha[3].upper():
                            list_granja[0] += 1
                        elif '@ALGAR.COM.BR' in linha[3].upper() or 'AGRO' in linha[3].upper():
                            list_holding[0] += 1

                    #Avaliar licensas Power BI
                    if 'POWER_BI_PRO' in linha[2].upper():
                        if 'ALGARTECH' in linha[3].upper():
                            list_tech[1] += 1
                        elif 'ALGARTELECOM' in linha[3].upper():
                            list_telecom[1] += 1
                        elif 'CSCALGAR' in linha[3].upper():
                            list_cscalgar[1] += 1
                            #verifica licencas por departamentos do CSC Algar
                            for tabelao in ativos_tabelao:
                                if linha[3].upper() == tabelao[1] or linha[0].upper() == tabelao[0]:
                                    if tabelao[2] in list_base_licences_csc_dep[0]:
                                        list_compras[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[1]:
                                        list_controladoria[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[2]:
                                        list_financeiro[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[3]:
                                        list_fiscal[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[4]:
                                        list_gente_gestao[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[5]:
                                        list_juridico[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[6]:
                                        list_superintendencia[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[7]:
                                        list_th[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[8]:
                                        list_ti_pmo[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[9]:
                                        list_projeto_erp[1] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[10]:
                                        pass
                                    else:
                                        list_depart.append(tabelao[2])

                        elif '@ALGAR.COM.BR' in linha[3].upper():
                            list_holding[1] += 1

                    #Avaliar licensas Project Essetials
                    if 'PROJECTESSENTIALS' in linha[2].upper():
                        if 'ALGARTECH' in linha[3].upper():
                            list_tech[2] += 1
                        elif 'ALGARTELECOM' in linha[3].upper():
                            list_telecom[2] += 1
                        elif 'CSCALGAR' in linha[3].upper():
                            list_cscalgar[2] += 1
                            # verifica licencas por departamentos do CSC Algar
                            for tabelao in ativos_tabelao:
                                if linha[3].upper() == tabelao[1] or linha[0].upper() == tabelao[0]:
                                    if tabelao[2] in list_base_licences_csc_dep[0]:
                                        list_compras[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[1]:
                                        list_controladoria[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[2]:
                                        list_financeiro[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[3]:
                                        list_fiscal[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[4]:
                                        list_gente_gestao[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[5]:
                                        list_juridico[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[6]:
                                        list_superintendencia[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[7]:
                                        list_th[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[8]:
                                        list_ti_pmo[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[9]:
                                        list_projeto_erp[2] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[10]:
                                        pass
                                    else:
                                        list_depart.append(tabelao[2])

                    #Avaliar licensas Project Professional
                    if 'PROJECTPROFESSIONAL' in linha[2].upper():
                        if 'ALGARTECH' in linha[3].upper():
                            list_tech[3] += 1
                        elif 'ALGARTELECOM' in linha[3].upper():
                            list_telecom[3] += 1
                        elif 'CSCALGAR' in linha[3].upper():
                            list_cscalgar[3] += 1
                            # verifica licencas por departamentos do CSC Algar
                            for tabelao in ativos_tabelao:
                                if linha[3].upper() == tabelao[1] or linha[0].upper() == tabelao[0]:
                                    if tabelao[2] in list_base_licences_csc_dep[0]:
                                        list_compras[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[1]:
                                        list_controladoria[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[2]:
                                        list_financeiro[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[3]:
                                        list_fiscal[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[4]:
                                        list_gente_gestao[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[5]:
                                        list_juridico[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[6]:
                                        list_superintendencia[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[7]:
                                        list_th[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[8]:
                                        list_ti_pmo[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[9]:
                                        list_projeto_erp[3] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[10]:
                                        pass
                                    else:
                                        list_depart.append(tabelao[2])
                        elif 'GRANJAMARILEUSA' in linha[3].upper() or 'SPACEEMPREENDIMENTOS' in linha[3].upper():
                            list_cscalgar[3] += 1

                    #Avaliar licensas Project Premium
                    if 'PROJECTPREMIUM' in linha[2].upper():
                        if 'ALGARTECH' in linha[3].upper():
                            list_tech[4] += 1
                        elif 'ALGARTELECOM' in linha[3].upper():
                            list_telecom[4] += 1
                        elif 'CSCALGAR' in linha[3].upper():
                            list_cscalgar[4] += 1
                            # verifica licencas por departamentos do CSC Algar
                            for tabelao in ativos_tabelao:
                                if linha[3].upper() == tabelao[1] or linha[0].upper() == tabelao[0]:
                                    if tabelao[2] in list_base_licences_csc_dep[0]:
                                        list_compras[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[1]:
                                        list_controladoria[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[2]:
                                        list_financeiro[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[3]:
                                        list_fiscal[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[4]:
                                        list_gente_gestao[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[5]:
                                        list_juridico[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[6]:
                                        list_superintendencia[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[7]:
                                        list_th[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[8]:
                                        list_ti_pmo[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[9]:
                                        list_projeto_erp[4] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[10]:
                                        pass
                                    else:
                                        list_depart.append(tabelao[2])

                    #Avaliar licensas Visio
                    if 'VISIOCLIENT' in linha[2].upper():
                        if 'ALGARTECH' in linha[3].upper():
                            list_tech[5] += 1
                        elif 'ALGARTELECOM' in linha[3].upper():
                            list_telecom[5] += 1
                        elif 'CSCALGAR' in linha[3].upper():
                            list_cscalgar[5] += 1
                            # verifica licencas por departamentos do CSC Algar
                            for tabelao in ativos_tabelao:
                                if linha[3].upper() == tabelao[1] or linha[0].upper() == tabelao[0]:
                                    if tabelao[2] in list_base_licences_csc_dep[0]:
                                        list_compras[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[1]:
                                        list_controladoria[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[2]:
                                        list_financeiro[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[3]:
                                        list_fiscal[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[4]:
                                        list_gente_gestao[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[5]:
                                        list_juridico[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[6]:
                                        list_superintendencia[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[7]:
                                        list_th[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[8]:
                                        list_ti_pmo[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[9]:
                                        list_projeto_erp[5] += 1
                                    elif tabelao[2] in list_base_licences_csc_dep[10]:
                                        pass
                                    else:
                                        list_depart.append(tabelao[2])
            return (list_tech,list_telecom,list_cscalgar, list_farming, list_granja, list_holding,list_compras, list_controladoria,list_financeiro, list_fiscal,
                    list_gente_gestao, list_juridico, list_superintendencia, list_th, list_ti_pmo, list_projeto_erp, list_depart, list_base_licences_emp_desc,
                    list_base_licences_emp, list_base_licences_csc_desc, list_base_licences_csc)