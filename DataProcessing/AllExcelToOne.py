#將資料夾內的xlxs根據Sheetname合併成一個xlsx並將欄位命名為ContractName
import os
import pandas as pd


# 指定資料夾路徑
folder_path = 'OptionData'

# 取得資料夾中的所有檔案
files = os.listdir(folder_path)

# 過濾出所有的 Excel 檔案
excel_files = [file for file in files if file.endswith('.xlsx')]

# 讀取並合併所有的 Excel 檔案
merged_df = pd.DataFrame()
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df_dict = pd.read_excel(file_path, sheet_name=None)
    for sheet_name, df in df_dict.items():
        df['ContractName'] = sheet_name
    merged_df = pd.concat([merged_df, pd.concat(df_dict.values(), ignore_index=True)], ignore_index=True)

# 寫入新的 Excel 檔案
merged_file_path = 'SPYNew.xlsx'
merged_df.to_excel(merged_file_path, index=False)

print("已將資料夾中的所有 Excel 檔案合併並新增 ContractName 欄位，儲存為新的 Excel 檔案：", merged_file_path)
