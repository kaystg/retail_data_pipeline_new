from pyspark.sql import SparkSession
from pyspark.sql.functions import sum


def create_sales_summary(sales_df):
    """
    Create a summary of sales by product category.
    """
    return (
        sales_df
        .groupBy("category")
        .agg(sum("sales_amount").alias("total_sales"))
    )


def main():
    spark = (
        SparkSession.builder
        .appName("RetailDataPipeline")
        .getOrCreate()
    )

    sales_data = [
        ("Electronics", 1000.0),
        ("Electronics", 1500.0),
        ("Clothing", 500.0),
        ("Clothing", 700.0),
    ]

    columns = ["category", "sales_amount"]

    sales_df = spark.createDataFrame(
        sales_data, columns
    )

    summary_df = create_sales_summary(sales_df)

    summary_df.show()

    spark.stop()


if __name__ == "__main__":
    main()