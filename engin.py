import time
import os
import platform
import header_design as design
import student as st
import loding
import emoji

operating_system = platform.system()


class StartMain:

    # Main Function
    @staticmethod
    def main(self):
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')

        design.art('Student Management System')

        choice = input('Please enter your choice:\n'
                       '[1] Add student\n'
                       '[2] Show student database\n'
                       '[3] Exit the program\n'
                       '\n'
                       '--> ')
        if choice == '1':
            st.student_input()
        elif choice == '2':
            st.student_database()
        elif choice == '3':
            print()

            msg = (emoji.emojize('[☺] Thanks for using this program. See you soon.\n\n' + '\t' * 4 + 'Exiting:thumbs_up:'))
            for i in range(3):
                loding.load(msg)
            time.sleep(1)
            exit()
        else:
            print()
            print(emoji.emojize('[✘] Wrong Input!:upside-down_face:'))
            time.sleep(.50)
            StartMain().main(self)
