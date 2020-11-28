#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-11-27 16:22:46
# @Author  : Lewis Tian (taseikyo@gmail.com)
# @Link    : github.com/taseikyo
# @Version : python3.8

"""
试图分析 DD 们的发言来发现有趣的东西
另外，顺便说一句，我是单推（理直气壮）
"""

import os
import time
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

# 房间名排序
# room_id: name
MY_WIVES = {
    # "41682": "早稻叽",
    # "3822389": "有栖Mana",
    # "6542258": "缀目日伞",
    # "8725120": "古守血遊",
    # "14052636": "夢乃栞Yumeno_Shiori",
    # "14327465": "花园Serena",
    # "21320551": "乙女音",
    # "21396545": "绯赤艾莉欧",
    # "21449083": "物述有栖",
    # "21602686": "新科娘",
    # "21685677": "鈴宮鈴",
    # "21701071": "永远酱",
    "21919321": "Hiiro",
    # "22347054": "椎名菜羽",
}


MERGE_RULES = (
    "233",
    "666",
    "nee",
    "8888",
    "wwww",
    "hhhh",
    "???",
    "？？？",
    "哈哈哈",
)


def merge_repetition(danmaku: str) -> str:
    """
    合并一些重复发言
    简单的用前缀匹配去除
    而重复字符串（打 call）需要正则匹配
    23333...3 => 2333
    8888...88 => 8888
    wwww...ww => wwww
    \nano/\nano/\nano/ => \nano/
    """
    for row in MERGE_RULES:
        if danmaku.startswith(row):
            return row

    # 去除打 call 的重复
    # \nano/\nano/\nano/ => \nano/
    # nano...nano...寂しい... => nano...
    # 上面这种去重是错误的，需要判断拦截一下
    # import re
    # pattern = re.compile(r"(.+?)\1+")
    # substr = pattern.findall(danmaku)
    # if (
    #     not substr
    #     or (len(substr[0]) == 1 and substr[0] * len(danmaku) != danmaku)
    #     or substr[0] * (len(danmaku) // len(substr[0])) != danmaku
    # ):
    #     return danmaku
    # return substr[0]

    # 正则还是有问题，还是用最蠢的方法，虽然耗时
    idx, size = 0, len(danmaku)
    while idx < size:
        idx += 1
        if size % idx:
            continue
        cnt = size // idx
        if danmaku[:idx] * cnt == danmaku:
            return danmaku[:idx]

    return danmaku


def obtain_danmakus(
    my_wife: Tuple[str, str],
    date: str = time.strftime("%Y-%m-%d", time.localtime()),
) -> Dict[str, int]:
    """
    获取对应老婆弹幕
    $my_wife: (rid, name)，房间号和名称
    $date: 日期
    """
    rid, _ = my_wife
    dd_danmakus = defaultdict(int)

    filename = f"bilibili-vtuber-danmaku/{rid}/{date}.txt"
    if not os.path.exists(filename):
        return {}
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            # 开始为时间戳的留下来，由于源文件中存在其他数据
            # 如 TIME20:xxx 和最后一行的总结，这些我不需要
            if not line.startswith("16"):
                continue
            danmaku = "".join(line.split(":")[2:]).replace("\n", "").strip()
            # 略过同传
            if danmaku.startswith("【"):
                continue
            dd_danmakus[merge_repetition(danmaku)] += 1
    return dd_danmakus


def top_n_danmakus(
    danmakus: Dict[str, int],
    limit: int = 10,
) -> List[Tuple[str, int]]:
    """
    获取排名前 n 的弹幕
    $danmakus: 弹幕
    $limit: 阈值
    """
    return Counter(danmakus).most_common(limit)


def save_danmakus(
    my_wife: Tuple[str, str],
    date: str = time.strftime("%Y-%m-%d", time.localtime()),
) -> None:
    """
    获取弹幕并另存为文本
    和 obtain_danmakus 大部分相同，不知道怎么合并
    $my_wife: (rid, name)，房间号和名称
    $date: 日期
    """
    rid, _ = my_wife
    dd_danmakus = []

    filename = f"bilibili-vtuber-danmaku/{rid}/{date}.txt"
    dst_filename = f"{rid}_{date}_purge.txt"
    if not os.path.exists(filename):
        return
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            # 开始为时间戳的留下来，由于源文件中存在其他数据
            # 如 TIME20:xxx 和最后一行的总结，这些我不需要
            if not line.startswith("16"):
                continue
            danmaku = "".join(line.split(":")[2:]).replace("\n", "").strip()
            dd_danmakus.append(danmaku)

    with open(dst_filename, "w", encoding="utf-8") as fp:
        fp.write("".join(dd_danmakus))


