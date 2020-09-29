import os
import time
import datetime
tasks=[]
from funcs import run

def te(input):

   #out = os.path.basename(input)
   path_df = os.path.abspath(input)
   tasks.append("Name of the file:")
   #tasks.append(out)
   print(str(path_df))
   print('foi ate aqui------------------------')
   run(path_df)
   return(tasks)



