##############################################################################
# clone, amelia, github.
cd ~/projects
git clone git@github.com:iogf/amelia.git amelia-code
##############################################################################
# push, github, amelia.
cd ~/projects/amelia-code
git status
git add *
git commit -a
git push
##############################################################################
# create, development, branch, amelia. 
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# switch, master, branch, change, amelia.
cd ~/projects/amelia-code
git checkout master
##############################################################################
# switch, development, branch, change, amelia.
cd ~/projects/amelia-code
git checkout development
##############################################################################
# undo, changes, amelia, github.
cd ~/projects/amelia-code
git checkout *
##############################################################################
# merge, development, into master, amelia.
cd ~/projects/amelia-code
git checkout master
git merge development
git push
git checkout development
##############################################################################
# merge, master, into, development, amelia.
cd ~/projects/amelia-code
git checkout development
git merge master
git push
git checkout development
##############################################################################
# install, amelia.
cd ~/projects/amelia-code
sudo bash -i
python2 setup.py install
rm -fr build
exit
##############################################################################
# remove, delete, .git, amelia.
find . -name .git -print -exec rm -fr {} \;
##############################################################################
# create, start, run, initialize, ameliarc, amelia.
amelia --init
amelia --run
##############################################################################
# uninstall, delete, remove, amelia, global, package, installation.
rm -fr ~/.amelia
sudo bash -i
rm -fr /usr/local~/projects/python2.7/dist-packages/amelia
exit
##############################################################################
## build, make, a tarball, disutils, amelia.
cd ~/projects/amelia-code
python2 setup.py sdist 
rm -fr dist
rm MANIFEST
##############################################################################
# amelia, pip.
cd ~/projects/amelia-code
python setup.py sdist register upload
rm -fr dist
##############################################################################
# py2 to py3.

cd ~/projects/ameliabot-code

# Apply them.
2to3  -w .

find . -name "*.bak" -exec rm -f {} \;



