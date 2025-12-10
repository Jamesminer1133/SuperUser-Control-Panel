import os
import subprocess
import tkinter
from tkinter import PhotoImage
import customtkinter
import winreg


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

window = customtkinter.CTk()
window.geometry("500x600")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

header = customtkinter.CTkLabel(window, text="SuperUser Control Panel")
header.pack(padx = 10, pady = 5)

tabview = customtkinter.CTkTabview(master=window)
tabview.pack(padx=20, pady=5)
tabview.configure(anchor="n")

tabview.add("Commands")  # add tab at the end
tabview.add("Settings")  # add tab at the end
tabview.set("Commands")  # set currently visible tab

window.title("SuperUser Menu")

commandsFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Commands"), width=400, height=500)
commandsFrame.pack(fill="both", expand=True, padx=10, pady=10)

settingsFrame = customtkinter.CTkScrollableFrame(master=tabview.tab("Settings"), width=400, height=500)
settingsFrame.pack(fill="both", expand=True, padx=10, pady=10)

button1 = customtkinter.CTkButton(commandsFrame, text="List All Installations", width=45)
button1.pack(padx = 10, pady = 5)
button1.bind("<ButtonRelease-1>", lambda event: runScript(event, "shellApps"))

button2 = customtkinter.CTkButton(commandsFrame, text="Godmode Settings", width=45)
button2.pack(padx = 10, pady = 5)
button2.bind("<ButtonRelease-1>", lambda event: runScript(event, "godMode"))

button3 = customtkinter.CTkButton(commandsFrame, text="Alternative File Explorer", width=45)
button3.pack(padx = 10, pady = 5)
button3.bind("<ButtonRelease-1>", lambda event: runScript(event, "explorer2"))

button4 = customtkinter.CTkButton(commandsFrame, text="Administrator Tools", width=45)
button4.pack(padx = 10, pady = 5)
button4.bind("<ButtonRelease-1>", lambda event: runScript(event, "adminTools"))

button5 = customtkinter.CTkButton(commandsFrame, text="Run Menu", width=45)
button5.pack(padx = 10, pady = 5)
button5.bind("<ButtonRelease-1>", lambda event: runScript(event, "run"))

button6 = customtkinter.CTkButton(commandsFrame, text="Local Start Menu Apps", width=45)
button6.pack(padx = 10, pady = 5)
button6.bind("<ButtonRelease-1>", lambda event: runScript(event, "start"))

button7 = customtkinter.CTkButton(commandsFrame, text="Global Start Menu Apps", width=45)
button7.pack(padx = 10, pady = 5)
button7.bind("<ButtonRelease-1>", lambda event: runScript(event, "commonStart"))

button8 = customtkinter.CTkButton(commandsFrame, text="Shutdown", width=45)
button8.pack(padx = 10, pady = 5)
button8.bind("<ButtonRelease-1>", lambda event: runScript(event, "shutdown"))

button9 = customtkinter.CTkButton(commandsFrame, text="Restart", width=45)
button9.pack(padx = 10, pady = 5)
button9.bind("<ButtonRelease-1>", lambda event: runScript(event, "restart"))

button9 = customtkinter.CTkButton(commandsFrame, text="Sign Out", width=45)
button9.pack(padx = 10, pady = 5)
button9.bind("<ButtonRelease-1>", lambda event: runScript(event, "logout"))

button10 = customtkinter.CTkButton(settingsFrame, text="Enable Dark Mode", width=45)
button10.pack(padx = 10, pady = 5)
button10.bind("<ButtonRelease-1>", lambda event: runScript(event, "darkmode"))

button11 = customtkinter.CTkButton(settingsFrame, text="Enable Light Mode", width=45)
button11.pack(padx = 10, pady = 5)
button11.bind("<ButtonRelease-1>", lambda event: runScript(event, "lightmode"))

button12 = customtkinter.CTkButton(settingsFrame, text="Enable Window & Start Menu Transparency", width=45)
button12.pack(padx = 10, pady = 5)
button12.bind("<ButtonRelease-1>", lambda event: runScript(event, "transparency1"))

button13 = customtkinter.CTkButton(settingsFrame, text="Disable Window & Start Menu Transparency", width=45)
button13.pack(padx = 10, pady = 5)
button13.bind("<ButtonRelease-1>", lambda event: runScript(event, "transparency0"))

restartLabel = customtkinter.CTkLabel(settingsFrame, text="A system restart is advised after applying the above changes.", fg_color="transparent")
restartLabel.pack(padx = 10, pady = 0)

button14 = customtkinter.CTkButton(commandsFrame, text="Open Windows Folder", width=45)
button14.pack(padx = 10, pady = 5)
button14.bind("<ButtonRelease-1>", lambda event: runScript(event, "windir"))

button15 = customtkinter.CTkButton(commandsFrame, text="Open System32", width=45)
button15.pack(padx = 10, pady = 5)
button15.bind("<ButtonRelease-1>", lambda event: runScript(event, "sys32"))

button16 = customtkinter.CTkButton(commandsFrame, text="Open Local Desktop", width=45)
button16.pack(padx = 10, pady = 5)
button16.bind("<ButtonRelease-1>", lambda event: runScript(event, "desktop"))

button17 = customtkinter.CTkButton(commandsFrame, text="Open Global Desktop", width=45)
button17.pack(padx = 10, pady = 5)
button17.bind("<ButtonRelease-1>", lambda event: runScript(event, "globalDesktop"))

button18 = customtkinter.CTkButton(commandsFrame, text="Open Control Panel", width=45)
button18.pack(padx = 10, pady = 5)
button18.bind("<ButtonRelease-1>", lambda event: runScript(event, "ctrlPanel"))

button19 = customtkinter.CTkButton(commandsFrame, text="Remove Or Modify Programs", width=45)
button19.pack(padx = 10, pady = 5)
button19.bind("<ButtonRelease-1>", lambda event: runScript(event, "changePrograms"))

button20 = customtkinter.CTkButton(commandsFrame, text="Open Program Files", width=45)
button20.pack(padx = 10, pady = 5)
button20.bind("<ButtonRelease-1>", lambda event: runScript(event, "progFiles"))

button21 = customtkinter.CTkButton(commandsFrame, text="Open Program Files(x64)", width=45)
button21.pack(padx = 10, pady = 5)
button21.bind("<ButtonRelease-1>", lambda event: runScript(event, "progFiles64"))

button22 = customtkinter.CTkButton(commandsFrame, text="Open Program Files(x86)", width=45)
button22.pack(padx = 10, pady = 5)
button22.bind("<ButtonRelease-1>", lambda event: runScript(event, "progFiles86"))

button23 = customtkinter.CTkButton(commandsFrame, text="Open Local Startup Folder", width=45)
button23.pack(padx = 10, pady = 5)
button23.bind("<ButtonRelease-1>", lambda event: runScript(event, "startup"))

button24 = customtkinter.CTkButton(commandsFrame, text="Open Global Startup Folder", width=45)
button24.pack(padx = 10, pady = 5)
button24.bind("<ButtonRelease-1>", lambda event: runScript(event, "globalStartup"))

window.mainloop()
