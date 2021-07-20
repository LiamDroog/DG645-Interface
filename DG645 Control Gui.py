import tkinter as tk
from DG645SFS import DG645
class ControlGui_645:
    def __init__(self):
        self.window = tk.Tk(className='DG645 Control')
        self.screenwidth = int(self.window.winfo_screenwidth() * 0.55)
        self.screenheight = int(self.window.winfo_screenheight() * 0.55)
        self.grid = [16, 9]
        self.rowarr = list(i for i in range(self.grid[1]))
        self.colarr = list(i for i in range(self.grid[0]))
        self.window.rowconfigure(self.rowarr, minsize=25, weight=1)
        self.window.columnconfigure(self.colarr, minsize=25, weight=1)

        self.comport = 'serial://COM3'
        self.connectbutton = tk.Button(master=self.window, text='Connect', command=self._connectToBox)
        self.connectbutton.grid(row=1, column=1, sticky='nsew')
        self.resetBoxButton = tk.Button(master=self.window, text='Reset', command=self._resetBox)
        self.resetBoxButton.grid(row=1, column=2, sticky='nsew')

        self.entrybar = tk.Entry(master=self.window)
        self.entrybar.configure(width=40)
        self.entrybar.grid(row=self.grid[1], column=0, columnspan=6, sticky='new')

        self.sendentrybtn = tk.Button(master=self.window, text='Send',
                                      command=lambda: self.sendCommand(self.entrybar.get()))
        self.sendentrybtn.grid(row=self.grid[1], column=7, sticky='ew')

        self.queryentrybtn = tk.Button(master=self.window, text='Query',
                                       command=lambda: self._sendQuery(self.entrybar.get(), ins=True))
        self.queryentrybtn.grid(row=self.grid[1], column=8, sticky='ew')

        self.triggerbtn = tk.Button(master=self.window, text='Fire!', command=self._trigger)
        self.triggerbtn.grid(row=5, column=5, sticky='nsew')

        self.repbutton = tk.Button(master=self.window, text='RepRate', command=lambda: self._trigger(rep=True))
        self.repbutton.grid(row=5, column=6, sticky='nsew')


        self.window.protocol("WM_DELETE_WINDOW", self._onClosing)

        self.window.mainloop()

    def _connectToBox(self):
        self.DG645 = DG645(self.comport)
        self.reprate = float(self._sendQuery('TRAT?'))

    def _trigger(self, rep=False):
        if not rep:
            if not self._sendQuery('TSRC?') == '5':
                self.sendCommand('TSRC 5')
            self.sendCommand('*TRG')
        else:
            if not self._sendQuery('TSRC?') == '0':
                self.sendCommand('TSRC 0')
            self.repbutton.config(text='Stop?', command=self._stopTrigger)

    def _stopTrigger(self):
        self.sendCommand('TSRC 5')
        self.repbutton.config(text='RepRate', command=lambda: self._trigger(rep=True))

    def _resetBox(self):
        self.DG645.close()
        del self.DG645
        self._connectToBox()

    def _onClosing(self):
        try:
            self.DG645.close()
            self.window.destroy()
        except AttributeError as e:
            self.window.destroy()

    def _sendQuery(self, command, ins=False):
        self.entrybar.delete(0, 'end')
        rtn = self.DG645.query(command)
        if ins:
            self.entrybar.insert(0, rtn)
            return
        return rtn
    def sendCommand(self, command):
        self.entrybar.delete(0, 'end')
        self.DG645.sendcmd(command)

if __name__ == '__main__':
    ControlGui_645()