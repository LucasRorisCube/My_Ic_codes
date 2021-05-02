import pandas as pd
import numpy as np

def Parser_MAF_File(Path, output_file):
    
    '''
    The objective of this function is transformate one .maf file in a .txt file that serves as input to nCOP algorithm
    Path = the path of .maf file
    output_file = the name of the output file
    '''
    
    print ("Reading arquive...")
    dados = pd.read_csv(Path,comment='#', sep='\t',header=0,index_col=False, low_memory = False)
    
    
    print ("Creating new dataFrame with only essential columns")
    df = pd.concat([dados['Hugo_Symbol'],dados['Tumor_Sample_Barcode']],axis=1)
    
    print ("Formating output file...")
    
    output = open(output_file + '.txt','w')
    list_temp = []
    i = 0
    while i < len(df.index):

        temp = df['Hugo_Symbol'][i]

        while i < len(df.index) and temp == df['Hugo_Symbol'][i]:
            if(list_temp.count(df['Tumor_Sample_Barcode'][i]) == 0):
                list_temp.append(df['Tumor_Sample_Barcode'][i])
            i += 1
            
        output.write(temp + ' ' + ' '.join(list_temp) + '\n')
        list_temp = []
    
    print ("Done.")
    output.close()