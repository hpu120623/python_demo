import re

seed_map_list = [
    {
        'pattern': r'https?://www.zhihu.com/question/\d+/answer/(\d+)/?',
        'seed_type': 'seed_zhihu_answer_id',
        'type': 'answer',
        'detail_kernel_code': 'zhihu-pc-answer-detail'
    },
    {
        'pattern': r'https?://www.zhihu.com/question/\d+/answer/(\d+)/?',
        'seed_type': 'seed_zhihu_answer_id',
        'type': 'comment',
        'detail_kernel_code': 'zhihu-pc-comment-defaultsort'
    },
    {
        'pattern': r'https?://www.zhihu.com/question/(\d+)/?',
        'seed_type': 'seed_zhihu_question_id',
        'type': 'question',
        'detail_kernel_code': 'zhihu-pc-question-detail'
    },
    {
        'pattern': r'https?://www.zhihu.com/question/(\d+)/?',
        'seed_type': 'seed_zhihu_question_id',
        'type': 'comment',
        'detail_kernel_code': 'zhihu-pc-comment-defaultsort'
    },
    {
        'pattern': r'https?://zhuanlan.zhihu.com/p/(\d+)/?',
        'seed_type': 'seed_zhihu_zhuanlan_id',
        'type': 'news',
        'detail_kernel_code': 'zhihu-pc-zhuanlan-detail'
    },
    {
        'pattern': r'https?://zhuanlan.zhihu.com/p/(\d+)/?',
        'seed_type': 'seed_zhihu_zhuanlan_id',
        'type': 'comment',
        'detail_kernel_code': 'zhihu-pc-zhuanlan-comment-defaultsort'
    },
    {
        'pattern': r'https?://m.weibo.cn/status/(\d+).*',
        'seed_type': 'seed_weibo_weibo_id',
        'type': 'weibo',
        'detail_kernel_code': 'weibo-wap-weibowithoutlogin-detail'
    },
    {
        'pattern': r'https?://.*weibo.com/(\d+/.*)',
        'seed_type': 'seed_weibo_pc_id',
        'type': 'weibo',
        'detail_kernel_code': 'weibo-pc-weibowithoutlogin-detail'
    },
    {
        'pattern': r'https?://zhidao.baidu.com/question/(\d+).html',
        'seed_type': 'seed_baidu_zhidao_id',
        'type': 'question',
        'detail_kernel_code': 'baidu_zhidao-pc-question-defaultsort'
    },
    {
        'pattern': r'https?://tieba.baidu.com/p/(\d+)?.*',
        'seed_type': 'seed_forum_tieba_post_id',
        'type': 'post',
        'detail_kernel_code': 'forum-tieba-pc-post-defaultsort'
    },
    {
        'pattern': r'(https?://mp.weixin.qq.com/s.*)',
        'seed_type': 'seed_weixin_url',
        'type': 'news',
        'detail_kernel_code': 'weixin-pc-official-detail'
    },
    {
        'pattern': r'(https?://weixin.sogou.com/api/share.*)',
        'seed_type': 'seed_weixin_url',
        'type': 'news',
        'detail_kernel_code': 'weixin-pc-official-detail'
    },
    {
        'pattern': r'(https?://101.200.126.90:8080/api/snapshot/article\?.*media_type=7.*)',
        'seed_type': 'seed_qinyuan_url',
        'type': 'news',
        'detail_kernel_code': 'qinyuan-pc-snapshot-defaultsort'
    },
    {
        'pattern': r'https?://www.toutiao.com/group/(\d+)?',
        'seed_type': 'seed_jinritoutiao_article_id',
        'type': 'news',
        'detail_kernel_code': 'jinritoutiao-pc-article-detail'
    },
    {
        'pattern': r'https?://www.toutiao.com/i(\d+)?',
        'seed_type': 'seed_jinritoutiao_article_id',
        'type': 'news',
        'detail_kernel_code': 'jinritoutiao-pc-article-detail'
    },
    {
        'pattern': r'https?://www.toutiao.com/a(\d+)?',
        'seed_type': 'seed_jinritoutiao_article_id',
        'type': 'news',
        'detail_kernel_code': 'jinritoutiao-pc-article-detail'
    },
    {
        'pattern': r'https?://www.jisilu.cn/question/(\d+)?',
        'seed_type': 'seed_jisilu_question_id',
        'type': 'question',
        'detail_kernel_code': 'jisilu-pc-question-detail'
    },
    {
        'pattern': r'https?://baobao.baidu.com/question/(\w+).html',
        'seed_type': 'seed_baobao_zhidao_id',
        'type': 'question',
        'detail_kernel_code': 'baobao_zhidao-pc-question-defaultsort'
    },
    {
        'pattern': r'https?://ask.bitauto.com/detail/\d+',
        'seed_type': 'seed_news_url',
        'type': 'question',
        'detail_kernel_code': 'cheyisou-pc-ask-detail'
    },
    {
        'pattern': r'https?://www.douban.com/note/(\d+)?',
        'seed_type': 'seed_forum_top_douban_diary_post_url',
        'type': 'post',
        'detail_kernel_code': 'forum-top-douban_diary-pc-post'
    },
    {
        'pattern': r'https?://www.douban.com/group/topic/(\d+)?',
        'seed_type': 'seed_forum_top_douban_group_post_url',
        'type': 'post',
        'detail_kernel_code': 'forum-top-douban_group-pc-post'
    },
    {
        'pattern': r'https?://bbs.tianya.cn/post.*.shtml',
        'seed_type': 'seed_forum_top_tianya_post_url',
        'type': 'post',
        'detail_kernel_code': 'forum-top-tianya-pc-post-defaultsort'
    },
    {
        'pattern': r'https?://istock.jrj.com.cn/article,(.*).html',
        'seed_type': 'seed_forum_jrj_guba_post_id',
        'type': 'post',
        'detail_kernel_code': 'forum-jrj_guba-pc-post'
    },
    {
        'pattern': r'https?://www.xcar.com.cn/bbs/viewthread.php?tid=\d+',
        'seed_type': 'seed_forum_xcar_post_id',
        'type': 'post',
        'detail_kernel_code': 'xcar-pc-post-detail'
    },
    {
        'pattern': r'https?://baa.bitauto.com/bj/thread-\d+.html',
        'seed_type': 'seed_news_url',
        'type': 'post',
        'detail_kernel_code': 'cheyisou-pc-forum-detail'
    },
    {
        'pattern': r'https?://baobao.baidu.com/article/(\w+).html',
        'seed_type': 'seed_forum_top_baobao_zhidao_post_id',
        'type': 'post',
        'detail_kernel_code': 'forum-top-baobao_zhidao-pc-post'
    },
    {
        'pattern': r'https?://s.dianping.com/topic/(\d+)?',
        'seed_type': 'seed_forum_dianping_post_id',
        'type': 'post',
        'detail_kernel_code': 'forum-dianping-pc-post'
    },
    {
        'pattern': r'https?://www.xiaohongshu.com/discovery/item/(\w+)?',
        'seed_type': 'seed_forum_xiaohongshu_post_id',
        'type': 'post',
        'detail_kernel_code': 'forum-xiaohongshu-pc-post'
    },
    {
        'pattern': r'https?://www.kanzhun.com/pl(\d+).html',
        'seed_type': 'seed_kanzhun_review_id',
        'type': 'dianping',
        'detail_kernel_code': 'kanzhun-pc-review-detail'
    },
    {
        'pattern': r'https?://www.toutiao.com/i(\d+)?',
        'seed_type': 'seed_jinritoutiao_article_id',
        'type': 'news',
        'detail_kernel_code': 'jinritoutiao-pc-article-detail'
    },
    {
        'pattern': r'https?://36kr.com/p/(\d+).html',
        'seed_type': 'seed-36kr-pc-article-id',
        'type': 'news',
        'detail_kernel_code': '36kr-pc-article-detail'
    },
    {
        'pattern': r'https?://iask.sina.com.cn/b/\d+.html',
        'seed_type': 'seed_iask_detail_url',
        'type': 'question',
        'detail_kernel_code': 'iask-pc-detail'
    },
    {
        'pattern': r'https?://wenda.so.com/q/\d+',
        'seed_type': 'seed_360_ask_detail_url',
        'type': 'question',
        'detail_kernel_code': 'ask_360-pc-detail'
    },
    {
        'pattern': r'https?://wenwen.sogou.com/z/q\d+.htm',
        'seed_type': 'seed_wenwen_detail_url',
        'type': 'question',
        'detail_kernel_code': 'wenwen-pc-detail'
    },
    {
        'pattern': r'https?://www.autohome.com.cn/market/.*.html',
        'seed_type': 'seed_hangqing_autohome_post_id',
        'type': 'news',
        'detail_kernel_code': 'autohome-pc-hangqing-detail'
    },
    {
        'pattern': r'https?://club.autohome.com.cn/bbs/thread/.*.html',
        'seed_type': 'seed_forum_autohome_post_id',
        'type': 'post',
        'detail_kernel_code': 'autohome-pc-post-detail'
    },
    {
        'pattern': r'https?://guba.eastmoney.com/news,(.*)_.*?.html',
        'seed_type': 'seed_forum_guba_post_id',
        'type': 'post',
        'detail_kernel_code': 'forum-east_guba-pc-post-defaultsort'
    },
    {
        'pattern': r'https?://bbs.hexun.com/money/post.*.html',
        'seed_type': 'seed_forum_top_hexun_post_url',
        'type': 'post',
        'detail_kernel_code': 'forum-top-hexun-pc-post'
    },
    {
        'pattern': r'https?://www.jiemian.com/article/(\d+).html',
        'seed_type': 'seed_jiemian_article_id',
        'type': 'news',
        'detail_kernel_code': 'jiemian-iOS-article-detail'
    },
    {
        'pattern': r'https?://www.jiemian.com/article/(\d+).html',
        'seed_type': 'seed_jiemian_article_id',
        'type': 'comment',
        'detail_kernel_code': 'jiemian-iOS-comment-defaultsort'
    },
    {
        'pattern': r'https://www.36kr.com/p/(\d+)',
        'seed_type': 'seed-36kr-pc-article-id',
        'type': 'news',
        'detail_kernel_code': '36kr-pc-article-detail'
    },
    {
        'pattern': r'http://baijiahao.baidu.com/s?id=(\d+)',
        'seed_type': 'seed_baijia_article_id',
        'type': 'news',
        'detail_kernel_code': 'baijia-article-detail'
    },
    {
        'pattern': r'https?://weibo.com/ttarticle/p/show\?id=(\d+).*?',
        'seed_type': 'seed_weibo_article_id',
        'type': 'news',
        'detail_kernel_code': 'weibo-pc-withoutlogin-article-detail'
    }
]


test = 'https://www.toutiao.com/i6708905740326666756/'

for seed_map in seed_map_list:
    matchs = re.findall(seed_map['pattern'], test)
    if matchs:
        print(matchs[0])