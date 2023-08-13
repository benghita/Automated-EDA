import pandas as pd
from sqlalchemy import create_engine
from visualization import *


class autoEDA:


    def __init__(self, data=None):
        self.data = data

    def load_data(self, file_path, format="csv", database_url=None, query=None):
        try :
            if format == "csv":
                self.data = pd.read_csv(file_path)
            elif format == "excel":
                self.data = pd.read_excel(file_path)
            elif format == "sql" and database_url and query:
                engine = create_engine(database_url)
                self.data = pd.read_sql(query, engine)
        except:
            raise ValueError("Invalid format or missing parameters for SQL.")
        if self.data.empty == False :
            print("data loaded successfully")
            print(self.data.describe())

        return self.data 
            


    def preprocess(self):

        if self.data is None:
            raise ValueError("No data loaded.")
        data = self.data  

        # Replace missing values with mean for numerical columns
        numeric_columns = data.select_dtypes(include=["int64", "float64"]).columns
        for col in numeric_columns:
            mean_value = data[col].mean()
            data[col].fillna(mean_value, inplace=True)
        
        # Replace missing values with the most repeated category for categorical columns
        categorical_columns = data.select_dtypes(include=["object"]).columns
        for col in categorical_columns:
            most_common_value = data[col].mode().iloc[0]
            data[col].fillna(most_common_value, inplace=True)
        
        # Scaling numerical features (min-max normalization)
        for col in numeric_columns:
            data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())
        
        return data
    

    def select_features(self, target_column, threshold=0.0):
        if self.data is None:
            raise ValueError("No data loaded.")
        df = self.data 
        variances = df.var(numeric_only=True)
        low_variance_cols = variances[variances <= threshold].index.tolist()
        for col in low_variance_cols :
            if  col!=target_column:
                df.drop(col, axis=1, inplace=True)
        return df



    def generate_dashboard(self, target_column):
        df = self.data
        # Select numerical columns
        numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
        # Generate a box plot for all numerical columns
        generate_box_plot(df, numerical_columns)

        for column in df.columns:
            if (df[column].dtype == "int64" or df[column].dtype == "float64") and column!=target_column:
                generate_histogram(df, column)
                generate_scatter_plot(df, column, target_column) 
            elif df[column].dtype == "object":
                generate_bar_plot(df, column)





