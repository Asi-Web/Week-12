## Asiwome Agbleze
## CMSC 111/1
## Assignment 4 - pandas_cvs_reader.py

# Import pandas so the program can read the CSV file into a DataFrame.
# If pandas is not installed, show a helpful error message.
try:
    import pandas as pd
except ImportError:
    print("Error: pandas is not installed.")
    print("Install it by running: pip install pandas")
    exit()

# Set the CSV file name so it can be reused easily in the program.
file_name = "data.csv"

# Try to read the CSV file into a DataFrame.
# Handle common errors such as the file not existing, being empty, or having invalid formatting.
try:
    df = pd.read_csv(file_name)

    # Print the full contents of the DataFrame.
    print(df.to_string(index=False))

    # Get the number of rows and columns using the DataFrame shape attribute.
    rows, columns = df.shape

    # Print the number of rows and columns.
    print(f"Rows: {rows}")
    print(f"Columns: {columns}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_name}' is empty.")

except pd.errors.ParserError:
    print(f"Error: The file '{file_name}' could not be parsed as a valid CSV file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

    