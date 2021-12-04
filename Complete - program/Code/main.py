import kivy
kivy.require('1.0.6') 
from evmdb import Database
from evmdb import Voter
from evmdb import Candidate
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from sms import Sms
from fig_auth import fingureprint

# Screen loaders
class StartWindow(Screen):
    pass

class InstWindow(Screen):
    
    
    def on_enter(self):
        pass
    
    def on_pre_enter(self):
        pass
    
    def onr(self):
        btn = self.ids['btn']
        btn.opacity = 0
               
    def onp(self):
        btn = self.ids['btn']
        rep = 1
        fp = fingureprint()
        while rep == 1:
            fp.search()
            fing = fp.fhash            
            db.cmp_fp(fing)
            db.fhash = fing
            if db.flag == "set":
                btn.background_color = 0,1,0,1
                btn.opacity = 1
                rep = 0
            else:
                rep =1

class VoteWindow(Screen):
    
    
    def initialise(self):
        self.v = Voter(db.fhash)
        self.sms = Sms()
        self.can1 = Candidate(1,self.v.vcst)
        self.can2 = Candidate(2,self.v.vcst)
        self.can3 = Candidate(3,self.v.vcst)
        self.can4 = Candidate(4,self.v.vcst)
           
    def on_pre_enter(self):
        pass
    
    def details(self):
        self.initialise()
        self.cdetails()
        self.vdetails()
        
    def upcnt1(self):
        self.sms.sendtxt(self.v.vcno,self.v.vname,self.can1.cparty)
        self.v.update()
        self.can1.update()
        for x in range(0,1000):
            print(x)
        
    def upcnt2(self):
        self.sms.sendtxt(self.v.vcno,self.v.vname,self.can2.cparty)
        self.v.update()
        self.can2.update()
        for x in range(0,1000):
            print(x)
    
    def upcnt3(self):
        self.sms.sendtxt(self.v.vcno,self.v.vname,self.can3.cparty)
        self.v.update()
        self.can3.update()
        for x in range(0,1000):
            print(x)
    
    def upcnt4(self):
        self.sms.sendtxt(self.v.vcno,self.v.vname,self.can4.cparty)
        self.v.update()
        self.can4.update()
        for x in range(0,1000):
            print(x)
          
    def cdetails(self):
        
        c1party = self.ids['c1party']
        c1name = self.ids['c1name']
        c1img = self.ids['c1img']
               
        c1name.text = self.can1.cname
        c1party.text = self.can1.cparty
        c1img.source = self.can1.csadd
        
        c2party = self.ids['c2party']
        c2name = self.ids['c2name']
        c2img = self.ids['c2img']
               
        c2name.text = self.can2.cname
        c2party.text = self.can2.cparty
        c2img.source = self.can2.csadd
        
        c3party = self.ids['c3party']
        c3name = self.ids['c3name']
        c3img = self.ids['c3img']
               
        c3name.text = self.can3.cname
        c3party.text = self.can3.cparty
        c3img.source = self.can3.csadd
        
        c4party = self.ids['c4party']
        c4name = self.ids['c4name']
        c4img = self.ids['c4img']
               
        c4name.text = self.can4.cname
        c4party.text = self.can4.cparty
        c4img.source = self.can4.csadd
    
    def vdetails(self):
        vname = self.ids['vname']
        vuid = self.ids['vuid']
        vconst = self.ids['vconst']
        vpic = self.ids['vpic']
        vname.text = self.v.vname
        vuid.text = str(self.v.vid)
        vconst.text = self.v.vcst
        vpic.source = self.v.viadd
        
class AckWindow(Screen):

    def on_enter(self):
        pass
    
    def stag(self):
        
        for x in range(0,50000):
            print(x)
        
        self.manager.transition.direction = "down"
        sm.current = "start"
        
###############################################################################
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("mainvp.kv")
sm = WindowManager()
db=Database()

screens = [StartWindow(name="start"), InstWindow(name="instructions"),VoteWindow(name="vote"), AckWindow(name="acknowledgement")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "start"

class MainVpApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    MainVpApp().run()
   