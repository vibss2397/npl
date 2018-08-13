import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import loading

def convert_arduino_to_number(line2):
    str1=line2.split(' c')[0]
    str2=line2.split('g: ')[1].split('g')[0]
    return str1,str2


def start_draw():
    axes = plt.gca()
    axes.set_xlim(0, 20)
    axes.set_ylim(-5, +50)
    axes.set_xlabel('time') ; axes.set_ylabel('weight')
    line, = axes.plot([], [],marker='o',linewidth=1.3, color='#17A2B8',markersize=3)
    return line,axes

def update_graph(a,b,lin,ax,count):
    xdata.append(a)
    ydata.append(b)
    xmin, xmax = ax.get_xlim()
    if b >= xmax:
        ax.set_xlim(xmin, (2)*xmax)
        ax.relim()
        ax.autoscale_view()
    plt.title(r'$Mass : %.3f g$'%(a),loc='right', fontsize=10)
    lin.set_xdata(ydata)
    lin.set_ydata(xdata)
    plt.draw()



def main(time_tot,counter,tot_list,xdata,ydata):
    with serial.Serial('Com3', 9600) as ser:
        print('Setting Up Arduino')
        t1=time.time()
        while(time_tot<5):
            if(counter<4):
                loading.loading_dots()
            ser.readline()
            counter+=1
            t2=time.time()
            time_tot+=t2-t1
            t1=t2
            counter+=1
        plt.show()
        line,axes=start_draw()
        temp_arr=np.zeros((2))
        calib_factor=ser.readline().decode("utf-8").split('g ')[-1]
        print(calib_factor)
        t3=time.time()
        while True:
            if(counter%10==0):
                np.save('readings.npy', np.array(tot_list))
            a,b=convert_arduino_to_number(ser.readline().decode("utf-8"))
            t4=time.time()
            temp_arr[0]=b
            temp_arr[1]=(t4-t3)
            tot_list.append(temp_arr)
            update_graph(temp_arr[0],temp_arr[1],line,axes,counter)
            plt.pause(1e-17)
            time.sleep(1)
            print(a)
            counter+=1

if __name__ == '__main__':
    time_tot,counter=0,0
    tot_list,xdata,ydata=[],[],[]
    main(time_tot,counter,tot_list,xdata,ydata)
