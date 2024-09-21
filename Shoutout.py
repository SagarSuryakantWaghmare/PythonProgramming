import subprocess

name = {"Sagar","Abhi","krishna","Nikhil","Ankita"}
for names in name:
 command = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{name}")'
 subprocess.run(['powershell', '-Command', command])


