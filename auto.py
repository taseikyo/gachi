#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2021-04-28 14:13:08
# @Author  : Lewis Tian (taseikyo@gmail.com)
# @Link    : github.com/taseikyo
# @Version : Python 3.9

import base64
import calendar
import datetime
import os
from urllib import request as urequest

import jieba
import matplotlib.pyplot as plt
import seaborn as sns
from imageio import imread
from wordcloud import WordCloud

sns.set(
    style="ticks",
    rc={
        "figure.figsize": [21, 9],
        "text.color": "white",
        "axes.labelcolor": "white",
        "axes.edgecolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "axes.facecolor": "#443941",
        "figure.facecolor": "#443941",
    },
)


def obatin_danmaku_of_vup_one_day(roomid: str, date: str) -> None:
    """
    下载某一天 roomid 房间的弹幕

    @roomid: 房间 id
    @date:   时间（格式：2021-1-12）

    eg: obatin_danmaku_of_vup_one_day("21402309", "2021-4-25")
    """
    assert len(date.split("-")) == 3

    url = f"https://raw.githubusercontent.com/dd-center/bilibili-vtuber-danmaku/master/{roomid}/{date}.txt"
    print(f"downloading {roomid} {date} danmakus...")
    if not os.path.exists(roomid):
        os.mkdir(roomid)
    if os.path.exists(f"{roomid}/{date}.txt"):
        print(f"{roomid} {date} danmakus already exists!")
        return
    try:
        urequest.urlretrieve(url, f"{roomid}/{date}.txt")
        print(f"The danmaku has been save to {roomid}/{date}.txt!")
    except:
        # 姑且放个空文件在这
        with open(f"{roomid}/{date}.txt", "w") as f:
            pass
        print(f"Fail to download the danmaku of {date}!")


def purge_danmakus(roomid: str, date: str) -> None:
    """
    提取 vup 某天的弹幕并另存为文本
    文本的名称为 {roomid}_{date}_purge.txt

    @roomid: 直播间 id
    @date: 日期（2021-3-10）
    """
    dd_danmakus = []

    filename = f"{roomid}/{date}.txt"
    dst_filename = f"{roomid}_{date}_purge.txt"
    if not os.path.exists(filename) or os.path.exists(dst_filename):
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


def obatin_danmaku_of_vup_one_month(roomid: str, year: int, month: int) -> None:
    """
    下载某个月 roomid 房间的弹幕

    @roomid: 房间 id
    @year:   年份
    @month:  月份

    eg: obatin_danmaku_of_vup_one_month("21402309", 2021, 5)
    """
    # 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
    days = calendar.monthrange(year, month)[-1]
    for day in range(1, days + 1):
        obatin_danmaku_of_vup_one_day(roomid, f"{year}-{month}-{day}")


def draw_cloud(
    filename: str,
    font_path: str = "SourceHanSansCN-Light.otf",
    image_path: str = "",
    color: str = "#FFFFFF",
    width: int = 1920,
    height: int = 1080,
) -> str:
    """
    画指定文件的词云图，返回存储的文件名

    @filename: 弹幕文件路径
    @font_path: 字体路径
    @image_path: 背景图片
    @color: 十六进制颜色
    """
    if not os.path.exists(filename):
        return

    purge_name = os.path.splitext(filename)[0]
    dst_filename = f"{purge_name}_wordcloud"
    if os.path.exists(f"images/{dst_filename}.png"):
        print(f"images/{dst_filename}.png is existed!")
        return dst_filename

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
            width=width,
            height=height,
        )

    try:
        wc.generate(my_word_str)
        # 保存
        wc.to_file(f"images/daily/{dst_filename}.png")
        # 显示
        # plt.imshow(wc, interpolation='bilinear')
        # plt.axis("off")
        return dst_filename
    except Exception as e:
        print(e)


def image_base64(img_name) -> str:
    """
    将图片转为 base64 格式字符串返回

    @img_name: 图片名称，不带后缀（如：14052636_2021-6-13_purge_wordcloud）
    """
    img_path = f"images/daily/{img_name}.png"
    if not os.path.exists(img_path):
        print(f"{img_path} is not existed!")
        return

    with open(img_path, "rb") as f:
        img = f.read()
        img_base64 = str(base64.b64encode(img), encoding="utf-8")
        return img_base64


def download_all_vup_day(date, rooms_filepath="rooms.txt") -> None:
    """
    下载某天的所有弹幕

    @date: 日期，格式同上
    @rooms_filepath: 记录房间号的文件路径
    """
    with open(rooms_filepath, encoding="utf-8") as f:
        for roomid in f:
            roomid = roomid.split(" ")[-1].replace("\n", "")
            obatin_danmaku_of_vup_one_day(roomid, date)
            purge_danmakus(roomid, date)


def generate_wordcloud_all_vup_day(date, rooms_filepath="rooms.txt") -> dict:
    """
    根据日期生成所有直播间一天的词云图

    @date: 日期，格式同上
    @rooms_filepath: 记录房间号的文件路径
    """
    if not os.path.exists(rooms_filepath):
        print(f"{rooms_filepath} is not existed!")
        return

    image_base64_dict = {}
    with open(rooms_filepath, encoding="utf-8") as f:
        for roomid in f:
            roomid = roomid.split(" ")[-1].replace("\n", "")
            img_base64 = image_base64(
                draw_cloud(f"{roomid}_{date}_purge.txt", width=1080, height=463)
            )
            image_base64_dict[roomid] = img_base64

    return image_base64_dict


