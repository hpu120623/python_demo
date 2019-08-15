family_dict = {
    '亲子摄影': 'g193',
    '儿童STEM': 'g188',
    '儿童乐园': 'g33803',
    '儿童摄影': 'g27813',
    '婴儿游泳': 'g27767',
    '幼儿园': 'g189',
    '幼儿外语': 'g27762',
    '幼儿才艺': 'g27763',
    '幼小衔接': 'g33779',
    '托班/托儿所': 'g20009',
    '早教中心': 'g27761',
    }

study_dict =  {
    '语言培训': 'g2872',
    '美术培训': 'g2874',
    '音乐培训': 'g2873',
    '升学辅导': 'g2876',
    '留学': 'g32722',
    '教育院校': 'g260',
    '书法培训': 'g33757',
    '兴趣生活': 'g2878',
    '在线教育网校': 'g34107',
    '运动培训': 'g34129',
    }


code = 'mongoexport -d dp_spider -c {0} -f column,category,name,url,address,phone,desc --csv -o ./{0}.csv'

for category in family_dict:
    print(code.format(category))