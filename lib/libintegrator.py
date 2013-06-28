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

def strftime( ts ):

    return ts.strftime("%Y-%m-%d %H:%M")

def readpath( path ):
    """Read data from the file at the given path."""

    result=None

    if ( os.path.exists( path ) ):

        file=open( path, "r" )
        result=file.read()
        file.close()

    return result

def get_changedir(dir,rev):
    """Get the directory used to contain logs."""

    changedir="%s/%s/" % (dir, rev)

    return changedir

def run_cmd(cmd, input=None, stdout=None, stderr=None, cwd=None, fail=True):
    """Run the given command and read its output"""

    print " # %s" % cmd

    pipe = subprocess.Popen(cmd, shell=True, cwd=cwd, stdout=stdout, stderr=stderr)

    (_out,_err) = pipe.communicate( input )
    result = pipe.poll()
        
    if result == 0:
        return 0
    elif result >= 0 and fail:
        raise Exception( "%s exited with %s" % (cmd, result) )

    return result

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

def parse_git_log_desc(line):

    return line[line.find( "DESC:" ) + len("DESC:"):]



def get_change_index_flat(scratch):
    """Get the full HG log output."""

    return parse_git_log_flat(get_git_log(scratch))

def get_git_log(scratch):
    """Get the output of 'git log'""" 

    os.chdir( scratch )

    output=read_cmd( "git log --format='%H %at %an DESC:%s'" )

    return output

def parse_git_log_flat(output):
    """Parse the git log by commit hash"""
    
    index=[]

    for line in output.split( "\n" ):

        changectx={}

        split=line.split( " " )

        if len( split ) < 3:
            continue


        changectx['commit']     = split[0]
        changectx['date']    = split[1]
        changectx['author']  = split[2]
        changectx['desc']    = parse_git_log_desc(line)

        index.append( changectx )

    return index

def get_rev_status(basedir,rev):
    """Return

    None if the rev is not tested
    -2 if it is testing
    -1 if it timed out during testing
     0 if it passed
    >0 if it failed (the exit code)."""

    path = "%s/%s" % (basedir, rev)
    
    if os.path.isdir( path ):

        exit_file="%s/exit.result" % (path)

        if ( os.path.exists( exit_file ) ):

            exit_result=open( exit_file, "r" )
            result=exit_result.read()
            exit_result.close()

            if result != "":
                return int(result)

        test_log="%s/test.log" % path

        if os.path.exists( test_log ):

            st=os.stat(test_log)    
            if st.st_mtime > time.time() - (2 * 60):
                return -2
                
    return None

def makedirWhenNotExists( dir ):

    if not os.path.exists( dir ):
        os.makedirs( dir )

def init_scratch(dir, repo):
    """Jump to the scratch dir and clone/update."""

    makedirWhenNotExists( dir )

    if not os.path.exists( "%s/.git" % dir ):

        os.chdir( dir )
        run_cmd( "git clone %s %s" % (repo,dir) )

    # change to the sratch dir and git pull
    os.chdir( dir )

    run_cmd( "git pull" )



    

