# -*- coding: utf-8 -*-
from config.common import app_host, app_port, app


if __name__ == '__main__':
    app.run(host=app_host, port=int(app_port))
