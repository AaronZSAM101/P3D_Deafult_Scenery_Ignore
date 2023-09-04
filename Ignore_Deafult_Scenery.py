import os
import csv

#region 设定目录
P3Daddress = input('P3D Address:')
DeafultSceneryListaddress = input('List Address:')
#endregion

#region 读取文件 转换为csv进行处理
with open(DeafultSceneryListaddress, 'r', encoding='utf-8') as f:
     file_contents = f.read()
file_contents = file_contents.replace('|', ',').replace('||', ',')

with open('airportlist.csv', 'w') as f:
     f.write(file_contents)
#endregion

#region 输入ICAO
Delete_ICAO = input('Please enter the ICAO Code you want to ignore:')
#endregion

#region 将第一列的内容进行匹配，并对应到对应的文件名
with open('airportlist.csv', 'r') as csvfile:
     csv_reader = csv.reader(csvfile)

DeafultSceneryFolder = None
DeafultSceneryName = None

for row in csv_reader:
    if row[0] == Delete_ICAO:
        DeafultSceneryFolder = row[6]
        DeafultSceneryName = row[7]
        break

    if DeafultSceneryFolder is not None and DeafultSceneryName is not None:
        print(f'已找到{Delete_ICAO}的默认地景，文件夹为{DeafultSceneryFolder}，名称为{DeafultSceneryName}')
    else:
        print('您输入的ICAO没有对应的默认地景，请检查是否输入正确，否则，请重启此脚本')
#endregion

#region 将文件名与P3D路径相结合，然后将拼合后的路径重命名为.off
DeafultSceneryPath = os.path.join(P3Daddress, 'Scenery', DeafultSceneryFolder, f"{DeafultSceneryName}")

#endregion