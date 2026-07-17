from scanner import Scanner

from organizer import Organizer

from report import print_report

files = Scanner().scan()

groups = Organizer().build(

    files

)

print_report(

    groups

)
