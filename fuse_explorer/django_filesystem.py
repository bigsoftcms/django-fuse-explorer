import fuse

import time

import stat    # for file properties
import os      # for filesystem modes (O_RDONLY, etc)
import errno   # for error number codes (ENOENT, etc) - note: these must be returned as negatives
from django.db.models.loading import get_apps
from django.db.models import loading

fuse.fuse_python_api = (0, 2)

# TODO Fix naming - it ain't pep8..

#def dirFromList(list):
#    """
#    Return a properly formatted list of items suitable to a directory listing.
#    [['a', 'b', 'c']] => [[('a', 0), ('b', 0), ('c', 0)]]
#    """
#    return [[(x, 0) for x in list]]
#
#def getDepth(path):
#    """
#    Return the depth of a given path, zero-based from root ('/')
#    """
#    if path == '/':
#        return 0
#    else:
#        return path.count('/')
#
#def getParts(path):
#    """
#    Return the slash-separated parts of a given path as a list
#    """
#    if path == '/':
#        return [['/']]
#    else:
#        return path.split('/')

class MyStat(fuse.Stat):
    def __init__(self):
        self.st_mode = stat.S_IFDIR | 0755
        self.st_ino = 0
        self.st_dev = 0
        self.st_nlink = 2
        self.st_size = 4096
        self.st_uid = 0
        self.st_gid = 0
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0
        self.st_blocks = 0
        self.st_blksize = 0
        self.st_rdev = 0

class ModelPlugin():
    apps = loading.cache.app_models

    def getattr(self, path_elements, st):
        if len(path_elements) == 3:
            st.st_mode = stat.S_IFREG | 0666
            st.st_nlink = 1
        return st

    def readdir(self, path_elements):
        print path_elements
        if len(path_elements) == 0:
            print self.apps.keys()
            return [app.encode('utf-8') for app in self.apps.keys()]
        elif len(path_elements) == 1:
            app = self.apps[path_elements[0]]
            print app.keys()
            return app.keys()
        elif len(path_elements) == 2:
            model = self.apps[path_elements[0]][path_elements[1]]
            return [str(obj).encode('utf-8') for obj in model.objects.all()]
        return -errno.ENOENT


PLUGINS = {
    'models': ModelPlugin(),
}

def get_path_elements(path):
    pe = path.split('/')[1:]
    print pe
    return pe

class DjangoFS(fuse.Fuse):
    """ TODO
    """

    def __init__(self, *args, **kw):
        super(DjangoFS, self).__init__(*args, **kw)

        print 'Init complete.'

    def getattr(self, path):
        """
        - st_mode (protection bits)
        - st_ino (inode number)
        - st_dev (device)
        - st_nlink (number of hard links)
        - st_uid (user ID of owner)
        - st_gid (group ID of owner)
        - st_size (size of file, in bytes)
        - st_atime (time of most recent access)
        - st_mtime (time of most recent content modification)
        - st_ctime (platform dependent; time of most recent metadata change on Unix,
                    or the time of creation on Windows).
        """

        print '*** getattr', path

#        depth = getDepth(path) # depth of path, zero-based from root
#        pathparts = getParts(path) # the actual parts of the path

        st = MyStat()  
        st.st_mode = stat.S_IFDIR | 0755  
        st.st_nlink = 2  
        st.st_atime = int(time.time())  
        st.st_mtime = st.st_atime  
        st.st_ctime = st.st_atime  

        pe = get_path_elements(path)
        if len(pe) == 1 and pe[0] in [''] + PLUGINS.keys(): # '/' or '/something'
            pass
        elif pe[0] in PLUGINS:
            PLUGINS[pe[0]].getattr(pe[1:], st)
        else:
            return -errno.ENOENT

        return st  

    def readdir(self, path, offset):
        print '*** readdir', path
        directories = ['.', '..']

        if path == '/':
            directories += PLUGINS.keys()
        else:
            pe = get_path_elements(path)
            try:
                plugin = PLUGINS[pe[0]]
            except KeyError:
                yield -errno.ENOENT
            directories += plugin.readdir(pe[1:])
        print "yielding", directories
        for e in directories:
            yield fuse.Direntry(e)

    def mythread ( self ):
        print '*** mythread'
        return -errno.ENOSYS

    def chmod ( self, path, mode ):
        print '*** chmod', path, oct(mode)
        return -errno.ENOSYS

    def chown ( self, path, uid, gid ):
        print '*** chown', path, uid, gid
        return -errno.ENOSYS

    def fsync ( self, path, isFsyncFile ):
        print '*** fsync', path, isFsyncFile
        return -errno.ENOSYS

    def link ( self, targetPath, linkPath ):
        print '*** link', targetPath, linkPath
        return -errno.ENOSYS

    def mkdir ( self, path, mode ):
        print '*** mkdir', path, oct(mode)
        return -errno.ENOSYS

    def mknod ( self, path, mode, dev ):
        print '*** mknod', path, oct(mode), dev
        return -errno.ENOSYS

    def open ( self, path, flags ):
        print '*** open', path, flags
        return -errno.ENOSYS

    def read ( self, path, length, offset ):
        print '*** read', path, length, offset
        return -errno.ENOSYS

    def readlink ( self, path ):
        print '*** readlink', path
        return -errno.ENOSYS

    def release ( self, path, flags ):
        print '*** release', path, flags
        return -errno.ENOSYS

    def rename ( self, oldPath, newPath ):
        print '*** rename', oldPath, newPath
        return -errno.ENOSYS

    def rmdir ( self, path ):
        print '*** rmdir', path
        return -errno.ENOSYS

    def statfs ( self ):
        print '*** statfs'
        return -errno.ENOSYS

    def symlink ( self, targetPath, linkPath ):
        print '*** symlink', targetPath, linkPath
        return -errno.ENOSYS

    def truncate ( self, path, size ):
        print '*** truncate', path, size
        return -errno.ENOSYS

    def unlink ( self, path ):
        print '*** unlink', path
        return -errno.ENOSYS

    def utime ( self, path, times ):
        print '*** utime', path, times
        return -errno.ENOSYS

    def write ( self, path, buf, offset ):
        print '*** write', path, buf, offset
        return -errno.ENOSYS
