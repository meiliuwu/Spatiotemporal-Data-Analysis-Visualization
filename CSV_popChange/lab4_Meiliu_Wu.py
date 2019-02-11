import math
import numpy
import matplotlib.pyplot as plt

class City:
    def __init__(self,name,label,lat,lon,pop):
        self.cname = name # change city name by assigning different values to the self.cname variable
        self.clable = label
        self.clat = lat
        self.clon = lon
        self.cpop = pop

    def printDistance(self,othercity):
        # calculate the distance between the two given cities
        # point 1 coordinate
        x1 = self.clat
        y1 = self.clon

        # point 2 coordinate
        x2 = othercity.clat
        y2 = othercity.clon
        
        # convert degrees to radians
        x1 = math.radians(x1)
        x2 = math.radians(x2)
        y1 = math.radians(y1)
        y2 = math.radians(y2)

        # calculate the distance
        d = 6300.0 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

        # return the calculated distance 
        return int(round(d))
        
    def printPopChange(self,year1,year2):
        # retrieve the pop values of the two years
        yr1_pop = float(self.cpop[year1])
        yr2_pop = float(self.cpop[year2])

        # calculate and	output the population change over two years.	
        pop_change = round(yr2_pop - yr1_pop,2)

        # return the calculated pop change 
        return pop_change

print "\n=====================Program Start=====================\n"

# deal with bad inputs when trying to read the file
try:
    f = open('CityPop.csv','r')
except:
    print "can't open the file"

Cities = [] # an empty list of cities
header = f.readline()
while True:
    line = f.readline()
    if len(line) == 0:
        break
    
    clist = line.strip().split(',')
    cname = clist[3]
    clabel = clist[4]
    clat = float(clist[1])
    clon = float(clist[2])
    cpop = {'yr1970':float(clist[5]),'yr1975':float(clist[6]),'yr1980':float(clist[7]),'yr1985':float(clist[8]),\
            'yr1990':float(clist[9]),'yr1995':float(clist[10]),'yr2000':float(clist[11]),'yr2005':float(clist[12]),\
            'yr2010':float(clist[13])}
    # create a city instance
    city = City(cname,clabel,clat,clon,cpop)
    # add the new city to the city list
    Cities.append(city)

    # print attributes, calling it by accessing the instance/object
    # accessing the attributes without constructing the printing format
    print city.cname,city.clable,city.clat,city.clon,city.cpop

# Task 2
c1 = Cities[0]
c2 = Cities[1]
print "\nThe distance on the Earth surface between",c1.cname,"and",c2.cname,"is",c1.printDistance(c2),"kilometers."
print "\nThe population change of",c1.cname,"from 1990 to 1995 is",c1.printPopChange('yr1990','yr1995'),"million."

# Task 3 plot the pop change of two cities
# use getattr() to access to the city object attributes
shanghai = Cities[6]
beijing = Cities[12]

sh = getattr(shanghai, 'cname')
sh_pop = getattr(shanghai, 'cpop')

bj = getattr(beijing, 'cname')
bj_pop = getattr(beijing, 'cpop')

# generate a numeric list of years
x = numpy.arange(1970,2011,5)

y_sh = [sh_pop['yr1970'],sh_pop['yr1975'],sh_pop['yr1980'],sh_pop['yr1985'],sh_pop['yr1990'],sh_pop['yr1995'] \
        ,sh_pop['yr2000'],sh_pop['yr2005'],sh_pop['yr2010']]

y_bj = [bj_pop['yr1970'],bj_pop['yr1975'],bj_pop['yr1980'],bj_pop['yr1985'],bj_pop['yr1990'],bj_pop['yr1995'] \
        ,bj_pop['yr2000'],bj_pop['yr2005'],bj_pop['yr2010']]

# rgb to hex code
color_self = ['#f4425c','#0000ff']
plt.gca().set_prop_cycle('color',color_self)

# set the parameter of the plot
plt.plot(x, y_sh, '-o', linewidth = 2.0)
plt.plot(x, y_bj, '--o', linewidth = 3.0)

plt.ylabel('population in million')
plt.xlabel('year')

plt.axis([1969,2011,0,20.0])
for a,b in zip(x, y_sh): 
    plt.text(a-1, b+0.3, str(b))
for a,b in zip(x, y_bj): 
    plt.text(a-1, b-1, str(b))

plt.legend(['Shanghai', 'Beijing'], loc='upper left')
plt.title('Population change of Shanghai and Beijing from 1970 to 2010')
plt.show()

print "\n=====================Program Ended=====================\n"
