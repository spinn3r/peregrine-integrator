#!/usr/bin/python

###
# 

###
#
# TODO
#
#
# - make the right page have some basic stats.
#
# - parse command line arguments
#    - timeout
#    - ignore-branches
#    - ignore-changesets
#
# - if we timeout we should STILL run tast-report , etc.

import datetime
import os
import re
import shutil
import subprocess
import sys
import time
import traceback

def read_cmd(cmd, input=None, cwd=None):
    """Run the given command and read its output"""

    pipe = subprocess.Popen( cmd,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             cwd=cwd)

    out=''
    err=''

    while True:

        (_out,_err) = pipe.communicate( input )

        out += _out
        err += _err

        result = pipe.poll()
        
        if result == 0:
            return out
        elif result >= 0:
            raise Exception( "%s exited with %s" % (cmd, result) )

def get_change_index_flat():
    """Get the full HG log output."""

    return parse_hg_log_flat(get_hg_log())

def get_hg_log(scratch):
    """Get the output of 'hg log'""" 

    os.chdir( scratch )

    output=read_cmd( "hg log --template '{rev} {branches} {date} {author} DESC:{desc}\n'" )
    #output=read_cmd( "hg log --template '{rev} {branches} {date}\n'" )
    #output=read_cmd( "hg log --template '{rev} {branches} {date} {author}\n'" )

    return output

def parse_hg_log_flat(output):
    """Parse the HG log by changeset ID"""
    
    index=[]

    for line in output.split( "\n" ):

        changectx={}

        split=line.split( " " )

        if len( split ) < 3:
            continue

        branch=split[1]

        if branch == "":
            branch = "default"

        changectx['rev']     = split[0]
        changectx['branch']  = branch
        changectx['date']    = split[2]
        changectx['author']  = split[3]
        changectx['desc']    = parse_hg_log_desc(line)

        index.append( changectx )

    return index

def get_rev_status(basedir,rev):
    """Return -1 if the rev isn not tested, 0 if it passed, and > 0 if it failed (the exit code)."""

    path = "%s/%s" % (basedir, rev)
    
    if os.path.isdir( path ):

        exit_file="%s/exit.result" % (path)

        if ( os.path.exists( exit_file ) ):

            exit_result=open( exit_file, "r" )
            result=exit_result.read()
            exit_result.close()
            return int(result)
            
    return -1
    
