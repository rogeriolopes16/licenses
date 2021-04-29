import urllib3
import csv
urllib3.disable_warnings()
from datetime import datetime

from modules.licensesGeneral import General
from modules.licenseWorkplace import Workplace
from modules.licenseTrend import Trend

list_tech,list_telecom,list_cscalgar, list_farming, list_granja, list_holding,list_compras, list_controladoria,list_financeiro, list_fiscal, \
list_gente_gestao, list_juridico, list_superintendencia, list_th, list_ti_pmo, list_projeto_erp, list_depart, list_base_licences_emp_desc, \
list_base_licences_emp, list_base_licences_csc_desc, list_base_licences_csc = General.general(None)

workplace_tech,workplace_telecom,workplace_csc_algar,workplace_farming,workplace_granja,workplace_holding,workplace_outros = Workplace.workplace(None)

trend_csc_algar,trend_farming,trend_granja,trend_holding,trend_outros = Trend.trend(None)

sysdate = datetime.now().strftime('%d/%m/%Y')
sysdateWSO2 = datetime.now().strftime('%m%Y')

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Inicio da atividade'))

#Plota no CSV de resposta
with open('C:/Automations/licenses/reports/result_licences_emp.csv', 'w', newline='',encoding='UTF8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["EMPRESA","LICENCA", "CONTRATADO","EM USO","SALDO","STATUS"])

    for n in list_base_licences_emp_desc:
        index = list_base_licences_emp_desc.index(n)
        if n == 'ALGAR_TECH':
            base_plot, list_plot, varWorkplace, varTrend = 'ALGAR TECH', list_tech, workplace_tech, 0

        elif n == 'ALGAR_TELECOM':
            base_plot, list_plot, varWorkplace, varTrend = 'ALGAR TELECOM', list_telecom, workplace_telecom, 0

        elif n == 'CSC_ALGAR':
            base_plot, list_plot, varWorkplace, varTrend = 'CSC ALGAR', list_cscalgar, workplace_csc_algar, trend_csc_algar

        elif n == 'FARMING':
            base_plot, list_plot, varWorkplace, varTrend = 'FARMING', list_farming, workplace_farming, trend_farming

        elif n == 'GRANJA':
            base_plot, list_plot, varWorkplace, varTrend = 'GRANJA', list_granja, workplace_granja, trend_granja

        elif n == 'HOLDING':
            base_plot, list_plot, varWorkplace, varTrend = 'HOLDING', list_holding, workplace_holding, trend_holding

        writer.writerow([base_plot, 'OFFICE 365', str(list_base_licences_emp[index][0]), str(list_plot[0]),str(int(list_base_licences_emp[index][0]) - list_plot[0]),str('OK' if (int(list_base_licences_emp[index][0])) >= list_plot[0] else 'FORA')])
        writer.writerow([base_plot, 'POWER BI', str(list_base_licences_emp[index][1]), str(list_plot[1]),str(int(list_base_licences_emp[index][1]) - list_plot[1]),str('OK' if (int(list_base_licences_emp[index][1])) >= list_plot[1] else 'FORA')])
        writer.writerow([base_plot, 'PROJECT PLAN 1', str(list_base_licences_emp[index][2]), str(list_plot[2]),str(int(list_base_licences_emp[index][2]) - list_plot[2]),str('OK' if (int(list_base_licences_emp[index][2])) >= list_plot[2] else 'FORA')])
        writer.writerow([base_plot, 'PROJECT PLAN 3', str(list_base_licences_emp[index][3]), str(list_plot[3]),str(int(list_base_licences_emp[index][3]) - list_plot[3]),str('OK' if (int(list_base_licences_emp[index][3])) >= list_plot[3] else 'FORA')])
        writer.writerow([base_plot, 'PROJECT PLAN 5', str(list_base_licences_emp[index][4]), str(list_plot[4]),str(int(list_base_licences_emp[index][4]) - list_plot[4]),str('OK' if (int(list_base_licences_emp[index][4])) >= list_plot[4] else 'FORA')])
        writer.writerow([base_plot, 'VISIO PLAN 2', str(list_base_licences_emp[index][5]), str(list_plot[5]),str(int(list_base_licences_emp[index][5]) - list_plot[5]),str('OK' if (int(list_base_licences_emp[index][5])) >= list_plot[5] else 'FORA')])
        writer.writerow([base_plot, 'WORKPLACE', str(list_base_licences_emp[index][6]), varWorkplace,str(int(list_base_licences_emp[index][6]) - varWorkplace),str('OK' if (int(list_base_licences_emp[index][6])) >= varWorkplace else 'FORA')])
        writer.writerow([base_plot, 'TREND', str(list_base_licences_emp[index][7]), varTrend,str(int(list_base_licences_emp[index][7]) - varTrend),str('OK' if (int(list_base_licences_emp[index][7])) >= varTrend else 'FORA')])
        
    if workplace_outros > 0:
        writer.writerow(['NÃO LOCALIZADO', 'WORKPLACE', 0, workplace_outros-1,0,'FORA'])
    if trend_outros > 0:
        writer.writerow(['NÃO LOCALIZADO', 'TREND', 0, trend_outros-1,0,'FORA'])


#Plota no CSV de resposta
with open('C:/Automations/licenses/reports/result_licences_cscalgar.csv', 'w', newline='',encoding='UTF8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["DEPARTAMENTO","LICENCA", "CONTRATADO","EM USO","SALDO","STATUS"])

    for n in list_base_licences_csc_desc:
        index = list_base_licences_csc_desc.index(n)
        if n == 'COMPRAS':
            base_plot, list_plot = 'COMPRAS', list_compras

        elif n == 'CONTROLADORIA':
            base_plot, list_plot = 'CONTROLADORIA', list_controladoria

        elif n == 'FINANCEIRO':
            base_plot, list_plot = 'FINANCEIRO', list_financeiro

        elif n == 'FISCAL':
            base_plot, list_plot = 'FISCAL', list_fiscal

        elif n == 'GENTE_GESTAO':
            base_plot, list_plot = 'GENTE GESTAO', list_gente_gestao

        elif n == 'JURIDICO':
            base_plot, list_plot = 'JURIDICO', list_juridico

        elif n == 'SUPERINTENDENCIA':
            base_plot, list_plot = 'SUPERINTENDENCIA', list_superintendencia

        elif n == 'TH':
            base_plot, list_plot = 'TH', list_th

        elif n == 'TI_PMO':
            base_plot, list_plot = 'TI_PMO', list_ti_pmo

        elif n == 'PROJETO_ERP':
            base_plot, list_plot = 'PROJETO_ERP', list_projeto_erp
            
        writer.writerow([base_plot,'OFFICE 365', str(list_base_licences_csc[index][0]),str(list_plot[0]), str(int(list_base_licences_csc[index][0]) - list_plot[0]),str('OK' if(int(list_base_licences_csc[index][0])) >= list_plot[0] else 'FORA')])
        writer.writerow([base_plot,'POWER BI', str(list_base_licences_csc[index][1]),str(list_plot[1]), str(int(list_base_licences_csc[index][1]) - list_plot[1]),str('OK' if(int(list_base_licences_csc[index][1])) >= list_plot[1] else 'FORA')])
        writer.writerow([base_plot,'PROJECT PLAN 1', str(list_base_licences_csc[index][2]),str(list_plot[2]), str(int(list_base_licences_csc[index][2]) - list_plot[2]),str('OK' if(int(list_base_licences_csc[index][2])) >= list_plot[2] else 'FORA')])
        writer.writerow([base_plot,'PROJECT PLAN 3', str(list_base_licences_csc[index][3]),str(list_plot[3]), str(int(list_base_licences_csc[index][3]) - list_plot[3]),str('OK' if(int(list_base_licences_csc[index][3])) >= list_plot[3] else 'FORA')])
        writer.writerow([base_plot,'PROJECT PLAN 5', str(list_base_licences_csc[index][4]),str(list_plot[4]), str(int(list_base_licences_csc[index][4]) - list_plot[4]),str('OK' if(int(list_base_licences_csc[index][4])) >= list_plot[4] else 'FORA')])
        writer.writerow([base_plot,'VISIO PLAN 2', str(list_base_licences_csc[index][5]),str(list_plot[5]), str(int(list_base_licences_csc[index][5]) - list_plot[5]),str('OK' if(int(list_base_licences_csc[index][5])) >= list_plot[5] else 'FORA')])

    if list_depart != []:
        list_depart = list(set(list_depart))
        writer.writerow(['NÃO LOCALIZADO', str(list_depart),0,0,0,0])

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Fim da atividade'))