def generate_kusa_all_vup_day(date, rooms_filepath="rooms.txt") -> dict:
    """
    根据日期生成所有直播间一天的 草 图

    @date: 日期，格式同上
    @rooms_filepath: 记录房间号的文件路径
    """
    if not os.path.exists(rooms_filepath):
        print(f"{rooms_filepath} is not existed!")
        return

    kusa_dict = {}
    with open(rooms_filepath, encoding="utf-8") as f:
        for roomid in f:
            roomid = roomid.split(" ")[-1].replace("\n", "")

            cnt = 0
            with open(f"{roomid}/{date}.txt", encoding="utf-8") as f:
                for line in f:
                    if line.find("草") >= 0:
                        cnt += 1
            kusa_dict[roomid] = cnt

    plt.figure(figsize=(18, 5))
    plt.bar(kusa_dict.keys(), kusa_dict.values(), color="white")
    plt.xlabel("VTuber", fontsize=16)
    plt.ylabel("Counts", fontsize=16)
    plt.title(f"Number of kusa ({date})", fontsize=24)
    plt.savefig(f"images/daily/{date}-kusa.png")

    return kusa_dict


def dump_daily_md(date, data, rooms_filepath="rooms.txt") -> None:
    """
    根据数据（data）生成日报

    @date: 日期
    @data: 数据
    @rooms_filepath: 记录房间号的文件路径
    """
    if not os.path.exists("daily"):
        os.mkdir("daily")

    vup_dict = {}
    with open(rooms_filepath, encoding="utf-8") as f:
        for roomid in f:
            _, name, roomid = roomid.split(" ")
            vup_dict[roomid.replace("\n", "")] = name

    file_header = f"""> @Date    : {date} 08:00:00
>
> @Author  : Lewis Tian (taseikyo@gmail.com)
>
> @Link    : github.com/taseikyo
"""

    today = datetime.datetime.today()
    day1 = today - datetime.timedelta(days=2)
    date1 = f"{day1.year}-{day1.month}-{day1.day}"
    date2 = f"{today.year}-{today.month}-{today.day}"
    with open(f"daily/docs/{date}.md", "w", encoding="utf-8") as f:
        f.write(file_header)
        f.write(f"\n# DD 日报（{date}）\n")
        anchor = f"\n[readme](../README.md) | [yesterday]({date1}.md) | [tomorrow]({date2}.md)\n"
        f.write(anchor)
        f.write("\n## 词云图\n\n")
        f.write("|VTuber|词云图|\n|:-:|-|\n")
        for roomid, img_base64 in data["wordcloud"].items():
            # 列表形式
            # f.write(f"- {vup_dict[roomid]}\n![][{roomid}-{date}]\n\n")
            # 表格形式
            # f.write(f"|{vup_dict[roomid]}|![][{roomid}-{date}]|\n")

            # 原图片形式，上面都是 base64 格式
            # 导致最后生成 md 文件过大，GitHub 无法加载
            f.write(
                f"|{vup_dict[roomid]}|![](../../images/daily/{roomid}_{date}_purge_wordcloud.png)|\n"
            )

        f.write("\n## 百草园\n\n")
        f.write("|VTuber|草|\n|:-:|-|\n")
        for roomid, kusa in data["kusa"].items():
            f.write(f"|{vup_dict[roomid]}|{kusa}|\n")

        f.write(anchor)

        # f.write("\n\n")
        # 将 base64 图片放到文档最后
        # for roomid, img_base64 in data["wordcloud"].items():
        #     f.write(f"[{roomid}-{date}]:data:image/png;base64,{img_base64}\n")


def update_daily_readme():
    """
    根据日刊更新 README
    """
    files = [f for f in os.listdir("daily/docs") if not f.startswith("README")]

    def sort_files(filename):
        """
        排序文件名，由于之前命名问题导致排序存在问题
        2021-7-23.md 会在 2021-7-3.md 之前
        """
        filename = filename.split(".")[0]
        y, m, d = [int(i) for i in filename.split("-")]
        return y * 100 + m * 50 + d

    files.sort(key=sort_files)
    print(files)

    # 表格每行 5 个，不足 5 个补空
    cnt = 0
    one_line = []
    all_line = []
    for file in files:
        one_line.append(f" [{file.split('.')[0]}](docs/{file}) ")
        cnt += 1
        if cnt == 5:
            all_line.append(one_line)
            one_line = []
            cnt = 0

    if 0 < cnt < 5:
        one_line += [" " for _ in range(cnt, 6)]
        all_line.append(one_line)

    table = "\n".join([f"|{'|'.join(x)}|" for x in all_line])

    license = "\n\n## License\n\nCopyright (c) 2021 Lewis Tian. Licensed under the MIT license.\n"

    with open("daily/README_TEMPLATE.md", encoding="utf-8") as f:
        lines = f.readlines()

    with open("daily/README.md", "w", encoding="utf-8") as f:
        f.write("".join(lines))
        f.write(table)
        f.write(license)


if __name__ == "__main__":
    today = datetime.datetime.today()
    yday = today - datetime.timedelta(days=1)
    date = f"{yday.year}-{yday.month}-{yday.day}"
    download_all_vup_day(date)
    data = {}
    data["kusa"] = generate_kusa_all_vup_day(date)
    data["wordcloud"] = generate_wordcloud_all_vup_day(date)
    dump_daily_md(date, data)
    update_daily_readme()
