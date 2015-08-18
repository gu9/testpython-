import time 

#ASSIGNMENT  Submitted by Gurpreet Singh(1446185-Student_id)

#provide Numeric input in the timeout varible otherwise program will not give required output


#I have written this whole code by myself so there will be no external refrence link except python.org , stackoverflow.com and class notes
#I am using  class because I used to do C++ prgramming and i am familiar with the classes and the usage of user defined objects

                                      
class IPac(object):

    counter=0                          #init(constructor) function is predefined function in Python which is called implicitly  by the interpreter.
    def __init__(self):                #self is similar to this-> object in java ,it is use to intialize the attributes of the class
        i=raw_input("<HOST_ID>:")
        self.pcname=i
        i=raw_input("<MAC ADDR>:")       #pcname,mac,ip,timeout are the attributes of the class IPac which will be unique for the each instance
        self.mac=i
        i=raw_input("<ip addr>:")
        self.ip=i
        i=raw_input("<time_out>:")
        self.timeout=i


class res_address(object):          #This class provide funcationality  to do resolve address in the ARP 

      def __init__(self,k,t):


        self.pcSource=k
        self.macResolve=''

        self.ipResolve=t
        self.timeCache=time.time()

      def cache_search(self,p,hid,ipaddress):

                                                                 #if input ip does not exit
          if check_ip(p,ipaddress)==0:

                print(hid,'could not resolve ',ipaddress)
                return 0

          else:
              
               for i in xrange(len(p)):

                  if p[i].ip == self.ipResolve:                                    #resolve the address by storing the mac in the host
                      self.macResolve=p[i].mac
                      return  
                                                                             #print'ARP response',p[i].mac,check_mac(p,hid),ipaddress
                      

def arpsend(p,name,tip):
    for j in xrange(len(p)):
        
        if p[j].pcname==name:
            
            temp_mac=p[j].mac
            temp_ip=p[j].ip
            print 'ARP request',p[j].mac,'FF:FF:FF:FF:FF:FF',p[j].ip,tip
            
def arpresponse(p,hid,ipaddress,c):
    
    for i in range(len(p)):
        
        
        if p[i].ip == ipaddress:
            print'ARP response',p[i].mac,check_mac(p,hid),ipaddress,check_host_ip(p,hid)
            
       
        
        
    
def print_out(p):
    for k in range(len(p)):

       print p[k].pcSource,p[k].timeCache

def print_out_cach(p):
    os.system("clear")
    print "We are inside print"    
    check=raw_input('Enter HOST_ID:')
    for k in range(len(p)):
        if check == p[k].pcSource:
            print p[k].pcSource,p[k].macResolve,p[k].ipResolve


def dup_check(p,ptemp,c):
    
    
     message='FF:FF:FF:FF:FF:FF'      #Duplicate check function if condition is true than the ipList[] will be updated
     for i in range(len(p)):
        if p[i].pcname==ptemp.pcname:
            print "hostname in List updated"
            p[i].mac=ptemp.mac
            p[i].ip=ptemp.ip
            p[i].timeout=ptemp.timeout
            print 'ARP request',p[i].mac,message,p[i].ip,p[i].ip           
            return 9

def print_connected(p,c):      #ip_conflit and gratious ARP request
    
    message='FF:FF:FF:FF:FF:FF'
    print p[c].pcname,'Connected \n'
    print 'ARP request',p[c].mac,message,p[c].ip,p[c].ip
    for i in range(len(p)):
        
        if p[c].ip==p[i].ip and p[c].pcname!=p[i].pcname:
                 print "\nARP Reply",p[c].mac, p[c].ip,p[c].ip, "\n"
                 print "\nError:Host detected IP Conflit",p[count].pcname  , "has been disconnected.\n"    
                 p.pop()
                 return 1
    return 0    


def check_pc(p,check):

    for k in range(len(p)):            #return the pc name
        if check == p[k].pcname:
            return 1

    return 0

def check_ip(p,check):
                                           #return the ip of the host
    for k in range(len(p)):
        if check == p[k].ip:
            return 1

    return 0

def check_entry(c,check_host,check_addr):

    for k in range(len(c)):
        if check_host == c[k].pcSource and check_addr==c[k].ipResolve:
            return c[k].timeCache
    return 0

def check_pos(p,hostaddr):
    
    for i in xrange(len(p)):
        
        if p[i].ip==hostaddr:
            return p[i].pcname
    return 0
def check_mac(p,hostaddr):
    
    for i in xrange(len(p)):
        
        if p[i].pcname==hostaddr:
            return p[i].mac
    return 0


def check_host_ip(p,phost):
    
    for i in xrange(len(p)):
        if p[i].pcname==phost:
            return p[i].ip
    return 0

def check_tabel(plist,recdata,hostn,c,ipaddress):


    for i in range(len(plist)):                   #if cache has the entries than message will be printed resolved other wise ARP expires 

        if hostn == plist[i].pcname:
            orignal= plist[i].timeout
            break



    curtime=time.time()
    time.sleep(1)
    xd=curtime-recdata
    if float(orignal)>xd:
        for k in range(len(c)):
            
            if hostn == c[k].pcSource and ipaddress==c[k].ipResolve:
                
                
                print hostn,'Resolved ',ipaddress,'to',c[k].macResolve
                c[k].timeCache=curtime
                #print'\nUpdated'
    else:
        print('ARP expires for this')  
        for o in range(len(c)):
           if hostn == c[o].pcSource and ipaddress==c[o].ipResolve:
               c.remove(c[o])
               break
               
                 
                 


