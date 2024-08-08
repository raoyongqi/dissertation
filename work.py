# import pandas as pd
# import sqlite3
# import openpyxl

# excel_path = 'path/to/your/excel_file.xlsx'
# db_path = 'path/to/your/database_file.db'

# excel_data = pd.read_excel(excel_path, sheet_name=1)

# conn = sqlite3.connect(db_path)
# query = "SELECT * FROM your_table_name"
# db_data = pd.read_sql_query(query, conn)
# conn.close()

# sorted_db_data = db_data.sort_values(by=[db_data.columns[0], db_data.columns[1]])

# workbook = openpyxl.load_workbook(excel_path)
# worksheet = workbook.worksheets[1]

# sorted_data_list = sorted_db_data.values.tolist()
# for col_num, cell_data in enumerate(sorted_data_list[0]):
#     worksheet.cell(row=2, column=col_num + 1, value=cell_data)

# def merge_row_cells(worksheet, row, start_col, end_col):
#     start_merge_col = start_col
#     last_value = worksheet.cell(row=row, column=start_col).value
#     for col_num in range(start_col + 1, end_col + 1):
#         current_value = worksheet.cell(row=row, column=col_num).value
#         if current_value != last_value:
#             if col_num - 1 > start_merge_col:
#                 worksheet.merge_cells(start_row=row, start_column=start_merge_col,
#                                       end_row=row, end_column=col_num - 1)
#             start_merge_col = col_num
#             last_value = current_value
#     if end_col > start_merge_col:
#         worksheet.merge_cells(start_row=row, start_column=start_merge_col,
#                               end_row=row, end_column=end_col)

# num_columns_sorted_db = len(sorted_db_data.columns)
# merge_row_cells(worksheet, 2, 1, num_columns_sorted_db)

# workbook.save(excel_path)

# print(f"数据已成功写入 {excel_path}")
