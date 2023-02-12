
# Using flask to make an api
# import necessary libraries and functions
from datetime import datetime
from flask import Flask, request,render_template
from data_scrap import Script_design 
# creating a Flask app
app = Flask(__name__,template_folder='views')
tema =  {
"Tarih"          : "NULL",
"Saat"           : "NULL",
"Enlem"          : "NULL",
"Boylam"         : "NULL",
"Derinlik"       : "NULL",
"MD"             : "NULL",
"ML"             : "NULL",
"Mw"             : "NULL",
"Yer"            : "NULL"
}
@app.route('/')
def main():
    return render_template('index.html')
@app.route('/tum',methods = ['Get'])
def tum():
    deprem_dict = {}
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    for counter,lists in enumerate(deprem_listesi,1):
        deprem_dict[counter] = {
                "Tarih"          : lists[0],
                "Saat"           : lists[1],
                "Enlem"          : lists[2],  
                "Boylam"         : lists[3],
                "Derinlik"       : lists[4],
                "MD"             : lists[5],
                "ML"             : lists[6],
                "Mw"             : lists[7],
                "Yer"            : lists[8]
                }
    return deprem_dict
@app.route('/ilk',methods = ['Get'])
def ilk():
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    tema["Tarih"] = deprem_listesi[0][0]
    tema["Saat"] = deprem_listesi[0][1]
    tema["Enlem"] = deprem_listesi[0][2]
    tema["Boylam"] = deprem_listesi[0][3]
    tema["Derinlik"] = deprem_listesi[0][4]
    tema["MD"] = deprem_listesi[0][5]
    tema["ML"] = deprem_listesi[0][6]
    tema["Mw"] = deprem_listesi[0][7]
    tema["Yer"] = deprem_listesi[0][8] 
    return tema
@app.route('/son',methods = ['Get'])
def son():
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    tema["Tarih"] = deprem_listesi[-1][0]
    tema["Saat"] = deprem_listesi[-1][1]
    tema["Enlem"] = deprem_listesi[-1][2]
    tema["Boylam"] = deprem_listesi[-1][3]
    tema["Derinlik"] = deprem_listesi[-1][4]
    tema["MD"] = deprem_listesi[-1][5]
    tema["ML"] = deprem_listesi[-1][6]
    tema["Mw"] = deprem_listesi[-1][7]
    tema["Yer"] = deprem_listesi[-1][8] 
    return tema
@app.route('/ilk/<int:num>',methods = ['Get'])
def ilk_num(num):
    deprem_dict = {}
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    for counter,lists in enumerate(deprem_listesi,1):
        deprem_dict[counter] = {
                "Tarih"          : lists[0],
                "Saat"           : lists[1],
                "Enlem"          : lists[2],  
                "Boylam"         : lists[3],
                "Derinlik"       : lists[4],
                "MD"             : lists[5],
                "ML"             : lists[6],
                "Mw"             : lists[7],
                "Yer"            : lists[8]
                }
        if counter == num:
            break
    return deprem_dict
@app.route('/son/<int:num>',methods = ['Get'])
def son_num(num):
    deprem_dict = {}
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    for counter,lists_num in enumerate(range(1,num+1),1):
        print(-abs(lists_num))
        deprem_dict[counter] = {
                "Tarih"          : deprem_listesi[-abs(lists_num)][0],
                "Saat"           : deprem_listesi[-abs(lists_num)][1],
                "Enlem"          : deprem_listesi[-abs(lists_num)][2],  
                "Boylam"         : deprem_listesi[-abs(lists_num)][3],
                "Derinlik"       : deprem_listesi[-abs(lists_num)][4],
                "MD"             : deprem_listesi[-abs(lists_num)][5],
                "ML"             : deprem_listesi[-abs(lists_num)][6],
                "Mw"             : deprem_listesi[-abs(lists_num)][7],
                "Yer"            : deprem_listesi[-abs(lists_num)][8]
                }
        if counter == num:
            break
    return deprem_dict
@app.route('/tum/<string:date_1>', methods= ['Get'])
def tum_tarih(date_1):
    deprem_dict = {}
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    date_1 = date_1.replace(".","/")
    date = datetime.strptime(date_1,'%Y/%m/%d')
    counter = 1
    for lists in deprem_listesi:
        deprem_date = datetime.strptime(lists[0].replace(".","/"),'%Y/%m/%d')
        if date == deprem_date:
            deprem_dict[counter] = {
                "Tarih"          : lists[0],
                "Saat"           : lists[1],
                "Enlem"          : lists[2],  
                "Boylam"         : lists[3],
                "Derinlik"       : lists[4],
                "MD"             : lists[5],
                "ML"             : lists[6],
                "Mw"             : lists[7],
                "Yer"            : lists[8]
                }
            counter = counter+1
    return deprem_dict
