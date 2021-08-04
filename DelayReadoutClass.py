import tkinter as tk

class DelayReadout:
    def __init__(self):
        self.window = tk.Tk(className='DelayReadout')   # toplevel for integration
        with open('delayex.txt', 'r') as f:
            for i, k in enumerate(f):
                j = k.split()
                channelReadout(self.window, j[0], j[2], j[-1], row=i)
        self.window.mainloop()

class channelReadout:
    def __init__(self, master, channel, target, delay, row=0, col=0):
        units = ['s', 'ms', 'us', 'ns', 'ps']
        self.frame = tk.Frame(master=master)
        threeDigitSection(self.frame, channel, row=0, col=0)
        threeDigitSection(self.frame, ' = ', row=0, col=1)
        threeDigitSection(self.frame, target, row=0, col=2)
        threeDigitSection(self.frame, ' + ', row=0, col=3)
        delay = delay.split('.')
        threeDigitSection(self.frame, delay[0] + '.', unit=units[0], row=0, col=4)
        for i, k in enumerate([delay[1][j:j+3] for j in range(0, len(delay[1]), 3)]):
            threeDigitSection(self.frame, k, unit=units[1+i], row=0, col=5+i)

        self.frame.grid(row=row, column=col, sticky='e')


class threeDigitSection:
    def __init__(self, master, text, unit='', row=0, col=0):
        self.frame = tk.Frame(master=master)
        self.toptext = tk.Label(master=self.frame, text=text)
        self.bottomtext = tk.Label(master=self.frame, text=unit)
        self.toptext.grid(row=0, column=0, sticky='sew')
        self.bottomtext.grid(row=1, column=0, sticky='new')
        self.frame.grid(row=row, column=col, sticky='ew')



if __name__ == '__main__':
    DelayReadout()