import globals
import unite
import configparser

# U N I T E L O A D E R
# @uniteloader
class UniteLoader():
    logger = logging.getLogger("UniteLoader")
    unite = None
    config = None
    """
    returns a Unite singleton.
    """

    @staticmethod
    def load(unite_root):
        UniteLoader.unite = Unite()
        # TODO check exist
        UniteLoader.unite.root = unite_root
        UniteLoader.loadConfig()
        UniteLoader.setDirectories()
        pass

    @staticmethod
    def loadConfig():
        # TODO: not sure what this structure should be. At first I was thinking list,
        # but we need to store their relationships somehow
        UniteLoader.config = configparser.ConfigParser()
        UniteLoader.unite.hosts = UniteLoader.config["MAIN"]["hosts"]
        UniteLoader.logger.debug("Config loaded MAIN.hosts = " + UniteLoader.unite.hosts)
        pass

    @staticmethod
    def setDirectories():
        # TODO check exists
        UniteLoader.unite.global_dir = UniteLoader.unite.root + "/" + UniteNamespace.GLOBAL
        UniteLoader.unite.var_dir = UniteLoader.unite.root + "/" + UniteNamespace.VAR
        UniteLoader.unite.public_keys_dir = UniteLoader.unite.root + "/" + UniteNamespace.PUBLIC_KEYS
        UniteLoader.unite.canon_dir = UniteLoader.unite.root + "/" + UniteNamespace.CANON
        UniteLoader.unite.description_dir = UniteLoader.unite.root + "/" + UniteNamespace.DESCRIPTION
        pass
    @staticmethod
    def loadDescriptionTree():
        UniteLoader.unite.description_tree = DescriptionTree(unite.description_dir)
        pass
