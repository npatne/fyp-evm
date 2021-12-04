import kivy
kivy.require('1.0.6') 
from evmdb import Database
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


# Screen loaders
class LoginWindow(Screen):
    
    uName= "a"
    pName= "k"
    
    def validation(self):
        uname= self.ids['uname']
        pname= self.ids['pname']
        war= self.ids['war']
        war.opacity = 0
        
        if uname.text == self.uName and pname.text == self.pName:
             sm.current = "buffer"
             
        else:
            war.opacity = 1
            war.text ="invalid credentials"
                       
            sm.current = "login"
            
    def clear(self):
        uname= self.ids['uname']
        pname= self.ids['pname']
        uname.text= ""
        pname.text=""
            
class BufferWindow(Screen):
    def switch(self):
         sm.current = "dash"

    def popy(self):
        pop= self.ids['pop']
        flag =input("press 1")
        flag = int(flag)
        if(flag == 1):
            pop.text="connected to network"
            btn= self.ids['btn']
            btn.disabled=False 
        
class DashWindow(Screen):
    
    def switch(self,txt):
         sm.current = txt
    
class ConstiWindow(Screen):
    def switch(self):
        
         sm.current = "dash"
         
    def initwids(self):
        mum= self.ids['mum']
        mlogo = self.ids['mlogo']
        mwp= self.ids['mwp']
        mwcan = self.ids['mwcan']
        
        nag= self.ids['nag']
        nlogo = self.ids['nlogo']
        nwp= self.ids['nwp']
        nwcan = self.ids['nwcan']
        
        dli= self.ids['dli']
        dlogo = self.ids['dlogo']
        dwp= self.ids['dwp']
        dwcan = self.ids['dwcan']
        
        kol= self.ids['kol']
        klogo = self.ids['klogo']
        kwp= self.ids['kwp']
        kwcan = self.ids['kwcan']
        
        db.constit(mum.text,nag.text,dli.text,kol.text)
        
        mlogo.source= db.constis[0].wpsymb
        mwp.text = db.constis[0].wpname
        mwcan.text = db.constis[0].wpcand
        
        nlogo.source= db.constis[1].wpsymb
        nwp.text = db.constis[1].wpname
        nwcan.text = db.constis[1].wpcand
        
        dlogo.source= db.constis[2].wpsymb
        dwp.text = db.constis[2].wpname
        dwcan.text = db.constis[2].wpcand
        
        klogo.source= db.constis[3].wpsymb
        kwp.text = db.constis[3].wpname
        kwcan.text = db.constis[3].wpcand
        
    def on_pre_enter(self):
        pass
        
# switches
    def kolkata(self):
        db.currentconsti = 3
        sm.current = "candi"
        
    def mumbai(self):
        db.currentconsti = 0
        sm.current = "candi"
        
    def delhi(self):
        db.currentconsti = 2
        sm.current = "candi"
    
    def nagpur(self):
        db.currentconsti = 1
        sm.current = "candi"

class CandiWindow(Screen):
    
    def on_pre_enter(self):
        pass
    
    def initwids(self):
        
        c1name = self.ids['c1name']
        c1pic = self.ids['c1pic']
        c1party= self.ids['c1party']
        c1votes= self.ids['c1votes']
        
        c2name = self.ids['c2name']
        c2pic = self.ids['c2pic']
        c2party= self.ids['c2party']
        c2votes= self.ids['c2votes']
        
        c3name = self.ids['c3name']
        c3pic = self.ids['c3pic']
        c3party= self.ids['c3party']
        c3votes= self.ids['c3votes']
        
        c4name = self.ids['c4name']
        c4pic = self.ids['c4pic']
        c4party= self.ids['c4party']
        c4votes= self.ids['c4votes']
        
        cstname = self.ids['cstname']
        cstname.text = db.constis[db.currentconsti].name
        
        c1name.text = db.constis[db.currentconsti].candis[0].cname
        c1pic.source = db.constis[db.currentconsti].candis[0].csadd
        c1party.text = db.constis[db.currentconsti].candis[0].cparty
        c1votes.text = str(db.constis[db.currentconsti].candis[0].count)
        
        c2name.text = db.constis[db.currentconsti].candis[1].cname
        c2pic.source = db.constis[db.currentconsti].candis[1].csadd
        c2party.text = db.constis[db.currentconsti].candis[1].cparty
        c2votes.text = str(db.constis[db.currentconsti].candis[1].count)
        
        c3name.text = db.constis[db.currentconsti].candis[2].cname
        c3pic.source = db.constis[db.currentconsti].candis[2].csadd
        c3party.text = db.constis[db.currentconsti].candis[2].cparty
        c3votes.text = str(db.constis[db.currentconsti].candis[2].count)
        
        c4name.text = db.constis[db.currentconsti].candis[3].cname
        c4pic.source = db.constis[db.currentconsti].candis[3].csadd
        c4party.text = db.constis[db.currentconsti].candis[3].cparty
        c4votes.text = str(db.constis[db.currentconsti].candis[3].count)
        
    def switch(self):
         sm.current = "dash"
    
class FRsltWindow(Screen):
    
    def on_pre_enter(self):
        pass
    
    def initwids(self):
        p1name= self.ids['p1name']
        p1logo=self.ids['p1logo']
        p1seats=self.ids['p1seats']
        
        p2name= self.ids['p2name']
        p2logo=self.ids['p2logo']
        p2seats=self.ids['p2seats']
        
        p3name= self.ids['p3name']
        p3logo=self.ids['p3logo']
        p3seats=self.ids['p3seats']
        
        p4name= self.ids['p4name']
        #p4logo=self.ids['p4logo']
        p4seats=self.ids['p4seats']
        
        db.frslts()
        
        p1name.text = db.frslt[0].party
        p1logo.source = db.frslt[0].partysymb
        p1seats.text = str(db.frslt[0].seats)
        
        p2name.text = db.frslt[1].party
        p2logo.source = db.frslt[1].partysymb
        p2seats.text = str(db.frslt[1].seats)
        
        p3name.text = db.frslt[2].party
        p3logo.source = db.frslt[2].partysymb
        p3seats.text = str(db.frslt[2].seats)
        
        #p4name.text = db.frslt[3].party
        #p4logo.source = db.frslt[3].partysymb
        #p4seats.text = str(db.frslt[3].seats)
    
    def switch(self):
         sm.current = "dash"
                    
###############################################################################
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("sync.kv")
sm = WindowManager()
screens = [LoginWindow(name="login"), BufferWindow(name="buffer"),DashWindow(name="dash"),FRsltWindow(name="frslt"),ConstiWindow(name="consti"),CandiWindow(name="candi")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "login"
###############################################################################
db = Database()

class SyncApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    SyncApp().run()
