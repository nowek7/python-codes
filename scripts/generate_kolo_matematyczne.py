#!/usr/bin/python

import os
import re
import sys

COUNT_TASKS_PER_CLASS_ID = 2

def help():
    text = '''
    Generator szablonu pojedynczej serii zadań dla koła matematycznego.
    \n
    Poprawna kolejność argumentów must-have
    \t python generate-kolo-matematyczne.py numer_serii rok_szkolny katalog_zapisu
    \n
    Opcjonalne jest ścieżek do pliku tex z paczkami. Domyślnie są "C:/users/public/inputNaszePakiety" i "C:/users/public/input/MakraKoloMatematyczne". Możliwe jest dodanie wiele ścieżek.
    \n
    \t python generate-kolo-matematyczne.py numer_serii rok_szkolny -p D:/tex/input/NaszePakietyD:/tex/input/MakraKoloMatematyczne
    \n
    Wszelkie propozycje zmian mile widziane. Wszystkie pytanie najlepiej pisać do Michała -> novvak.michal04@gmail.com
    '''

    print(text)
    sys.exit(0)


def get_header() -> str:
    return r'\documentclass[a4paper,12pt]{mwart}'

def get_styles() -> str:
    return r'''
    \marginsize{2cm}{2cm}{0.6cm}{0.6cm}
    \setlength{\tabcolsep}{0.6mm}

    %\usepackage{showframe}

    \pagestyle{empty}
    %\pagestyle{fancyplain}
    \lhead[ \fancyplain { } { } ]
        { \fancyplain { } {                     } }
    \rhead[ \fancyplain { } {                     } ]
        { \fancyplain { } { } }
    \chead[ \fancyplain { } {\textbf{UWAGA!} NASTĘPNE  KOŁO MATEMATYCZNE:  7. LISTOPADA 2019} ]
        { \fancyplain { } {\textbf{UWAGA!} NASTĘPNE  KOŁO MATEMATYCZNE:  7. LISTOPADA 2019} }
    \cfoot[ ]{ }
    '''

def generate_file(serial_number: int, school_year: str, dest_directory: str, package_paths: list = []):
    if not package_paths:
        package_paths = [
            'C:/users/public/input/NaszePakiety',
            'C:/users/public/input/MakraKoloMatematyczne'
        ]

    # Preambula
    content = f'% Koło matematyczne w Szczecinie - {school_year} - seria 0{serial_number} \n'
    content += get_header()
    content += '\n'

    for path in package_paths:
        content += f'\input{{{path}}} \n'

    content += get_styles().strip()
    content += '\n'

    # Document
    content += f'\\begin{{document}} \n'

    for i in range(COUNT_TASKS_PER_CLASS_ID):
        for class_id in ['III', 'IV', 'V', 'VI']:
            content += r'''
                \Tytul{{SZCZECINIE}}{{ {0} }}{{1}}
                \vspace{{2mm}}

                \begin{{Zadania}}\itemsep=3mm
            '''.format(class_id)
            for num_item in range(1, 10):
                content += f'''
                    % {0}
                    \item \n
                '''.format(num_item)
            content += f'\end{{Zadania}} \n'

            if i == 1 and class_id != 'VI':
                content += f'\\newpage \n'

    content += r'\end{document}'

    if not os.path.isdir(dest_directory):
        os.mkdir(dest_directory)

    file_name = f'{dest_directory}/seria_0{serial_number}.tex'
    with open(file_name, 'w+') as tex_file:
        tex_file.write(content)

if __name__ == "__main__":
    arguments = sys.argv[1:]

    if len(arguments) < 3:
        help()

    serial_number = arguments[0]
    school_year = arguments[1]
    dest_directory = arguments[2]

    package_paths = []
    if (len(arguments) > 3 and arguments[3] == '-p'):
        package_paths = arguments[4:]

    generate_file(serial_number, school_year, dest_directory, package_paths)