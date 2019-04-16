version: '2'
services:
  spider-chinaso:
    image: harbor.1datatech.cn/python/spider_man_plus:beta-v1.8.0.1
    stdin_open: true
    network_mode: bridge
    tty: true
    command:
    - python3
    - ./manage.py
    - -e
    - beta
    - -s
    - news.chinaso
    labels:
      io.rancher.container.pull_image: always
  spider-baidu:
    image: harbor.1datatech.cn/python/spider_man_plus:beta-v1.8.0.1
    stdin_open: true
    network_mode: bridge
    tty: true
    command:
    - python3
    - ./manage.py
    - -e
    - beta
    - -s
    - news.baidu
    labels:
      io.rancher.container.pull_image: always
  spider-sina:
    image: harbor.1datatech.cn/python/spider_man_plus:beta-v1.8.0.1
    stdin_open: true
    network_mode: bridge
    tty: true
    command:
    - python3
    - ./manage.py
    - -e
    - beta
    - -s
    - news.sina
    labels:
      io.rancher.container.pull_image: always
  spider-jianshu:
    image: harbor.1datatech.cn/python/spider_man_plus:beta-v1.8.0.1
    stdin_open: true
    network_mode: bridge
    tty: true
    command:
    - python3
    - ./manage.py
    - -e
    - beta
    - -s
    - news.jianshu
    labels:
      io.rancher.container.pull_image: always
  spider-hexun:
    image: harbor.1datatech.cn/python/spider_man_plus:beta-v1.8.0.1
    stdin_open: true
    network_mode: bridge
    tty: true
    command:
    - python3
    - ./manage.py
    - -e
    - beta
    - -s
    - news.hexun
    labels:
      io.rancher.container.pull_image: always
  spider-so:
    image: harbor.1datatech.cn/python/spider_man_plus:beta-v1.8.0.1
    stdin_open: true
    network_mode: bridge
    tty: true
    command:
    - python3
    - ./manage.py
    - -e
    - beta
    - -s
    - news.so
    labels:
      io.rancher.container.pull_image: always
  spider-sogou:
    image: harbor.1datatech.cn/python/spider_man_plus:beta-v1.8.0.1
    stdin_open: true
    network_mode: bridge
    tty: true
    command:
    - python3
    - ./manage.py
    - -e
    - beta
    - -s
    - news.sogou
    labels:
      io.rancher.container.pull_image: always
  spider-ifeng:
    image: harbor.1datatech.cn/python/spider_man_plus:beta-v1.8.0.1
    stdin_open: true
    network_mode: bridge
    tty: true
    command:
    - python3
    - ./manage.py
    - -e
    - beta
    - -s
    - news.ifeng
    labels:
      io.rancher.container.pull_image: always
