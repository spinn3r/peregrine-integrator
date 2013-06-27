#!/usr/bin/python

import datetime
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
import libintegrator

# from string import Template

# title = "hello world"

# tmpl=Template( """
# <html>
# <head>
# <title>${title}</title>
# <body>

# </body>

# """ )

# html=tmpl.substitute( title=title )

# print html


print libintegrator.get_rev_status( "/var/lib/integration/peregrine/test-1_1_2_3", 3658 )
print libintegrator.get_rev_status( "/var/lib/integration/peregrine/test-1_1_2_3", 3591 )

print libintegrator.get_git_log("/root/temp/peregrine-integrator")
