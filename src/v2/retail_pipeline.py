VERSION = "2.0"

def run_pipeline():
    print("Running Retail Pipeline Version 2.0")
    print("Green environment is active.")
    print("Calculating total sales and transactions...")

    sales = {
        "Electronics": [1000, 1500],
        "Clothing": [500, 700]
    }

    for category, transactions in sales.items():
        total_sales = sum(transactions)
        transaction_count = len(transactions)

        print(f"Category: {category}")
        print(f"Total Sales: {total_sales}")
        print(f"Transactions: {transaction_count}")

    return True


if __name__ == "__main__":
    run_pipeline()