import os
import time

source = ['/home/fuse-power/Desktop/python-source/p-trash']

target_dir = '/home/fuse-power/Desktop/python-source/backup'

target = target_dir + os.sep +time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в ', target)
else:
    print('Создание резервной копии НЕ удалось')