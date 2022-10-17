# this script builds the website from templates using Jinja2
# of course, this is a little obfuscated since I still have to build content of each page individually,
# but I chose to do it this pythonic way to follow DRY principle in case of later layout redesigns, 
# then I'll only have to change base.html 

#execute this script in the project root folder that contains css, pages, etc

import pathlib
import re
import jinja2
import os
projroot="."
cssfolder = "css"
pagefolder = "pages"
staticfolder = "static"
imgfolder = "img"
templatefolder = "templates"
#stylepath = os.path.join(cssfolder,"style.css")
#stylepath = os.path.abspath(stylepath)
#aboutpath = os.path.join(pagefolder,"about.html")
projectpath = os.path.join(projroot,pagefolder,"projects.html")
indexoutpath = "./index.html"
hobbiespath = os.path.join(projroot,pagefolder,"hobbies.html")

########################build this approach it is better
#pagelist=[os.path.join(pagefolder,p) for p in os.listdir(templatefolder)]



#set up the jinja2 environment for building the html files
fsloader = jinja2.FileSystemLoader("./templates")
env1 = jinja2.Environment(loader=fsloader)
basetempl = env1.get_template("base.html")
indextempl = env1.get_template("index.html")
projecttempl = env1.get_template("projects.html")
hobbiestempl = env1.get_template("hobbies.html")

#can pass a dict into template rendering

templdict = {}
templdict['indexpath'] = indextempl
templdict['projectpath'] = projecttempl
templdict['hobbiespath'] = hobbiestempl


#print(vardict)
#need to build a loop now that follows this general pattern, looping over pages with proper paths etc:

#note that this check for matching directory does NOT account for subfolders, only one level of recursion
for tk,tv in templdict.items():
    if tv.name=='index.html':
        curpath=os.path.join(projroot,"index.html")
    else:
        curpath=os.path.join(projroot,pagefolder,tv.name)
    numseps = len(re.findall(os.sep,curpath))
    vardict = {}
    #vardict['stylepath'] = stylepath
    vardict['indexpath'] = os.path.join((".."+os.sep)*(numseps-1),indextempl.name)
    vardict['projectpath'] = os.path.join((".."+os.sep)*(numseps-1),pagefolder,projecttempl.name)
    vardict['hobbiespath'] = os.path.join((".."+os.sep)*(numseps-1),pagefolder,hobbiestempl.name)
    vardict['stylepath']=os.path.join((".."+os.sep)*(numseps-1),cssfolder,"style.css")
    vardict['imgdirpath']=os.path.join((".."+os.sep)*(numseps-1),staticfolder,imgfolder,"")
    #print(vardict)
    if numseps>1:
        #print(curpath,numseps)
        vardict['indexpath'] = os.path.join((".."+os.sep)*(numseps-1),os.path.basename(indexoutpath))
    renderedindex = tv.render(vardict)
    with open(curpath,mode="w") as f:
        f.write(renderedindex)