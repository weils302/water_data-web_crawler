import csv
import xlwings as xw
import re

month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

input_file_name1 = ''
input_file_name2 = ''
spot1_path = ''
spot2_path = ''
year = re.split('_', input_file_name1)[1]
spot1_name = re.split('[_.]', input_file_name1)[0]
spot2_name = re.split('[_.]', input_file_name2)[0]
Test_Data = 'MergeData_%s_%s_%s.csv' % (year, spot1_name, spot2_name)
data_type = re.split('[_.]', input_file_name1)[3]
print(spot1_name)
print(data_type)
print(year)
print(re.split('[_.]', input_file_name1))

csv_row = []
count = 1
with open(Test_Data, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for month in range(1, 13):
        spot1 = xw.Book(spot1_path + '%s_%s_%s_%s.xlsx' % (spot1_name, year, month, data_type))
        spot2 = xw.Book(spot2_path + '%s_%s_%s_%s.xlsx' % (spot2_name, year, month, data_type))
        spot1_sht = spot1.sheets[0]
        spot2_sht = spot2.sheets[0]
        if month in month_31:
            for x in range(5, 36):
                for y in range(2, 26):
                    spot1_value = spot1_sht[x, y].value
                    spot2_value = spot2_sht[x, y].value
                    csv_row = [spot1_value, spot2_value]
                    writer.writerow(csv_row)
                    print(count)
                    count = count + 1
        elif month in month_30:
            for x in range(5, 35):
                for y in range(2, 26):
                    spot1_value = spot1_sht[x, y].value
                    spot2_value = spot2_sht[x, y].value
                    csv_row = [spot1_value, spot2_value]
                    writer.writerow(csv_row)
                    print(count)
                    count = count + 1
        else:
            for x in range(5, 33):
                for y in range(2, 26):
                    spot1_value = spot1_sht[x, y].value
                    spot2_value = spot2_sht[x, y].value
                    csv_row = [spot1_value, spot2_value]
                    writer.writerow(csv_row)
                    print(count)
                    count = count + 1
        spot1.app.quit()
