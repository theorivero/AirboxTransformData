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
reev_df['Empresa'] = CleanCompanyName(reev_df,pctrl_df)
reev_df['Telefone'],reev_df['Celular'] = CleanPhones(pctrl_df)
reev_df['URL'] = pctrl_df['Site']
new_csv_name = input('Digite o nome do novo arquivo csv')
reev_df.to_csv(f'{new_csv_name}.csv')
