import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Student_Performance_Dataset.csv")

print("Dataset loaded successfully!")
print(df.head())