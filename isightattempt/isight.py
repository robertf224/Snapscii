import QTKit
import Cocoa

class iSightGrabber(Cocoa.NSObject):
    def init(self):
        # set ourselves up
        self = super(iSightGrabber, self).init()

        # set up movie
        self.movie = QTKit.QTMovie.alloc().init()

        # set up session
        self.session = QTKit.QTCaptureSession.alloc().init()

        # get default camera (isight)
        self.camera = QTKit.QTCaptureDevice.defaultInputDeviceWithMediaType_(QTKit.QTMediaTypeVideo)
        self.camera.open_(None) # (True, None) if success

        # initialize input capture
        self.input_capture = QTKit.QTCaptureDeviceInput.alloc().initWithDevice_(self.camera)
        self.session.addInput_error_(self.input_capture, None)

        # initialize output capture
        self.output_capture = QTKit.QTCaptureDecompressedVideoOutput.alloc().init()
        self.output_capture.setDelegate_(self) # not right, need obj or something

        self.session.addOutput_error_(self.output_capture, None)

        self.frame = None
        self.running = True

        return self

    def snap(self):
        self.running = True
        self.session.startRunning()
        while self.running:
            pass
        self.running = False
        return self.frame

    def captureOutput_didOutputVideoFrame_withSampleBuffer_fromConnection_(self, captureOutput, videoFrame, sampleBuffer, connection):
        self.session.stopRunning()
        self.frame = videoFrame
        self.running = False

#grabber = iSightGrabber.alloc().init()
#frame = grabber.snap()





