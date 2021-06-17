from PySide2 import QtCore, QtWidgets, QtGui
import sys,os,subprocess,time,traceback

# class used to implement a reusable thread which executes a function passed as argument
class Worker(QtCore.QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.Slot()
    def run(self):
        # execute function, catch errors during execution
        try:
            result = self.fn(
                *self.args, **self.kwargs,
            )
        except ValueError as err:
            # signal of error sent to the caller of the run function
            self.signals.error.emit(err.args[0])
        else:
            # signal of progress sent to the caller of the run function
            self.signals.result.emit(result)
        finally:
            # signal of done sent to the caller of the run function
            self.signals.finished.emit(self.args[0], self.args[1])

# class which defines worker signals used to communicate from worker to caller and viceversa
class WorkerSignals(QtCore.QObject):
    finished = QtCore.Signal(int, int)
    error = QtCore.Signal(str)
    result = QtCore.Signal(object)
    progress = QtCore.Signal(int)