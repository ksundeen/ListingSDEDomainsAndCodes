# Script created 10/2015 by Kim Sundeen
"""
Python script to access and export out to a .csv file all of your geodatabase's
(SDE gdb for example) domains and domain values for each. This script is especially
useful for documenting and viewing all your domains and values in case you need
to review, modify, or delete some. 
"""

import arcpy, os
from datetime import datetime

## ESTABLISHES WORKSPACE CONNECTION TO SDE DATABASE WHILE ARCMAP IS OPEN:
arcpy.env.workspace = r"Database Connections\cihl-gisdat-01_sde_current_gisuser.sde"
domains = arcpy.da.ListDomains(arcpy.env.workspace)
i = datetime.now()
todaysDatetime = i.strftime("Domains as of %m/%d/%Y %H:%M:%S")

print 'Created outFile\n'
# OUTPUT FILE TO SAVE DATA
outFile = open(r"S:\GIS_Public\GIS_Data\Metadata\UtilitiesMetadata\SDE_GIS_DomainsAndCodes.csv", 'w')

# SEND OUTPUT TO A *.CSV FILE, WITH ';' AS THE DELIMETER IF OPENING IN EXCEL
outFile.write('DomainName;DomainType;Values\n' + todaysDatetime + '\n')

for domain in domains:
    outFile.write('{0}'.format(domain.name))
    if domain.domainType == 'CodedValue':
        coded_values = domain.codedValues
        outFile.write(';IsCodedValueDomain\n')
        for val, desc in coded_values.iteritems():
            outFile.write(';;;;;;;;;;;{0} : {1}'.format(val, desc)+ '\n')
    elif domain.domainType == 'Range':
        outFile.write(';IsRangeDomain\n')
        outFile.write(';;Min: {0}'.format(domain.range[0]) + '\n')
        outFile.write(';;Max: {0}'.format(domain.range[1]) + '\n')
    else: print 'conditional statement is wrong'

print 'Completed Domain exports'
del outFile