def print_pro(hostnam,p,c):   #print entries in the cache or show no entries message and Unknown Pc 
                               #than remove the old cache entries
    
    
    flag=0
    if len(c)==0 :
        print'NO entries'
        return 0
    for i in xrange(len(p)):
        if hostnam==p[i].pcname:
            orignal=p[i].timeout
            break
            
    curtime=time.time()

    try:
        for i in range(len(c)):
                if hostnam==c[i].pcSource:
                    flag=1
                    recdata=c[i].timeCache
                    xd=0
                    xd=curtime-recdata
                    if float(orignal)>xd:
                        print c[i].macResolve,c[i].ipResolve,'(',float(orignal)-xd,'seconds)'
                    else:
                        print('ARP expires')
                        for o in range(len(c)):
                            if hostnam ==c[o].pcSource:
                                print 'Deleting cache entry',c[i].macResolve,c[i].ipResolve
                                c.remove(c[i])
                                break        
        
    except:print'\n'
        
                     
    if flag==0:
        print'no entry'
          
def check_tab(pList,ip_h,c,ipaddr):    #printing the resolved message by retriving from the cache entries
                                        
    for k in range(len(c)):
        
         if ip_h == c[k].pcSource and ipaddr==c[k].ipResolve:
              
                    print ip_h,'Resolved ',ipaddr,'to',c[k].macResolve    
  
def ip_conflit(p,c):
    
     for i in range(len(p)):
         
         if p[c].ip==p[i].ip:
             print "\nARP Reply", p[c].pcname,p[c].mac, p[c].ip,p[c].ip, "\n"
             print "\nHost",p[count].pcname  , "has been disconnected.\n"    
             p.pop()
             return 1
     return 0
             
    
ipList = []
cache_items=[]

count=0
#Taking the run time input from user and match according to the variable data
data=raw_input('WELCOME TO ARP SIMULATOR v1.0 ENTER THE Commands\nconfig\nresolve\nprint\nquit\n')
while data!='quit':


        if data=='config':
                                #append the host in ipList and cache values in cache_items list

              if count==0:
                  
                  ipList.append(IPac())       #calling the init function implicitly by the class and appending to the list
                  print_connected(ipList,count)
                  count=count+1
                  
              else:
                  d=IPac()
                                                         #checking for duplicates and the ip conflit 
                  if dup_check(ipList,d,cache_items)!=9:
                       ipList.append(d)
                       z=print_connected(ipList,count) 
                       count=count+1-z

        elif data=='print':
            jput=raw_input('<Host_ID>:')
           #print_out_cach(cache_items)
            if len(cache_items)==0:
                print'Cache Empty'  
                                                         #print_out(cache_items)                    
            elif check_pc(ipList,jput)!=0:               #after host resolved the entries can be check by running the print command
                t=print_pro(jput,ipList,cache_items)
           
            else:
                print'Error:unknown pc',jput
         


        elif data=='resolve':


            ip_host=raw_input("Host_ID:")                 #user input for ARP
                                                         #storing value for RARP(reverse ARP)
            ip_addr=raw_input("<ip addr>:")
            rhostname=check_pos(ipList,ip_addr)
            rhostip=check_host_ip(ipList,ip_host)            
            check_val=check_pc(ipList,ip_host)
            #ck_ip=check_ip(ipList,ip_addr)
            if(check_val==0):
                print('Error: Unknown Host',ip_host)
                                                               #checking PC name in the ipList

            rectime=check_entry(cache_items,ip_host,ip_addr)
            rectime2=check_entry(cache_items,rhostname,rhostip)      #retriving the cache time 
            if rectime!=0 :
                z=ctable=check_tabel(ipList,rectime,ip_host,cache_items,ip_addr)
                #if rectime2!=0:
                 #   print '\nUpdate table ARP (peers)'
                  #  z=ctable=check_tabel(ipList,rectime2,rhostname,cache_items,rhostip)
                    

                 #print 'Entry found\n',rectime                         #Entry found in the cache and ARP has been resolved for both ARP and RARP time will be updated on  the peers
                 
                 #if z>=0:
                  #   cache_items.pop(z)

            #if rectime2!=0:
                
               
               # z=ctable=check_tabel(ipList,rectime2,rhostname,cache_items,rhostip)
               # if z>=0:
                #    cache_items.pop(z)            

            else:
                if check_val!=0 :
                    arpsend(ipList,ip_host,ip_addr)      #ARP send function
                    pksend=res_address(ip_host,ip_addr)
                    
                    pkrecv=res_address(rhostname,rhostip)
                    check_r=pksend.cache_search(ipList,ip_host,ip_addr)
                    arpresponse(ipList,ip_host,ip_addr,cache_items)         #ARP response function
                    check_rec=pkrecv.cache_search(ipList,rhostname,rhostip)
                    
                    if check_r!=0:
                      cache_items.append(pksend)                      #if entry is not in the cache than append the cache_items
                      check_tab(ipList,ip_host,cache_items,ip_addr)
                      
                      
                      
                    if check_rec!=0:
                        
                        cache_items.append(pkrecv)

        data=raw_input('\nconfig\nresolve\nprint\nquit\nEnter Your Choice:')