@app.route('/tum/<string:date_1>/<int:num>', methods= ['Get'])
def tum_tarih_limit(date_1,num):
    deprem_dict = {}
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    date_1 = date_1.replace(".","/")
    date = datetime.strptime(date_1,'%Y/%m/%d')
    counter = 1
    for lists in deprem_listesi:
        deprem_date = datetime.strptime(lists[0].replace(".","/"),'%Y/%m/%d')
        if date == deprem_date:
            deprem_dict[counter] = {
                "Tarih"          : lists[0],
                "Saat"           : lists[1],
                "Enlem"          : lists[2],  
                "Boylam"         : lists[3],
                "Derinlik"       : lists[4],
                "MD"             : lists[5],
                "ML"             : lists[6],
                "Mw"             : lists[7],
                "Yer"            : lists[8]
                }
            counter = counter +1
            if counter == num+1:
                break
    return deprem_dict
@app.route('/tum/<string:date_1>-<string:date_2>', methods= ['Get'])
def tum_tarih_ara(date_1,date_2):
    deprem_dict = {}
    error = {"Error" : "Date'ler ayni olamaz"}
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    date_1 = date_1.replace(".","/")
    date_1 = datetime.strptime(date_1,'%Y/%m/%d')
    date_2 = date_2.replace(".","/")
    date_2 = datetime.strptime(date_2,'%Y/%m/%d')
    counter = 1
    if date_1 == date_2:
        return error
    for lists in deprem_listesi:
        deprem_date = datetime.strptime(lists[0].replace(".","/"),'%Y/%m/%d')
        if date_1 > date_2:
            if date_1 >= deprem_date >= date_2:
                deprem_dict[counter] = {
                "Tarih"          : lists[0],
                "Saat"           : lists[1],
                "Enlem"          : lists[2],  
                "Boylam"         : lists[3],
                "Derinlik"       : lists[4],
                "MD"             : lists[5],
                "ML"             : lists[6],
                "Mw"             : lists[7],
                "Yer"            : lists[8]
                }
                counter = counter +1
        if date_1 < date_2:
            if date_2 >= deprem_date >= date_1:
                deprem_dict[counter] = {
                "Tarih"          : lists[0],
                "Saat"           : lists[1],
                "Enlem"          : lists[2],  
                "Boylam"         : lists[3],
                "Derinlik"       : lists[4],
                "MD"             : lists[5],
                "ML"             : lists[6],
                "Mw"             : lists[7],
                "Yer"            : lists[8]
                }
                counter = counter +1
    return deprem_dict
@app.route('/tum/<string:date_1>-<string:date_2>-<int:limit>', methods= ['Get'])
def tum_tarih_ara_limit(date_1,date_2,limit):
    deprem_dict = {}
    error = {"Error" : "Date'ler ayni olamaz"}
    deprem_datas = Script_design("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
    deprem_listesi = deprem_datas.data_organize()
    date_1 = date_1.replace(".","/")
    date_1 = datetime.strptime(date_1,'%Y/%m/%d')
    date_2 = date_2.replace(".","/")
    date_2 = datetime.strptime(date_2,'%Y/%m/%d')
    counter = 1
    if date_1 == date_2:
        return error
    for lists in deprem_listesi:
        deprem_date = datetime.strptime(lists[0].replace(".","/"),'%Y/%m/%d')
        if date_1 > date_2:
            if date_1 >= deprem_date >= date_2:
                deprem_dict[counter] = {
                "Tarih"          : lists[0],
                "Saat"           : lists[1],
                "Enlem"          : lists[2],  
                "Boylam"         : lists[3],
                "Derinlik"       : lists[4],
                "MD"             : lists[5],
                "ML"             : lists[6],
                "Mw"             : lists[7],
                "Yer"            : lists[8]
                }
                counter = counter +1
                if limit == counter-1:
                    break
        if date_1 < date_2:
            if date_2 >= deprem_date >= date_1:
                deprem_dict[counter] = {
                "Tarih"          : lists[0],
                "Saat"           : lists[1],
                "Enlem"          : lists[2],  
                "Boylam"         : lists[3],
                "Derinlik"       : lists[4],
                "MD"             : lists[5],
                "ML"             : lists[6],
                "Mw"             : lists[7],
                "Yer"            : lists[8]
                }
                counter = counter +1
                if limit == counter-1:
                    break
    return deprem_dict

# driver function
if __name__ == '__main__':
    app.run(debug = True)
