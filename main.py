import pandas as pd
from funcs import *

pctrl_df = pd.read_csv('consultoriaSC.csv')
reev_df = pd.DataFrame({'Nome':[],
                       'Sobrenome':[],
                       'E-mail':[],
                       "Empresa":[],
                       "Cargo":[],
                       "Telefone":[],
                       "Celular":[],
                       "Endereço":[],
                       "URL":[],
                       "Linkedin":[],
                       "Variável 1":[],
                       "Variável 2":[],
                       "Variável 3":[],
                       "Grupo":[],
                       "Origem(dropdown)":[],
                       "Segmento(dropdown)":[],
                       "Quantidade de funcionários(input)":[],
                       "Utiliza alguma ferramenta(input)":[]})


reev_df['Nome'] = CleanNames(pctrl_df)
reev_df['Sobrenome'] = CleanLastNames(pctrl_df)
reev_df['E-mail'] = CleanEmail(reev_df,pctrl_df)
print(reev_df['E-mail'].value_counts())