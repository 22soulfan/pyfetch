# PyFetch
A neofetch-inspired utility module that is coded in Python and used for specialized operating systems.

## What is PyFetch?
PyFetch is a neofetch-inspired utility that will be used by ArryanOS, WhirlyOS, OpenMyriad, and Lynux Webs.

Unlike neofetch which uses the bash programming language, pyfetch uses the Python programming language and the os module.

PyFetch will be only preinstalled in the four operating systems mentioned.

To run pyfetch, make sure you have python3 installed. Type in the terminal python3, then type import pyfetch to load the module. After that create a = PyFetch(), then type a.pyfetch() to load the
utility.

## How to use
![Screenshot](Screenshots/Screenshot%20from%202026-06-01%2015-54-40.png)

> Note that the module is a simulator, but we will try to use the os module.
1. Download the pyfetch.py from the Releases page.
2. In the terminal, type the commands
   - On Windows:
     If you have Python IDLE installed, go to File > Run Module, and go to the location where you download the pyfetch script then execute.
     Type this command:
     ``` bash
     from pyfetch import *
     ```
     Then type the following commands:
     ``` bash
     py = pyfetch("Sys")
     py.utility()
     ```
   - On Linux or macOS:
     In the file explorer, go to the location where you download the pyfetch script, right-click an empty area, then click Run In Terminal and typing python3.
     Type these commands:
     ``` bash
     from pyfetch import *
     py = pyfetch("Sys")
     py.utility()
     ```     
