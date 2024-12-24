import subprocess
import time
import pyautogui
import pygetwindow as gw

screen_width, screen_height = pyautogui.size()

pyautogui.FAILSAFE = False

app_name = "airreceiver" # airreceiver app

subprocess.Popen(["start", app_name], shell=True)

time.sleep(5)

windows = gw.getWindowsWithTitle(app_name)

if windows:
    app_window = windows[0]

    app_window_center_x = app_window.left + app_window.width // 2
    app_window_center_y = app_window.top + app_window.height // 2

    if app_window_center_x < 10:
        app_window_center_x = 10
    if app_window_center_x > screen_width - 10:
        app_window_center_x = screen_width - 10
    if app_window_center_y < 10:
        app_window_center_y = 10
    if app_window_center_y > screen_height - 10:
        app_window_center_y = screen_height - 10

    pyautogui.moveTo(app_window_center_x, app_window_center_y)

    if not app_window.isMaximized:
        app_window.maximize()

    pyautogui.doubleClick(x=app_window_center_x, y=app_window_center_y)

    time.sleep(2)
    pyautogui.moveTo(-100, -100)
