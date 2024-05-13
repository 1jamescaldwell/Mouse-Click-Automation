import pyautogui
import time
import os
import pygetwindow
import pyautogui

# Function to adjust mouse settings in Logi+ Options
def adjust_mouse_settings():
    # Click on Mouse Settings
    pyautogui.moveTo(996, 500, duration=1)  # Move the mouse cursor to the specified coordinates over 0.5 seconds
    pyautogui.click(996, 500)  # Replace with the actual coordinates
    time.sleep(1)  # Add a delay to allow the tab to load
    
    # Click on the Thumb Button
    pyautogui.moveTo(900, 575, duration=1)
    pyautogui.click(900, 575)  # Replace with the actual coordinates
    time.sleep(3)  # Add a delay to ensure the slider is clicked
    
    # Move to Scroll area
    pyautogui.moveTo(1400, 600, duration=1)
    pyautogui.click(1400,600)
    # Scroll down
    pyautogui.scroll(-1500)

    # Select minimize window
    pyautogui.moveTo(1400, 250, duration=1)
    pyautogui.click(1400,250)

def open_logi_options():
    # Replace the path with the actual path to the Logi+ Options executable
    # logi_options_path = "C:\\Program Files\\Logitech\\LogiOptions\\LogiOptions.exe"
    logi_options_path = "C:\\Program Files\\LogiOptionsPlus\\logioptionsplus.exe"
    
    if os.path.exists(logi_options_path):
        os.startfile(logi_options_path)
        return True
    else:
        print("Logi+ Options app not found.")
        return False

def bring_to_foreground():
    # Get the reference to the Logi+ Options window
    logi_window = pygetwindow.getWindowsWithTitle("LogiOptions") #[0]  # Assuming the window title is "LogiOptions"
    if logi_window:
        logi_window.activate()
    else:
        print("Logi+ Options window not found.")

def close_logi_options():
    pyautogui.hotkey('alt', 'f4')

if __name__ == "__main__":
    # Assume Logi+ Options app is already open
    if open_logi_options():
        print("Logi+ Options app opened successfully.")
        time.sleep(3)  # Add a short delay to ensure the application is fully loaded
        # bring_to_foreground()
        time.sleep(5)  # Add a short delay to ensure the application is fully loaded
        adjust_mouse_settings()

        close_logi_options()
