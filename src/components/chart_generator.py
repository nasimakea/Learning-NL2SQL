import pandas as pd
import matplotlib.pyplot as plt
from src.utils.logger import logging

logger = logging.getLogger(__name__)

class ChartGenerator:
    def __init__(self):
        logger.info("ChartGenerator initialized")

    def generate_chart(self, result: dict):
        """
        Generates best-fit chart based on data
        """
        try:
            columns = result["columns"]
            rows = result["rows"]

            df = pd.DataFrame(rows, columns=columns)

            logger.info(f"Columns detected: {columns}")

            # 🔹 Case 1: Only one column → Histogram
            if len(columns) == 1:
                col = columns[0]
                if pd.api.types.is_numeric_dtype(df[col]):
                    df[col].plot(kind="hist", bins=10)
                    plt.title(f"Distribution of {col}")

            # 🔹 Case 2: Two columns
            elif len(columns) == 2:
                x_col, y_col = columns

                x_is_numeric = pd.api.types.is_numeric_dtype(df[x_col])
                y_is_numeric = pd.api.types.is_numeric_dtype(df[y_col])

                # Both numeric → Scatter plot
                if x_is_numeric and y_is_numeric:
                    df.plot(kind="scatter", x=x_col, y=y_col)
                    plt.title("Scatter Plot")

                # One categorical + one numeric → Bar chart
                elif not x_is_numeric and y_is_numeric:
                    df.plot(kind="bar", x=x_col, y=y_col)
                    plt.title("Bar Chart")

                #  Time-based → Line chart
                elif "date" in x_col.lower() or "time" in x_col.lower():
                    df.plot(kind="line", x=x_col, y=y_col)
                    plt.title("Time Series")

            #  Case 3: More than 2 columns → Line / Multi-line
            else:
                numeric_cols = df.select_dtypes(include='number').columns

                if len(numeric_cols) >= 2:
                    df[numeric_cols].plot(kind="line")
                    plt.title("Multi-line Chart")
                else:
                    logger.info("No suitable numeric columns found")

            #  Final styling
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            logger.error(f"Chart generation failed: {str(e)}")