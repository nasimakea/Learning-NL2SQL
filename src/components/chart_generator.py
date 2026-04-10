import pandas as pd
import matplotlib.pyplot as plt
from src.utils.logger import logging


logger = logging.getLogger(__name__)


class ChartGenerator:
    def __init__(self):
        logger.info("ChartGenerator initialized")

    def generate_chart(self, result: dict):
        """
        Converts query result into a chart.
        """
        try:
            columns = result["columns"]
            rows = result["rows"]

            df = pd.DataFrame(rows, columns=columns)

            # Simple logic
            if len(columns) == 2:
                x_col = columns[0]
                y_col = columns[1]

                df.plot(kind="bar", x=x_col, y=y_col)
                plt.title("Query Result")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            else:
                logger.info("Not enough columns for chart")

        except Exception as e:
            logger.error(f"Chart generation failed: {str(e)}")