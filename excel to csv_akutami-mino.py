import csv
import xlwings as xw

month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

year = 2009
Test_Data = 'TestData_%s_akutami_mino.csv' % year
akutami_path = ''
mino_path = ''
csv_row = []
count = 1
with open(Test_Data, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for a in range(1, 13):
        akutami = xw.Book(akutami_path + 'akutami_%s_%s.xlsx' % (year, a))
        mino = xw.Book(mino_path + 'mino_%s_%s.xlsx' % (year, a))
        akutami_sht = akutami.sheets[0]
        mino_sht = mino.sheets[0]
        if a in month_31:
            for x in range(5, 36):
                for y in range(2, 26):
                    akutami_value = akutami_sht[x, y].value
                    mino_value = mino_sht[x, y].value
                    csv_row = [akutami_value, mino_value]  # x=akutami y=mino
                    writer.writerow(csv_row)
                    print(count)
                    count = count + 1
        elif a in month_30:
            for x in range(5, 35):
                for y in range(2, 26):
                    akutami_value = akutami_sht[x, y].value
                    mino_value = mino_sht[x, y].value
                    csv_row = [akutami_value, mino_value]  # x=akutami y=mino
                    writer.writerow(csv_row)
                    print(count)
                    count = count + 1
        else:
            for x in range(5, 33):
                for y in range(2, 26):
                    akutami_value = akutami_sht[x, y].value
                    mino_value = mino_sht[x, y].value
                    csv_row = [akutami_value, mino_value]  # x=akutami y=mino
                    writer.writerow(csv_row)
                    print(count)
                    count = count + 1
        akutami.app.quit()
