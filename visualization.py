import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def generate_histogram(df, column_name):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x=column_name, bins=20, kde=True)
    plt.title(f"Histogram of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.show()

def generate_box_plot(df, numerical_columns):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df[numerical_columns])
    plt.title(f"Box Plot of numerical_columns")
    plt.ylabel(numerical_columns.all())
    plt.show()

def generate_scatter_plot(df, x_column, y_column):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column)
    plt.title(f"Scatter Plot of {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def generate_bar_plot(df, column_name):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x=column_name)
    plt.title(f"Bar Plot of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()