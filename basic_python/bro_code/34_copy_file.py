# copyfile() = coppies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
shutil.copyfile('text.txt','coppy.txt') # scr,dst