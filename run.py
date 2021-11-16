import input.bu_bu_gao
import input.nao_bai_jin
import input.the_elder
import model.cpm2
import model.gpt3
import bminf

cpm2 = bminf.models.CPM2()
text = """
第四章 当众打脸": "话音落下，大门方向就传来了高跟鞋踩在地板上的哒哒声。\n王野扭头一看，一双白皙的大长腿映入眼帘。\n再往上一看，紧身职业装包裹着完美身材。绝美的容貌，乌黑的长发。气质高贵无比！\n那双大长腿迈着优雅的步伐走来，每一步都像是踩在男人们的心里，让人蠢蠢欲动。\n所有人都看得呆了，这位，就是云城第一商界女精英……夏清心。\n美貌与智慧并存的顶级名媛，旗下资产千亿。

总结：
夏清心是<span>
<span>是主角
<span>在<span>做了<span>,结果<span>
"""

for result in cpm2.fill_blank(text,
                              top_p=1.0,
                              top_n=10,
                              temperature=0.1,
                              frequency_penalty=0,
                              presence_penalty=0,
                              max_tokens=32
                              ):
    value = result["text"]
    text = text.replace("<span>", "\033[0;32m" + value + "\033[0m", 1)
print(text)
