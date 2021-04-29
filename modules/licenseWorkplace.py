import csv

class Workplace():
    def __init__(self):
        pass

    def workplace(self):
        #Verifica licenças do Workplace
        workplace_tech,workplace_telecom, workplace_csc_algar, workplace_farming, workplace_granja, workplace_holding, workplace_outros = 0,0,0,0,0,0,0
        with open('C:/Automations/licenses/import/workplace.csv', newline='', encoding='utf8') as arquivo:
            linhas = csv.reader(arquivo, delimiter=';')
            for linha in linhas:
                if 'ALGARTECH' in linha[1].upper() or 'ACS' in linha[1].upper():
                    workplace_tech += 1
                elif 'ALGARTELECOM' in linha[1].upper() or 'INOVACAOBRAIN' in linha[1].upper() or 'ACCENTURE' in linha[1].upper():
                    workplace_telecom += 1
                elif 'CSCALGAR' in linha[1].upper():
                    workplace_csc_algar += 1
                elif 'FARMING' in linha[1].upper():
                    workplace_farming += 1
                elif 'GRANJAMARILEUSA' in linha[1].upper() or 'SPACEEMPREENDIMENTOS' in linha[1].upper():
                    workplace_granja += 1
                elif '@ALGAR.COM.BR' in linha[1].upper() or 'UNIALGAR' in linha[1].upper() or 'INSTITUTOALGAR' in linha[1].upper() or 'AVIATION' in linha[1].upper() or 'ALGARAGRO' in linha[1].upper():
                    workplace_holding += 1
                else:
                    workplace_outros += 1
        return (workplace_tech,workplace_telecom,workplace_csc_algar,workplace_farming,workplace_granja,workplace_holding,workplace_outros)