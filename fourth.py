import pandas as pd
import matplotlib.pyplot as plt
import datetime

if __name__ == "__main__":
    df = pd.read_excel("Analyst_Data.xls", sheetname=4)
    groups = df.groupby('Номер троллейбуса')
    for name, group in groups:
        group = group.reset_index()
        plt.plot(group['Время прибытия'], group['Количество человек'])
        plt.show()
        pause_list = []
        j = datetime.time()
        for i in group['Время прибытия']:
            pause_list.append(datetime.datetime.combine(datetime.date(2014, 3, 23),i)-datetime.datetime.combine(datetime.date(2014, 3, 23),j))
            j=i
        print("%s %d" %('# ', name))
        print("%s %d" %('count ', len(group.index)))
        print('pause_list')
        pause_list[0] = datetime.timedelta()
        pause_list.remove(datetime.timedelta())
        for i in pause_list:
            print(i.seconds)
        ser = pd.Series(pause_list)
        print("%s %s" %("mean ", ser.mean()))
        print("%s %d" %('total_numb', sum(group['Количество человек'])))
