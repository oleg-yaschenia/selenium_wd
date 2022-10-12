import pandas

file_path = pandas.ExcelFile('Reports/x_report.xlsx')
open_df = pandas.read_excel(file_path,'cs-1')
open_df.insert(1, "Time", [1, 2, 3, 6], True)
open_df.to_excel(file_path)
try:
    writer = pandas.ExcelWriter('Reports/x_report.xlsx', engine='xlsxwriter')
    writer.insert(1, "Time", [1, 2, 3, 6], True)
    writer.to_excel('Reports/x_report.xlsx', index=False, sheet_name='cs-2')
    writer.save()

except:
    new_df = pandas.DataFrame({
        'Case CS-1': ["Opening All orders menu",
                      "Search by",
                      "Opening the SO",
                      "Test time"],
        'Time': [1, 2, 3, 7]
    })

    writer = pandas.ExcelWriter('Reports/x_report.xlsx', engine='xlsxwriter')
    new_df.to_excel(writer, index=False, sheet_name='cs-1')
    new_df.to_excel(writer, index=False, sheet_name='cs-2')
    new_df.to_excel(writer, index=False, sheet_name='r-1')
    writer.save()
