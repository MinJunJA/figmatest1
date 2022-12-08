import xml.etree.ElementTree as ET
import pandas as pd
import MySQLdb

labels = ['banana','chip','heim','onion','oreo','pepero','pie','pizza','shrimp','turtle']
datas = []
for label in labels: 
    # parse xml file
    doc = ET.parse("./xml/"+label+".xml")
    
    # get root node
    root = doc.getroot()

    first_node = root.find("div_cd")
    nutrition = first_node.find("nutrition_info").text
    nutrition = nutrition[1:]
    nutrition = nutrition[:-2]
    # print(nutrition)

    nutrition_list = nutrition.split(",")
    # print(nutrition_list)

    nutrition_totaldata = []
    
    for nutrition_info in nutrition_list:
        nutrition_info = nutrition_info.replace('"','')
        n = nutrition_info.split(":")
        nutrition_totaldata.append(n)
    del nutrition_totaldata[-6]

    columns = []
    data=[]
    for nut in nutrition_totaldata:    
        columns.append(nut[0])
        data.append(nut[1])
    datas.append(data)

df = pd.DataFrame(datas,columns=columns)
# print(df)

x = df.to_csv("test.csv",encoding='cp949')



