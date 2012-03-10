# All portions of the code written by Andrew Lei are Copyright (c) 2011

def pricegrab(link):
        
        import urllib.request
        import re
        import smtplib 

        try:
                content = urllib.request.urlopen(link).read()
        except:
                #print("oh noes!")
                return None

        #This returns values of type list, which is later refit to string
        usedpriceS = re.search(r'Amazon for \$(\d+\.\d\d)', str(content))

        tradepriceS = re.search(r'Your Copy for \$(\d+\.\d\d)', str(content))


        #This was to see the code and what it was doing and how to make the program.  This isn't needed
        #For anything otherwise.  
        #f = open('sourcecode.txt','w')
        #f.write(str(content))

        if usedpriceS:
                usedprice = usedpriceS.group(1)
                print(usedprice)
        else:
                return None

        if tradepriceS:
                tradeprice = tradepriceS.group(1)
                print(tradeprice)
        else:
                return None

  
        if float(tradeprice) - float(usedprice) - 3.99 > 0:
                p = open('profitbooks.txt','a')
                print(link, "  $", float(tradeprice) - float(usedprice) - 3.99)
                print(link, "  $", float(tradeprice) - float(usedprice) - 3.99," ",usedprice,file = p)
                p.close()
                
##                Testing sending notifications to myself on profitable books, not completely smoothed out yet                 
##                if float(tradeprice) / (float(usedprice) + 3.99) > 1.19:
##                        fromaddr = '' 
##                        toaddrs  = '' 
##                        #msg = 'Here is the link: ' + link + ' and the trade price: ' + tradeprice + ' & used price ' + str(float(usedprice) - 3.99)
##                        #print(msg)
##                        print(type(link))
##                        msg = str(link)
##                        # Credentials (if needed) 
## 
##                         
##                        # The actual mail send 
##                        server = smtplib.SMTP('smtp.gmail.com:587') 
##                        server.starttls() 
##                        server.login(username,password) 
##                        server.sendmail(fromaddr, toaddrs, a) 
##                        server.quit()  
        else:
                return None


isbn = open('cleanisbn.txt','rU')
for a in isbn:
        #Grabs book price from isbnlist and plugs it into the URL after cleaning it of \n 
        pricegrab('http://www.amazon.com/dp/' + str(a.rstrip()) + '/') 
        
isbn.close()
