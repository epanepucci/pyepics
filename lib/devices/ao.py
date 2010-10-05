#!/usr/bin/python
import epics  

class ao(epics.Device):
    "Simple analog output device"

    _fields = ('OUT', 'LINR', 'RVAL', 'ROFF', 'EGUF', 'EGUL', 'AOFF',
               'ASLO', 'ESLO', 'EOFF', 'VAL', 'EGU', 'HOPR', 'LOPR',
               'PREC', 'NAME', 'DESC', 'DTYP', 'HIHI', 'LOLO', 'HIGH',
               'LOW', 'HHSV', 'LLSV', 'HSV', 'LSV', 'HYST', 'OMSL', 'DOL',
               'OIF', 'DRVH', 'DRVL', 'OROC', 'OVAL')
    
    def __init__(self, prefix):
        if not prefix.endswith('.'):
            prefix = "%s." % prefix
        epics.Device.__init__(self, prefix, self._fields)
