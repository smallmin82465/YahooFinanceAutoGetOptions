#將一個從optionget.py得到的xlsx檔案整理成一個根據ContractName的xlsx檔案
import pandas as pd

# 讀取 Excel 檔案
file_path = 'StockOptionSPY04-16-2023.xlsx'
df_dict = pd.read_excel(file_path, sheet_name=None)

# 合併所有的 Sheet
merged_df = pd.concat(df_dict.values(), ignore_index=True)

# 新增一欄 sheetname
merged_df['ContractName'] = pd.concat([pd.Series([sheet_name] * len(df)) for sheet_name, df in df_dict.items()], ignore_index=True)

# 寫入新的 Excel 檔案
merged_file_path = 'NewSpy.xlsx'
merged_df.to_excel(merged_file_path, index=False)

print("已將所有 Sheet 合併並新增 sheetname 欄位，儲存為新的 Excel 檔案：", merged_file_path)
