import time
from tkinter import *

class StopWatch(Frame):
    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self.start=0.0
        self.elapsedtime = 0.0
        self.running = 0
        self.timestr = StringVar()

        self.makeWidgets()

    def makeWidgets(self):
        l = Label(self,textvariable=self.timestr)
        self._setTime(self.elapsedtime)
        l.pack(fill=X,expand=NO,pady=2,padx=2)

    def _update(self):
        self.elapsedtime = time.time() - self._start
        self._setTime(self.elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        minutes = int(elap / 60)
        hours = int(minutes / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d:%02d' % (hours, minutes, seconds, hseconds))

    def Start(self):
        if not self.running:
            self._start = time.time() - self.elapsedtime
            self._update()
            self.running = 1
    
    def Stop(self):
        if self.running:
            self.after_cancel(self._timer)
            self.elapsedtime = time.time() - self._start
            self._setTime(self.elapsedtime)
            self.running = 0
    
    def Reset(self):
        self._start = time.time()
        self.elapsedtime = 0.0
        self._setTime(self.elapsedtime)