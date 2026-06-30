import os, subprocess, winreg, ctypes, neotkinter as ntk

# reg values
Registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
key = winreg.OpenKey(Registry,
                      "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
value, regtype = winreg.QueryValueEx(key, "SystemUsesLightTheme")
print(value)
winreg.CloseKey(key)

def shellApps():
    subprocess.run(["Explorer", "Shell:AppsFolder"])

def godMode():
    subprocess.run("start shell:::{ED7BA470-8E54-465E-825C-99712043E01C}", shell=True)

def run():
    subprocess.run(["explorer", "Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"])

def startMenu():
    subprocess.run(["explorer", "Shell:Programs"])

def desktop():
    subprocess.run(["explorer", "Shell:Desktop"])

def globalDesktop():
    subprocess.run(["explorer", "Shell:Common Desktop"])

def shutdown():
    os.system("shutdown -t 0")

def logout():
    os.system("shutdown /l")

def restart():
    os.system("shutdown -r -t 0")

def winDir():
    subprocess.run(["explorer", "Shell:Windows"])

def progFiles():
    subprocess.run(["explorer", "Shell:ProgramFiles"])

def progFiles64():
    subprocess.run(["explorer", "Shell:ProgramFilesX64"])

def progFiles86():
    subprocess.run(["explorer", "Shell:ProgramFilesX86"])

def sys32():
    subprocess.run(["explorer", "Shell:System"])

def modifyPrograms():
    subprocess.run(["explorer", "Shell:ChangeRemoveProgramsFolder"])

def ctrlPanel():
    subprocess.run(["explorer", "Shell:ControlPanelFolder"])

def startup():
    subprocess.run(["explorer", "Shell:Startup"])

def globalStartup():
    subprocess.run(["explorer", "Shell:Common Startup"])

def cmd32():
    subprocess.Popen("C:\\Windows\\System32\\cmd.exe")

def setWallpaper():
    path = ntk.filedialog.askopenfile(initialdir="/", title="Select an image", filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg*"), ("JPEG Files", "*.jpeg*")))
    path = path.name

    # Constants for setting the wallpaper
    SPI_SETDESKWALLPAPER = 20  # Action to change wallpaper
    SPIF_UPDATEINIFILE = 0x01  # Update user profile
    SPIF_SENDWININICHANGE = 0x02  # Notify change to system

    try:
        # Call Windows API to change wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
        return True
    except Exception as e:
        # Print error message if wallpaper change fails
        print(f"Error changing wallpaper: {e}")
        return False

def setDarkMode():
    keyPath = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        # Open the key for setting values
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        keyPath,
        0,
        winreg.KEY_SET_VALUE
    )
    
    winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, 0)
    
    winreg.CloseKey(key)
    os.system("taskkill /F /IM explorer.exe")
    os.system("start explorer.exe")

def setLightMode():
    keyPath = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        # Open the key for setting values
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        keyPath,
        0,
        winreg.KEY_SET_VALUE
    )
    
    winreg.SetValueEx(key, "AppsUseLightTheme", 1, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, "SystemUsesLightTheme", 1, winreg.REG_DWORD, 1)
    
    winreg.CloseKey(key)
    os.system("taskkill /F /IM explorer.exe")
    os.system("start explorer.exe")

def setTransparency1():
    keyPath = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        # Open the key for setting values
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        keyPath,
        0,
        winreg.KEY_SET_VALUE
    )
            
    winreg.SetValueEx(key, "EnableTransparency", 1, winreg.REG_DWORD, 1)
    
    winreg.CloseKey(key)
    os.system("taskkill /F /IM explorer.exe")
    os.system("start explorer.exe")

def setTransparency0():
    keyPath = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        # Open the key for setting values
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        keyPath,
        0,
        winreg.KEY_SET_VALUE
    )
    
    winreg.SetValueEx(key, "EnableTransparency", 0, winreg.REG_DWORD, 0)
    
    winreg.CloseKey(key)
    os.system("taskkill /F /IM explorer.exe")
    os.system("start explorer.exe")

