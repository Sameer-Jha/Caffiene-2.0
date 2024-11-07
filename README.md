# Caffeine 2.0

Caffeine 2.0 is a Python application designed to keep your computer "awake" by simulating keyboard input at regular intervals. This is useful for preventing the computer from going idle during long periods of use. The app includes features such as battery monitoring and an intuitive GUI built using Tkinter.

## Features
- **Stay Awake**: Keeps your system active by simulating keyboard presses.
- **Battery Monitor**: Notifies you when your battery level is below 20% (and you're not plugged in).
- **Play/Pause**: Start and stop the "stay awake" function easily.
- **Elapsed Time**: Displays how long the function has been running.
- **Start Time**: Shows when the function was started.
- **Customizable UI**: Built using Tkinter with an easy-to-use interface.

---

## Requirements

Before you begin, ensure you have the following installed:
- **Python 3.x** (preferably 3.6+)
- **Virtual Environment (optional but recommended)**

You can install the required dependencies using the following Python packages:
- `psutil` - for battery monitoring.
- `plyer` - for system notifications.
- `pyautogui` - for simulating keyboard events.
- `tkinter` - for building the GUI (comes with Python by default).
- `Pillow` - for handling icons in Tkinter.

---

## Installation Instructions

### Step 1: Set Up a Virtual Environment (Optional)

1. **Create a virtual environment** (if you don’t already have one):
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or manually install the necessary packages using:
   ```bash
   pip install psutil plyer pyautogui Pillow
   ```

### Step 2: Packaging the Application Using PyInstaller

1. **Install PyInstaller**:
   If you don't already have PyInstaller, install it using:
   ```bash
   pip install pyinstaller
   ```

2. **Package the Python script into an executable**:
   In the directory containing your Python script (e.g., `main.py`), run the following command:
   ```bash
   pyinstaller --onefile --noconsole --icon="Caffeine.ico" main.py
   ```

   - `--onefile` creates a single executable file.
   - `--noconsole` prevents a command prompt window from appearing when you run the app (useful for GUI apps).
   - `--icon="Caffeine.ico"` adds a custom icon to your application.

3. **Find the Executable**:
   After running the above command, PyInstaller will generate the executable inside the `dist` folder. Look for `main.exe` in the `dist` folder.

---

## Usage

### Running the Application

- **Double-click** on the `main.exe` executable to launch the Caffeine 2.0 application.
- The app will open a window with the following:
  - **Play/Pause button** to start or stop the "stay awake" function.
  - **Status label** showing "Wide Awake" when running and "Can catch some ZZZZ" when paused.
  - **Elapsed Time** and **Start Time** displayed on the window.
  - **Battery Status**: The app will notify you if your battery is below 20% (and not plugged in).

---

## Creating an Installer (Optional)

You can use **Inno Setup** to create an installer for your application. Here's how:

1. **Download and install Inno Setup** from [Inno Setup website](https://jrsoftware.org/isinfo.php).

2. **Create an Inno Setup Script**: Use the following example script to package your app with Inno Setup.

   ```ini
   [Setup]
   AppName=Caffeine 2.0
   AppVersion=1.0
   DefaultDirName={pf}\Caffeine 2.0
   DefaultGroupName=Caffeine 2.0
   OutputDir=.\Output
   OutputBaseFilename=Caffeine2.0_Installer
   SetupIconFile=Caffeine.ico
   Compression=lzma
   SolidCompression=yes

   [Files]
   Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
   Source: "Caffeine.ico"; DestDir: "{app}"; Flags: ignoreversion

   [Icons]
   Name: "{group}\Caffeine 2.0"; Filename: "{app}\main.exe"
   Name: "{desktop}\Caffeine 2.0"; Filename: "{app}\main.exe"

   [Run]
   Filename: "{app}\main.exe"; Description: "Launch Caffeine 2.0"; Flags: nowait postinstall skipifsilent
   ```

3. **Compile the Script**:
   After setting up the script in Inno Setup, click **Compile** to generate the installer.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## Contact

Created by **Sameer Jha**. For more information or if you encounter any issues, feel free to open an issue or contact me at [Sameer-Jha.github.io](https://Sameer-Jha.github.io).
```

You can save this as `README.md` in your project directory. This `README.md` provides detailed instructions for installing dependencies, packaging the app into an executable, and creating an installer, along with basic usage and features of the app.