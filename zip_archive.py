#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  zip_archive.py
#  Python Example
#
#  Created by Liu Ming on 2018-11-02.
#  Copyright 2018 Liu Ming. All rights reserved.
#
#  解决的问题：利用shell的zip操作，存档指定路径下的所有文件。
#  
#  Tag：shell、zip、time、os

import os, time

SOURCE_DIR = ['/Users/liuming/Project/'] # 需要备份的源目录
BACKUP_DIR = '/Users/liuming/backup'     # 备份路径
BACKUP = BACKUP_DIR + '/' + time.strftime('%Y%m%d%H%M%S') + '.zip' # 备份文件

# 判断备份路径是否存在，不存在创建。
if not os.path.exists(BACKUP_DIR):
    os.mkdir(BACKUP_DIR)

# 备份shell命令
zip_command = "zip -qr '%s' %s" % (BACKUP, ' '.join(SOURCE_DIR))
os.system(zip_command) # 执行 shell 命令

# 命令行提示
print("开始备份，请等待...")
os.system('sleep 2') # 等待2秒