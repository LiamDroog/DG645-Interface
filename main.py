import instruments as ik
import instruments.units as u
import time
from DG645SFS import DG645
def main():
    srs = DG645('serial://COM3')
    # srs = ik.srs.SRSDG645.open_from_uri('serial://COM3')
    print(srs.query('*IDN?'))
    # try:
    #     srs.sendcmd('TRAT 3')
    #     print(srs.query('TRAT?'))
    #     srs.sendcmd('TSRC 5')
    #     srs.sendcmd('DISP 0,2')
    #     time.sleep(1)
    #     srs.sendcmd('TSRC 0')
    #     time.sleep(3)
    #     srs.sendcmd('TRAT 10')
    #     time.sleep(5)
    #     srs.sendcmd('TSRC 5')
    #
    #     # srs.sendcmd('*TRG')
    #     # srs.sendcmd('DISP 11,3')
    # finally:
    #     # input()
    #     srs.sendcmd('IFRS 0')
    srs.close()
if __name__ == '__main__':
    main()