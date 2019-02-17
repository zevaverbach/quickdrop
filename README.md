# QuickDrop

This is a simple CLI for quickly sharing a file or folder via Dropbox 
that's already located in a Dropbox folder.

It's as simple as 

    $ export DROPBOX_ACCESS_TOKEN=yourdropboxaccesstoken
    $ export DROPBOX_ROOT_PATH=yourdropboxrootpath
    $ pip install quickdrop

    Collecting quickdrop
    ...
    Successfully installed quickdrop-x.y.z

    $ url <filepath.whatever>

    Okay, <filepath.whatever> is now shared, accessible via
    https://www.dropbox.com/sh/bunchofrandomchars/morerandomcharsnstuff?dl=0.
