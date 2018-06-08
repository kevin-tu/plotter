import os,sys
# import excelpy, csv
# import psspy, pssarrays
import dyntools

FILEPATH = os.path.abspath('U:\\Projects\\PS101926_2208519A\\05_WrkPapers\\WP\\GPS Report Technical Record\\Results_7June18')
print('WD=' + FILEPATH)

#redirect.psse2py()
#psspy.psseinit(10000)

Excel ='Template.xlsx'

for outfile in os.listdir(FILEPATH):
    if outfile.endswith(".out"):
		dyn = dyntools.CHNF(outfile)
                # xl = excelpy.workbook(xlsfile=Excel,mode='w')
		extract = dyn.xlsout(show=False,channels='', outfile='', sheet='Raw')
		# xl.close()

print 'You Are Done'


		### Use this to write in excel template
		#dyntools.CHNF.xlsout(dyn, channels=[], show=False, xlsfile=Excel, outfile=outfile,sheet=outfile,overwritesheet=True)

		#xl = excelpy.workbook(xlsfile=Excel,mode='w')
		#dyn.xlsout(channels='',xlsfile=Excel,outfile=outfile,sheet=outfile,overwritesheet=True)
		#dyn.xlsout(channels='',xlsfile=Excel, outfile=outfile, sheet=outfile,overwritesheet=True)
		#dyn.xlsout(channels='',xlsfile=Excel,outfile=outfile, sheet=outfile,overwritesheet=True)
		#xl.close()
		#xl.save()
		#xl.close()

