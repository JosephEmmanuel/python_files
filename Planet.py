
#Planet class

SURFRACE_PRESSURE_UNKNOWN=-1

class Planet:
    def __init__(self,name,mass,diameter,density,gravity,escapevelocity,rotationalperiod,lengthofday,distancefromsun,perihelion,aphelion,orbitalperiod,orbitalvelocity,orbitalinclination,orbitaleccentricity,obliquitytoorbit,meantemperature,surfacepressure, numberofmoons,ringsystem,globalmagneticfield ):
        self.name=name
        self.mass=mass*(10**24)
        self.diameter=diameter
        self.density=density
        self.gravity=gravity
        self.escapevelocity=escapevelocity
        self.rotationalperiod=rotationalperiod
        self.lengthofday=lengthofday
        self.distancefromsun=distancefromsun*10**6
        self.perihelion=perihelion*10**6
        self.aphelion=aphelion*10**6
        self.orbitalperiod=orbitalperiod
        self.orbitalvelocity=orbitalvelocity
        self.orbitalinclination=orbitalinclination
        self.orbitaleccentricity=orbitaleccentricity
        self.obliquitytoorbit=obliquitytoorbit
        self.meantemperature=meantemperature
        self.surfacepressure=surfacepressure
        self.numberofmoons=numberofmoons
        self.ringsystem=ringsystem
        self.globalmagneticfield=globalmagneticfield
        if(name=="MOON"):
            self.issatelite=True
        else:
            self.issatelite=False

    def print(self):
        print("\n")
        print("Name = ",self.name)
        print("Mass (kg) = ",self.mass)
        print("Diameter (km)= ",self.diameter)
        print("Density (kg/m^3)= ",self.density)
        print("Gravity (m/sec^2)= ",self.gravity)
        print("Escape velocity (km/sec)= ",self.escapevelocity)
        print("Rotational period (hours)= ",self.rotationalperiod)
        print("Length of day (hours)= ",self.lengthofday)
        print("Distance from sun (km)= ",self.distancefromsun)
        print("Perihelion (km)= ",self.perihelion)
        print("Aphelion (km)= ",self.aphelion)
        print("Prbital Period (days)= ",self.orbitalperiod)
        print("Orbital Velocity (km/sec)= ",self.orbitalvelocity)
        print("Orbital Inclination (degrees)= ",self.orbitalinclination)
        print("Orbital Eccentricity = ",self.orbitaleccentricity)
        print("Obliquity to Orbit (degrees)= ",self.obliquitytoorbit)
        print("Mean Temperature C= ",self.meantemperature)
        print("Surface Pressure (bars)= ",self.surfacepressure)
        print("Number of Moons = ",self.numberofmoons)
        print("Ring System = ",self.ringsystem)
        print("Global magnetic field = ",self.globalmagneticfield)
        print("\n\n")


mercury=Planet("MERCURY",0.33,4879,5427,3.7,4.3,1407.6,4222.6,57.9,46,69.8,88,47.4,7,0.205,0.034,167,0,0,"No","Yes")
venus=Planet("VENUS",4.87,12104,5243,8.9,10.4,-5832.5,2802,108.2,107.5,108.9,224.7,35,3.4,0.007,177.4,464,92,0,"No","No")
earth=Planet("EARTH",5.97,12756,5514,9.8,11.2,23.9,24,149.6,147.1,152.1,365.2,29.8,0,0.017,23.4,15,1,1,"No","Yes")

moon=Planet("MOON",0.073,3475,3340,1.6,2.4,655.7,708.7,0.384,0.363,0.406,27.3,1.0,5.1,0.055,6.7,-20,0,0,"No","No")

mars=Planet("MARS",0.642,6792,3933,3.7,5,24.6,24.7,227.9,206.6,249.2,687,24.1,1.9,0.094,25.2,-65,0.01,2,"No","No")
jupiter=Planet("JUPITER",1898,142984,1326,23.1,59.5,9.9,9.9,778.6,740.5,816.6,4331,13.1,1.3,0.049,3.1,-110,SURFRACE_PRESSURE_UNKNOWN,79,"Yes","Yes")
saturn=Planet("SATURN",568,120536,687,9,35.5,10.7,10.7,1433.5,1352.6,1514.5,10747,9.7,2.5,0.057,26.7,-140,SURFRACE_PRESSURE_UNKNOWN,82,"Yes","Yes")
uranus=Planet("URANUS",86.8,51118,1271,8.7,21.3,-17.2,17.2,2872.5,2741.3,3003.6,30589,6.8,0.8,0.046,97.8,-195,SURFRACE_PRESSURE_UNKNOWN,27,"Yes","Yes")
neptune=Planet("NEPTUNE",102,49528,1638,11,23.5,16.1,16.1,4495.1,4444.5,4545.7,59800,5.4,1.8,0.011,28.3,-200,SURFRACE_PRESSURE_UNKNOWN,14,"Yes","Yes")
pluto=Planet("PLUTO",0.0146,2370,2095,0.7,1.3,-153.3,153.3,5906.4,4436.8,7375.9,90560,4.7,17.2,0.244,122.5,-225,1E-05,5,"No","Unknown")

mercury.print()
venus.print()
earth.print()
mars.print()
jupiter.print()
saturn.print()
uranus.print()
neptune.print()
pluto.print()
        
        
    



