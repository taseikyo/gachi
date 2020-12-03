> @Date    : 2020-11-27 20:00:00
>
> @Author  : Lewis Tian (taseikyo@gmail.com)
>
> @Link    : github.com/taseikyo

<img src="images/50539309.png" align="right" height="120" title="this image from dd-center">

# gachi

> 誰でも大好き

顺便，我是单推（认真

突然迸发的想法，有 [dd-center/bilibili-vtuber-danmaku](https://github.com/dd-center/bilibili-vtuber-danmaku) 收集的弹幕，我能做些什么？收集一下 DD 发言（学习一下），看看有哪些机器人（独轮车），做做词云图等等，应该还挺好玩的。

[>> 非正式的 VTuber & DD 月刊 :jack_o_lantern:](monthly)

## Table of Contents

- [使用方法](#使用方法)
- [节 目 效 果](#节-目-效-果)
	- [沙雕弹幕频率](#沙雕弹幕频率)
	- [词云图](#词云图)
	- [最受欢迎的 VTuber](#最受欢迎的-vtuber)
	- [VTuber 一个月观看人数变化](#vtuber-一个月观看人数变化)
- [DD 斩首](#dd-斩首)
	- [只要我 D 的够快，就没人发现我是 DD](#只要我-d-的够快就没人发现我是-dd)
	- [什么嘛，原来我 D 的还蛮多的](#什么嘛原来我-d-的还蛮多的)
	- [阿伟，你又在 D 哦](#阿伟你又在-d-哦)
	- [我生于世上的理由](#我生于世上的理由)

## 使用方法

```Bash
git clone https://github.com/taseikyo/gachi.git
cd gachi
git submodule init && git submodule update
python iamnotdd.py
```

目前还在开发中，不知道后续会加入什么功能。

- [x] 获取弹幕并保存（纯弹幕，不包括时间戳和发送者 id）
- [x] 单日发送频率最高的弹幕
- [x] 单日弹幕词云图
- [x] 处处 D（单日最活跃 DD，见下面 DD 斩首）

## 节 目 效 果

### 沙雕弹幕频率

下面是 Hiiro 11-25 直播弹幕的展示，记得是斗地主回，血压拉满笑死了。

下表中的弹幕基本都是在教 Hiiro 怎么出牌，但是没懂 g 是什么鬼，众 DD 血压飙升以至于劝 Hiiro 买个挂？

> Hiiro 2020-11-25 弹幕频率 TOP 20

|   弹幕  | 次数|
|:-------:|:---:|
| pass   | 7999 |
| 2      | 6401 |
| yes    | 6000 |
| 草     | 4608 |
| no     | 3331 |
| ？？？ | 2855 |
| A      | 2548 |
| 得     | 2341 |
| 哈哈哈 | 2110 |
| 6      | 1892 |
| j      | 1699 |
| a      | 1516 |
| 3      | 1481 |
| 10     | 1437 |
| 7      | 1391 |
| 甜菜   | 1341 |
| J      | 1155 |
| 334455 | 1145 |
| g      | 1140 |
| 8      | 1132 |

### 词云图

|x|y|
|:-:|:-:|
|![](images/21919321-2020-11-25-wordcloud.png)|![](images/21919321-2020-11-25-wordcloud_1.png)|

\**Hiiro 2020-11-25 弹幕词云图*

### 最受欢迎的 VTuber

下面"人数"计算的是发过弹幕的 id 数，一个人发过 100 条也只算 1 条。

> 2020-10 月最受欢迎 VTuber

|                                           头像                                           |        昵称        |     id    | 房间号   | 人数    |
|:----------------------------------------------------------------------------------------:|:------------------:|:---------:|----------|---------|
| ![](http://i1.hdslb.com/bfs/face/163d99bc28a349410731d0404b180aa92c4d791e.jpg_64x64.jpg) | 绯赤艾莉欧Official | 407106379 | 21396545 | 1251789 |
| ![](http://i1.hdslb.com/bfs/face/422215a006f40f18e015d63701d5fb1e46080c0e.jpg_64x64.jpg) | 乙女音Official     | 406805563 | 21320551 | 503153  |
| ![](http://i1.hdslb.com/bfs/face/b3d6b3320baea31e82af616e59e6d4e95fa3d3a8.jpg_64x64.jpg) | 雫るる_Official    | 387636363 | 21013446 | 402365  |
| ![](http://i1.hdslb.com/bfs/face/a7edad60dab7f5bf46b4ce6460e9ff988acbc68e.jpg_64x64.jpg) | 古守血遊official   | 2299184   | 8725120  | 339484  |
| ![](http://i1.hdslb.com/bfs/face/6e84a8b680abff39ccc435949c6975c135138f1f.jpg_64x64.jpg) | HiiroVTuber        | 508963009 | 21919321 | 331887  |
| ![](http://i1.hdslb.com/bfs/face/b5e82aca42450be98952a72681eccb3a5c7b096b.jpg_64x64.jpg) | 黑桃影             | 456368455 | 21641569 | 329720  |
| ![](http://i1.hdslb.com/bfs/face/bcd5ff96ab7d9edf71411fe7a937ac56e2dad3fd.jpg_64x64.jpg) | 阿媂娅Artia        | 511613155 | 21908196 | 276205  |
| ![](http://i1.hdslb.com/bfs/face/2c2e481c5f01f630be750f90aca4f27581720a2b.jpg_64x64.jpg) | 花园Serena         | 380829248 | 14327465 | 244961  |
| ![](http://i1.hdslb.com/bfs/face/102e965ec24219e874a4d43c695cad1d558a1465.jpg_64x64.jpg) | 鈴宮鈴             | 480432362 | 21685677 | 207562  |
| ![](http://i1.hdslb.com/bfs/face/99bb8e6a7411b0bffb969b8c8440486a4a62f961.jpg_64x64.jpg) | 神楽Mea_Official   | 349991143 | 12235923 | 206385  |
| ![](http://i1.hdslb.com/bfs/face/b47463d917ec2dc7ef34951d51df490fa7f89531.jpg_64x64.jpg) | 物述有栖Official   | 434565011 | 21449083 | 204260  |
| ![](http://i1.hdslb.com/bfs/face/1b748478876acebe106d332ea917184a115eecbe.jpg_64x64.jpg) | 进击的冰糖         | 198297    | 876396   | 203197  |
| ![](http://i1.hdslb.com/bfs/face/8c07e8eaba492068f7627e437d2a327ca34f0530.jpg_64x64.jpg) | 阿萨Aza            | 480680646 | 21696950 | 193233  |
| ![](http://i1.hdslb.com/bfs/face/09aad335d63e5470ddb217bf4112ec4683cfd8bf.jpg_64x64.jpg) | 星野饼美           | 82389     | 3561767  | 188105  |
| ![](http://i1.hdslb.com/bfs/face/09088e15e8149c4c6411f0df1483476fb8a9b3e2.jpg_64x64.jpg) | 帕里_Paryi         | 1576121   | 4895312  | 183979  |
| ![](http://i1.hdslb.com/bfs/face/1c202e4750bceb1692b60f5a0d6a004a2013d242.jpg_64x64.jpg) | 猫芒ベル_Official  | 487550002 | 21811136 | 181080  |
| ![](http://i1.hdslb.com/bfs/face/9be44522dea053bba58ed26daa3f7e0455f64f07.jpg_64x64.jpg) | 呜米               | 617459493 | 22384516 | 176831  |
| ![](http://i1.hdslb.com/bfs/face/cbc695338514954b4285ad40b674779e5e6f72bf.jpg_64x64.jpg) | Overidea_China     | 18149131  | 704808   | 173858  |
| ![](http://i1.hdslb.com/bfs/face/9ea6ed607cb0b4adb19ace945586d2cf50797589.jpg_64x64.jpg) | 咩栗               | 745493    | 8792912  | 162781  |
| ![](http://i1.hdslb.com/bfs/face/c9a854ef9b98c0c335482cae5c3f6ad26c5e939f.jpg_64x64.jpg) | NoWorld_Official   | 434662713 | 21448649 | 159396  |

### VTuber 一个月观看人数变化

鲸落哥永远滴神，谢谢他让我认识了团长艾莉欧，进而认识了巧克拉拉这群可爱努力有实力且会整活的孩子。

![](images/2020-10-vup-monthly-trending.png)

\**团长（绯赤艾莉欧Official）10 月份观看人数变化*

## DD 斩首

数据均来自 [dd-center/bilibili-vtuber-danmaku](https://github.com/dd-center/bilibili-vtuber-danmaku)，使用的脚本为 [iamnotdd.py](iamnotdd.py)，仅图一乐，如有错误，欢迎指出；如有冒犯，也欢迎指出，我立马删除。

下面表中 "处处 D" 的数字是指去这么多直播间发过弹幕，并不是发的弹幕条数。

### 只要我 D 的够快，就没人发现我是 DD

草！你们为什么这么能 D 啊！

> 2020-11-25 最活跃的 20 位 DD 一览表

|                                               头像                                              |      昵称      |     ID    | 处处 D | 关注数（不包括悄悄关注） |
|:-----------------------------------------------------------------------------------------------:|:--------------:|:---------:|:-----------:|:------:|
| ![](http://i1.hdslb.com/bfs/face/00771cbe7cb326e09ae34453817ac1d090c9081b.jpg_64x64.jpg) |  猫耳缘子团子  |  5391099  |     250     |   941  |
| ![](http://i1.hdslb.com/bfs/face/140116ba80abd18c3471d6558d3ce8b53b2ae996.jpg_64x64.jpg) |   アクシオン   |  6700920  |     168     |   130  |
| ![](http://i1.hdslb.com/bfs/face/8bab2f78e81e9e63758eec0194e204c7af3fdabe.jpg_64x64.jpg) |     キラル     |  2061407  |     151     |   902  |
| ![](http://i1.hdslb.com/bfs/face/615e833d7598d015caf676509e7c6cd6c15c074f.jpg_64x64.jpg) |    闲云散客    |  22460464 |     147     |  1424  |
| ![](http://i1.hdslb.com/bfs/face/7c1b98959c9d03b19b4724c24b81a907c36ffc8c.jpg_64x64.jpg) |   Darth_Clark  |   221976  |     143     |   699  |
| ![](http://i1.hdslb.com/bfs/face/52d9d20478dee1b0a903a6b46bf99e56ed90ab99.jpg_64x64.jpg) |       Oue      |  5149140  |     136     |   748  |
| ![](http://i1.hdslb.com/bfs/face/937bef36b807a406d1f6cf4db5790626b0f9e05c.jpg_64x64.jpg) |    隣人Aさん   |   749693  |     130     |   244  |
| ![](http://i1.hdslb.com/bfs/face/9ca4398e12c705966cf42da393d1ab68586701c1.jpg_64x64.jpg) |    鱼果desu    |  88936852 |     119     |   469  |
| ![](http://i1.hdslb.com/bfs/face/1c3dd08170eab298237fd243b8193232b7399290.jpg_64x64.jpg) |    小旭专属    |  8129904  |     108     |   994  |
| ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) |   凛祢立华奏   |  19184692 |     108     |  1051  |
| ![](http://i1.hdslb.com/bfs/face/694ace84bd28d8385768ffa8066f8613003315b2.jpg_64x64.jpg) |    丹羽夕弦    |  17792597 |     105     |   230  |
|             ![](http://i0.hdslb.com/bfs/face/member/noface.jpg_64x64.jpg)                |    黯月x流光   |  49756319 |     104     |   116  |
| ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) |     柴可罗     | 414854124 |     104     |  1609  |
| ![](http://i1.hdslb.com/bfs/face/756b35d658aabdf8187587793c68d4a0c327f4b8.jpg_64x64.jpg) |   knkn家的柠   | 480789646 |     102     |   452  |
|             ![](http://i0.hdslb.com/bfs/face/member/noface.jpg_64x64.jpg)                |  U2895343005P  | 686696337 |      96     |   15   |
| ![](http://i1.hdslb.com/bfs/face/b5dd874bd4605c8f5f9cdcd1204194134b60890d.jpg_64x64.jpg) | 奈亚拉托提督君 |  45484350 |      94     |   996  |
| ![](http://i1.hdslb.com/bfs/face/a064b5690c29acf99457eaae2dbc8921346cbccc.jpg_64x64.jpg) |   lyfKiririn   |   698894  |      91     |   354  |
| ![](http://i1.hdslb.com/bfs/face/b1dca4af68b75a23f685b695a6cb24718ea140df.jpg_64x64.jpg) |   Malus_Mill   |  15567746 |      91     |  1904  |
| ![](http://i1.hdslb.com/bfs/face/22f1f29db06a9d6e493b241f91fcf687d602ab5b.jpg_64x64.jpg) |    灼心夜玩    |  8112391  |      88     |   776  |
| ![](http://i1.hdslb.com/bfs/face/98c35f9202219d657972d8baf25a3f4c4bf28b90.jpg_64x64.jpg) |    Shark絵丸   |  38806109 |      82     |   639  |

### 什么嘛，原来我 D 的还蛮多的

前面几天数据有点怪，我看了下原弹幕文件，有的弹幕文件缺失了，或许是没录到？

> 2020-10 月每日 DD 前三

|    日期    |                                           头像                                           |         昵称         |          ID         |          处处 D          | 关注数 |
|:----------:|:----------------------------------------------------------------------------------------:|:--------------------:|:-------------------:|:------------------------:|--------|
| 2020-10-1  | ![](http://i1.hdslb.com/bfs/face/f509e495e8d08dd29bba1291996d064b8071e79f.jpg_64x64.jpg) | GB_Official          | 6481343             | 3                        | 633    |
| 2020-10-1  | ![](http://i1.hdslb.com/bfs/face/ee89fead2a2efbcabc031f748e7adb836a590b88.jpg_64x64.jpg) | 艾利欧斯-艾文        | 20674351            | 2                        | 590    |
| 2020-10-1  | ![](http://i1.hdslb.com/bfs/face/cb37d23873caad6c44be62ff84038a8dccd74d25.jpg_64x64.jpg) | 一代鬃狮             | 1395983             | 2                        | 68     |
| 2020-10-2  | ![](http://i1.hdslb.com/bfs/face/30279c73dc80f5f33782649d2b46777a5a663ae9.jpg_64x64.jpg) | 梓杏子不能吃         | 34765893            | 2                        | 1414   |
| 2020-10-2  | ![](http://i1.hdslb.com/bfs/face/2626ccab3bcb02fc4e7e9a618158baca40e41d68.jpg_64x64.jpg) | AlizerMolone_重工    | 288030163           | 2                        | 998    |
| 2020-10-2  | ![](http://i1.hdslb.com/bfs/face/61e7475c7d80ae6c27dff152ff57189485924d93.jpg_64x64.jpg) | 我永远喜欢叶毛毛     | 21480468            | 2                        | 281    |
| 2020-10-3  | ![](http://i1.hdslb.com/bfs/face/063b8048abfe7db8a437b2014c9408c425120d85.jpg_64x64.jpg) | 冥小音               | 400648349           | 2                        | 105    |
| 2020-10-3  | ![](http://i1.hdslb.com/bfs/face/b34ecb794929bb8838d85aae1860224498698700.jpg_64x64.jpg) | 铃娅                 | 12230279            | 2                        | 124    |
| 2020-10-3  | ![](http://i1.hdslb.com/bfs/face/62d690c996d9bb9e5be949306079d3bbc6b330af.jpg_64x64.jpg) | Wenshuanglin         | 77273672            | 2                        | 280    |
| 2020-10-4  | ![](http://i1.hdslb.com/bfs/face/ee89fead2a2efbcabc031f748e7adb836a590b88.jpg_64x64.jpg) | 艾利欧斯-艾文        | 20674351            | 2                        | 590    |
| 2020-10-4  | ![](http://i1.hdslb.com/bfs/face/7f7bfdc1011d1f2fd289974515cc93cca6d8e8dd.jpg_64x64.jpg) | 无色剔透             | 259638827           | 2                        | 1116   |
| 2020-10-4  | ![](http://i1.hdslb.com/bfs/face/78130c02b5c50961eb13d03402b014dee2f54544.jpg_64x64.jpg) | 丨千恋万花丨         | 4311386             | 2                        | 1941   |
| 2020-10-5  | ![](http://i1.hdslb.com/bfs/face/77cf5e2dda6bb26b3ef7e408dffc3a25ef9a37a1.jpg_64x64.jpg) | 冰钦玉雪             | 108020589           | 2                        | 144    |
| 2020-10-5  | ![](http://i1.hdslb.com/bfs/face/ac115d589b26c4d08362696ab8d565bbf6df9371.jpg_64x64.jpg) | 旗舰小和             | 1490616             | 2                        | 499    |
| 2020-10-5  | ![](http://i1.hdslb.com/bfs/face/5515dab978e76ff1a59f14b11b514a76e4ce8910.jpg_64x64.jpg) | 我是良辰我怕谁丶     | 8499244             | 2                        | 254    |
| 2020-10-6  | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 5                        | 1051   |
| 2020-10-6  | ![](http://i1.hdslb.com/bfs/face/18744cdc1be7f37a347846dd56059644999079a8.jpg_64x64.jpg) | 藍川有希             | 337035              | 3                        | 20     |
| 2020-10-6  | ![](http://i1.hdslb.com/bfs/face/62d690c996d9bb9e5be949306079d3bbc6b330af.jpg_64x64.jpg) | Wenshuanglin         | 77273672            | 2                        | 280    |
| 2020-10-7  | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 73                       | 1578   |
| 2020-10-7  | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 42                       | 237    |
| 2020-10-7  | ![](http://i1.hdslb.com/bfs/face/29ad759052dc088b02fe549a31c67687b91a4804.jpg_64x64.jpg) | 雅左銀               | 16192613            | 36                       | 166    |
| 2020-10-8  | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 67                       | 1051   |
| 2020-10-8  | ![](http://i1.hdslb.com/bfs/face/29d3ad7dfb43e9ded013e4946add8a02fcddb81e.jpg_64x64.jpg) | 妖哥哥呦             | 12097824            | 60                       | 87     |
| 2020-10-8  | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 52                       | 237    |
| 2020-10-9  | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 66                       | 237    |
| 2020-10-9  | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 51                       | 677    |
| 2020-10-9  | ![](http://i1.hdslb.com/bfs/face/db7eedc48215bce66e04b803534d3c4f85c88a10.jpg_64x64.jpg) | 坑死小学生233        | 32468573            | 46                       | 217    |
| 2020-10-10 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 87                       | 1578   |
| 2020-10-10 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 76                       | 677    |
| 2020-10-10 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 73                       | 237    |
| 2020-10-11 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 65                       | 1578   |
| 2020-10-11 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 62                       | 677    |
| 2020-10-11 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 42                       | 237    |
| 2020-10-12 | ![](http://i1.hdslb.com/bfs/face/68d34f1c03c16f3dd4a5277cfdc7d007d8ced741.jpg_64x64.jpg) | 拿磨阿弥陀佛         | 393020288           | 100                      | 0      |
| 2020-10-12 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 49                       | 1578   |
| 2020-10-12 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 47                       | 677    |
| 2020-10-13 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 89                       | 237    |
| 2020-10-13 | ![](http://i1.hdslb.com/bfs/face/29d3ad7dfb43e9ded013e4946add8a02fcddb81e.jpg_64x64.jpg) | 妖哥哥呦             | 12097824            | 55                       | 87     |
| 2020-10-13 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 54                       | 1578   |
| 2020-10-14 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 98                       | 237    |
| 2020-10-14 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 46                       | 1578   |
| 2020-10-14 | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 43                       | 1051   |
| 2020-10-15 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 62                       | 237    |
| 2020-10-15 | ![](http://i1.hdslb.com/bfs/face/e98d7ba0d8f9cf6e6a4c117c45136f62ec93d12f.jpg_64x64.jpg) | 无心将军             | 6441436             | 46                       | 723    |
| 2020-10-15 | ![](http://i1.hdslb.com/bfs/face/db7eedc48215bce66e04b803534d3c4f85c88a10.jpg_64x64.jpg) | 坑死小学生233        | 32468573            | 44                       | 217    |
| 2020-10-16 | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 85                       | 1051   |
| 2020-10-16 | ![](http://i1.hdslb.com/bfs/face/db7eedc48215bce66e04b803534d3c4f85c88a10.jpg_64x64.jpg) | 坑死小学生233        | 32468573            | 42                       | 217    |
| 2020-10-16 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 41                       | 237    |
| 2020-10-17 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 65                       | 237    |
| 2020-10-17 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 62                       | 677    |
| 2020-10-17 | ![](http://i1.hdslb.com/bfs/face/db7eedc48215bce66e04b803534d3c4f85c88a10.jpg_64x64.jpg) | 坑死小学生233        | 32468573            | 58                       | 217    |
| 2020-10-18 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 70                       | 677    |
| 2020-10-18 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 48                       | 237    |
| 2020-10-18 | ![](http://i1.hdslb.com/bfs/face/db7eedc48215bce66e04b803534d3c4f85c88a10.jpg_64x64.jpg) | 坑死小学生233        | 32468573            | 48                       | 217    |
| 2020-10-19 | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 66                       | 1051   |
| 2020-10-19 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 44                       | 1578   |
| 2020-10-19 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 43                       | 677    |
| 2020-10-20 | ![](http://i1.hdslb.com/bfs/face/92fc44f3a8f3cb51bef912aa5856b0878c813063.jpg_64x64.jpg) | 没有感情的答谢姬长磐 | 29561320            | 36                       | 1956   |
| 2020-10-20 | ![](http://i1.hdslb.com/bfs/face/f0ace4408818233bbed2df3070084d96bd241afc.jpg_64x64.jpg) | Raindio_             | 9769753             | 34                       | 174    |
| 2020-10-20 | ![](http://i1.hdslb.com/bfs/face/3aa4ca3f4dc37cbc62e56718ffb8a95ea25f2f02.jpg_64x64.jpg) | Huzzame              | 270673937           | 30                       | 15     |
| 2020-10-21 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 73                       | 237    |
| 2020-10-21 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 53                       | 1578   |
| 2020-10-21 | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 43                       | 1051   |
| 2020-10-22 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 73                       | 1578   |
| 2020-10-22 | ![](http://i1.hdslb.com/bfs/face/0f078e191cb55a1180333d256ecc597db305ab02.jpg_64x64.jpg) | 啃饼饼               | 8032961             | 56                       | 189    |
| 2020-10-22 | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 50                       | 1051   |
| 2020-10-23 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 55                       | 237    |
| 2020-10-23 | ![](http://i1.hdslb.com/bfs/face/7c07a41718db4f461fb56f757270893e73dec7f5.jpg_64x64.jpg) | 扫视天空之人         | 1986750             | 42                       | 116    |
| 2020-10-23 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 42                       | 677    |
| 2020-10-24 | ![](http://i1.hdslb.com/bfs/face/c3d0db57bdc253ec5e2f57c04356a67e6f701e6a.gif)           | 苏黎世°              | 394098              | 79                       | 517    |
| 2020-10-24 | ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy      | 641906              | 73                       | 237    |
| 2020-10-24 | ![](http://i1.hdslb.com/bfs/face/7c5f2b5750f64b3f8dcff96c29b6d644b61c4f0f.jpg_64x64.jpg) | 十周年转正了         | 381357206           | 69                       | 1720   |
| 2020-10-25 | ![](http://i1.hdslb.com/bfs/face/2c6881484a4e78b282980bb5dbd32d66cbd76caa.jpg_64x64.jpg) | 低音鲨channel        | 1530836             | 73                       | 442    |
| 2020-10-25 | ![](http://i1.hdslb.com/bfs/face/576ca1b36e57f082906648c9c6a37d0d36df2aaf.jpg_64x64.jpg) | Eki11                | 1356009             | 65                       | 385    |
| 2020-10-25 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 46                       | 677    |
| 2020-10-26 | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 50                       | 1051   |
| 2020-10-26 | ![](http://i1.hdslb.com/bfs/face/0f078e191cb55a1180333d256ecc597db305ab02.jpg_64x64.jpg) | 啃饼饼               | 8032961             | 44                       | 189    |
| 2020-10-26 | ![](http://i1.hdslb.com/bfs/face/92fc44f3a8f3cb51bef912aa5856b0878c813063.jpg_64x64.jpg) | 没有感情的答谢姬长磐 | 29561320            | 38                       | 1956   |
| 2020-10-27 | ![](http://i1.hdslb.com/bfs/face/0f078e191cb55a1180333d256ecc597db305ab02.jpg_64x64.jpg) | 啃饼饼               | 8032961             | 44                       | 189    |
| 2020-10-27 | ![](http://i1.hdslb.com/bfs/face/955a1092d4b911d5e7bd02c212351616228b951d.jpg_64x64.jpg) | 凛祢立华奏           | 19184692            | 41                       | 1051   |
| 2020-10-27 | ![](http://i1.hdslb.com/bfs/face/c3d0db57bdc253ec5e2f57c04356a67e6f701e6a.gif)           | 苏黎世°              | 394098              | 39                       | 517    |
| 2020-10-28 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 56                       | 677    |
| 2020-10-28 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 49                       | 1578   |
| 2020-10-28 | ![](http://i1.hdslb.com/bfs/face/0f078e191cb55a1180333d256ecc597db305ab02.jpg_64x64.jpg) | 啃饼饼               | 8032961             | 44                       | 189    |
| 2020-10-29 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 69                       | 1578   |
| 2020-10-29 | ![](http://i1.hdslb.com/bfs/face/29d3ad7dfb43e9ded013e4946add8a02fcddb81e.jpg_64x64.jpg) | 妖哥哥呦             | 12097824            | 68                       | 87     |
| 2020-10-29 | ![](http://i1.hdslb.com/bfs/face/0f078e191cb55a1180333d256ecc597db305ab02.jpg_64x64.jpg) | 啃饼饼               | 8032961             | 63                       | 189    |
| 2020-10-30 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 237                      | 1578   |
| 2020-10-30 | ![](http://i1.hdslb.com/bfs/face/c3d0db57bdc253ec5e2f57c04356a67e6f701e6a.gif)           | 苏黎世°              | 394098              | 65                       | 517    |
| 2020-10-30 | ![](http://i1.hdslb.com/bfs/face/0fc1d0770a84faa28a751b613e4046bac6b5c4d7.jpg_64x64.jpg) | bibi何伟健           | 423126963           | 65                       | 1933   |
| 2020-10-31 | ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) | 柴可罗               | 414854124           | 230                      | 1578   |
| 2020-10-31 | ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) | 21449580             | 21449580            | 54                       | 677    |
| 2020-10-31 | ![](http://i1.hdslb.com/bfs/face/0fc1d0770a84faa28a751b613e4046bac6b5c4d7.jpg_64x64.jpg) | bibi何伟健           | 423126963           | 50                       | 1933   |

### 阿伟，你又在 D 哦

好家伙，从上面那个表滑下来是不是发现很多相同的头像？于是我进一步提取数据，看看哪些人老在 D。下表是 10 月份出现在上表中次数最多的前三位，我愿称你们为 **最 强 の D D**！

> 2020-10 最 强 の D D

|                                           头像                                           |       昵称      | 上榜次数 |
|:----------------------------------------------------------------------------------------:|:---------------:|:--------:|
| ![](http://i1.hdslb.com/bfs/face/65e35428e3f51487257d23731d236b53ea2598ee.jpg_64x64.jpg) | VersaceGivenchy |    14    |
| ![](http://i1.hdslb.com/bfs/face/164a7b589fb138047a4b5e06033751f1649b341b.jpg_64x64.jpg) |      柴可罗     |    13    |
| ![](http://i1.hdslb.com/bfs/face/dfe77fd9fb029011dbdde35e6960f652ead8ee84.jpg_64x64.jpg) |     21449580    |    11    |

### 我生于世上的理由

10 月份，弹幕数最多的 20 位 DD，最多是 20988 条，也就是平均约 700 条/每天，太强了！

![](images/2020-10-danmaku-king.png)

\**2020-10 弹幕数最多的 20 位 DD 详情*

## License

Copyright (c) 2020 Lewis Tian. Licensed under the MIT license.