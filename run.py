import input.bu_bu_gao
import input.nao_bai_jin
import input.the_elder
import model.cpm2
import model.gpt3

input_text = """
第十三章 不许动！": "“你……你究竟是什么人？”\r\n秦嬴还没拷问鬼祟男人，鬼祟男人反倒是先问起秦嬴来了。\r\n打人如挂画，这种技能实在是太过惊世骇俗，以至于此刻鬼祟男人脑海中已经掀起风暴，全都是猜测秦嬴真实身份的。\r\n某个古武世家的嫡传子弟？\r\n某个杀手组织的王牌杀手？\r\n某个国家部门的神秘底牌？\r\n不管是哪一个，总之都是鬼祟男人惹不起的存在。\r\n鬼祟男人忽然后悔接了这次任务了。\r\n就为了那么一点线人费，搭上小命，不值得！\r\n现在唯一能做的就是祈祷那位姑奶奶赶快来到，用国家机器的力量让这个来历不明的高手退却。\r\n秦嬴没有回答鬼祟男子，而是冷冷看着鬼祟男子的眼睛，就像是看待一条微不足道的小虫子。\r\n一只手指就可以轻易碾死。\r\n“爸爸，你是在跟这个爷爷表演魔术吗？”\r\n秦嬴背后响起兮兮的声音。\r\n鬼祟男子本来就已经绝望的心脏，再次抽搐起来。\r\n我今年才三十五岁，怎么就成爷爷了？\r\n你才是爷爷！你全家都是爷爷！\r\n可惜秦嬴跟兮兮都听不到鬼祟男子的内心呐喊，秦嬴摸摸兮兮小脑袋，道：“是啊。你喜欢吗？”\r\n兮兮敷衍的点点头：“还行吧！就是下次能不能换个好看点的助手。人家那些魔术师的助手都可漂亮了呢！”\r\n鬼祟男子只觉心脏又被插了一刀。\r\n“今天算你走运，我不想在孩子面前杀人。我不管你什么来路、什么目的，记住，没有下次！”\r\n秦嬴注视着鬼祟男子，冷冷说道。\r\n说完，就领着兮兮朝巷子深处走去。\r\n被鬼祟男子一耽搁，时间上却是有些来不及了。秦嬴准备翻墙走壁，抄个近路。\r\n而随着秦嬴离开，一直黏在墙上的鬼祟男子啪一声摔落在地。\r\n如一幅失去了黏性的图画，缓缓滑落，卷成一团。\r\n鬼祟男子眼中闪烁着死里逃生的心悸光芒，暗暗发誓这辈子都不想再招惹那个男人了。\r\n只是，他誓言还没消散，就听巷口陡然响起一阵急促脚步声。\r\n与此同时传来一个飒爽女声：“田鸡，嫌疑人在哪里？！”\r\n鬼祟男子欲哭无泪。\r\n冲说话的女子拼命使眼色，暗示女子快走。\r\n没想到，女子却误以为田鸡在提示她什么。\r\n目光一转，果然就看到了远处巷尾一个怀抱小女孩的男人身影。\r\n那个小女孩，不是兮兮是谁？\r\n“哈哈，踏破铁鞋无觅处，得来全不费工夫！田鸡你这次立了大功，线人费给你涨一倍！”\r\n女子大喜过望，脚下发力，蹭一下就扑出去数米远，朝着男人背影追了过去。\r\n而田鸡呆呆看着女子，半晌后才从嘴里挤出一句话：“袁队，我是让你快跑！不是让你快追啊！完了，这下全完了……”\r\n这个女子，不是别人，正是江州特勤安全处的袁夏！\r\n袁夏本来只是随手给田鸡发布了一个线人任务，让田鸡在幼儿园附近找找拐走兮兮的嫌疑犯。\r\n没想到还真让田鸡给找到了！\r\n所以袁夏接到田鸡的信号之后就立马赶了过来，都没来得及去幼儿园跟苏予杺会面。\r\n“站住！你已经触犯了华夏法律，放下孩子，争取宽大处理！”\r\n秦嬴抱着兮兮正想翻墙呢，忽然听到身后传来一个警告声音。\r\n秦嬴好奇的转头，然后就看到了一身警务制服的袁夏。\r\n“抱歉，我不觉得我触犯了哪条法律。如果你没其他事的话，请不要打扰我赶路。”\r\n秦嬴淡淡对袁夏说道，然后就要翻墙离去。\r\n“呵呵，不愧是情报里所说的罪大恶极的凶犯！都已经到了这种地步，竟然还觉得自己没有犯法！识相点就放下孩子，束手就擒！不然我可不介意将你当场格杀！”袁夏嗤笑一声，捏了捏指骨。\r\n如果不是担心兮兮，她早就冲上去将这个嫌犯打成猪头了！\r\n家里那么多女子格斗大赛冠军奖牌，岂是摆设？\r\n什么暗世界高手，什么顶级凶犯，她都不放在眼里！\r\n野路子出身的民间练家子，怎么可能是正规训练的格斗冠军的对手？\r\n听到袁夏的话，秦嬴不由笑了起来。\r\n“看来不解决你，你是不会罢休的。那就勉强让你见识一下什么是‘天外有天，人外有人’吧！”\r\n秦嬴说完这句话，下一秒身形就消失在原地。\r\n等到袁夏察觉秦嬴消失，已经晚了。\r\n一只手掌如泰山压顶一般轰隆落下，落在袁夏的头顶。\r\n刚刚还信心满满的袁夏，骤然花容变色，脸上写满了恐惧。\r\n这个男人的力量，竟然这么强！\r\n强到仅仅是掌风，就已经让她如芒在背、不堪重负了！\r\n如果这一掌结结实实拍在她的头上，可以想象她的脑袋一定会像西瓜一样裂开！\r\n“完了，托大了！”袁夏闭上眼睛，准备等死。\r\n不是她不想反抗，实在是秦嬴这一掌太过强大，将她整个身体都封印在了掌风里面。\r\n让她无从躲避！\r\n“爸爸，她是袁阿姨，妈妈的好朋友……”\r\n兮兮后知后觉的声音传来，正好卡在了秦嬴手掌落下的节点上。\r\n砰！\r\n一股犹如漩涡一样的气爆在袁夏头顶炸开，将袁夏一头齐耳短发吹拂的根根炸起。\r\n像是被狂风席卷过一般。\r\n半晌，气爆才缓缓消失，露出悬在袁夏头顶上方的秦嬴手掌。\r\n只差半寸，袁夏就要香消玉殒了。\r\n秦嬴冷冷收回手掌，看也没看袁夏一眼，重新将地上的兮兮抱起。\r\n一句话没说，转过身就要离开。\r\n死里逃生的袁夏长舒一口气，本该知难而退。\r\n只是此时却听巷口传来一阵噪杂的脚步声，却是袁夏的手下队员赶到了！\r\n袁夏虽然答应苏予杺不报告领导，却还是带了特勤安全处的几个手下，以防万一。\r\n“不许动！举起手来！”\r\n这些手下一看情形，立马明白袁夏没有占到便宜。当机立断举起了手中手枪，对准秦嬴。\r\n连队长都无可奈何的嫌犯，他们要是还妄想赤手空拳制服对方，那岂不成了弱智？！\r\n袁夏在犹豫一下之后，也摸出了腰间手枪。\r\n“不许动！放下孩子！跟我回局里一趟！”\r\n想了想，袁夏又补充一句：“鉴于你还没有伤害孩子，我们可以考虑对你从轻处理。但是前提是你必须配合！”\r\n秦嬴叹口气：“逃个学，就这么难吗？真以为你们拿枪就有用了？”\r\n不知为什么，袁夏听了秦嬴这句话没来由一阵紧张。\r\n她磕磕巴巴道：“我们有六个人、六枝枪，就算你再厉害，也不可能躲得过六人齐射。就算你侥幸躲过，但是你不考虑一下你怀里的孩子吗？我想你幕后的老板，也不想在目的达成之前就将人质杀害吧？”

本章最精彩的部分是"""

model.cpm2.generate(input_text)
