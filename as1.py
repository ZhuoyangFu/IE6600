import pandas
import pandas as pd

# Question 1
data = [[1, 'John', 'Milk', 5],
           [2, 'John', 'Pencil', 3],
           [3, 'John', 'Bread', 2],
           [4, 'Victor', 'Milk', 1],
           [5, 'Sarah', 'Pencil', 4],
           [6, 'Sarah', 'Bread', 2],
           [3, 'John', 'Bread', 2]]

dataset = pd.DataFrame(data, columns=['ID', 'Name', 'Product', 'Quantity'])
# print(dataset)

# Question 2
dataset = dataset.drop_duplicates()
# print(dataset)

# Question 3
dataset = dataset.set_index('ID')
# print(dataset)

# Question 4
shape = dataset.shape
# print(shape)

# Question 5
groupDataset = dataset.groupby('Product').groups
# print(groupDataset)

