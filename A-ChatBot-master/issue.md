# _If you got this error_

_You will probably get an error after some time, where it says_\
`File "C:\Python38\lib\site-packages\sqlalchemy\util\compat.py", line 264, in time_func = time.clock`

`AttributeError: module 'time' has no attribute 'clock'`

_This is because time.clock() function was removed in Py 3.8._

* Go to the search bar and then paste the location given right above the last line of error

It will look something like this :\
`C:\Python38\lib\site-packages\sqlalchemy\util\compat.py`

* Open file with IDLE or whatever editor you have

* Then , go to line 264 in that . It would be written
  time_func = time.clock()

* Instead of this change, it to time.perf_counter()

* Save the file and now run it. It will work.
