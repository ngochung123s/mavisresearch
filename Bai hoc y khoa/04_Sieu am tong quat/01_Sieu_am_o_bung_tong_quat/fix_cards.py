import json
with open(r'F:\DL\mavisresearch\Bai hoc y khoa\04_Sieu am tong quat\01_Sieu_am_o_bung_tong_quat\Sieu_am_o_bung_tong_quat_2026-06-28.cards.json', 'r', encoding='utf-8-sig') as f:
    raw = f.read().strip()
content = '{"cards": ' + raw + '}'
data = json.loads(content)
with open(r'F:\DL\mavisresearch\Bai hoc y khoa\04_Sieu am tong quat\01_Sieu_am_o_bung_tong_quat\Sieu_am_o_bung_tong_quat_2026-06-28.cards.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Fixed: ' + str(len(data['cards'])) + ' cards')
