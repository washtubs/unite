# unite
directory synchronization framework (uses unison as backend)

implemented in python

# TODO

Make an easy way to test. We will need to check lots of mocked up examples and be able to change environments quickly.
Streamlined testing is REALLY important here. We want to be able to run all the tests with different pluggables. so it’s 
vital they can be automated.
- [x] describe the basic namespace of a unite directory, plus all relevant environment vars in a single src file. 
- [ ] use multiple scenarios, and script situations for two live systems
- [ ] unit tests should be environment aware

- [x] Flesh out high level state machine

Internalize .description directory as an object Description 
- [ ] mock up a sample .description directory
- [x] ~~determine whether multiple inheritance will be a problem~~
    Will not be a problem as long as:
    1. no two predicates contradict.
    2. any set of predicates in any order canonicalizes to the same description.
- [ ] import .description directory to singleton Description object
- [ ] Description can have a SHA to use as a fingerprint
- [ ] resolve predicates in order (stable) for a given file path

Experiment with tracking .description and .canon in a git repo

Function that takes a relpath (from `UNITE_ROOT`) or full path, and retrieves.
the local file, the global file, or the description.

filesystem monitor daemon. Watch for important events like 
- [ ] when descriptions are modified
- [ ] when a local file is modified
- [ ] grounding for event manager

filename utils
- [ ] canonicalize extensions: i.e. encrypt[key2].diff.canon[sortu].encrypt[key1] --> canon[sortu].encrypt[key1].encrypt[key2].diff

Encrypt file using key

config file reader

validate state:
- [ ] every file AND directory in local has a twin in mirror directories: global and ~~description~~
    * this is false for .description, the files in description can be completely different, all that matters is 
    how they *happen* to align, this is true for global though 
- [ ] no file in local is a symlink
- [ ] no file in local is hidden (besides reserved folders)
- [ ] check for contradictory predicates **(right now, this does not exist)**
- [x] ~~trim extraneous files in description directory (not critical)~~ 
 * not necessary or preferrable, the point of the description dir is to be decoupled from any particular unite dir,
 so extraneous files are fine, and should be expected

resolve predicates to actions.
- [ ] encrypt[key1] should find key1 on the local machine and encrypt or decrypt depending on the direction.
- [ ] encrypt[scramble] should find a custom algorithm on the local machine and run it
- [ ] canon[sortu] should find the corresponding canon script and run it

# Questions

Description modification: what to do about conflicts, since these folders will be tracked globally?
shouldn’t happen very often. Lets aim for resolving these issues automatically in the future, but for the time being, it should not happen too often.

# Notes

- [ ] prior to any global interaction, we will want to ensure that the .description dir is identical. To do this, we will make 
a SHA fingerprint a part of the Description object and use that prior to any and all global exchanges, to ensure they are consistent.

- [ ] canon scripts should be presented as `canon new old`. This way a canonicalizer can merge the two based on updated date, when it is otherwise difficult to decide.

# related packages installed

Checked if needed

- [x] pyinotify 

# unite directory structure with env

```
$UNITE_DIFF
$UNITE_OBFISCATORS
$UNITE_PRIVATE_KEYS
$UNITE_ROOT/
    |
    +--- .global
    +--- .var (locks, prevent the file monitor from making dangerous asynchronous calls)
    +--- .public-keys [*]
    +--- .canon [*]
    +--- .description [*] (possible extensions: encrypt[], canon[], diff)
    +--- .config [*]
        hosts, unite_diff_save_cmd, push_cmd, theirs_cmd
    |
    +--- devlog/devlog
    +--- devlog/devlog.theirs
    |
    +--- encryption/devlog.ts

```
