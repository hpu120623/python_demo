from time import sleep

def progress(percent=0, width=30):
    """
    本代码实现进度条效果
    sep的作用是以什么为分隔符，默认是空格，这里设置空是为了每个字符更紧凑
    end的作用是以什么为结尾，默认是回车换行符，这里为了实现进度条的效果，同样设置为空
    flush的作用主要是刷新，默认flush=False，不刷新，print到f中的内容先存到内存中，当flush=True时会立即把内容刷新输出
    """
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f'{percent:.0f}%',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)