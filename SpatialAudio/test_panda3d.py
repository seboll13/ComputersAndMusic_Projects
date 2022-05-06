from direct.showbase import Audio3DManager
from direct.showbase.ShowBase import ShowBase

import time

def play_sound(file, spatial_audio):
    base = ShowBase()
    test_sound, audio3d = None, None
    if spatial_audio:
        audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)
        test_sound = audio3d.load_sfx(file)
        #audio3d.attachSoundToObject(test_sound, camera)
    else:
        test_sound = base.loader.loadSfx(file)
    test_sound.play()
    time.sleep(5)
    test_sound.stop()

if __name__ == '__main__':
    play_sound('piano_testfile.wav', True)