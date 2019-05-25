'''
Created on 2019年5月25日

@author: bkd
'''
import PySimpleGUI as sg      

layout = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
         [sg.InputText(), sg.FileBrowse()],
         [sg.Submit(), sg.Cancel()]]      

(event, (source_filename,)) = sg.Window('SHA-1 & 256 Hash', layout).Read()  

print(event, source_filename)  
