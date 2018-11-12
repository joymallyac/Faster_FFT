from FFT import FFT
from scipy.io import arff
import pandas as pd
import numpy as np
import pandas as pd
import time,csv


metrics=['accuracy','recall','precision','false_alarm']

metrics_dic={'accuracy':-2,'recall':-6,'precision':-7,'false_alarm':-4}

start_time = time.time()
df1 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_1.csv')
df2 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_2.csv')
df3 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_3.csv')
df4 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_4.csv')
df5 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_5.csv')
df6 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_6.csv')
df7 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_7.csv')
df8 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_8.csv')
frames = [df1,df2,df3,df4,df5,df6,df7,df8]
df = pd.concat(frames)
# total_rows = df.shape[0]
df.drop('Name',axis=1, inplace=True)
df_1 = pd.read_csv('C:/Tim_Menzies/MY_FFT/defect-prediction/src/data/turk_labeled/abinit/abinit_9.csv')
df_1.drop('Name',axis=1, inplace=True)
# training_rows = (int)(total_rows * 8 / 10)
# df_train = df.iloc[:(training_rows), :]
# df_test = df.iloc[(training_rows):, :]
df_train = df
df_test = df_1


# data = arff.loadarff('haberman.arff')
# df = pd.DataFrame(data[0])
# df_train = df
# df_test = df

def FFT1():
    dic={}
    dic1={}
    for i in metrics:
        fft = FFT(max_level=5)
        fft.criteria= 'recall'
        fft.target = df.columns.values[-1]       
        training_df = pd.DataFrame(df_train)
        testing_df = pd.DataFrame(df_test)
        fft.train, fft.test = training_df, testing_df
        fft.build_trees()
        t_id = fft.find_best_tree()    
        fft.eval_tree(t_id)
        description=fft.print_tree(t_id)        
        dic[i]=fft.performance_on_test[t_id][metrics_dic[i]]
        dic1[i]=description
    print([dic])
    end_time = time.time()
    print('Execution Time',end_time - start_time)

FFT1()


