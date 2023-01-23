#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-type:text/html\r\n\r\n")
import os
import pymysql
import cgi
db=pymysql.connect(user="root",password="root",host="localhost",database="onlineauction")
if db:
    cursor=db.cursor()
    sql="select * from tbl_session"
    userid=""
    useremail=""
    userrole=""
    if(cursor.execute(sql)>0):
        results=cursor.fetchall()
        for row in results:
            userid=row[0]
            useremail=row[1]
            userrole=row[2]
    if(userrole=="ROLE_03"):
        form=cgi.FieldStorage()
        category=form.getvalue("category-name")
        query="select ifnull(max(sno),0) from category"
        cursor.execute(query)
        result=cursor.fetchone()
        prefix="CATE_"
        postfix=result[0]+1
        categoryid=prefix+str(postfix)

        equery="select * from category where category='%s'"%(category)
        if(cursor.execute(equery)>0):
            print("<script>alert('Already Exists');location.href='upload-category.py';</script>")
        else:
            iquery="insert into category(id_category,category) values('%s','%s')"%(categoryid,category)
            res=cursor.execute(iquery)
            if(res==1):
                db.commit()
                print("<script>alert('Inserted');location.href='upload-category.py';</script>")
            else:
                db.rollback()
                print("<script>alert('Error in Inserting');location.href='upload-category.py';</script>")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
