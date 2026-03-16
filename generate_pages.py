import os

# 蔬菜數據 (ID, 名稱, 基本做法, 特別食譜, 分類)
data = [
    ("butter-cabbage", "有機奶油白菜", "奶油白菜清炒", "奶油白菜煎培根格拉辛", "快炒"),
    ("komatsuna", "有機小松菜", "小松菜炒蛋", "小松菜堅果青醬", "快炒"),
    ("baby-bok-choy", "有機小白菜", "蒜炒小白菜", "韓式小白菜煎餅", "快炒"),
    ("baby-mustard", "有機小芥菜", "小芥菜清炒", "家傳雪裡紅肉絲", "快炒"),
    ("you-cai", "有機油菜", "蒜香油菜", "日式胡麻油菜花拌飯", "快炒"),
    ("water-spinach", "有機空心菜", "蒜炒空心菜", "泰式辣炒空心菜", "快炒"),
    ("gai-lan", "有機芥藍菜", "蒜炒芥藍", "廣式薑汁糖酒芥藍", "快炒"),
    ("tongho", "有機茼蒿", "茼蒿豆腐湯", "酥脆茼蒿天婦羅", "快炒"),
    ("bok-choy", "有機青江菜", "蒜炒青江菜", "鑲肉青江菜心", "快炒"),
    ("qing-you-cai", "有機青油菜", "青油菜豆腐湯", "青油菜培根溫沙拉", "快炒"),
    ("black-leaf-cabbage", "有機黑葉白菜", "黑葉白菜快炒", "味噌奶油黑葉白菜", "快炒"),
    ("a-cai", "有機Ａ菜", "清炒Ａ菜", "腐乳豆乳Ａ菜", "快炒"),
    ("mizuna", "有機京都水菜", "京都水菜豆腐鍋", "日式豬肉哈里哈里鍋", "湯/火鍋"),
    ("mountain-spinach", "有機山菠菜", "山菠菜蒜炒", "山菠菜豆腐蛋花羹", "湯/火鍋"),
    ("swiss-chard", "有機瑞士菠菜", "瑞士菠菜清湯", "彩虹瑞士菠菜烘蛋", "湯/火鍋"),
    ("japanese-tongho", "有機日本茼蒿", "日本茼蒿清湯", "柴魚湯浸日本茼蒿", "湯/火鍋"),
    ("sweet-choy-sum", "有機甜菜心", "甜菜心蒜炒", "干貝蠔油甜菜心", "湯/火鍋"),
    ("beet-greens", "有機甜菜葉", "甜菜葉清炒", "俄式紅菜頭葉冷湯", "湯/火鍋"),
    ("spinach", "有機菠菜", "菠菜蛋花湯", "印度菠菜起司泥", "湯/火鍋"),
    ("radish-leaf", "有機葉蘿蔔", "葉蘿蔔蛋花湯", "韓式葉蘿蔔水泡菜", "湯/火鍋"),
    ("butter-lettuce", "有機奶油萵苣", "奶油萵苣溫沙拉", "低醣生菜包肉捲", "生食/沙拉"),
    ("sweet-romaine", "有機甜蘿蔓", "甜蘿蔓凱薩沙拉", "焦香炭烤蘿蔓心", "生食/沙拉"),
    ("fushan-lettuce", "有機福山萵苣", "福山萵苣水果沙拉", "水果堅果優格沙拉", "生食/沙拉"),
    ("emerald-lettuce", "有機綠寶石萵苣", "綠寶石萵苣沙拉", "煙燻鮭魚綠寶石卷", "生食/沙拉"),
    ("chicory", "有機菊苣", "菊苣溫沙拉", "法式里昂風沙拉", "生食/沙拉"),
    ("romaine", "有機蘿蔓", "蘿蔓凱薩沙拉", "牛肉漢堡沙拉碗", "生食/沙拉"),
    ("oak-leaf-lettuce", "有機鹿角萵苣", "鹿角萵苣沙拉", "柑橘油醋煙燻雞肉沙拉", "生食/沙拉"),
    ("you-ai-cabbage", "有機優愛白菜", "優愛白菜清炒", "金沙鹹蛋優愛白菜", "特色菜"),
    ("qianbao-cai", "有機千寶菜", "千寶菜蒜炒", "培根厚切炒千寶菜", "特色菜"),
    ("weimei-cai", "有機味美菜", "味美菜清炒", "蒜片腰果炒味美菜", "特色菜"),
    ("tagu-cai", "有機塔菇菜", "塔菇菜炒香菇", "上海鹹肉塔菇菜菜飯", "特色菜"),
    ("hiroshima-greens", "有機廣島菜", "廣島菜和風拌菜", "和風廣島菜淺漬", "特色菜"),
    ("kale", "有機羽衣甘藍", "羽衣甘藍炒蒜片", "氣炸羽衣甘藍脆片", "特色菜"),
    ("lotus-cabbage", "有機荷葉白菜", "荷葉白菜豆腐湯", "蒜蓉粉絲蒸荷葉白菜", "特色菜"),
    ("amaranth", "有機莧菜", "莧菜吻仔魚湯", "濃郁皮蛋莧菜湯", "特色菜"),
    ("michelle-cabbage", "有機蜜雪兒白菜", "蜜雪兒白菜快炒", "蜜雪兒白菜蝦仁滑蛋", "特色菜"),
    ("snow-cai", "有機雪菜", "雪菜豆腐", "雪菜毛豆炒百葉", "特色菜"),
    ("qingsong-cai", "有機青松菜", "青松菜蒜炒", "櫻花蝦快炒青松菜", "特色菜"),
    ("cabbage", "有機高麗菜", "高麗菜清炒", "手撕包菜 (湖南風味)", "特色菜"),
    ("broccoli", "有機青花菜", "蒜香青花菜", "焗烤起司青花菜", "特色菜"),
    ("cauliflower", "有機白花菜", "白花菜炒肉片", "香煎花椰菜排", "特色菜"),
    ("cucumber", "有機小黃瓜", "涼拌小黃瓜", "日式鹽漬小黃瓜", "特色菜")
]

css = "body { font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; } .recipe-card { border-left: 5px solid #2e5a27; background: #f9fbf9; padding: 15px; margin: 20px 0; } .btn { display: inline-block; padding: 10px; border: 1px solid #2e5a27; text-decoration: none; color: #2e5a27; }"

for vid, name, std, spec, cat in data:
    html = f"<html><head><meta charset='utf-8'><style>{css}</style></head><body><p>{cat}</p><h1>{name}</h1><div class='recipe-card'><h3>家常做法</h3><p>{std}</p></div><div class='recipe-card'><h3>特別推薦</h3><p>{spec}</p></div><a class='btn' href='vegetables.html'>返回</a></body></html>"
    with open(f"{vid}.html", "w", encoding="utf-8") as f:
        f.write(html)

print("Done!")
