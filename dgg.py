import mysql.connector

def ini():
    m = mysql.connector.connect(host="localhost",
                            port="3306",
                            user="root",
                            password="mypass",
                            database="devi",
                            auth_plugin='mysql_native_password')
    b = m.cursor()
    
    # for i in n:
    #    print(i)
    l=[]
    # 
    
    b.execute("select * from orghospital")
    r=b.fetchall()

    for i in range(0,len(r)):
        h_name=r[i][1]
        loc=r[i][3]
        rank=r[i][2]
        d={"h_name1":h_name,"rank1":rank,"loc1":loc}
        l.append(d)
    
    
    return l

s=ini()



