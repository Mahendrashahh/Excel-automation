#this code is required when we do not want to take xl file as an input
# so this checks that pandas reading file or not 
'''
import pandas as pd

df = pd.read_excel("input/sales1.xlsx")
print(df.head())
'''

#we are making excel automation with gui day1
import pandas as pd
import os

def process_excel(file_paths, output_file="output/merged_output.xlsx", operation="merge"):
    print("🔍 Function entered. File list:", file_paths)
    all_dataframes = []

    for path in file_paths:
        print("📂 Checking file:", path)
        if isinstance(path, str) and path.strip().lower().endswith(".xlsx"):
            try:
                # Read all sheets as a dict of DataFrames
                sheets_dict = pd.read_excel(path, sheet_name=None)
                for sheet_name, df in sheets_dict.items():
                    print(f"🗂️ Processing sheet: {sheet_name} in file: {path}")
                    df_processed = df.copy()
                    # Standardize column names for merging
                    df_processed.columns = [col.strip().lower() for col in df_processed.columns]
                    # Clean operation: remove empty rows and unnamed columns
                    if operation == "clean":
                        df_processed = df_processed.dropna(how='all')
                        df_processed = df_processed.loc[:, ~df_processed.columns.str.contains("^unnamed")]  # Remove index columns
                    # Add total column operation
                    if operation == "add_total_column":
                        if "price" in df_processed.columns and "quantity" in df_processed.columns:
                            df_processed.loc[:, "total"] = df_processed["price"] * df_processed["quantity"]
                            print(f"➕ Calculated 'Total' column for: {path} | Sheet: {sheet_name}")
                    # Format operation: uppercase columns
                    if operation == "format":
                        df_processed.columns = [col.upper() for col in df_processed.columns]
                    all_dataframes.append(df_processed)
                    print(f"✅ Loaded: {path} | Sheet: {sheet_name}")
            except Exception as e:
                print(f"❌ Error reading {path}: {e}")

    if all_dataframes:
        if operation in ["merge", "clean", "add_total_column", "format"]:
            merged_df = pd.concat(all_dataframes, ignore_index=True)
            if not os.path.exists("output"):
                os.makedirs("output")
            merged_df.to_excel(output_file, index=False)
            print(f"\n✅ Merged file saved at: {output_file}")
        else:
            print(f"⚠️ Unknown operation: {operation}")
    else:
        print("⚠️ No valid Excel files found to process.")



