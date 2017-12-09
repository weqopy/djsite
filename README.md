# Django learn

`py_dj_xadmin`分支来自慕课网课程[Python升级3.6 强力Django+杀手级Xadmin打造在线教育平台](http://coding.imooc.com/class/78.html)

[自强学堂](https://code.ziqiangxuetang.com/django/django-tutorial.html)

[Django Documentation](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)

# 部署

> [djsite](https://djsite.herokuapp.com/)

1. 根目录添加`Procfile`文件，内容为`web: gunicorn djsite.wsgi --log-file -`
2. `heroku apps:create djsite`
3. `git remote -v`确认已创建 heroku 仓库
4. `heroku config:set DISABLE_COLLECTSTATIC=1`
5. 修改`settings.py`文件，设置`static`文件信息
6. `git push heroku master`


# 注意事项

- 更改 models.py 文件后，需要使用`python manage.py makemigrations`将更改记录为迁移文件，之后需要使用`python manage.py migrate`运行迁移文件

# 临时笔记
- pk 为'primary key'（主键）的缩写，此时可忽略主键具体变量名，尽量使用 pk
- 尽量多的 test
