# Django learn

[自强学堂](https://code.ziqiangxuetang.com/django/django-tutorial.html)

# 部署

> [djsite](https://djsite.herokuapp.com/)

1. 根目录添加`Procfile`文件，内容为`web: gunicorn djsite.wsgi --log-file -`
2. `heroku apps:create djsite`
3. `git remote -v`确认已创建 heroku 仓库
4. `heroku config:set DISABLE_COLLECTSTATIC=1`
5. 修改`settings.py`文件，设置`static`文件信息
6. `git push heroku master`
