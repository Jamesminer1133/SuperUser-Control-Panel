import os
import subprocess
import neotkinter as ntk
import winreg
import ctypes

# reg values
Registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
key = winreg.OpenKey(Registry, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
value, regtype = winreg.QueryValueEx(key, "SystemUsesLightTheme")
print(value)
winreg.CloseKey(key)

def runScript(event, script):
    if script == "shellApps":
        subprocess.run(["explorer", "shell:AppsFolder"])
    
    elif script == "godMode":
        subprocess.run('start shell:::{ED7BA470-8E54-465E-825C-99712043E01C}', shell=True)
        
    elif script == "run":
        subprocess.run(["explorer", "Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"])
        
    elif script == "start":
        subprocess.run(["explorer", "Shell:Programs"])

    elif script == "desktop":
        subprocess.run(["explorer", "Shell:Desktop"])

    elif script == "globalDesktop":
        subprocess.run(["explorer", "Shell:Common Desktop"])
        
    elif script == "shutdown":
        os.system("shutdown -t 0")
        
    elif script == "logout":
        os.system("shutdown /l")
        
    elif script == "restart":
        os.system("shutdown -r -t 0")

    elif script == "windir":
        subprocess.run(["explorer", "Shell:Windows"])

    elif script == "progFiles":
        subprocess.run(["explorer", "Shell:ProgramFiles"])

    elif script == "progFiles64":
        subprocess.run(["explorer", "Shell:ProgramFilesX64"])

    elif script == "progFiles86":
        subprocess.run(["explorer", "Shell:ProgramFilesX86"])

    elif script == "sys32":
        subprocess.run(["explorer", "Shell:System"])

    elif script == "changePrograms":
        subprocess.run(["explorer", "Shell:ChangeRemoveProgramsFolder"])

    elif script == "ctrlPanel":
        subprocess.run(["explorer", "Shell:ControlPanelFolder"])

    elif script == "startup":
        subprocess.run(["explorer", "Shell:Startup"])

    elif script == "globalStartup":
        subprocess.run(["explorer", "Shell:Common Startup"])

    elif script == "cmd":
        subprocess.Popen("C:\\Windows\\System32\\cmd.exe")

    elif script == "setWallpaper":
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
        
    elif script == "darkmode":
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
        
    elif script == "lightmode":
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


    elif script == "transparency1":
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

    elif script == "transparency0":
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
        
    elif script == "commonStart":
        subprocess.run(["explorer", "Shell:Common Programs"])
        
    elif script == "adminTools":
        subprocess.run(["explorer","Shell:::{D20EA4E1-3957-11d2-A40B-0C5020524153}"])
        
    elif script == "explorer2":
        subprocess.run(["explorer", "shell:AppsFolder\\c5e2524a-ea46-4f67-841f-6a9465d9d515_cw5n1h2txyewy!App"])

window = ntk.NTk()
window.geometry("500x600")

header = ntk.NTkLabel(window, text="SuperUser Control Panel")
header.pack(padx = 10, pady = 5)

tabview = ntk.NTkTabview(master=window)
tabview.pack(padx=10, pady=10, expand=True, fill="both")
tabview.configure(anchor="n")

tabview.add("Commands")  # add tab at the end
tabview.add("Settings")  # add tab at the end
tabview.set("Commands")  # set currently visible tab

window.title("SuperUser Menu")

commandsFrame = ntk.NTkScrollableFrame(master=tabview.tab("Commands"), width=400, height=500)
commandsFrame.pack(padx=10, pady=10, expand=True, fill="both")

settingsFrame = ntk.NTkScrollableFrame(master=tabview.tab("Settings"), width=400, height=500)
settingsFrame.pack(padx=10, pady=10, expand=True, fill="both")

button1 = ntk.NTkButton(commandsFrame, text="List All Installations", width=45)
button1.pack(padx = 10, pady = 5)
button1.bind("<ButtonRelease-1>", lambda event: runScript(event, "shellApps"))

button2 = ntk.NTkButton(commandsFrame, text="Godmode Settings", width=45)
button2.pack(padx = 10, pady = 5)
button2.bind("<ButtonRelease-1>", lambda event: runScript(event, "godMode"))

button3 = ntk.NTkButton(commandsFrame, text="Alternative File Explorer", width=45)
button3.pack(padx = 10, pady = 5)
button3.bind("<ButtonRelease-1>", lambda event: runScript(event, "explorer2"))

button4 = ntk.NTkButton(commandsFrame, text="Administrator Tools", width=45)
button4.pack(padx = 10, pady = 5)
button4.bind("<ButtonRelease-1>", lambda event: runScript(event, "adminTools"))

button5 = ntk.NTkButton(commandsFrame, text="Run Menu", width=45)
button5.pack(padx = 10, pady = 5)
button5.bind("<ButtonRelease-1>", lambda event: runScript(event, "run"))

button6 = ntk.NTkButton(commandsFrame, text="Local Start Menu Apps", width=45)
button6.pack(padx = 10, pady = 5)
button6.bind("<ButtonRelease-1>", lambda event: runScript(event, "start"))

button7 = ntk.NTkButton(commandsFrame, text="Global Start Menu Apps", width=45)
button7.pack(padx = 10, pady = 5)
button7.bind("<ButtonRelease-1>", lambda event: runScript(event, "commonStart"))

button8 = ntk.NTkButton(commandsFrame, text="Shutdown", width=45)
button8.pack(padx = 10, pady = 5)
button8.bind("<ButtonRelease-1>", lambda event: runScript(event, "shutdown"))

button9 = ntk.NTkButton(commandsFrame, text="Restart", width=45)
button9.pack(padx = 10, pady = 5)
button9.bind("<ButtonRelease-1>", lambda event: runScript(event, "restart"))

button9 = ntk.NTkButton(commandsFrame, text="Sign Out", width=45)
button9.pack(padx = 10, pady = 5)
button9.bind("<ButtonRelease-1>", lambda event: runScript(event, "logout"))

button10 = ntk.NTkButton(settingsFrame, text="Enable Dark Mode", width=45)
button10.pack(padx = 10, pady = 5)
button10.bind("<ButtonRelease-1>", lambda event: runScript(event, "darkmode"))

button11 = ntk.NTkButton(settingsFrame, text="Enable Light Mode", width=45)
button11.pack(padx = 10, pady = 5)
button11.bind("<ButtonRelease-1>", lambda event: runScript(event, "lightmode"))

button12 = ntk.NTkButton(settingsFrame, text="Enable Window & Start Menu Transparency", width=45)
button12.pack(padx = 10, pady = 5)
button12.bind("<ButtonRelease-1>", lambda event: runScript(event, "transparency1"))

button13 = ntk.NTkButton(settingsFrame, text="Disable Window & Start Menu Transparency", width=45)
button13.pack(padx = 10, pady = 5)
button13.bind("<ButtonRelease-1>", lambda event: runScript(event, "transparency0"))

restartLabel = ntk.NTkLabel(settingsFrame, text="A system restart is advised after applying the above changes.", fg_color="transparent")
restartLabel.pack(padx = 10, pady = 0)

button14 = ntk.NTkButton(commandsFrame, text="Open Windows Folder", width=45)
button14.pack(padx = 10, pady = 5)
button14.bind("<ButtonRelease-1>", lambda event: runScript(event, "windir"))

button15 = ntk.NTkButton(commandsFrame, text="Open System32", width=45)
button15.pack(padx = 10, pady = 5)
button15.bind("<ButtonRelease-1>", lambda event: runScript(event, "sys32"))

button16 = ntk.NTkButton(commandsFrame, text="Open Local Desktop", width=45)
button16.pack(padx = 10, pady = 5)
button16.bind("<ButtonRelease-1>", lambda event: runScript(event, "desktop"))

button17 = ntk.NTkButton(commandsFrame, text="Open Global Desktop", width=45)
button17.pack(padx = 10, pady = 5)
button17.bind("<ButtonRelease-1>", lambda event: runScript(event, "globalDesktop"))

button18 = ntk.NTkButton(commandsFrame, text="Open Control Panel", width=45)
button18.pack(padx = 10, pady = 5)
button18.bind("<ButtonRelease-1>", lambda event: runScript(event, "ctrlPanel"))

button19 = ntk.NTkButton(commandsFrame, text="Remove Or Modify Programs", width=45)
button19.pack(padx = 10, pady = 5)
button19.bind("<ButtonRelease-1>", lambda event: runScript(event, "changePrograms"))

button20 = ntk.NTkButton(commandsFrame, text="Open Program Files", width=45)
button20.pack(padx = 10, pady = 5)
button20.bind("<ButtonRelease-1>", lambda event: runScript(event, "progFiles"))

button21 = ntk.NTkButton(commandsFrame, text="Open Program Files(x64)", width=45)
button21.pack(padx = 10, pady = 5)
button21.bind("<ButtonRelease-1>", lambda event: runScript(event, "progFiles64"))

button22 = ntk.NTkButton(commandsFrame, text="Open Program Files(x86)", width=45)
button22.pack(padx = 10, pady = 5)
button22.bind("<ButtonRelease-1>", lambda event: runScript(event, "progFiles86"))

button23 = ntk.NTkButton(commandsFrame, text="Open Local Startup Folder", width=45)
button23.pack(padx = 10, pady = 5)
button23.bind("<ButtonRelease-1>", lambda event: runScript(event, "startup"))

button24 = ntk.NTkButton(commandsFrame, text="Open Global Startup Folder", width=45)
button24.pack(padx = 10, pady = 5)
button24.bind("<ButtonRelease-1>", lambda event: runScript(event, "globalStartup"))

button25 = ntk.NTkButton(commandsFrame, text="Open Command Prompt (System32)", width=45)
button25.pack(padx = 10, pady = 5)
button25.bind("<ButtonRelease-1>", lambda event: runScript(event, "cmd"))

button26 = ntk.NTkButton(commandsFrame, text="Set Desktop Wallpaper", width=45)
button26.pack(padx = 10, pady = 5)
button26.bind("<ButtonRelease-1>", lambda event: runScript(event, "setWallpaper"))

window.mainloop()
