import PySimpleGUI as sg
from pathlib import Path

smileys = [
    'happy', [':)', 'xD', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'other', [':3']
]

smiley_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Add', smileys]
]

sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key='-DOCNAME-')],
    [sg.Multiline(no_scrollbar=True, size=(40, 30), key='-TEXTBOX-')]
]

window = sg.Window('Text editor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Open':
        file_path = sg.popup_get_file('open', no_window=True)
        if file_path:
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text())
            window['-DOCNAME-'].update(file.name)

    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window=True, save_as=True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file.name)

    if event == 'Word Count':
        text = values['-TEXTBOX-'].replace('\n', ' ')
        word_count = len(text.split(" "))
        char_count = len(text.replace(' ', ''))
        sg.Popup(f"Number of words: {word_count}\n"
                 f"Number of chars: {char_count}")

    if event in smiley_events:
        updated_text = values['-TEXTBOX-'] + f" {event}"
        window['-TEXTBOX-'].Update(updated_text)

window.close()