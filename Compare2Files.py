'''
Created on 2019年5月25日

@author: bkd
'''
import PySimpleGUI as sg      

layout = [[sg.Text('Enter 2 files to comare')],
             [sg.Text('File 1', size=(8, 1)), sg.InputText(), sg.FileBrowse()],
             [sg.Text('File 2', size=(8, 1)), sg.InputText(), sg.FileBrowse()],
             [sg.Submit(), sg.Cancel()]]      

window = sg.Window('File Compare', layout)  

event, values = window.Read()  
window.Close()
print(event, values)      
