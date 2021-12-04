import sqlite3


class Voter():
    
    
    def __init__(self, voterfpin):
        
        con = sqlite3.connect('evm.db')
        csr = con.cursor()        
        csr.execute("SELECT * FROM voter WHERE fhash=?", (voterfpin,))        
        voterdetails = csr.fetchall()
        
        for row in voterdetails:
            
            self.vname= row[2]
            self.vid = row[0]
            self.vcst = row[3]
            self.vcno = row[4]
            self.viadd = row[5]
            self.vfhash = row[1]
            self.vflag = row[6]
        
        con.close()
    
    def update(self):
        
        con = sqlite3.connect('evm.db')
        c = con.cursor()
        self.vflag = 1
        c.execute("UPDATE voter SET flag= 1 WHERE fhash=?",(self.vfhash,))
        con.commit()
        con.close()

class Candidate(object):
    

    def __init__(self,cid,tname):
        self.tname=tname
        con = sqlite3.connect('evm.db')
        csr = con.cursor()        
        csr.execute("SELECT * FROM {} WHERE c_id={}".format(tname,cid) )       
        candidetails = csr.fetchall()
        
        for row in candidetails:
            
            self.cname= row[1]
            self.csadd = row[3]
            self.ccadd = row[4]
            self.cparty = row[2]
            self.count = row[5]
            self.c_id = row[0]
            
        con.close()
            
    def update(self):
        con = sqlite3.connect('evm.db')
        c = con.cursor()
        c.execute("SELECT * FROM {}".format(self.tname))    
        candidate = c.fetchall()  
        cid = self.c_id         
        self.count = candidate[cid-1][5]        
        self.count= self.count+1   
        c.execute("UPDATE {} SET count= {} WHERE c_id={}".format(self.tname,self.count, cid))
        con.commit()
        con.close()
        
        
class Constituency():
    
    def __init__(self,name):
        self.name = name
        self.candis = []
        self.candis.append(Candidate(1,name))
        self.candis.append(Candidate(2,name))
        self.candis.append(Candidate(3,name))
        self.candis.append(Candidate(4,name))
        
        self.sortwin()
    
    def sortwin(self):
        self.candis.sort(key = lambda x: x.count, reverse = True)
        self.wpsymb = self.candis[0].csadd
        self.wpname = self.candis[0].cparty
        self.wpcand = self.candis[0].cname
        
class FinalResult(object):
    def __init__(self,party,seats):
        self.party = party
        self.seats = seats
        partysymb = "{}.png".format(party)
        partysymb = partysymb.replace(" ","")
        self.partysymb = partysymb.lower()
        
class Database():
    currentconsti = 0
    def __init__(self):
        self.fhash = " "
        self.flag=""
        self.constis = []
        self.frslt = []

    def constit(self, c1,c2,c3,c4):
        self.constis.append(Constituency(c1))
        self.constis.append(Constituency(c2))
        self.constis.append(Constituency(c3))
        self.constis.append(Constituency(c4))
        
        for i in range(len(self.constis)):
            self.constis[i].sortwin()

    def frslts(self):
            party = []
            for i in range(len(self.constis)):
                party.append(self.constis[i].wpname)
            party_dict = {i:party.count(i) for i in party}
            for x in party_dict:
                self.frslt.append(FinalResult(x,party_dict[x]))
            
            self.frslt.sort(key = lambda x: x.seats, reverse = True)
            for i in range(len(self.frslt)):
                print(self.frslt[i].partysymb)

    def cmp_fp(self, fpin):
        v=Voter(fpin)
        if v.vfhash == fpin:
            print("voter found")
            if v.vflag == 1:
                print("your vote has been registered")
                self.flag = ""
            else:
                self.flag = "set"
        else:
            print("voter not found")



    
 

   
        
    
