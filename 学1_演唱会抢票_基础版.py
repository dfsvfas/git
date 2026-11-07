# -*- coding:utf-8 -*-
"""
演唱会抢票
==========
从键盘输入要抢几张。从第 1 秒数到第 30 秒。

秒数能被 7 整除：这一秒在维护。打印「第 N 秒：维护，跳过」，再 continue，这一秒不放票。
秒数能被 5 整除：放一张。张数加 1，把这一秒放进列表，打印抢到第几张。
张数够了：打印「抢满了」，再用 break 离开。
30 秒走完还不够：for 后面的 else 打印「没有抢满」。

然后打印一共几张。几张写成 len。再打印放票的那些秒。
够了就打印「抢满 N 张，收工看演唱会去！」。不够就打印「只抢到 N 张，没抢满」。
最后调用 ask_spark。

先输入 2，应看到：

    第 5 秒：放票！抢到第 1 张
    第 7 秒：维护，跳过
    第 10 秒：放票！抢到第 2 张
    抢满了
    一共 2 张
    放在这些秒： [5, 10]
    抢满 2 张，收工看演唱会去！

再输入 3。第 14 秒会跳过，第 15 秒是第 3 张，然后抢满了。一共 3 张。

再输入 8。票不够，循环走完，打出「没有抢满」。一共 6 张。
放在这些秒： [5, 10, 15, 20, 25, 30]
最后一行是「只抢到 6 张，没抢满」。

三组都要打对。星火那一行有字就对。钥匙空着时，上面这些行仍要打对。

文件开头有两行：API_KEY 和 API_SECRET。
这是基础版。地址是 v1，模型名是 lite，两样必须配对。能开通 X2 就用旁边不带「基础版」的那一份。
到讯飞开放平台开通「星火认知大模型」后，把 APIKey 贴进第一行引号，把 APISecret 贴进第二行引号。
ask_spark 已经写在文件开头，那一段不用改。
"""
import json
import urllib.request

# 这是基础版。地址是 v1，模型名是 lite，两样必须配对。能开通 X2 就用旁边不带「基础版」的那一份。
# 把 APIKey 贴进 API_KEY 的引号，把 APISecret 贴进 API_SECRET 的引号。
# 这两项不要发给别人。引号里还是空的，前面的打印仍会出来。
API_KEY = ""
API_SECRET = ""


def ask_spark(question):
    """向星火提一句。两项还是空的就跳过。回了字会自己打印「星火：」。"""
    if not (API_KEY and API_SECRET):
        print("还没有填写 API_KEY 和 API_SECRET，前面的内容已经打完。")
        return
    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
    body = json.dumps({
        "model": "lite",
        "messages": [{"role": "user", "content": question}],
        "max_tokens": 60,
        "temperature": 0.5,
        "stream": False,
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": "Bearer " + API_KEY + ":" + API_SECRET,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        choices = result.get("choices") or []
        if not choices:
            print("星火没有返回正文。")
            return
        text = ((choices[0].get("message") or {}).get("content") or "").strip()
        if text:
            print("星火：", text)
        else:
            print("星火没有返回正文。")
    except Exception as exc:
        print("请求没有发出：", exc)


# TODO ① 读入要抢几张。张数和列表都建在循环外


need=int(input("要抢的票数:"))
got=0
hits=[]
for item in range(1,31):
    if item % 2 == 0:
        #print("第", item, "秒，崩溃了")
        continue
    if item % 5== 0:

        got+=1
        hits.append(item)
        #print ("第", item,"秒，放票：")
    if got>=need:
        print("抢满了")
        print("一共", len(hits), "张")
        print("放在这些秒", hits)
        print("抢满", got, "张，收工")

        break
else:
    print("没有抢满")
    print("一共",len(hits),"张")
    print("放在这些秒",hits)

    print("没抢满，只有",got,"张，GG")

# TODO ② for：维护秒 continue；逢 5 放票并记进列表；够了 break；走完不够走 else


# TODO ③ len 打印一共几张。够了打印收工，不够打印没抢满。再调用 ask_spark
