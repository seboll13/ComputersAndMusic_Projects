from direct.showbase import Audio3DManager
from direct.showbase.ShowBase import ShowBase

import time

if __name__ == '__main__':
    # Mono
    base = ShowBase()
    test_sound = base.loader.loadSfx('piano_testfile.wav')
    test_sound.play()
    time.sleep(5)
    test_sound.stop()