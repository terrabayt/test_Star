import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #f = open('first.txt', 'w')
    df1 = pd.read_excel("Analyst_Data.xls", sheetname=1, header=None)
    df2 = pd.read_excel("Analyst_Data.xls", sheetname=2, header=None)
    df1 = df1.drop(0, axis=0)
    df1.columns = ['col1', 'col2']
    df1.corr()
