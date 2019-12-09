from fake_useragent import UserAgent

ua = UserAgent()
for i in range(1, 10):
    print(ua.random)    # 随机打印任意厂家的浏览器
    print(ua.chrome)    # 随机打印chrome浏览器任意版本
    print(ua.firefox)   # 随机打印firefox浏览器任意版本