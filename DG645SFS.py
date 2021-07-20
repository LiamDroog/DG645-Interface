import instruments as ik
class DG645:
    def __init__(self, comstring):
        try:
            self.unit = ik.srs.SRSDG645.open_from_uri(comstring)
        except:
            self.unit = None
            raise IOError('Unable to connect to DG645 - Check your com port and ensure it was closed properly before'
                          ' connecting again')
        else:
            print('Connection was successful.')

    def sendcmd(self, command):
        self.unit.sendcmd(command)

    def query(self, command):
        return self.unit.query(command)

    def close(self):
        self.unit.sendcmd('IFRS 0')
        print('Connection closed successfully')
