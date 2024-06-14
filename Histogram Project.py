import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\ezdis\OneDrive\Desktop\data.csv")
data.head
print("hello")

data = data[['Hard Drive Size (in GB)', 'RAM (in GB)']]

data.plot()
plt.show()


