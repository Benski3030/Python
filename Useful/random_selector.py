
import pandas as pd

#Read in the data 
zips = pd.read_csv(r"foo.csv")
zips.head()

#Make sure its in the right format (zips are strings)
zips['zip'] = zips['zip'].astype(str)
zips['zip'] = zips['zip'].str.rstrip('.0')
sum(zips['circ'])/2

zipsamp = zips.sample(frac = 0.5)
87500 <= sum(zipsamp['circ']) <= 88000

def zipsearch(frame):
    test = 87500 <= sum(zipsamp['circ']) <= 88000
    if test == True:
        print "Yup, its there" 
        return zipsamp
    while test == False:
        zipsampredo = zips.sample(frac = 0.5)
        if 87500 <= sum(zipsampredo['circ']) <= 88000:
            break
            print"Got a new one"
    return zipsampredo


newzip = zipsearch(zipsamp)
sum(newzip['circ'])

newzip.head()

