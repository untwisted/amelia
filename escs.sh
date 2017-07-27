##############################################################################
# clone, ameliabot, github.
cd ~/projects
git clone git@github.com:iogf/ameliabot.git ameliabot-code
##############################################################################
# push, github, ameliabot.
cd ~/projects/ameliabot-code
git status
git add *
git commit -a
git push
##############################################################################
# create, development, branch, ameliabot. 
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# switch, master, branch, change, ameliabot.
cd ~/projects/ameliabot-code
git checkout master
##############################################################################
# switch, development, branch, change, ameliabot.
cd ~/projects/ameliabot-code
git checkout development
##############################################################################
# undo, changes, ameliabot, github.
cd ~/projects/ameliabot-code
git checkout *
##############################################################################
# merge, development, into master, ameliabot.
cd ~/projects/ameliabot-code
git checkout master
git merge development
git push
git checkout development
##############################################################################
# merge, master, into, development, ameliabot.
cd ~/projects/ameliabot-code
git checkout development
git merge master
git push
git checkout development
##############################################################################
# install, ameliabot.
cd ~/projects/ameliabot-code
sudo bash -i
python2 setup.py install
rm -fr build
exit
##############################################################################
# remove, delete, .git, ameliabot.
find . -name .git -print -exec rm -fr {} \;
##############################################################################
# create, start, run, initialize, ameliarc, ameliabot.
amelia --init
amelia --run
##############################################################################
# uninstall, delete, remove, ameliabot, global, package, installation.
rm -fr ~/.amelia
sudo bash -i
rm -fr /usr/local~/projects/python2.7/dist-packages/ameliabot
exit
##############################################################################
## build, make, a tarball, disutils, ameliabot.
cd ~/projects/ameliabot-code
python2 setup.py sdist 
rm -fr dist
rm MANIFEST
##############################################################################
# ameliabot, pip.
cd ~/projects/ameliabot-code
python setup.py sdist register upload
rm -fr dist
##############################################################################
# py2 to py3.

cd ~/projects/ameliabot-code

# Apply them.
2to3  -w .

find . -name "*.bak" -exec rm -f {} \;


