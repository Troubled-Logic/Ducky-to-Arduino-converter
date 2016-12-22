Input_file = ("input.txt")
Output_file = ("output.ino")
counter = int(0)
Ducky_code = []
Arduino_code = []

Run = input("how many times do you want the code to run?")
Arduino_code.append("void setup() {")
if not Run == "1":
    Arduino_code.append("}")
    Arduino_code.append("void loop(){")
            
F_Keys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]
F_KEYS = int(0)

Release = ("  Keyboard.releaseAll();")
Windows = ("  Keyboard.press(KEY_LEFT_GUI);")
Delay = ("  delay(100);")

Tab = ("  Keyboard.press(KEY_TAB);")
Shift = ("  Keyboard.press(KEY_LEFT_SHIFT);")
Crtl = ("  Keyboard.press(KEY_LEFT_CRTL);")
Enter = ("  Keyboard.press(KEY_ENTER);")
Space = ("  Keyboard.press(KEY_SPACE);")
Delete = ("  Keyboard.press(KEY_DELETE);")
Alt = ("  Keyboard.press(KEY_LEFT_ALT);")
Insert = ("  Keyboard.press(KEY_INSERT);")
Esc = ("  Keyboard.press(KEY_ESC);")
Home = ("  Keyboard.press(KEY_HOME):")
Break = ("  Keyboard.press(KEY_BREAK);")
End = ("  Keyboard.press(KEY_END);")
Pause = ("  Keyboard.press(KEY_PAUSE);")

Capslock = ("  Keyboard.press(KEY_CAPS_LOCK);")
Numlock = ("  Keyboard.press(KEY_NUM_LOCK);")
Scrolllock = ("  Keyboard.press(KEY_SCROLL_LOCK);")
Pageup = ("  Keyboard.press(KEY_PAGE_UP);")
Pagedown = ("  Keyboard.press(KEY_PAGE_DOWN);")
Printscreen = (" Keyboard.press(KEY_PRINT_SCREEN);")

U_arrow = ("  Keyboard.press(KEY_UP_ARROW);")
D_arrow = ("  Keyboard.press(KEY_DOWN_ARROW);")
L_arrow = ("  Keyboard.press(KEY_LEFT_ARROW);")
R_arrow = ("  Keyboard.press(KEY_RIGHT_ARROW);")


with open(Input_file, "r") as file:
    for line in file:
        Ducky_code.append(line)
file.close()

