import os

#需要用户自己填的：
root_dir = '/Users/macbookpro/Downloads/edu-doc/code/edu-code'
branch_name='master'

def get_respository_dirs(root_dir):
    os.chdir(root_dir)
    dirs=os.listdir('./')
    for dir in dirs:
        if dir.startswith("."):
            dirs.remove(dir)
    return ('%s/%s' % (root_dir, x) for x in dirs)

if __name__ == '__main__':
    for i in get_respository_dirs(root_dir):
        print('start to handler %s ...'%i)
        os.chdir(i)
        print('\n'.join((os.popen('git checkout %s' % branch_name).readlines())))
        print('\n'.join((os.popen('git pull').readlines())))


