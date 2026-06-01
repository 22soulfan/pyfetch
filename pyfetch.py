''' PyFetch is a neofetch-inspired utility that will be used by
ArryanOS, WhirlyOS, OpenMyriad, and Lynux Webs.

Unlike neofetch which uses the bash programming language, pyfetch
uses the Python programming language and the os module.

PyFetch will be only preinstalled in the four operating systems
mentioned.

To run pyfetch, make sure you have python3 installed. Type in the
terminal python3, then type import pyfetch to load the module.
After that create a = PyFetch(), then type a.pyfetch() to load the
utility.

'''
import os # This is the most important component to load
''' The pyfetch logo used in this project is the upcoming ArryanOS
logo.'''

# define the values
operating_system = ""
host_name = ""
kernel_type = ""
uptime = ""
packages = ""
shell_type = ""
screen_size = ""
terminal_type = ""
cpu = ""
graphics_card = ""
memory = ""
# create a class called pyfetch
class pyfetch:
    def __init__(self, sys):
        print("Welcome")
    def utility(self):
        # We're using the ArryanOS logo
        print('''
////    ////    ////    ////    %s@lynuxwebs
    ////    ////    ////        ------------------------
        ////    ////            OS: Lynux Webs v0.1 Alpha
            ////                Host: MsTarantula
        ////    ////            Kernel: 0.0.1-python
    ////    ////    ////        Uptime: %s mins
////    ////    ////    ////    Packages: 2 (bee)
    ////    ////    ////        Shell: pyshell 0.0.1
        ////    ////            Resolution: 1366x768
            ////                Terminal: pyterminal
        ////    ////            CPU: RSA Raven NexT 1st Generation
    ////    ////    ////        GPU: RSA Froen Video 4th Generation
                                Memory: 1000MiB / 12000MiB

                           
''')


        
