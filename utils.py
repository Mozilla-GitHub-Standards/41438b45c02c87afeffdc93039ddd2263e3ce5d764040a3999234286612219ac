import re
from time import strftime

# Takes a string and attempts to extract bug ids in it
# TODO: Make this better
def extract_bug_ids(msg):
    m = re.search(r'([0-9]{5,})', msg, re.I)     
    if m and m.groups():
        return m.groups()
    else:
        return None

# Takes a repository name as a tring and breaks it into parts that can be the used
# to construct data for a routing key
# TODO: Make this better
def repo_parts(repo):
    return repo.split('-')

# Takes a datetime object and returns a normalized UTC string
# (so other/non-python clients can convert it to a native type)
def time_to_string(mydatetime):
    # RFC 2822 format
    return strftime("%a, %d %b %Y %H:%M:%S %z", mydatetime.utctimetuple())
