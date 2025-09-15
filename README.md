this is a USB rubber ducky defender writtin in python.
the way it works is pretty simple:

since a rubby ducky works by pretending to be a keyboard device and the computer can't tell apart a real keyboard and a rubber ducky so it thinks that it is really a keybaord.
then the ducky starts sending key presses as if it's a keyboard (the ducky has these command pre codded into it by the attacker) which the computer executes and the ducky can now do whatever it wants.
now this defender works by suppress all key presses (both from the ducky and your actual keyboard until a specific seires of keys is typed these keys are like a password that you know and will enter it to unlock it.
these keys are in the "code-keys.txt" file I have an example code in there but you'll want to make your own so just type it in there. (becouse of how pynput works not all keys are supported basicly just the letter keys and number key are not supported but the f keys and basicly everthing else can be used)
it should be noted that technicaly if the rubber duckys types the code in it will unlock which is why your code should long and pretty random to minumize the chances of the ducky knowing your code.



to use simply install the requirmets write your code in the code-keys.txt file and run main.py before plugging in the suspicious USB.









WARNING: although this program can defend againt rubber duckys USB can contain malware besides rubber ducky which this can't do anything against so even with this still you plug in any USBs at your own risk.
