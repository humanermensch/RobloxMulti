**RobloxMulti** is an educational project designed to demonstrate how mutexes and process management work in Windows environments. 
This project allows users to run multiple instances of Roblox.

**Disclaimer:**
This project is strictly for educational purposes. 
It is not intended to bypass Roblox's terms of service or encourage unethical behavior. 
Running multiple instances of Roblox may violate their policies and could result in account bans or other consequences. 
Use this project responsibly and at your own risk.

**Why RobloxMulti?**
With RobloxMulti, you can run multiple instances of Roblox without relying on potentially harmful third-party tools. 
This project is designed to help people run Roblox multiple times in a safe and controlled manner.

**Extra Info:**
  Autostart (Optional)

  To automatically run the script when your computer starts:

      Press Win + R, type shell:startup, and press Enter. This opens the Startup folder.

      Create a shortcut to the script (RobloxMulti.py) and place it in the Startup folder.
  
      Ensure Python is added to your system's PATH so the script can run at startup.

  Important Notes

      Run the script before launching Roblox to ensure the mutex is active.
  
      The mutex will persist until the script is stopped or the system is restarted.
  
      Use this script responsibly and for educational purposes only.

**Contributing:**
Contributions are welcome! If you have ideas for improvements or want to add features, feel free to open an issue or submit a pull request.

**Installation:**

    Clone the repository:
      git clone https://github.com/yourusername/RobloxMulti.git

    Install the required dependencies:
      pip install pywin32

    Run the script BEFORE you run ROBLOX:
      python RobloxMulti.py
