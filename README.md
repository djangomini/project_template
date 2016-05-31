# Django(mini) - Template for new project

When you start work on new project that based on **Django(mini)** - please add this repostory as one of parent repositories for your project. It will help you to fetch new updates from this repository to keep your project **up-to-date** at any time.

Everyday we make improvements and bug fixes to this repository. Also we upgrade to new version of libraries (like Bootstrap, jQuery). You don't need to migrate your project manually, by looking the diff between older and newer versions. All what you need to do - run only one commnd to fetch new changes from this repository and apply on top of your project.

Stay tuned. We will publich updates soon.

### Quick Start

```
# clone your project repository
git clone git@github.com:...

# add djangomini template for your project
# it allows to update project template files later
git remote add djangomini git@github.com:djangomini/new_project.git
git remote set-url djangomini --push "You can't push to djangomini"

# get initial project structure
git remote update
git fetch --all
git pull djangomini master
```
