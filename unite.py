#!/usr/bin/env python
import globals

from enum import Enum
from unite_cmd import CmdParse

class UniteNamespace(Enum):
    GLOBAL = ".global"
    VAR = ".var"
    PUBLIC_KEYS = ".public-keys"
    CANON = ".canon"
    DESCRIPTION = ".description"

# U N I T E
# @unite

class Unite():

    config_file = None

    hosts = None
    # difft %old %new
    unite_diff_save_cmd = ""
    # unison %src %dest
    push_cmd = ""
    # unison -theirs %src %dest
    theirs_cmd = ""

    description_tree = None

    # directories
    root = ""
    global_dir = ""
    var_dir = ""
    public_keys = ""
    canon_dir = ""
    description_dir = ""

    def loadUnite(upath):
        pass

    def add_key():
        pass

    def track():
        pass

    def init():
        pass

if __name__ == "__main__":
    CmdParse.dispatch()
