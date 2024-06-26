import sys
import pandas as pd

def convert_to_xlsx(output_file, csv_files):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            # Create a sheet name from the CSV filename, excluding the extension and limiting to 31 characters
            sheet_name = csv_file.replace('.csv', '')[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f">[i] Conversion complete: '{output_file}' has been created.")

def main():
    if len(sys.argv) < 3:
        print("Usage: redcsv2xlsx output.xlsx file1.csv file2.csv ...")
        sys.exit(1)

    output_xlsx = sys.argv[1]
    csv_files = sys.argv[2:]

    convert_to_xlsx(output_xlsx, csv_files)

if __name__ == "__main__":
    main()

