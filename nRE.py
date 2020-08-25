#!/usr/bin/env python

import re

def match(pattern, string, flags=0):
    m = re.match(pattern, string, flags)
    return True if m is not None else False

def group(pattern, string, flags=0):
    m = re.match(pattern, string, flags)
    if m is not None:
        return m.group()
    else:
        return False
