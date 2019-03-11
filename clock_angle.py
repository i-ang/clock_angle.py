#Create a function that will calculate the angle between the
#minute and the hour arms of an Analog Clock.

#the MINUITE hand moves 6 degrees per minuite so
# angle_min = (6*m)

#the HOUR hand moves 0.5 degrees every minuite, as well as every HOUR
# so angle_hour = (0.5*m) + (h*60)*0.5

def angle(hr,min):
    ang = 0 #the angle value we return
    hr_ang = 0
    mn_ang = 0
    if(hr == 12):
        hr = 0
    if(min == 60):
        min = 0

    hr_ang = (0.5*min) + (60*hr)*0.5
    hr_min = (6*min)
    ang = abs(hr_ang - hr_min)
    #returning the smaller of 2 possible angles
    ang = min(360 - ang, ang)
    return ang

x = angle(13,30) #sample time
print(x)
