import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    f = open('first.txt', 'w')
    df = pd.read_excel("Analyst_Data.xls", sheetname=0, header=None)
    df.columns = ['col']
    groups = df.groupby("col")
    list = []
    for name, group in groups:
        list.append(tuple([name, len(group.index)]))
    list.sort(key=lambda tup: tup[0])
    f.write("Discrete variational series\n")
    for i in list:
        f.write(str(i)[1:-1] + '\n')
    f.write("%s %f \n" % ("Mean of list is ", df.col.mean()))
    f.write("%s %f %f %f \n" %("Mode of list is ", df.col.mode()[0], df.col.mode()[1], df.col.mode()[2]))
    f.write("%s %f \n" % ("Median of list is ", df.col.median()))
    f.write("%s %f \n" % ("Dispersion of list is ", df.col.std()**2))
    f.write("%s %f \n" % ("Standard deviation of list is ", df.col.std()))
    f.write("%s %d \n" % ("Range of list is ", df.col.max() - df.col.min()))
    f.write("%s %f \n" % ("Coefficient of skew of list is ", df.col.skew()))
    f.write("%s %f \n" % ("Coefficient of kurtosis of list is ", df.col.kurtosis()))
    f.close()
    cumulate = []
    sum_cum = 0
    for i in list:
        sum_cum+=i[1]
        cumulate.append(tuple([i[0], sum_cum, i[1]]))
    df1234 = pd.DataFrame(cumulate, columns=['x', 'y1', 'y2'])
    plt.plot(df1234.y1)
    plt.title("Cumulate curve")
    plt.savefig("First_task_cumulate_curve")
    plt.close()
    plt.plot(df1234.y2)
    plt.savefig("First_task_poligon_of_frequency")
    plt.close()
