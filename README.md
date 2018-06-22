# Flask-Fast

<p align="center">
<img src="./doc/logo-python.png">
<img src="./doc/logo-flask.png">
</p>

## 模板项目特性

* 将Flask应用最小化、模块化，并实现前后端分离
* 使用[Flask-RestPlus](http://flask-restplus.readthedocs.io)实现RESTful API
    * 结合[Swagger](http://flask-restplus.readthedocs.io/en/stable/swagger.html)将**接口自动文档化**
* 使用[PyTest](http://pytest.org)进行接口测试和代码覆盖率测试

## 模板项目结构

模板项目使用Flask & Flask-RestPlus构建RESTful API。

### Blueprints

整个应用主要使用两个blueprint：

* Api Blueprint

    使用Flask-RestPlus或普通的app.route来serve资源，在`/api`端点。

* Client Blueprint

    Flask仅仅serve Web应用的入口点，在`/`根路径端点。

## 安装

#### 环境

* Python 2.7+或3.x

#### 模板和依赖

* Clone仓库

* 创建一个[virtual enviroment](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies)（推荐）

    ```
    $ pip install --user pipenv
    ```

* 安装Python依赖，使用**pipenv**或pip命令（在项目根目录下）

    `$ pipenv install`或`pip install -r requirements.txt`

## 服务

### 开发服务器（Development Server）

使用Flask serve所有API端点。服务器能在文件改动保存时自动重载。

项目根目录，执行

```
$ python run.py
```

或执行

```
$ sh ./run.sh -d
```

这会在`localhost:5000`启动Flask开发服务器，并在`/api`端点响应接口请求。

### 生产环境服务器（Production Server）

项目根目录，执行以下步骤。

* 设置环境变量：

    执行

    ```
    $ export FLASK_CONFIG="Production"
    ```

* 运行Flask应用：

    执行

    ```
    $ python run.py
    ```

    或执行

    ```
    $ sh ./run.sh
    ```

    或使用**Gunicorn** serve整个应用：

    ```
    $ gunicorn app:app
    ```

## 开发

### 接口

#### 接口定义

普通接口：[`app/api/normal.py`](./app/api/normal.py)

RESTful接口：[`app/api/rest`](./app/api/rest/res_sample.py)

RESTful接口**自动文档化**，在API路径下的`doc`路径，如http://localhost:5000/api/doc/。

#### 接口测试

编写pytest测试集：[test](./test)（另见“测试”）

推荐使用[PostMan](https://www.getpostman.com/)进行API开发和测试。

#### 接口Mock

假数据：`app/client/mock`。

## 测试

确保dev依赖：

```
$ pipenv install --dev
```

运行pytest：

```
$ pipenv run pytest
```

## Todo

* [x] [Flask-CAS](https://github.com/cameronbwhite/Flask-CAS)
* [x] [Flask-CORS](https://github.com/corydolphin/flask-cors)
* [ ] [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy) [Quickstart](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)
* [ ] Celery
