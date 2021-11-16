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
