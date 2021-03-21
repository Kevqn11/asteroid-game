import subprocess
from tkinter import font

def INSTALL():
    try:
        import PIL
    except ImportError:
        print("PIL module not installed. Installing now.")
        import sys
        subprocess.run((sys.executable, '-m', 'pip', 'install', 'pillow'))
    
        try:
            import PIL
        except:
            print("Could not install Pillow library automatically. Please install manually.")
            exit()

        print("Success.")
    
    if "LLPixel" not in font.families():
        print("Font not installed. Installing now.")
        import platform
        system = platform.system()
        if system == "Windows":
            subprocess.run(('copy', '/Y', 'assets/LLPixel3.ttf', '%WINDIR%/Fonts'))
        elif system == "Linux":
            subprocess.run(('cp', 'assets/LLPixel3.ttf', '/home/.fonts/'))
        elif system == "Darwin": # MacOS
            subprocess.run(('cp', 'assets/LLPixel3.ttf', '/Library/Fonts/'))
        
        if "LLPixel" not in font.families():
            print("Could not install assets/LLPixel3.ttf font automatically. Please install manually.")
            exit()
        
        print("Success.")