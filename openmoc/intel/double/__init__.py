import openmoc
import _openmoc_intel_double
from openmoc_intel_double import *
import signal

# Tell Python to recognize CTRL+C and stop the C++ extension module
# when this is passed in from the keyboard
signal.signal(signal.SIGINT, signal.SIG_DFL)

setLogLevel(str(openmoc.getLogLevel()))
setOutputDirectory(openmoc.getOutputDirectory())
setLogfileName(openmoc.getLogfileName())

Timer = openmoc.Timer