def commonStart():
    subprocess.run(["explorer", "Shell:Common Programs"])

def adminTools():
    subprocess.run(["explorer", "Shell:::{D20EA4E1-3957-11d2-A40B-0C5020524153}"])

def explorerAccessible():
    subprocess.run(["explorer",
            "shell:AppsFolder\\c5e2524a-ea46-4f67-841f-6a9465d9d515_cw5n1h2txyewy!App",])


#       GUI       #


class Button:
    def __init__(self, func: callable, parent: object, text: str):
        self.button = ntk.NTkButton(parent, text=text, width=45, command = func)
        self.button.pack(padx=10, pady=5)


window = ntk.NTk()
window.geometry("500x600")
window.title("SuperUser Control Panel")

ntk.NTkLabel(window, text="SuperUser Control Panel").pack(padx = 10, pady = 5)

tabview = ntk.NTkTabview(master=window)
tabview.pack(padx=10, pady=10, expand=True, fill="both")
tabview.configure(anchor="n")

tabview.add("Commands")
tabview.add("Settings")
tabview.set("Commands")

commandsFrame = ntk.NTkScrollableFrame(master=tabview.tab("Commands"), width=400, height=500)
commandsFrame.pack(padx=10, pady=10, expand=True, fill="both")

settingsFrame = ntk.NTkScrollableFrame(master=tabview.tab("Settings"), width=400, height=500)
settingsFrame.pack(padx=10, pady=10, expand=True, fill="both")

#       COMMANDS       #

button1 = Button(shellApps, commandsFrame, "List All Installations")
button2 = Button(godMode, commandsFrame, "Godmode Settings")
button3 = Button(explorerAccessible, commandsFrame, "Alternative File Explorer")
button4 = Button(adminTools, commandsFrame, "Administrator Tools")
button5 = Button(run, commandsFrame, "Run Menu")
button6 = Button(startMenu, commandsFrame, "Local Start Menu Apps")
button7 = Button(commonStart, commandsFrame, "Global Start Menu Apps")
button8 = Button(shutdown, commandsFrame, "Shutdown")
button9 = Button(restart, commandsFrame, "Restart")
button10 = Button(logout, commandsFrame, "Sign Out")
button11 = Button(winDir, commandsFrame, "Open Windows Folder")
button12 = Button(sys32, commandsFrame, "Open System32")
button13 = Button(desktop, commandsFrame, "Open Local Desktop")
button14 = Button(globalDesktop, commandsFrame, "Open Global Desktop")
button15 = Button(ctrlPanel, commandsFrame, "Open Control Panel")
button16 = Button(modifyPrograms, commandsFrame, "Remove Or Modify Programs")
button17 = Button(progFiles, commandsFrame, "Open Program Files")
button18 = Button(progFiles64, commandsFrame, "Open Program Files (x64)")
button19 = Button(progFiles86, commandsFrame, "Open Program Files (x86)")
button20 = Button(startup, commandsFrame, "Open Local Startup Folder")
button21 = Button(globalStartup, commandsFrame, "Open Global Startup Folder")
button22 = Button(cmd32, commandsFrame, "Open Command Prompt (System32)")

#       SETTINGS       #

button23 = Button(setLightMode, settingsFrame, "Enable Light Mode")
button24 = Button(setDarkMode, settingsFrame, "Enable Dark Mode")
button25 = Button(setTransparency1, settingsFrame, "Enable Taskbar & Start Menu Transparency")
button26 = Button(setTransparency0, settingsFrame, "Disable Taskbar & Start Menu Transparency")

ntk.NTkLabel(settingsFrame, text="A system restart is advised after applying the above changes.", fg_color="transparent").pack(padx = 10, pady = 0)

button27 = Button(setWallpaper, settingsFrame, "Set Desktop Wallpaper")

window.mainloop()
