import input.bu_bu_gao
import input.nao_bai_jin
import input.the_elder
import model.cpm2
import model.gpt3
import bminf

cpm2 = bminf.models.CPM2()
text = """
文章内容：
第四章 当众打脸": "话音落下，大门方向就传来了高跟鞋踩在地板上的哒哒声。\n王野扭头一看，一双白皙的大长腿映入眼帘。\n再往上一看，紧身职业装包裹着完美身材。绝美的容貌，乌黑的长发。气质高贵无比！\n那双大长腿迈着优雅的步伐走来，每一步都像是踩在男人们的心里，让人蠢蠢欲动。\n所有人都看得呆了，这位，就是云城第一商界女精英……夏清心。\n美貌与智慧并存的顶级名媛，旗下资产千亿。

文章总结：
文章中夏清心是<span>
文章中<span>是主角
文章简介是：令人震惊！<span>在<span>做了<span>,结果，<span>当众打脸<span>！
"""
#
# text = """
# “初宁，回来了啊，妈妈给你做了你最爱吃的糖醋排骨，快点洗手来吃饭。”\n母亲慈爱又关切的声音响起的时候，叶初宁的目光，看向了一旁的继父，心底有一种异样感。\n为了不让继父继姐不开心，在他面前，母亲对她都是十分冷淡严厉，甚至连个佣人都不如。\n今天为何这般反常？\n其实这么多年下来，她也已经习惯了母亲对她的态度，做为二婚，又带着自己，母亲嫁到白家后的日子并不好过，继父是个十分冷漠又自私的人，这些年生意做起来了，对她就更冷漠了。\n“妈。”叶初宁轻唤了一声。\n叶母的眼底，闪过一抹不安，只是叶初宁没有看到。\n母亲突如其来的慈爱，让她眼眶有些酸涩，她转身去了洗手间，洗了手就进了餐厅。\n母亲与继父已经坐好了。\n“不等姐姐吗？”白佳诗是继父的女儿。\n“不等她了，我们吃吧。”叶母说完，低下了头吃饭。
#
# 文章总结：
# 文章中<span>是主角，<span>是配角
# 文章简介是：令人震惊！<span>在<span>做了<span>,结果，<span>嫁给老头子<span>！
# """

for result in cpm2.fill_blank(text,
                              # top_p=0.9,
                              # top_n=25,
                              temperature=0.2,
                              frequency_penalty=0,
                              presence_penalty=0,
                              max_tokens=128
                              ):
    value = result["text"]
    text = text.replace("<span>", "\033[0;32m" + value + "\033[0m", 1)
print(text)
