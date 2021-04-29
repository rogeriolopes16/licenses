import csv

class Trend():
    def __init__(self):
        pass

    def trend(self):
        #Verifica licenças do trend
        trend_csc_algar, trend_farming, trend_granja, trend_holding, trend_outros = 0,0,0,0,0
        with open('C:/Automations/licenses/import/trend.csv', newline='', encoding='utf8') as arquivo:
            linhas = csv.reader(arquivo, delimiter=';')
            for linha in linhas:
                if 'CSC' in linha[1].upper() or 'HYP' in linha[1].upper():
                    trend_csc_algar += 1
                elif 'FAR' in linha[1].upper():
                    trend_farming += 1
                elif 'GRM' in linha[1].upper() or 'SPACE' in linha[1].upper() or 'SPC' in linha[1].upper():
                    trend_granja += 1
                elif 'EST' in linha[1].upper() or 'HLD' in linha[1].upper() or 'UNI' in linha[1].upper() or 'AGRO' in linha[1].upper() :
                    trend_holding += 1
                else:
                    trend_outros += 1
        return (trend_csc_algar,trend_farming,trend_granja,trend_holding,trend_outros)