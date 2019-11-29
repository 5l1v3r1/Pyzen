
# pyzen
# Copyright (C) 2018-2019 M.Anish <aneesh25861@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

''' This is a simple python3 library developed by M.Anish to create simple GUI using zenity for linux'''

try:

  import os
  import platform

except ImportError:

  print('\nCritical Error: Required Modules are Missing!\n\nPress any key to continue...')
  x=input()

if platform.system().lower()!='linux':
   print('\nSorry:This Module works for Linux only!\n\nPress any key to continue...')
   x=input()

if os.system('zenity --help>temp.log')!=0:
   os.remove('temp.log')

# prints Error Message in a GUI form.
def error(msg):
    i=os.system('zenity --error --title "ERROR!" --text '+msg)

# prints Information Message in a GUI form.
def info(msg):
    i=os.system('zenity --info  --text '+msg)

# prints Warning Message in a GUI form.
def warn(msg):
    i=os.system('zenity --warning  --text '+msg)

# Gives a Notification
def notify(msg):
    i=os.system('zenity --notification --text '+msg)

# GUI form to ask yes or no questions returns 0 if yes else 1 for no.
def question(msg):
    msg=list(msg)
    for i in range(len(msg)):
        if msg[i]==' ':
           msg[i]='\ '
    msg=''.join(msg)
    i=os.system('zenity --question --text '+msg)
    if i!=0:
       return 1
    return 0

# Used to select a file using GUI.
def selectfile():
    i=os.system('zenity --file-selection>temp.log')
    if os.path.exists('temp.log'):
       with open('temp.log','r') as f:
            buff=f.read().strip()
       os.remove('temp.log')
       return buff

# Used to print License.
def license(file):
    i=os.system('zenity --text-info --title "LICENSE" --filename='+file+' --checkbox="I have read and accept the terms"')

# Used to select a Date using Calendar.    
def calendar():
    i=os.system('zenity --calendar --title="Calendar">temp.log')
    if os.path.exists('temp.log'):
       with open('temp.log','r') as f:
            buff=f.read().strip()
            buff=buff[3:6]+buff[0:3]+buff[6:]
       os.remove('temp.log')
       return buff
