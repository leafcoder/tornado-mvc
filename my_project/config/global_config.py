#-*- coding: utf-8 -*-

import posixpath
for name in posixpath.__all__:
    globals()['posix_' + name] = getattr(posixpath, name)

# 绑定的 IP 地址
address = '0.0.0.0'

# 绑定的服务器端口地址
port = 9090

# 测试模式是否开启
debug = True

project_name = 'my_project'

# 项目根目录绝对路径
project_base = posix_abspath(
    posix_join(posix_dirname(__file__), posix_pardir, posix_pardir)
)

# 项目中，主要目录的绝对路径
for name in ('config', 'controller', 'model', 'view'):
    globals()[name + '_base'] = posix_join(project_base, project_name, name)

# 静态文件所在目录
static_path = posix_join(view_base, 'static')

# 模板文件所在目录
template_path = posix_join(view_base, 'template')

# 本地化文件所在目录
locale_dir = posix_join(view_base, "translations")

default_setting = dict(
    xsrf_cookies=True,                                      # 跨站伪造请求的防范
    cookie_secret='dde4eba37cae4a69832be2a7b86594bf',       # 加密 Cookie 密钥
    template_path=template_path,
    static_path=static_path,
    login_url='/login',                                     # 默认登录页面
    debug=debug
)

# 当前模块 from xxx import * 时，将被导出变量、属性或方法
__all__ = [
    'project_base', 'project_name', 'address', 'port', 'debug',
    'config_base', 'controller_base', 'model_base', 'view_base',
    'static_path', 'template_path', 'default_setting'
]
