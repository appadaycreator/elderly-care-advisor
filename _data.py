LEGACY_HTML = True  # 既存HTMLを保持（再アセンブル禁止）
TITLE = '介護費用診断【無料】親の介護 月いくかかる？施設選びガイド'
DESCRIPTION = '要介護度・地域・希望から介護施設の種類と費用相場を無料シミュレーション。在宅・施設比較付き。'
JS_CODE = 'var Qs = [\n  { text:"対象者の現在の状況は？", opts:["自立（元気）","少し介助が必要","要支援1〜2","要介護1〜2","要介護3〜5（重度）"], key:"level" },\n  { text:"認知症の状況は？", opts:["なし・軽度の物忘れ","軽度（日常は自立）","中程度（見守り必要）","重度（常時介護必要）"], key:"dementia" },\n  { text:"居住エリアは？", opts:["都市部（東京・大阪・名古屋等）","地方都市","郊外・農村部"], key:"area" },\n  { text:"月に使える介護費用（自己負担）は？", opts:["5万円未満","5〜10万円","10〜20万円","20万円以上"], key:"budget" },\n  { text:"最も重視することは？", opts:["費用を抑えたい","自宅に近い施設","医療ケアの充実","レクリエーション等の充実"], key:"priority" }\n];\nvar cur=0,ans={};\n\nvar facilityMap = {\n  "low-low": { type:"デイサービス（通所介護）", desc:"自宅で生活しながら日中だけ施設を利用。介護の負担を軽減しつつ自宅での生活を継続できます。", cost:"月2〜5万円", detail:"要支援・要介護1〜2に最適。送迎付きで安心。週2〜5回の利用が一般的。" },\n  "low-high": { type:"グループホーム（認知症対応）", desc:"少人数（5〜9名）で共同生活する施設。認知症の方に最も適した環境です。", cost:"月13〜18万円", detail:"認知症の進行を穏やかにする効果が期待できます。定員が少ないため早めの申し込みを。" },\n  "high-low": { type:"介護老人保健施設（老健）", desc:"医療ケアを受けながら在宅復帰を目指すリハビリ施設。医師・看護師が常駐。", cost:"月8〜15万円", detail:"退院後の自宅復帰を目指す方に最適。3〜6ヶ月の利用が一般的。" },\n  "high-high": { type:"特別養護老人ホーム（特養）", desc:"要介護3以上が入居できる公的施設。24時間介護体制で費用が比較的安い。", cost:"月6〜15万円", detail:"要介護3以上が対象。待機者が多いため早めに申し込みを。介護保険で費用を大幅に抑えられます。" }\n};\n\nfunction startDiagnosis() { show(\'questions\'); renderQ(); }\n\nfunction show(name) {\n  document.querySelectorAll(\'.screen\').forEach(function(s){ s.classList.remove(\'active\'); });\n  document.getElementById(\'screen-\'+name).classList.add(\'active\');\n}\n\nfunction renderQ() {\n  var q = Qs[cur];\n  var pct = Math.round((cur+1)/Qs.length*100);\n  document.getElementById(\'q-label\').textContent=\'質問 \'+(cur+1)+\' / \'+Qs.length;\n  document.getElementById(\'q-pct\').textContent=pct+\'%\';\n  document.getElementById(\'prog\').style.width=pct+\'%\';\n  document.getElementById(\'q-text\').textContent=q.text;\n  var c=document.getElementById(\'opts\'); c.innerHTML=\'\';\n  q.opts.forEach(function(opt,i){\n    var b=document.createElement(\'button\');\n    b.className=\'option-btn\'; b.textContent=opt;\n    b.onclick=function(){ pick(i,opt,q.key); };\n    c.appendChild(b);\n  });\n}\n\nfunction pick(i,val,key) {\n  ans[key]={i:i,val:val};\n  document.querySelectorAll(\'.option-btn\').forEach(function(b,j){ b.classList.toggle(\'selected\',j===i); });\n  setTimeout(function(){\n    cur++;\n    if(cur<Qs.length){ renderQ(); } else { show(\'loading\'); setTimeout(showResults,1600); }\n  },300);\n}\n\nfunction showResults() {\n  var levelIdx = ans.level ? ans.level.i : 2;\n  var dementiaIdx = ans.dementia ? ans.dementia.i : 0;\n  var isHeavy = levelIdx >= 3;\n  var hasDementia = dementiaIdx >= 2;\n  var key = (isHeavy?\'high\':\'low\')+\'-\'+(hasDementia?\'high\':\'low\');\n  var facility = facilityMap[key] || facilityMap[\'high-low\'];\n  document.getElementById(\'res-type\').textContent = facility.type;\n  document.getElementById(\'res-desc\').textContent = facility.desc;\n  document.getElementById(\'res-cost\').textContent = facility.cost;\n  document.getElementById(\'res-detail\').textContent = facility.detail;\n  show(\'results\');\n}\n\nfunction restart() { cur=0; ans={}; show(\'intro\'); }'
MAIN_HTML = '<div><button class="btn">開始する</button></div>'
FAQ = [
    ('介護費用診断は無料で使えますか？', 'はい、完全無料・登録不要でご利用いただけます。'),
    ('何回でも使えますか？', 'はい、回数制限なく何度でもご利用いただけます。'),
    ('入力したデータはサーバーに送信されますか？', 'いいえ。すべての処理はブラウザ内で完結し、入力内容はサーバーへ送信されません。'),
    ('スマートフォンでも使えますか？', 'はい、スマートフォン・タブレット・PCすべてに最適化されています。'),
    ('結果を保存・共有できますか？', 'スクリーンショットでの保存またはSNSシェアボタンからご共有いただけます。'),
]
HOW_TO = [
    'ページを開き、入力フォームの項目を確認する',
    '必要な情報を入力または選択する',
    '実行ボタンをクリックして結果を取得する',
    '表示された結果・アドバイスを確認する',
    '必要に応じてコピー・SNSシェアで活用する',
]
FOOTER_LINKS = [('https://appadaycreator.com/sleep-quality-checker/', '睡眠の質チェッカー'), ('https://appadaycreator.com/bmi-body-tracker/', 'BMI・体重管理'), ('https://appadaycreator.com/household-budget-analyzer/', '家計簿診断')]
