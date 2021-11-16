import input.bu_bu_gao
import input.nao_bai_jin
import input.the_elder
import model.cpm2
import model.gpt3
import bminf

cpm2 = bminf.models.CPM2()
text = """
第十三章 不许动！": "“你……你究竟是什么人？”\r\n秦嬴还没拷问鬼祟男人，鬼祟男人反倒是先问起秦嬴来了。\r\n打人如挂画，这种技能实在是太过惊世骇俗，以至于此刻鬼祟男人脑海中已经掀起风暴，全都是猜测秦嬴真实身份的。\r\n某个古武世家的嫡传子弟？\r\n某个杀手组织的王牌杀手？\r\n某个国家部门的神秘底牌？\r\n不管是哪一个，总之都是鬼祟男人惹不起的存在。\r\n鬼祟男人忽然后悔接了这次任务了。\r\n就为了那么一点线人费，搭上小命，不值得！\r\n现在唯一能做的就是祈祷那位姑奶奶赶快来到，用国家机器的力量让这个来历不明的高手退却。\r\n秦嬴没有回答鬼祟男子，而是冷冷看着鬼祟男子的眼睛，就像是看待一条微不足道的小虫子。\r\n一只手指就可以轻易碾死。
段落总结：
主角是<span>
主角在<span>做了<span>,结果<span>
"""

for result in cpm2.fill_blank(text,
                              top_p=1.0,
                              top_n=10,
                              temperature=0.9,
                              frequency_penalty=0,
                              presence_penalty=0,
                              max_tokens=32
                              ):
    value = result["text"]
    text = text.replace("<span>", "\033[0;32m" + value + "\033[0m", 1)
print(text)
