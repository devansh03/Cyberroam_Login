# ITS ENABLES THE USE OF MOUSE AND KEYBOARD.
import pyautogui

# ITS ENABLES US TO MAKE THE PROGRAM SLEEP i.e. WAIT FOR SOME TIME.
import time

# print (pyautogui.size())   ==> This can be used by you to know the screen size of your desktop.

# This should be used by you to know exact position of your cursor.
print (pyautogui.position())

# This is used to move your cursor to your Browser Icon.
pyautogui.moveTo(78,448)
pyautogui.click(78,448)
# I use Ubuntu and have my browser on launcher, so my browser icon position has such readings.
# It might change from every laptop to laptop, so you should first know the position of your browser icon, the change the code accordingly.

# To make the program wait. This will reduce the chances of error and make the program efficient.
time.sleep(0.5)

# These commands are to move your cursor to the Address Bar where we will have to type the url.
# Again, use your pyautogui.position beforehand to find the position of your Address Bar where we will have to click. These values might differ for each laptop.
pyautogui.moveTo(2669,136)
pyautogui.click(2669,136)
pyautogui.click(2669,136)
pyautogui.click(2669,136)
# We click three times so as to avoid any errors. In all browsers, on clicking three times selects the entire url which was already there or selects the empty Address Bar.

# Using the pyautogui.typewrite , we enable the use of keyboard and the string entered in it is typed.
pyautogui.typewrite("https://172.16.1.1:8090/httpclient.html?u=http://www.msftconnecttest.com/redirect")
# The String here is the string for Cyberroam Login Site for BIT Mesra Students.

time.sleep(0.5)

# The enter key on the keyboard should be typed to enter the url and get to the site.
pyautogui.press('enter')

time.sleep(0.5)

# This is done to move the cursor to the Username TextField and click there so we can type our username.
pyautogui.moveTo(1851,791)
pyautogui.click(1851,791)
# Again, use your pyautogui.position beforehand to find the position of your Address Bar where we will have to click. These values might differ for each laptop.

time.sleep(0.5)

# In the string here write your username i.e. your Cyberroam Login ID.
pyautogui.typewrite("Type your username here")

time.sleep(0.5)

# This is done to move the cursor to the Password TextField and click there so we can type our password.
pyautogui.moveTo(1875,888)
pyautogui.click(1875,888)
# Again, use your pyautogui.position beforehand to find the position of your Address Bar where we will have to click. These values might differ for each laptop.

time.sleep(0.5)

# In the string here write your password i.e. your Cyberroam Login Password.
pyautogui.typewrite("Type your password here")

time.sleep(0.5)

# This is done to move the cursor to the Login Button and click there so we can type complete the process of logging in.
pyautogui.moveTo(1708,939)
pyautogui.click(1708,939)
# Again, use your pyautogui.position beforehand to find the position of your Address Bar where we will have to click. These values might differ for each laptop.









