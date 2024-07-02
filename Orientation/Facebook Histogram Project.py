import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\ezdis\OneDrive\Desktop\data.csv")
data.head
print("hello")

data = data[['Hard Drive Size (in GB)', 'RAM (in GB)']]

plt.hist(data, bins=30, edgecolor='black')  
plt.title('Histogram of Data')
plt.xlabel('Hard Drive Size')
plt.ylabel('RAM')
plt.grid(True)  
plt.show()
