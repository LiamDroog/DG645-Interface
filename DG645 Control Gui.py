import tkinter as tk
from DG645SFS import DG645
class ControlGui_645:
    def __init__(self):
        self.optlist = ['0', 't', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        self.window = tk.Tk(className='\DG645 Control')
        self.screenwidth = int(self.window.winfo_screenwidth() * 0.55)
        self.screenheight = int(self.window.winfo_screenheight() * 0.55)
        self.grid = [16, 9]
        self.rowarr = list(i for i in range(self.grid[1]))
        self.colarr = list(i for i in range(self.grid[0]))
        self.window.rowconfigure(self.rowarr, minsize=25, weight=1)
        self.window.columnconfigure(self.colarr, minsize=25, weight=1)

        self.comport = 'serial://COM3'
        self.connectbutton = tk.Button(master=self.window, text='Connect', command=self._connectToBox)
        self.connectbutton.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nsew')
        self.resetBoxButton = tk.Button(master=self.window, text='Reset', command=self._resetBox)
        self.resetBoxButton.grid(row=0, column=2, rowspan=2, columnspan=2, sticky='nsew')

        self.reprateentryLabel = tk.Label(master=self.window, text='Rep-Rate-O-Meter')
        self.reprateentryLabel.grid(row=self.grid[1] - 4, column=0, columnspan=7, sticky='new')
        self.reprateentrybar = tk.Entry(master=self.window)
        self.reprateentrybar.configure(width=40)
        self.reprateentrybar.grid(row=self.grid[1]-3, column=0, columnspan=7, sticky='new')

        self.repratesendentrybtn = tk.Button(master=self.window, text='Send',
                                      command=lambda: self.sendCommand('TRAT ' + str(self.reprateentrybar.get())))
        self.repratesendentrybtn.grid(row=self.grid[1]-3, column=7, sticky='ew')

        self.entryLabel = tk.Label(master=self.window, text='Command-O-Matic')
        self.entryLabel.grid(row=self.grid[1]-1, column=0, columnspan=7, sticky='new')
        self.entrybar = tk.Entry(master=self.window)
        self.entrybar.configure(width=40)
        self.entrybar.grid(row=self.grid[1], column=0, columnspan=7, sticky='new')

        self.sendentrybtn = tk.Button(master=self.window, text='Send',
                                      command=lambda: self.sendCommand(self.entrybar.get()))
        self.sendentrybtn.grid(row=self.grid[1], column=7, sticky='ew')

        self.queryentrybtn = tk.Button(master=self.window, text='Query',
                                       command=lambda: self._sendQuery(self.entrybar.get(), ins=True))
        self.queryentrybtn.grid(row=self.grid[1], column=8, sticky='ew')

        self.triggerbtn = tk.Button(master=self.window, text='Fire!', command=self._trigger)
        self.triggerbtn.grid(row=3, column=5, sticky='nsew')

        self.repbutton = tk.Button(master=self.window, text='RepRate', command=lambda: self._trigger(rep=True))
        self.repbutton.grid(row=3, column=6, sticky='nsew')

        self.viewheader = tk.Label(master=self.window, text='Change View')
        self.viewheader.grid(row=0, column=11, columnspan=3, sticky='new')

        self.reprateview = tk.Button(master=self.window, text='Rate', command=lambda: self.sendCommand('DISP 0,0'))
        self.reprateview.grid(row=1, column=11, sticky='nsew')
        self.zero_view = tk.Button(master=self.window, text='t0', command=lambda: self.sendCommand('DISP 11,0'))
        self.zero_view.grid(row=1, column=12, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='t1', command=lambda: self.sendCommand('DISP 11,1'))
        self.t_view.grid(row=1, column=13, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='A', command=lambda: self.sendCommand('DISP 11,2'))
        self.t_view.grid(row=2, column=11, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='B', command=lambda: self.sendCommand('DISP 11,3'))
        self.t_view.grid(row=2, column=12, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='C', command=lambda: self.sendCommand('DISP 11,4'))
        self.t_view.grid(row=2, column=13, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='D', command=lambda: self.sendCommand('DISP 11,5'))
        self.t_view.grid(row=3, column=11, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='E', command=lambda: self.sendCommand('DISP 11,6'))
        self.t_view.grid(row=3, column=12, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='F', command=lambda: self.sendCommand('DISP 11,7'))
        self.t_view.grid(row=3, column=13, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='G', command=lambda: self.sendCommand('DISP 11,8'))
        self.t_view.grid(row=4, column=11, sticky='nsew')
        self.t_view = tk.Button(master=self.window, text='H', command=lambda: self.sendCommand('DISP 11,9'))
        self.t_view.grid(row=4, column=12, sticky='nsew')

        self.delayEntry = tk.Entry(master=self.window)
        self.delayEntry.configure(width=12)
        self.delayEntry.grid(row=5, column=12, columnspan=1)

        self.chosenDelayTarget = tk.StringVar(master=self.window)
        self.chosenDelayTarget.set(self.optlist[0])
        self.delayTarget = tk.OptionMenu(self.window, self.chosenDelayTarget, *self.optlist)
        self.delayTarget.grid(row=5, column=8, sticky='nsew')

        self.chosenDelayTargetLink = tk.StringVar(master=self.window)
        self.chosenDelayTargetLink.set(self.optlist[0])
        self.delayTargetLink = tk.OptionMenu(self.window, self.chosenDelayTargetLink, *self.optlist)
        self.delayTargetLink.grid(row=5, column=10, sticky='nsew')



        self.delayplus = tk.Label(master=self.window, text=' = ')
        self.delayplus.grid(row=5, column=9)
        self.delayequal = tk.Label(master=self.window, text=' + ')
        self.delayequal.grid(row=5, column=11)
        self.unitdict = {
            's'     :   'e0',
            'ms'    :   'e-3',
            'us'    :   'e-6',
            'ns'    :   'e-9',
            'ps'    :   'e-12'
        }
        self.unitList = list(i for i in self.unitdict.keys())
        self.chosenDelayUnit = tk.StringVar(master=self.window)
        self.chosenDelayUnit.set(self.unitList[0])

        self.timeTarget = tk.OptionMenu(self.window, self.chosenDelayUnit, *self.unitList)
        self.timeTarget.grid(row=5, column=13, sticky='nsew')

        self.setDelayButton = tk.Button(master=self.window, text='Set', command=self.setDelay)
        self.setDelayButton.grid(row=5, column=14, sticky='nsew')
        self.window.protocol("WM_DELETE_WINDOW", self._onClosing)


        self.window.mainloop()

    def _connectToBox(self):
        self.DG645 = DG645(self.comport)
        self.DG645.get_all_delays()
        self.reprate = float(self._sendQuery('TRAT?'))
        self.connectbutton.config(bg='green')

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

    def setDelay(self):
        target = self.chosenDelayTarget.get()
        link = self.chosenDelayTargetLink.get()
        unit = self.chosenDelayUnit.get()
        delay = self.delayEntry.get()
        try:
            float(delay)
        except:
            print('Invalid input, ya doofus')
            return
        string = 'DLAY '
        string += str(self.optlist.index(target)) + ','
        string += str(self.optlist.index(link)) + ','
        string += str(delay) + str(self.unitdict[unit])
        print(string)
        self.sendCommand(string)





if __name__ == '__main__':
    ControlGui_645()
