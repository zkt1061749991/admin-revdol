#!/bin/bash
pip install -r requirements.txt -i https://pypi.douban.com/simple/ selenium

# 加模块
python manage.py startapp <name>

# 加表
新增继承自models.Model的类

# 改字段
修改model的字段

# 最后
python manage.py makemigrations
python manage.py migrate