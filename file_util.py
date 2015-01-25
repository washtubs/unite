import globals

class FilteUtil:
    """
    if file is a symlink will follow this symlink and consecutive symlinks, until the file is found.
    if file is a real file, returns the file
    if real file not found returns None
    """
    @staticmethod
    def follow_symlink(f):
        pass
    @staticmethod
    def is_symlink(f):
        pass
    """
    returns immediate link
    """
    @staticmethod
    def symlink(f):
        pass
    @staticmethod
    def extension_search(root, ext):
        pass
    @staticmethod
    def extension_search(root, base, ext):
        pass
    @staticmethod
    def is_under(f, root):
        pass
    """
    f is under root. returns twin where twin is the corresponding file under mirror
    """
    @staticmethod
    def twin(root, mirror, f):
        #return twin
        pass

