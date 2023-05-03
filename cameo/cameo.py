import cv2
from capture_manager import CaptureManager
from window_manager import WindowManager
from fs_utils import ensure_directory_exists

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeyPress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """Run the main loop."""

        ensure_directory_exists('output')

        self._windowManager.createWindow()

        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            if frame is not None:
                # TODO: Filter the frame.
                pass

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeyPress(self, keycode):
        """Handle key presses.
            space -> Take a screenshot.
            tab -> Start/stop recording a video.
            escape -> Quit.
        """

        # space
        if keycode == 32:
            self._captureManager.writeImage('output/screenshot.png')
        # tab
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('output/video.mkv')
            else:
                self._captureManager.stopWritingVideo()
        # escape
        elif keycode == 27:
            self._windowManager.destroyWindow()

if __name__ == "__main__":
    Cameo().run()

