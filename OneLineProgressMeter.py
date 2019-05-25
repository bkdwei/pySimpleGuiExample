'''
Created on 2019年5月25日

@author: bkd
'''
import PySimpleGUI as sg      

for i in range(1000):      
    sg.OneLineProgressMeter('One Line Meter Example', i + 1, 1000, 'key')    
