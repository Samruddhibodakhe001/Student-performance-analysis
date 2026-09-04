# Data Cleaning & Visualization Project

## 📌 Project Overview

This project focuses on cleaning, processing, analyzing, and visualizing a student performance dataset.

The main goal is to find useful patterns and insights from student data using Python.

---

## 🎯 Objectives

* Clean the raw dataset
* Handle missing values
* Remove duplicate records
* Detect and handle outliers
* Analyze student performance
* Create charts and visualizations
* Create a simple dashboard
* Find important insights from the data

---

## 📊 Dataset

The dataset contains information about student performance.

### Main Columns

* `Student_ID` – Unique ID of the student
* `Age` – Age of the student
* `Gender` – Gender of the student
* `Class` – Student class
* `Study_Hours_Per_Day` – Daily study hours
* `Attendance_Percentage` – Attendance percentage
* `Parental_Education` – Parent's education level
* `Internet_Access` – Internet access availability
* `Extracurricular_Activities` – Participation in activities
* `Math_Score` – Mathematics score
* `Science_Score` – Science score
* `English_Score` – English score
* `Previous_Year_Score` – Previous year score
* `Final_Percentage` – Final percentage
* `Performance_Level` – Student performance category
* `Pass_Fail` – Final result

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook / VS Code

---

## 📁 Project Structure

```text
Data_Cleaning_Visualization/
│
├── data/
│   └── Student_Performance_Dataset.csv
│
├── output/
│   └── student_dashboard.png
│
├── analysis.py
│
└── README.md
```

---

## 🧹 Data Cleaning

The following cleaning operations are performed:

### 1. Missing Values

Missing values are checked using:

```python
df.isnull().sum()
```

Numerical missing values are handled using the median.

### 2. Duplicate Values

Duplicate records are checked and removed.

```python
df.duplicated().sum()
```

### 3. Outliers

Outliers are identified using the IQR (Interquartile Range) method.

### 4. Data Types

The data types of columns are checked and corrected when required.

---

## 📈 Data Visualization

The following charts are created:

### 1. Gender Distribution

Shows the number of male and female students.

### 2. Performance Level

Shows how students are distributed across different performance levels.

### 3. Study Hours vs Final Percentage

Shows the relationship between daily study hours and final percentage.

### 4. Attendance vs Final Percentage

Shows the relationship between attendance and final percentage.

---

## 📊 Dashboard

A simple student performance dashboard is created using Matplotlib and Seaborn.

The dashboard contains:

* Gender Distribution
* Performance Level
* Study Hours vs Final Percentage
* Attendance vs Final Percentage

The dashboard is saved as:

```text
output/student_dashboard.png
```

---

## 🔍 Key Findings

The project helps answer questions such as:

* How are students distributed by gender?
* What is the most common performance level?
* Does studying more relate to higher final percentage?
* Does better attendance relate to better performance?
* What patterns can be found in student results?

The exact findings are calculated from the cleaned dataset.

---

## ▶️ How to Run the Project

### Step 1: Install Python

Install Python from the official Python website.

### Step 2: Install Required Libraries

Open the VS Code terminal and run:

```bash
python -m pip install pandas numpy matplotlib seaborn openpyxl
```

### Step 3: Place Dataset

Put the dataset inside the `data` folder:

```text
data/Student_Performance_Dataset.csv
```

### Step 4: Run the Python Program

Run:

```bash
python analysis.py
```

### Step 5: View Results

The generated dashboard and cleaned data can be found in the `output` folder.

---

## 💡 Conclusion

This project demonstrates how Python can be used to clean raw data, analyze student performance, create visualizations, and communicate important findings through a simple dashboard.

The project provides practical experience with data preprocessing, exploratory data analysis, visualization, and data storytelling.

---

## 👩‍💻 Author

**Samruddhi Bodakhe**

B.Tech – Artificial Intelligence & Data Science

---

## ⭐ Project Skills

`Python` `Pandas` `NumPy` `Matplotlib` `Seaborn` `Data Cleaning` `Data Analysis` `Data Visualization` `EDA` `Data Storytelling`
