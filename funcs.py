import pandas as pd

def CleanNames(old_df):
    names_split = old_df['socio'].str.split(' ')
    first_names = []

    for name in names_split:     
        try:
            first_names.append(name[0])
        except:
            first_names.append('-')
    
    nome_df = pd.DataFrame({'nome':first_names})

    return nome_df["nome"]

def PopFirstName(names):
    last_names= []
    for name in names:
        if name != '-':
            last_name = name.split()
            last_name.pop(0)
            separator = ' '
            last_name = separator.join(last_name)
            last_names.append(last_name)
        else:
            last_names.append('-')
    
    return last_names

def CleanLastNames(old_df):
    names_split = old_df['socio'].str.split('(')
    names = []

    for name in names_split:     
        try:
            names.append(name[0])
        except:
            names.append('-')
    
    last_names = PopFirstName(names)
    lastname_df = pd.DataFrame({'Sobrenome':last_names})

    return lastname_df["Sobrenome"]

def listToString(s):  
    str1 = ""  
     
    for ele in s:  
        str1 += ele   
       
    return str1  

def CleanEmail(new_df, old_df):
    old_df["email"].fillna('-', inplace=True)
    new_df["E-mail"] = old_df["email"]
    new_df["E-mail"] = new_df["E-mail"].str.split(',')
    new_df["E-mail"].apply(lambda x: str(x[0]))
    new_df['E-mail'] = [listToString(l) for l in new_df['E-mail']]
    
    return new_df['E-mail']

def ChooseCompanyName(company_names):  
    if company_names[0] != '-':
        company_name = company_names[0] 
    else:
        company_name = company_names[1]
    return company_name

def CleanCompanyName(new_df, old_df):
    old_df["nome fantasia"].fillna('-', inplace=True) 
    fantasy_name = old_df["nome fantasia"]
    both_company_names = []
    razao_social = old_df["razao social"]

    for fantasy,razao in zip(fantasy_name, razao_social):
        both_company_names.append([fantasy,razao])
    
    both_company_names_df = pd.DataFrame({'Empresa':both_company_names})
    new_df['Empresa'] = both_company_names_df["Empresa"]
    new_df['Empresa'] = [ChooseCompanyName(names) for names in new_df['Empresa']]

    return new_df['Empresa']

def CleanPhones(old_df):
    old_df['telefone'].fillna('-', inplace=True)
    phones = []
    cellphones = []

    for phone in old_df['telefone']:
        if phone != "-":
            phone = phone.split(',') 
            phones.append(phone[0])
            try:
                cellphones.append(phone[1])
            except:
                cellphones.append('-')                
        else:
            phones.append('-')
            cellphones.append('-')

    phones_df = pd.DataFrame({'Telefone':phones})
    cellphones_df = pd.DataFrame({'Celular':cellphones})

    return phones_df['Telefone'],cellphones_df['Celular']