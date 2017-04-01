# Anti-Duplicator

Script find duplicate files (same file name and size) in specified directory.

# Requirements

To run Anti-Duplicator you need python 3.5 only.

# Usage

`$ python duplicates.py <directory path>`

For example:

```#!bash

$ python duplicates.py test_dir

Duplicates files:
--------------------------
/home/user/test/glyphicons-halflings-regular.eot
/home/user/test/fonts/glyphicons-halflings-regular.eot
--------------------------
/home/user/test/bootsrap/js/bootstrap.js
/home/user/test/js/bootstrap.js

```

If you need help just type:

`$ python duplicates.py --help`