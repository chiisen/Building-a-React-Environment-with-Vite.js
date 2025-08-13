import pandas as pd # type: ignore
import os
import json
import math

# 輔助函數：檢查值是否為有效值（非 None 且非 NaN）
def is_valid_value(value):
    if value is None:
        return False
    if isinstance(value, float) and math.isnan(value):
        return False
    return True

# 1. 目錄準備
os.makedirs('./json', exist_ok=True)

# 2. 讀 Excel
df = pd.read_excel("翻譯文件2025.xlsx", sheet_name="一般翻譯工作表")
fileList = [
    ('zh-tw', 4),
    ('en-us', 5),
]

# 取得表頭
header_row = df.columns
# 這裡 D 欄是第 3（從 0 開始），翻譯欄對照 fileList 裡的 col
header_F = header_row[3]

# 3. 逐語言處理
for lang, col in fileList:

    obj = {}

    # 加入_header描述
    obj[str(header_F)] = str(header_row[col])

    seen_keys = set()  # 用來記錄已出現過的 key

    for idx, row in df.iterrows():
        key = row[3]  # D 欄

        value = row[col]

        if is_valid_value(key) and is_valid_value(value):
            if key in seen_keys:
                print(f'重複的 key: {key}')
            else:
                seen_keys.add(key)

            valStr = str(value).replace(',', '++')  # 內容逗號先替換
            valStr = (
                valStr.replace('[**', '{{')
                .replace('**]', '}}')
                .replace('{{break}}', '')
                .replace('(縮字)', '')
                .replace('(缩字)', '')
                .replace('\u00A0', '')
            )

            obj[str(key)] = valStr

    # 4. 輸出 json 檔案
    finalContent = json.dumps(obj, ensure_ascii=False, indent=2)
    finalContent = finalContent.replace(',', ',\n').replace('++', ',')
    finalContent = finalContent.replace(r' ":', r'":').replace('\r', '').replace('\n\n', '\n')

    with open(f'./json/{lang}.json', 'w', encoding='utf-8', newline='') as f:
        f.write(finalContent)

    print(f'{lang}.json is converted')

    

# 5. 產生 i18nKeys.js（略過第一筆 key）
js_lines = []
js_lines.append('// 自動產生 key 靜態成員，避免拼字錯誤\nexport class i18nKeys {')

# 注意這裡略過 df.iterrows() 的第一筆資料
for idx, row in enumerate(df.iterrows()):
    #if idx == 0:
    #    continue  # 略過第一行
    _, r = row
    key = r[3]  # D 欄(完整代碼)
    tw = r[4] # E 欄(繁體中文) 
    en = r[5] # F 欄(英文) 
    if is_valid_value(key):
        clean_key = str(key).strip().replace('\n', '')
        #js_key = clean_key.upper() # 看要要不要轉大寫
        js_key = clean_key
        js_key = ''.join([ch if ch.isalnum() else '_' for ch in js_key])
        tw_str = str(tw) if is_valid_value(tw) else ""
        en_str = str(en) if is_valid_value(en) else ""
        js_lines.append(f'  /** {tw_str} | {en_str} */') # JSDoc 格式的註解，IDE 才能自動偵測
        js_lines.append(f'  static {js_key} = "{clean_key}";')

js_lines.append('}')

with open('./json/i18nKeys.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(js_lines))
print('i18nKeys.js 已產生')
