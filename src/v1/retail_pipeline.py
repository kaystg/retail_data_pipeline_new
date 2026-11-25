VERSION = "1.0"

def run_pipeline():
    print("Running Retail Pipeline Version 1.0")
    print("Blue environment is active.")
    print("Calculating total sales by category...")

    sales = {
        "Electronics": 2500,
        "Clothing": 1200
    }

    for category, total in sales.items():
        print(f"{category}: {total}")

    return True


if __name__ == "__main__":
    run_pipeline()