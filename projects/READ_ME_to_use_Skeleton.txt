Using the Skeleton
You are now done with most of your yak shaving. Whenever you want to start a new project, just do this:

Make a copy of your skeleton directory. Name it after your new project.
Rename (move) the NAME directory to be the name of your project or whatever you want to call your root module.
Edit your setup.py to have all the information for your project.
Rename tests/NAME_tests.py to also have your module name.
Double check it's all working by using nosetests again.
Start coding.
-----------------------
Example:

Copy skeleton to ex47.
Rename everything with NAME to ex47.
Change the word NAME in all the files to ex47.
Finally, remove all the *.pyc files to make sure you're clean.
