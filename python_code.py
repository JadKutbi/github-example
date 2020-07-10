Last login: Fri Jul 10 16:27:30 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
jads-MacBook-Pro:~ engkutbi$ conda install -c conda-forge jupyterlab
-bash: conda: command not found
jads-MacBook-Pro:~ engkutbi$ git clone https://github.com/ipython/ipython-in-depth
Cloning into 'ipython-in-depth'...
remote: Enumerating objects: 2362, done.
remote: Total 2362 (delta 0), reused 0 (delta 0), pack-reused 2362
Receiving objects: 100% (2362/2362), 14.95 MiB | 1.88 MiB/s, done.
Resolving deltas: 100% (1354/1354), done.
jads-MacBook-Pro:~ engkutbi$ conda install ipython jupyter
-bash: conda: command not found
jads-MacBook-Pro:~ engkutbi$ pip install --upgrade pip
-bash: pip: command not found
jads-MacBook-Pro:~ engkutbi$ pip install --upgrade ipython jupyter
-bash: pip: command not found
jads-MacBook-Pro:~ engkutbi$ cd ipython-in-depth
jads-MacBook-Pro:ipython-in-depth engkutbi$ jupyter notebook
-bash: jupyter: command not found
jads-MacBook-Pro:ipython-in-depth engkutbi$ cd ~/Desktop/projects/github-example
jads-MacBook-Pro:github-example engkutbi$ python

WARNING: Python 2.7 is not recommended. 
This version is included in macOS for compatibility with legacy software. 
Future versions of macOS will not include Python 2.7. 
Instead, it is recommended that you transition to using 'python3' from within Terminal.

Python 2.7.16 (default, Apr 17 2020, 18:29:03) 
[GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20) (-macos10.15-objc- on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello Github!")
Hello Github!
>>> emacs python_code.py
  File "<stdin>", line 1
    emacs python_code.py
                    ^
SyntaxError: invalid syntax
>>> python_code.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python_code' is not defined
>>> print("Hello Github!")
Hello Github!
>>> 
