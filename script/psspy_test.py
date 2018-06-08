import os,sys
import time
from glob import glob

PSSE_LOCATION = "C:/Program Files (x86)/PTI/PSSE34/PSSPY27"
print(PSSE_LOCATION)
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION 

import dyntools

DATA_FOLDER = os.path.abspath('U:\\Projects\\PS101926_2208519A\\05_WrkPapers\\WP\\GPS Report Technical Record\\Results_7June18\\FaultRideThrough\\Winter High')

start_time = time.time()
outfiles = glob(DATA_FOLDER + "/Winter High Case 5b*.out")

for outfile in outfiles:
    dyn = dyntools.CHNF(outfile)
    extract = dyn.xlsout(show=False,channels='', outfile='', sheet='Raw')
    print(extract)

    end_time = time.time()
    print "Run time: {}ms".format(round(end_time-start_time)*1000,3)