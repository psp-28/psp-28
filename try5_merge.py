# Final code... Trial


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import json
import os
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import pyautogui
import threading


if __name__ == "__main__":
    

    # Initialize the Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized

    # Set up the WebDriver
    service = Service(ChromeDriverManager().install())  # Automatically download and use the appropriate ChromeDriver


    prefs = {
            "printing.print_preview_sticky_settings.appState": json.dumps({
                "recentDestinations": [
                    {
                        "id": "Save as PDF",
                        "origin": "local",
                        "account": "",
                    }
                ],
                "selectedDestinationId": "Save as PDF",
                "version": 2,
                "pageSize": "Tabloid",
                "layout": 0,  # 0 for Portrait, 1 for Landscape
                "marginsType": 2,  # 0 for Default, 1 for None, 2 for Minimum
                "scalingType": 3,  # 3 for Default
                "scaling": "53",
                "isHeaderFooterEnabled": False,
                "isBackgroundGraphicsEnabled": True,
            }),
            # "savefile.default_directory": download_folder,  # Path to save the PDF directly.
            # "savefile.filename": "Cybersec Incident Report.pdf",  # Ensure the file name is auto-generated
            # "savefile.directory": download_folder,  # Ensure it saves to the desired directory
            # "print.always_print_silent": True,  # Auto print silently without dialog
            # "print.show_print_progress": False,  # Disable print progress
            # "download.prompt_for_download": False,  # Disable download prompt
            # "download.directory_upgrade": True,  # Automatically download to the specified folder
            # "safebrowsing.enabled": True  # Enable safe browsing for downloads
        }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=service, options=chrome_options)
        # driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
        
        
        


    ##################   TIMER   ##########################

    def show_timer_dialog():
        def update_timer(remaining_time, dialog, label):
            if remaining_time >= 30:
                label.config(text=f"Printing Page in: {remaining_time} seconds")
                dialog.after(1000, update_timer, remaining_time - 1, dialog, label)
            else:
                dialog.destroy()  # Close the window when the countdown is done
                dialog.quit()

        def update_timer2(remaining_time, dialog, label):
            if remaining_time >= 0:
                label.config(text=f"Printing Page in: {remaining_time} seconds")
                dialog.after(1000, update_timer2, remaining_time - 1, dialog, label)
            else:
                dialog.destroy()  # Close the window when the countdown is done
                dialog.quit()

        # Expose the update_timer and update_timer2 functions for later use
        return {
            "update_timer": lambda: _start_timer(update_timer, 80),
            "update_timer2": lambda: _start_timer(update_timer2, 30),
        }

    def _start_timer(timer_function, remaining_time):
        # Create a new Tkinter window
        dialog = tk.Tk()
        dialog.title("Countdown Timer")
        dialog.geometry("420x150")  # Set the size of the window

        # Add a label to show the countdown
        label = tk.Label(dialog, text="Print", font=("Arial", 13))
        label.pack(pady=20)

        # Start the timer
        timer_function(remaining_time, dialog, label)

        # Run the Tkinter event loop
        dialog.mainloop()



    # Get the timer functions

    # fun_call_timer = show_timer_dialog()
    # fun_call_timer["update_timer"]()        # call first timer
    # fun_call_timer["update_timer2"]()       #call second timer


    # Show the dialog
    # show_timer_dialog()


    #####################################


            
    def page_scroll():
        """"Pressing tab to scroll down the page"""
        
        # pyautogui.press("down", presses=4, interval=0.5)
        # pyautogui.press("up", presses=4, interval=0.5)
        pyautogui.press("tab", presses=55, interval=0.1)
        
    def page_scroll_thread():
        
        page_scrolling_thread = threading.Thread(target=page_scroll)
        page_scrolling_thread.start()
        return page_scrolling_thread



    root = None

    # Function to prompt user for credentials with a styled Tkinter UI
    def get_credentials():
        
        global root
        
        username = None
        password = None
        
        # Create the main window
        root = tk.Tk()
        root.title("Login")
        root.geometry("720x500")  # Set window size

        # Set the background color of the window (no image)
        root.configure(bg="#9FB6F5")

        # Create a frame for input fields
        frame = tk.Frame(root, bg="#9FB6F5", bd=5, relief="solid", padx=10, pady=10)
        frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.3, anchor="center")

        # Add padding inside the frame
        padding = 10

        # Username Label and Entry
        username_label = tk.Label(frame, text="Username:", font=("Arial", 12), bg="#9FB6F5")
        username_label.grid(row=0, column=0, padx=padding, pady=padding)
        username_entry = tk.Entry(frame, font=("Arial", 12))
        username_entry.grid(row=0, column=1, padx=padding, pady=padding)

        # Password Label and Entry
        password_label = tk.Label(frame, text="Password:", font=("Arial", 12), bg="#9FB6F5")
        password_label.grid(row=1, column=0, padx=padding, pady=padding)
        password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
        password_entry.grid(row=1, column=1, padx=padding, pady=padding)

        # Regex for username validation
        username_regex = r"^[a-zA-Z0-9._%+-]+@totalstart\.onmicrosoft\.com$"

        # Variables to store username and password
        username, password = None, None

        # Flag to track if the form is submitted correctly
        valid_credentials = False

        def submit():
            nonlocal valid_credentials, username, password

            # Get the username and password from the fields
            username = username_entry.get()
            password = password_entry.get()

            # Validate the username using regex
            if not re.match(username_regex, username):
                messagebox.showwarning("Input Error", "Please enter a valid username in the format 'Demo@total.onmicrosoft.com'")
                return
            
            if not username or not password:
                messagebox.showwarning("Input Error", "Please enter both username and password")
                return

            # Mark the credentials as valid and close the window
            valid_credentials = True
            root.quit()  # Close the Tkinter window after submission

        # Submit Button
        submit_button = tk.Button(root, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white", command=submit)
        submit_button.place(relx=0.5, rely=0.85, anchor="center")
        # Bind the Enter key to the submit function
        root.bind("<Return>", lambda event: submit())
        # Start the Tkinter main loop               
        root.mainloop()

        # Return username and password if valid credentials were provided
        if valid_credentials:
            print(f"Credentials captured")
            return username, password
        else:
            print("No valid credentials entered or user canceled")
            return None, None





    def destroy_login():
        """This will be used to destry the get_credentials() method, I can use this method directly in other method."""
        global root
        if root is not None:
            print("Closing the get_credentials window from automate")
            root.quit()  # Stops the Tkinter mainloop
            root.destroy()  # Destroys the Tkinter window
        else:
            print("No active Tkinter window to close.")
            

            


    def Print_function():


        try: 
            
            # Trigger the print dialog programmatically (CTRL + P)
            pyautogui.hotkey("ctrl", "p")
            
            # Pause briefly to allow the print dialog to open
            time.sleep(5)

            # Automate the print dialog settings using PyAutoGUI
            print("Automating print dialog settings...")

            # Wait for the print dialog to appear
            time.sleep(3)

            # 1. Select "Save as PDF"
            pyautogui.press("tab", presses=5, interval=0.3)  # Navigate to the Destination field
            
            
            max_options = 10  # Maximum expected options in the drop-down
            for i in range(max_options - 1):  # Loop one less than the total options
                pyautogui.press("down")
                time.sleep(0.5)
            
            pyautogui.typewrite("Save as PDF", interval=0.05)  # Type "Save as PDF"
            pyautogui.press("tab", presses=2, interval=0.5)
            pyautogui.press("enter", interval=0.5)
            pyautogui.press("esc", interval=0.5)
            time.sleep(0.5)

            # 2. Select Pages as "All"     
            pyautogui.press("tab", presses=1, interval=0.2)
            pyautogui.typewrite("All", interval=0.1)  # Type "All"
            time.sleep(0.5)
            
            # 3. Select Layout as "Portrait"
            pyautogui.press("tab", presses=1, interval=0.2)
            pyautogui.typewrite("Portrait", interval=0.1)  # Type "Portrait"
            time.sleep(0.5)

            # 4. Open More Settings (expand options)
            pyautogui.press("tab", presses=1, interval=0.2)
            pyautogui.press("space")  # Expand the More Settings section
            time.sleep(0.5)
            
            # 5. Select Paper size as "Tabloid"
            pyautogui.press("tab", presses=1, interval=0.2)
            pyautogui.typewrite("Tabloid", interval=0.1)  # Type "Tabloid"
            time.sleep(0.5)
            
            # 6. Select Margins as "None"
            pyautogui.press("tab", presses=2, interval=0.2)
            pyautogui.typewrite("None", interval=0.1)  # Type "None"
            time.sleep(1)

            # 7. Select Scale as "Custom"
            pyautogui.press("tab", presses=1, interval=0.2)
            pyautogui.typewrite("Custom", interval=0.5)  # Type "Custom"
            time.sleep(0.5)
            
            # Set custom scale value
            pyautogui.press("tab", presses=1, interval=0.4)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite('53')
            time.sleep(0.5)
            
            # 8. Enable Background graphics
            pyautogui.press("tab", presses=1, interval=0.4)
            pyautogui.press("space")  # Enable background graphics
            
        
            time.sleep(5)
            
            # 9. Trigger Save without the Save As dialog appearing
            pyautogui.press("tab", presses=1, interval=0.5)
            pyautogui.press("enter")  # PDF should automatically save without the dialog
            
            time.sleep(5)

            username = os.getlogin()
            file_name = "START - Cybersec Incident Report.pdf"
            file_path = rf"C:\Users\{username}\Downloads"
            pyautogui.typewrite(file_name,interval=0.05)
            pyautogui.press("tab", presses=7, interval=0.4)
            pyautogui.press("enter")
            pyautogui.typewrite(file_path, interval=0.1)
            pyautogui.press("enter")
            
            pyautogui.alert(rf"Click on the 'Save' button to save the file. \nPDF file downloded at file location: \n{file_path}")
            
            while not os.path.exists(file_path):
                time.sleep(3)
                # driver.quit()
            time.sleep(10)

        finally:
            # Ensure the browser is only closed after the PDF is generated
            print("Closing the browser after saving the PDF.")
            # driver.quit()




    def automate():
        
        try:
            
            popup = tk.Tk()
            popup.title("PDF Export")
            message_label = tk.Label(popup, text="Notification \n\n\nDo not touch your PC, until automation task ends", font=("Helvetica", 16))
            message_label.pack(pady=20)
            popup.after(6000, popup.destroy)
            popup.mainloop()
            
            
            
            username, password = get_credentials()

            # Check if credentials are valid
            if username is None or password is None:
                raise ValueError("Invalid credentials provided or user canceled")

            # chrome_options = Options()
            # chrome_options.add_argument("--start-maximized")  # Start browser maximized

            # # Set up the WebDriver
            # service = Service(ChromeDriverManager().install())  # Automatically download and use the appropriate ChromeDriver
            # driver = webdriver.Chrome(service=service, options=chrome_options)

        # try:
            

            
            wait = WebDriverWait(driver, 100)  # Wait for a max 100 seconds

            driver.get("https://myapplications.microsoft.com/")  # Replace with your actual URL
            wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@id='i0116']"))).click()    
            wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@id='i0116']"))).send_keys(username)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@id='idSIButton9']"))).click()
            time.sleep(5)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@id='i0118']"))).send_keys(password)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@id='idSIButton9']"))).click()
            time.sleep(5)
            destroy_login()
            wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@id='KmsiCheckboxField']"))).click()
            wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@id='idSIButton9']"))).click()
            time.sleep(2)

            print("User logged in successfully!")
            
            
            
            SNOW_url = "https://launcher.myapps.microsoft.com/api/signin/599447f7-6c65-4c14-95ef-01e2d61b89a3?tenantId=877d0bbe-a3ee-4968-971e-1941530ea8c8"  # Replace with the desired URL
            driver.get(SNOW_url)
            time.sleep(30)
            url2 = "https://startsn.service-now.com/now/nav/ui/classic/params/target/%24pa_dashboard.do%3Fsysparm_dashboard%3D4abb6ffb47d51a10bd36cd84f26d431b"
            driver.get(url2)
            
            time.sleep(10)
            
            fun_call_timer = show_timer_dialog()        # I am call timer
            fun_call_timer["update_timer"]()
            page_scroll_thread()                        # pausing timer for 5 second to press tabs to scroll down the page
            fun_call_timer["update_timer2"]()           # Again run timer.
            

            # driver.execute_script("document.elementFromPoint(294.896, 48).click();")
            time.sleep(2)
            # time.sleep(50)
            
            Print_function()
        



        except Exception as e:
            print(f"An error occurred: {e}")


    automate()









            