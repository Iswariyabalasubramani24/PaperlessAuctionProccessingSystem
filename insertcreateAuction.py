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
    if(userrole=="ROLE_02"):
        form=cgi.FieldStorage()
        try:
            import msvcrt # Microsoft Visual C/C++ runtime lib
            msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
            msvcrt.setmode (1, os.O_BINARY) # stdout = 1
        except ImportError:
           pass
        fp=form['upload']
        if fp.filename:
            fn=os.path.basename(fp.filename)
            #Below line will upload files in specified folder named it as "files"
            open("uploads/"+fn,'wb').write(fp.file.read())
            file_name=fp.filename
            #print "%s Uploaded Successfully"%(file_name)
            upload=form.getvalue('upload')
            itemprice=int(form.getvalue('item-price'))
            itemreserve=int(form.getvalue('item-reserve'))
            
            if(itemprice<0 or itemreserve<0):
                print('<script>alert("Your Price Values are less than zero");location.href=createAuction.py;</script>')
            elif(itemreserve < itemprice):
                print('<script>alert("Your reserve price must be higher than your starting price");location.href=createAuction.py;</script>')   
            else:
                itemduration=form.getvalue('item-duration')
              
                itemtitle=form.getvalue('item-title')
                itemstate=form.getvalue('item-state')
                itemcategory=form.getvalue('item-category')
                itemdescription=form.getvalue('item-description')
               
                import time
                localtime = time.localtime(time.time())
                startdate=str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)
           
                starttime=str(localtime.tm_hour)+":"+str(localtime.tm_min)+":"+str(localtime.tm_sec)
             
                stime=str(startdate)+" "+str(starttime)
              
                enddate=str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)
                endtime=str(localtime.tm_hour)+":"+str(localtime.tm_min)+":"+str(localtime.tm_sec)
                etime=str(enddate)+" "+str(endtime)
                
                query="select ifnull(max(id),0) from item"
                cursor.execute(query)
                result=cursor.fetchone()
                iid=result[0]

                prefix="ITEM"
                postfix=iid+1
                itemid=str(prefix)+str(postfix)
               
                iquery="insert into item(ID_ITEM,PIC,TITLE,DESCRIPTION,ID_CATEGORY,ID_STATE) values('%s','%s','%s','%s','%s','%s')"%(itemid,file_name,itemtitle,itemdescription,itemcategory,itemstate)
                
                res=cursor.execute(iquery)
                lastid=cursor.lastrowid
                if(res==1):
                    db.commit()
                    
                    itemquery="select * from item where id=%d"%(int(lastid))
                    print(itemquery)
                    cursor.execute(itemquery)
                    result1=cursor.fetchone()
                    item_id=result1[1]
                    print(item_id)
                    
                    aquery="select ifnull(max(id),0) from auction"
                    
                    cursor.execute(aquery)
                    result2=cursor.fetchone()
                    aid=result2[0]

                    prefix="AUCTION"
                    postfix=aid+1
                    auctionid=str(prefix)+str(postfix)
                    print(auctionid)
                    
                    insertquery="insert into auction(id_auction,id_seller,id_item,start_price,start_timestamp,expiration_time,reserved_price,expired,counter)values('%s','%s','%s','%s','%s','%s','%s',%d,%d)"%(auctionid,userid,item_id,itemprice,stime,etime,itemreserve,0,0)
                    print(insertquery)
                    res=cursor.execute(insertquery)
                    if(res==1):
                        db.commit()
                        print("<script>alert('created Auction');location.href='createAuction.py';</script>")
                    else:
                        db.rollback()
                        print("<script>alert('Error in Creating Auction');location.href='createAuction.py';</script>")
                    
                else:
                    db.rollback()
                    
                
            
        else:
            print("No file exist")
else:
    print("Error in Connecting with DB")
