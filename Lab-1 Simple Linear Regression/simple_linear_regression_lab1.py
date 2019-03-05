import csv
import numpy as np 
import matplotlib.pyplot as plt 


def print_csv(self):
    f = open(self.file_path, "r", encoding="Latin-1")
    reader = csv.reader(f)
    my_list = list(reader)
    f.close()

    for i in range(len(my_list) - 1, -1, -1):
        my_list[i] = list(filter(lambda x: x != '', my_list[i]))
        if not my_list[i]:
            my_list.remove(my_list[i])
    print(*my_list, sep="\n")
    return my_list

class FileReader:
    pcsv = print_csv

def __init__(self, file_path):
    self.file_path = file_path

X_Age = []
y_Experience = []

with open("team.csv") as f:
    csv_list = list(csv.reader(f))

for row in csv_list:
    if row != csv_list[0]:
        X_Age.append(int(row[4]))
        y_Experience.append(int(row[6]))
        
def estimate_coef(X, y): 
    # number of observations/points 
    n = np.size(X) 
  
    # mean of x and y vector 
    m_X, m_y = np.mean(X), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*X) - n * m_y * m_X 
    SS_xx = np.sum(X*X) - n * m_X * m_X 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1 * m_X 
  
    return(b_0, b_1)      
    
def plot_regression_line(X, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(X, y, color = "b",
               marker = "o", s = 30)
    # predicted response vector 
    y_pred = b[0] + b[1]*X
    # plotting the regression line 
    plt.plot(X, y_pred, color = "red")
    # putting labels 
    plt.xlabel('Age') 
    plt.ylabel('Experience')
    # function to show plot 
    plt.show()
def main():
    
    x=np.array(X_Age)
    y=np.array(y_Experience)
    
    b = estimate_coef(x, y) 
    plot_regression_line(x, y, b)
    # estimating coefficients 

if __name__ == "__main__": 
    main() 
