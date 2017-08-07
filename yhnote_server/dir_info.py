import json
import file_info


class Dir_info(object):
    def __init__(self):
        self.uuid = ''
        self.user_id = ''
        self.parent_id = ''
        self.name = ''
        self.last_time = 0L
        self.type = 'dir'
        self.childen_dirs = {}
        self.childen_files = {}


if __name__ == '__main__':
    dir1 = Dir_info()
    dir2 = Dir_info()

    dir1.name = "dir1"
    dir1.uuid = "1111111"
    dir1.parent_id = '0000000'
    dir1.last_time = 123456

    dir2.name = "dir2"
    dir2.uuid = "222222"
    dir2.parent_id = '1111111'
    dir2.last_time = 123456


    dir1.childen_dirs[dir2.uuid] = dir2

    file1 = file_info.File_info()
    file1.name = 'file1'
    file1.uuid = '33333'
    file1.parent_id = '1111111'
    file1.format = 'md'
    file1.last_time = 234567

    dir1.childen_files[file1.uuid] = file1

    import copy
    dir3 = copy.deepcopy(dir2)
    dir3.uuid = '12345678'
    dir3.name = 'dir3'

    file2 = copy.deepcopy(file1)
    file2.uuid = '87654321'
    file2.name = 'file2'

    dir_init = Dir_info()
    dir_init.name = 'my_note'
    dir_init.uuid = 0
    dir_init.last_time = 0
    dir_init.childen_dirs[dir1.uuid] = dir1
    dir_init.childen_dirs[dir3.uuid] = dir3
    dir_init.childen_files[file2.uuid] = file2


    print json.dumps(dir_init, default=lambda o: o.__dict__, indent=4)

