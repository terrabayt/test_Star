import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_excel("Analyst_Data.xls", sheetname=4)
    groups = df.groupby('Номер троллейбуса')
    for name, group in groups:
        plt.plot(group['Время прибытия'], group['Количество человек'])
        plt.show()
        plt.plot(group['Время прибытия'])
        plt.show()
        print("%s %d" %('# ', name))
        print("%s %d" %('count ', len(group.index)))
        print("%s %d" %('total_numb', sum(group['Количество человек'])))
