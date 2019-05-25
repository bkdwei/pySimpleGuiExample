'''
Created on 2019年5月25日

@author: bkd

Very basic window.  Return values as a list      

'''
import PySimpleGUI as sg  
 
layout = [      
         [sg.Text('Please enter your Name, Address, Phone')],
         [sg.Text('Name', size=(15, 1)), sg.InputText()],
         [sg.Text('Address', size=(15, 1)), sg.InputText()],
         [sg.Text('Phone', size=(15, 1)), sg.InputText()],
         [sg.Submit(), sg.Cancel()]      
        ]      

window = sg.Window('Simple data entry window', layout)  
event, values = window.Read()   
window.Close()
print(event, values[0], values[1], values[2])  
    
