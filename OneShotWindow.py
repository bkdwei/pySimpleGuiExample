'''
Created on 2019年5月25日

@author: bkd
'''
import PySimpleGUI as sg    
  
layout = [[sg.Text('My one-shot window.')],
                 [sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

event, values = window.Read()    
window.Close()

text_input = values[0]    
print(text_input)