def draw_cloud(
    my_wife: Tuple[str, str],
    font_path: str = "C:/Windows/Fonts/msyh.ttc",
    image_path: str = "",
    date: str = time.strftime("%Y-%m-%d", time.localtime()),
    color: str = "#FFFFFF",
):
    """
    词云图
    $my_wife: (rid, name)，房间号和名称
    $font_path: 字体路径
    $image_path: 背景图片
    $date: 日期
    $color: 十六进制颜色
    """
    import jieba
    from imageio import imread
    from wordcloud import WordCloud

    rid, _ = my_wife
    filename = f"{rid}_{date}_purge.txt"
    if not os.path.exists(filename):
        return
    with open(filename, encoding="utf-8") as fp:
        text = fp.read()
    # 中文分词
    seg_list = jieba.cut(text, cut_all=False)

    with open("stopwords.txt", encoding="utf-8") as fp:
        stop_seg_list = fp.read().splitlines()

    # 把文本中的 stopword 剃掉
    my_word_list = []

    for my_word in seg_list:
        if len(my_word.strip()) > 1 and not my_word.strip() in stop_seg_list:
            my_word_list.append(my_word)

    if not os.path.exists("images"):
        os.mkdir("images")

    my_word_str = " ".join(my_word_list)
    dst_filename = f"{rid}-{date}-wordcloud"
    idx = 1
    while os.path.exists(f"images/{dst_filename}.png"):
        dst_filename = f"{rid}-{date}-wordcloud_{idx}"
        idx += 1

    if image_path:
        wc = WordCloud(
            font_path=font_path,
            background_color=color,
            mask=imread(image_path),
        )
    else:
        wc = WordCloud(
            font_path=font_path,
            background_color=color,
            random_state=1024,
            width=1920,
            height=1080,
        )
    try:
        wc.generate(my_word_str)
        wc.to_file(f"images/{dst_filename}.png")
    except Exception as e:
        print(e)


def active_dd(
    date: str = time.strftime("%Y-%m-%d", time.localtime()),
    limit: int = 10,
):
    """
    某一天最活跃的 DD
    活跃是指在某一天到处发弹幕的 DD
    $data: 斩首那一天的 DD
    """
    folders = [x for x in os.listdir("bilibili-vtuber-danmaku")]
    dd_occurrences = defaultdict(int)
    for folder in folders:
        filename = f"bilibili-vtuber-danmaku/{folder}/{date}.txt"
        if not os.path.exists(filename):
            continue
        dd_set = set()
        with open(filename, encoding="utf-8") as fp:
            for line in fp:
                # 开始为时间戳的留下来，由于源文件中存在其他数据
                # 如 TIME20:xxx 和最后一行的总结，这些我不需要
                if not line.startswith("16"):
                    continue
                dd_id = line.split(":")[1]
                dd_set.add(dd_id)
        for x in dd_set:
            dd_occurrences[x] += 1
    return Counter(dd_occurrences).most_common(limit)


def obatin_dd_info(mid: str = "623441612") -> Tuple[str, str, int]:
    """
    获取 DD 的信息（昵称，头像，关注数）
    """
    import requests

    url = f"https://api.bilibili.com/x/space/app/index?mid={mid}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers)
        data = r.json()["data"]["info"]
    except Exception as e:
        print(e)
        return ()
    name = data["name"]
    # http://i1.hdslb.com/bfs/face/{id}.jpg
    avatar_id = data["face"].split("/")[-1]
    following = data["following"]
    return (name, avatar_id, following)


def main():
    """
    食用注意设定阈值（limit）和时间（date）
    相关函数也有默认值
    """
    limit = 20
    date = "2020-11-25"
    for wife in MY_WIVES.items():
        danmakus = obtain_danmakus(my_wife=wife, date=date)
        topn = top_n_danmakus(danmakus, limit=limit)
        print(topn)
        save_danmakus(my_wife=wife, date=date)
        draw_cloud(my_wife=wife, date=date)
        draw_cloud(my_wife=wife, date=date, image_path="images/box.png")


def oct_top3():
    print("日期\t头像\t昵称\tID\t处处 D\t关注数")
    for x in range(1, 32):
        date = f"2020-10-{x}"
        for mid, cnt in active_dd(date, 3):
            info = obatin_dd_info(mid)
            print(f"{date}\t{info[1]}\t{info[0]}\t{mid}\t{cnt}\t{info[2]}")


if __name__ == "__main__":
    main()
