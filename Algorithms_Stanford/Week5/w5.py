import gzip
import shutil

with gzip.open('SCC.txt.gz', 'rb') as read, open('SCC.txt', 'wb') as write:
    shutil.copyfileobj(read, write)
