import csv
f = open("seoul.csv");
data = csv.reader(f);
header = next(data);
max_tmp = -999;
max_data = "";
for row in data:
    try:
        row[-1] = float(row[-1])

    except:
        row[-1] = -999
        
    if row[-1] > max_tmp:
        max_tmp = row[-1];
        max_date= row[0];
f.close();

print(f"기상 관측 아래 서울의 최고 기온이 가장 높았던 날은 {max_date}로, {max_tmp}도 였습니다.")
