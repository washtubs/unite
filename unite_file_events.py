import pyinotify
import logging

class UniteFileEventHandler(pyinotify.ProcessEvent):
    def my_init(self, file_object=sys.stdout):
        """
        This is your constructor it is automatically called from ProcessEvent.__init__(),
        And extra arguments passed to __init__() would be delegated automatically to
        my_init().
        """
        self._file_object = file_object

    def process_IN_DELETE(self, event):
        """
        This method processes a specific type of event: IN_DELETE. event
        is an instance of Event.
        """
        self._file_object.write('deleting: %s\n' % event.pathname)

    def process_IN_CLOSE(self, event):
        """
        This method is called on these events: IN_CLOSE_WRITE and
        IN_CLOSE_NOWRITE.
        """
        self._file_object.write('closing: %s\n' % event.pathname)

    def process_default(self, event):
        """
        Eventually, this method is called for all others types of events.
        This method can be useful when an action fits all events.
        """
        self._file_object.write('default processing\n')

# A way to instantiate this class could be:
p = MyEventHandler(file('/tmp/output', 'w'))
