import pandas as pd
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         ((mean(xs) * mean(xs)) - mean(xs * xs)))

    b = mean(ys) - m * mean(xs)

    return m, b

if __name__ == "__main__":
    df = pd.read_excel("Analyst_Data.xls", sheetname=3)
    clf = LinearRegression(n_jobs=-1)
    tmp = pd.DataFrame(df.X)
    X = np.array(tmp)
    Y = np.array(df.Y)
    clf.fit(X, Y)
    m,b = best_fit_slope_and_intercept(df.X, df.Y)
    print(m,b)
    regression_line1 = [(m * x) + b for x in df.X]
    m,b = clf.coef_[0], clf.intercept_
    print(m, b)
    regression_line2 = [(m * x) + b for x in df.X]
    plt.scatter(df.X, df.Y, color='#003F72')
    plt.plot(df.X, regression_line1, color='red')
    plt.plot(df.X, regression_line2, color='blue')
    plt.show()