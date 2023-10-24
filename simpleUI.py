# pip install PySimpleGUI
# pip install pandas
# pip install openpyxl

from pathlib import Path
import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkAmber')

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'Data_Entry.xlsx'

df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('테스트 결과 입력시트 :')],
    [sg.Text('[1] Project', size=(15,1)), sg.InputText(key='Project')],
    [sg.Text('[2] Covering Option', size=(15,1)), sg.InputText(key='Seat_Option')],
    [sg.Text('[3] Row', size=(15,1)), sg.Combo(['1열', '2열', '3열'], key='Row')],
    [sg.Text('[4] Option', size=(15,1)),
        sg.Checkbox('VENT', key='Vent'),
        sg.Checkbox('HEATER', key='Heater'),
        sg.Checkbox('A/REST', key='ArmRest')],
    #[sg.Text('No. of Children', size=(15,1)), sg.Spin([i for i in range(0,16)],initial_value=0, key='Children')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('테스트 DATA 입력시트 Hip-point', layout) # 창표기 이름 

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)  # This will create the file if it doesn't exist
        sg.popup('Data saved!') 
        clear_input()
window.close()

