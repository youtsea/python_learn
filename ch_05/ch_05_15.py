
def bad_filename(filename):
    return repr(filename)[1:-1]

try:
    print filename
except UnicodeEncodeError:
    print bad_filename()