while counter < len(Ducky_code):
    Line = Ducky_code[counter]
    Line = Line.replace("\n", "")

    if "REM" in Line[:3]:
        Line = Line.replace("REM ",  "  //")
        Line += ":"
        Arduino_code.append(Line)
        Line = ""

    elif "STRING" in Line[:6]:
        Line = Line.replace("STRING ", "")
        KEY = Line
        if len(Line) == 1:
            Line = ("  Keyboard.press('")
            Line += KEY
            Line += ("');")
        else:
            Line = ('  Keyboard.print("')
            Line += (KEY)
            Line += ('");')
        Arduino_code.append(Line)
        Line = ""

    elif "DEFAULT_DELAY" in Line[:13] or "DEFAULTDELAY" in Line[:12]:
        Arduino_code.append(Delay)
        Line = ""

    elif "DELAY" in Line[:5]:
        Line = Line.replace("DELAY ", "")
        KEY = Line
        Line = ("  delay(")
        Line += (KEY)
        Line += (");")
        Arduino_code.append(Line)
        Line = ""

    elif "BREAK" in Line[:5]:
        Arduino_code.append(Break)
        Line = ""

    elif "PAUSE" in Line[:5]:
        Arduino_code.append(Pause)
        Line = ""

    elif "DELETE" in Line[:6]:
        Arduino_code.append(Delete)
        Line = ""

    elif "ENTER" in Line[:5]:
        Arduino_code.append(Enter)
        Line = ""

    elif "HOME" in Line[:4]:
        Arduino_code.append(Home)
        Line = ""

    elif "INSERT" in Line[:6]:
        Arduino_code.append(Insert)
        Line = ""

    elif "CAPSLOCK" in Line[:8]:
        Arduino_code.append(Capslock)
        line = ""

    elif "NUMLOCK" in Line[:7]:
        Arduino_code.append(Numlock)
        Line = ""

    elif "SCROLLLOCK" in Line[:10]:
        Arduino_code.append(Scrolllock)
        Line = ""

    elif "PRINTSCREEN" in Line[:11]:
        Arduino_code.append(Printscreen)
        Line = ""

    elif "END" in Line[:3]:
        Arduino_code.append(End)
        Line = ""

    elif "SPACE" in Line[:5]:
        Arduino_code.append(Space)
        Line = ""

    elif "ESC" in Line[:3] or "ESCAPE" in Line[:6]:
        Arduino_code.append(Esc)
        Line = ""

    elif "PAGEUP" in Line[:6]:
        Arduino_code.append(Pageup)
        Line = ""

    elif "PAGEDOWN" in Line[:8]:
        Arduino_code.append(Pagedown)
        Line = ""
        
    elif "MENU" in Line[:4]:
        Arduino_code.append(Shift)
        Arduino_code.append(Delay)
        Arduino_code.append("  Keyboard.press(KEY_F10);")
        Line = ""

    elif "TAB" in Line[:3]:
        Arduino_code.append(Tab)
        line = ""

    elif "GUI" in Line[:3] or "WINDOWS" in Line[:7]:
        Line = Line.replace("GUI ", "")
        Line = Line.replace("Windows ", "")
        Arduino_code.append(Windows)
        Arduino_code.append(Delay)
        Line = Line.replace(" ", "")
        KEY = (Line)
        Line = ("  Keyboard.press('")
        Line += (KEY)
        Line += ("');")
        Arduino_code.append(Line)
        Line = ""

    elif "DOWN" in Line[:4] or "DOWNARROW" in Line[:9]:
        Arduino_code.append(D_arrow)
        Line = ""

    elif "LEFT" in Line[:4] or "LEFTARROW" in Line[:9]:
        Arduino_code.append(L_arrow)
        Line = ""

    elif "RIGHT" in Line[:5] or "RIGHTARROW" in Line[:10]:
        Arduino_code.append(R_arrow)
        Line = ""

    elif "UP" in Line[:2] or "UPARROW" in Line[:7]:
        Arduino_code.append(U_arrow)
        Line = ""

    elif "REPLAY" in Line[:5]:
        Line = Line.replace("REPLAY ", "")
        Last_line = Arduino_code[counter-1]
        if "  Keyboard.releaseAll();" == Last_line or "   //" in Last_line:
            Last_line = Arduino_code[counter-2]
        else:
            Arduinio_code.append("  while(con <",Line,"){")
            Arduino_code.append(Last_line)
            Arduino_code.append("con++;")
            Arduino_code.append("}")
        Line = ""
        
    elif not len(Line) == 0:
        while len(Line) > 0:
            if "CRTL" in Line[:4] or "CONTROL" in Line[:7]:
                Line = Line.replace("CRTL ", "")
                Line = Line.replace("CONTROL ", "")
                Arduino_code.append(Crtl)
                Arduino_code.append(Delay)

            if "ALT" in Line[:3]:
                Line = Line.replace("ALT ", "")
                Arduino_code.append(Alt)
                Arduino_code.append(Delay)
                
            if "ESC" in Line[:3] or "ESCAPE" in Line[:6]:
                Line = Line.replace("ESC ", "")
                Line = Line.replace("ESCAPE ", "")
                Arduino_code.append(Esc)
                Arduino_code.append(Delay)

            if "DELETE" in Line[:6]:
                Line = Line.replace("DELETE ", "")
                Arduino_code.append(Delete)
                Arduino_code.append(Delay)
                
            if "BREAK" in Line[:5]:
                Line = Line.replace("BREAK ", "")
                Arduino_code.append(Break)
                Arduino_code.append(Delay)

            if "SPACE" in Line[:5]:
                Arduino_code.append(Space)
                Line = Line.replace("SPACE ", "")
                Arduino_code.append(Delay)

            if "END" in Line[:3]:
                Line = Line.replace("END ", "")
                Arduino_code.append(End)
                Arduino_code.append(Delay)

            if "PAUSE" in Line[:5]:
                Line = Line.replace("PAUSE ", "")
                Arduino_code.append(Pause)
                Arduino_code.append(Delay)
                
            if "TAB" in Line[:3]:
                Line = Line.replace("TAB ", "")
                Arduino_code.append(Tab)
                Arduino_code.append(Delay)

            if "F" in Line[:1] and len(Line) > 1:
                if " " not in Line[:3]:
                    Arduino_code.append(Line[:3])
                    Line = Line.replace(Line[:3], "")
                elif " " not in Line[:2]:
                    Arduino_code.append(Line[:2])
                    Line = Line.replace(Line[:2], "")
                    
            if len(Line) == 1 or len(Line) == 2:
                Line = Line.replace(" ", "")
                Arduino_code.append("  Keyboard.press('",Line, "');")
                Line = ""

    Check = Arduino_code[counter]
    if not "DELAY" in Check[:5] and not "//" in Check[:2] and not "STRING" in Check[:6]:
        Arduino_code.append(Delay)
        Arduino_code.append(Release)
    counter = counter + 1
    
if Run == "1":
    Arduino_code.append("  }")
    Arduino_code.append("void loop(){")
    Arduino_code.append("  }")
else:
    Arduino_code.append("  }")
    
counter = int(0)
while counter < len(Arduino_code):
    Line = Arduino_code[counter]
    with open(Output_file, 'a')as outputfile:
        outputfile.write (Line)
        outputfile.write ("\n")
        counter = counter + 1
print("Conversion done enjoy your code")
open("input", 'w').close()

            
            
