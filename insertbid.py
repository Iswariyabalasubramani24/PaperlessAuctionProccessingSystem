#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-type:text/html\r\n\r\n")
import os
import pymysql
import cgi
form=cgi.FieldStorage()
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
    if(userrole=="ROLE_01"):
        auctionid=form.getvalue('auctionid')
        bidamt=form.getvalue('bidamt')
        
        selectquery="select start_price from auction where id_auction='%s'"%(auctionid)
        cursor.execute(selectquery)
        result=cursor.fetchone()
        startprice=result[0]
        if(bidamt<=startprice):
            print("<script>alert('Bid Price Cannot be less than Start Price');location.href='searchtobid.py?submit=%s';</script>"%(auctionid))
        else:
            print(startprice)
            import time
            localtime = time.localtime(time.time())
            startdate=str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)
            starttime=str(localtime.tm_hour)+":"+str(localtime.tm_min)+":"+str(localtime.tm_sec)
            presenttime=str(startdate)+" "+str(starttime)
            bididquery="select ifnull(max(ID),0) from bid"
            cursor.execute(bididquery)
            result=cursor.fetchone()
            prefix='BID'
            postfix=int(result[0])+1
            bidid=str(prefix)+str(postfix)
            
            insertquery="insert into bid(ID_BID,ID_BUYER,ID_AUCTION,PRICE,TIME) values('%s','%s','%s','%s','%s')"%(bidid,userid,auctionid,bidamt,presenttime)
            res=cursor.execute(insertquery)
            if(res==1):
                db.commit()
                print("<script>alert('Congratualtions! Your bid was successful!');location.href='searchtobid.py?submit=%s';</script>"%(auctionid))
            else:
                db.rollback()
                print("<script>alert('Error in Bidding');location.href='searchtobid.py?submit=%s';</script>"%(auctionid))
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
