
import glob

import pandas as pd

pd.set_option('expand_frame_Repr',False)

path = r'C:\Users\Mat\Desktop\Forex_7' #Location of Forex_1 folder

allfiles = glob.glob(path + "/*.txt")  #Loads all the text files onto my dataframe.

frame = pd.DataFrame()  #Frame of dataframe

list_=[]

for file_ in allfiles:
    df = pd.read_csv(file_,index_col=None,sep='~',header=0)
    list_.append(df) #Tells python how to read my files in the dataframe
    
frame = pd.concat(list_)

frame
    