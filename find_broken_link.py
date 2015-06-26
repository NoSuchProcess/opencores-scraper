#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Python script to process the index.html file and validate the projects that
have a github link.
'''
_i = "index.html"
_o = "index_out.html"

import re, requests

_out = open(_o,"w")
_fnd=0
_tot=0
for ln in [line.rstrip('\n') for line in open(_i, "r")]:
    #print "#######\n", ln, "\n"

    if len(ln)>0:
        if ln.startswith("<tr><th><div hidden>"):
            # find the link inside this two marks (reg expression)
            m = re.search("</th><td><a href='https://github.com(.+?)'>code</a></td><td>", ln)
            if m:
                _link = m.group(1)
                if len(_link)>0:
                    _tot += 1
                    # is it an existing page?
                    print "Checking link:", _link
                    anw = requests.get('https://github.com'+_link)
                    if anw.ok:
                        _out.write(ln+"\n")
                        print "All good."
                        _fnd += 1
                    else:
                        print "This link does not seem to exist."
        else:
            _out.write(ln+"\n")
print "Of a total of",_tot, "projects I have found and validated", _fnd
_out.close()
