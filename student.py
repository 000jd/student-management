import os
import platform
import csv
import time
from prettytable import from_csv
import header_design as design
import engin
import loding
import emoji

operating_system = platform.system()


def id_generator():
    id_list = []
    default_id = 1
    try:
        with open('student_database.csv', 'r') as file:
            data = csv.reader(file)
            for student_id in data:
                id_list.append(student_id[0])
            student_id = int(id_list[-1]) + 1
            return student_id
    except Exception as e:
        return default_id


# Adding New Student
def student_input():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')

    design.art('New Student Form')
    student_id = id_generator()
    first_name = input('[+] Enter first name: ')
    last_name = input('[+] Enter last name: ')
    age = input('[+] Enter age: ')
    gender = input('[+] Enter gender: ')
    department = input('[+] Enter department: ')

    while True:
        confirm = input('\n[!] Do you want to save? (y/n): ').lower()
        if confirm == 'y':
            name = first_name + ' ' + last_name

            # Saving information
            with open('student_database.csv', 'a', newline='') as file:
                data = csv.writer(file)
                data.writerow([student_id, name, age, gender, department])
            print()

            msg = '[!] Please wait. \n\n' + '\t' * 4 + 'Saving'
            for i in range(5):
                loding.load(msg)
            print(emoji.emojize('\n[✔] Saved:thumbs_up:'))
            time.sleep(.5)

            engin.StartMain.main(self='self')
            break
        elif confirm == 'n':
            print()
            msg = (emoji.emojize('\t' * 4 + '[!] Please wait:grinning_face_with_big_eyes:'))
            for i in range(5):
                loding.load(msg)
            time.sleep(.5)
            engin.StartMain.main(self='self')
            break
        else:
            print()
            print(emoji.emojize('[X] Wrong Input!:upside-down_face:'))
            time.sleep(.50)


# Show student database
def student_database():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')
    design.art('Student Database')

    try:
        with open('student_database.csv', 'r') as fr:
            data_table = from_csv(fr, field_names=['Student ID', 'Student Name', 'Age', 'Gender', 'Department'])

        # Show student database
        print(data_table)
    except Exception as e:
        print(e)
        print(emoji.emojize('\nempty database. Please add some student first..\n:grinning_face_with_big_eyes:'))

    choice = input('\nPlease enter your choice:\n'
                   '[1] Main Menu\n'
                   '\n'
                   '--> ')

    if choice == '1':
        engin.StartMain.main(self='self')
    else:
        print()
        print('[X] Wrong Input!')
        time.sleep(.50)
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')
        student_database()
