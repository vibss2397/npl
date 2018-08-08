# use this script to calibrate the hx711 cell using python
# the setting that worked best for me till now was -5818.2 as a calibration factor,
# but i was using a mass balance of 300g loadcell
# for 50kg use -96500 but try different values as per your convinience
import serial
import time


def main():
    time_tot=0
    counter=0
    comm_port='Com3'
    channel=9600
    with serial.Serial(comm_port, channel) as ser:
        print('setting up arduino...')
        t1=time.time()
        while(time_tot<4):
            ser.readline()
            t2=time.time()
            time_tot+=t2-t1
            t1=t2
        while True:
            if(counter>0 and counter%10==0):
                print('do you want to change calibration factor \n')
                print('press a,s,d,f to increase it by a factor of 10,100,1000,10000')
                print('press z,x to decrease it by a factor of 10,100,1000,10000')
                print('press w if not to change')
                callib=input()
                if(callib=='a' or callib=='s' or callib=='d' or callib=='f' or callib=='z' or callib=='x' or callib=='c' or callib=='v'):
                    ser.write(callib.encode('ASCII'))
                elif(callib=='w'):
                    print('proceeding')
                else:
                    print('not a valid key, try again in a "bit" :)')
            print(ser.readline().decode('utf-8'))
            counter+=1

if __name__=='__main__':
    main()
