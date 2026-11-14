import streamlit as st
import random

# 頁面配置
st.set_page_config(
    page_title="數位資產素養與社群防詐平台",
    page_icon="📌",
    layout="wide"
)

# 初始化 Session State
if 'user_id' not in st.session_state:
    st.session_state.user_id = f"Student-{random.randint(10000, 99999)}"
if 'user_points' not in st.session_state:
    st.session_state.user_points = 210

if 'cookie_count' not in st.session_state:
    st.session_state.cookie_count = 0
if 'cookie_history' not in st.session_state:
    st.session_state.cookie_history = []

if 'completed_units' not in st.session_state:
    st.session_state.completed_units = ["unit_1"]

if 'wall_posts' not in st.session_state:
    st.session_state.wall_posts = [
        {
            "url": "https://www.lbank.com/bonus/center?icode=66I9H", 
            "comment": "這是 LBank 官方合法行銷活動連結，經系統審核為安全白名單。", 
            "risk": "🟢 合法官方活動/推廣網址", 
            "reporter": "Student-32808",
            "image": None
        },
        {
            "url": "https://fake-uniswap-rewards.com", 
            "comment": "假冒 Uniswap 官方發放空投獎勵，要求 Permit 授權，點擊後錢包資產全數被清空！", 
            "risk": "🔴 高風險釣魚 (AI自動審核)", 
            "reporter": "Student-88219",
            "image": None
        }
    ]

# 頂部導覽列與即時積分狀態
st.title("📌 數位資產素養與社群防詐推廣平台")
st.markdown("### 結合影音內容與社群媒體之新興數位資產素養平台設計與經營")
st.success("📌 **115學年度元培醫事科技大學資訊管理系畢業專題** | 指導老師：杜建志 老師 | 組員：林俊磊、吳品毅、林建愷、楊杰斯")

# 計算當前素養等級與模擬排名
pts = st.session_state.user_points
if pts >= 400:
    level_str = "🏆 資安防禦專家 (Lv.4)"
    rank_str = "全國排名 Top 5% (校內排名前 3名)"
elif pts >= 250:
    level_str = "🥈 資進階防護生 (Lv.3)"
    rank_str = "全國排名 Top 18% (校內排名前 12名)"
else:
    level_str = "🥉 資安新手 (Lv.2)"
    rank_str = "全國排名 Top 45% (建議加強微學習)"

# 積分與動態身分看板
st.markdown("---")
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.info(f"👤 **當前登入訪客編號**\n\n`{st.session_state.user_id}` (動態生成)")
with col_s2:
    st.warning(f"⭐ **平台學習積分 (Coins)**\n\n`{st.session_state.user_points} 點`")
with col_s3:
    st.success(f"📌 **資安素養防禦等級**\n\n{level_str}")

with st.expander("📊 【點我展開】查看詳細資安防禦等級、同儕排名與積分特權對照表"):
    st.markdown(f"""
    * **訪客專屬代號**：`{st.session_state.user_id}`
    * **累積學習積分**：`{st.session_state.user_points} 點 Coins`
    * **當前資安素養階級**：`{level_str}`
    * **即時同儕防禦排名**：`{rank_str}`
    * **積分特權說明**：積分可用於解鎖高級防詐白名單查詢權限與專屬測驗勳章！
    """)

st.markdown("---")

# 🧭 側邊欄導覽選單
st.sidebar.title("🧭 系統功能導覽選單")
menu = st.sidebar.radio("選擇功能分頁：", [
    "🏠 專題核心與數位資產素養總覽",
    "🎬 短影音微學習專區",
    "🔍 防詐網址審核與留言牆",
    "🥠 幸運餅乾盲盒",
    "👥 團隊成員與 WBS 分工"
])

# 1. 核心總覽與豐富的數位資產素養專論 (已強化青年使用現況)
if menu == "🏠 專題核心與數位資產素養總覽":
    st.header("🏠 新興數位資產素養平台設計與教育核心總覽")
    st.write("""
    本專題針對大專院校學生與青年世代，打造兼具**「數位資產素養教育」**、**「短影音微學習」**與**「社群同儕防詐互助」**的 Web3 資安教育生態系。
    """)
    
    st.markdown("---")
    st.subheader("📖 深度專論：現代青年如何使用新興數位資產與建立素養？")
    st.write("""
    在 Web3、區塊鏈與去中心化金融（DeFi）迅速發展的時代，現代青年世代參與和使用新興數位資產的模式已高度多樣化：
    * **多元應用參與**：青年族群普遍透過加密貨幣與穩定幣（如 USDT）進行跨境理財、參與 NFT 數位收藏品鑄造、體驗去中心化金融（DeFi）質押挖礦，或透過 Discord / Telegram 參與各類社群空投（Airdrop）活動。
    * **資安自主與風險**：個人享有完全自主管理資產的權利（Self-Sovereignty），但這也伴隨著絕對的個人資安責任。在傳統集中式金融（CeFi）中，如銀行帳戶遭盜領可透過客服凍結；但在區塊鏈上，交易一旦透過私鑰簽章送出即**絕對不可逆（Irreversibility）**。
    
    因此，本專題將「數位資產素養」深化拆解為以下三大核心防禦構面：
    """)
    
    # 三大構面詳細卡片 (已修正排版格式)
    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        st.info("🧠 **1. 技術認知構面 (Technical)**\n\n* **核心內涵**：理解區塊鏈底層心智模型、公私鑰加密原理。\n* **防禦重點**：明確區分冷熱錢包管理差異，牢記「助記詞/私鑰絕對不上雲端」之鐵律。")
    with col_d2:
        st.warning("🛡️ **2. 風險防護構面 (Protection)**\n\n* **核心內涵**：落實零信任（Zero Trust）原則。\n* **防禦重點**：識別釣魚網站（Punycode 網域偽造）、假空投誘餌與 Permit2 無限授權合約陷阱。")
    with col_d3:
        st.success("🤝 **3. 資訊審核構面 (Verification)**\n\n* **核心內涵**：運用群眾智慧與同儕審查（Peer Verification）。\n* **防禦重點**：透過白名單與鏈上數據交叉核查，聯手建構去中心化防詐警報網。")

    st.markdown("---")
    st.subheader("🌟 平台四大核心互動模組架構")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("### 🎬 模組一：直立式短影音微學習")
        st.info("參考刑事警察局與網紅合製之《30秒虛擬貨幣詐騙out！》概念，將複雜區塊鏈資安拆解為短影音，搭配防刷分隨堂測驗機制，解決傳統政宣過於枯燥的痛點。")
        st.markdown("### 🔍 模組二：社群防詐網址智慧審核牆")
        st.warning("內建 AI 智慧白名單與知名交易所官方白名單過濾機制，支援使用者提交可疑網址、心得留言及詐騙現場截圖上傳。")
    with col_c2:
        st.markdown("### 🥠 模組三：Web3 幸運餅乾盲盒")
        st.info("結合趣味盲盒機制，每位訪客每日享有 3 次抽獎機會，獲得防禦籤文與積分獎勵，大幅提升平台趣味性與黏著度。")
        st.markdown("### 👥 模組四：動態訪客身分與積分排位")
        st.warning("系統自動隨機生成專屬訪客代號，並根據累積積分動態計算資安防禦素養等級與同儕排位。")

# 2. 短影音學習
elif menu == "🎬 短影音微學習專區":
    st.header("🎬 直立式短影音微學習與隨堂測驗專區")
    st.write("參考國家打詐政策與刑事局《30秒虛擬貨幣詐騙out！》宣導精神，觀看下方防詐短片後，必須完成**隨堂防詐情境測驗**！答對即可獲得積分，每個單元限通關一次，杜絕重複刷分。")
    
    col_v1, col_v2 = st.columns([1.2, 0.8])
    with col_v1:
        st.markdown("### 📱 30秒防詐微影音播放器與測驗")
        
        with st.container():
            unit_choice = st.selectbox("🎯 選擇學習單元：", [
                "單元 1：30秒虛擬貨幣詐騙out！(刑事局聯名宣導)",
                "單元 2：助記詞絕對不上雲端！",
                "單元 3：識別 Discord 假官方空投",
                "單元 4：小心 Permit2 無限授權合約",
                "單元 5：私鑰保管與硬體錢包安全"
            ])
            
            if "單元 1" in unit_choice:
                u_key = "unit_1"
                st.info("▶️ **[官方防詐短片播放中] 30秒虛擬貨幣詐騙out！**\n\n*核心觀念：內政部警政署刑事警察局與專業自媒體合作之 30 秒快節奏識詐短片，教您一眼識破虛擬貨幣假投資陷阱。*")
                st.video("https://www.youtube.com/watch?v=kl5fjC2mrPE")
                q_title = "隨堂考：根據 30 秒防詐短片與宣導，遇到宣稱『保證獲利、穩賺不賠』的虛擬貨幣投資群組，您應該？"
                options = ["立刻投入小額資金試試看", "100% 是詐騙，應立即退出並封鎖檢舉", "把錢轉給群組管理員幫操作"]
                correct_ans = "100% 是詐騙，應立即退出並封鎖檢舉"
            elif "單元 2" in unit_choice:
                u_key = "unit_2"
                st.warning("▶️ **[微影音播放中] 助記詞絕對不上雲端**\n\n*核心觀念：私鑰與助記詞為資產完全控制權，絕對不可截圖存於手機相簿！*")
                q_title = "隨堂考：如果朋友私訊跟你要助記詞幫忙解鎖錢包，你應該怎麼做？"
                options = ["直接把助記詞截圖傳給他", "絕對不交出，助記詞等於資產所有權", "先轉 0.1 ETH 給他驗證"]
                correct_ans = "絕對不交出，助記詞等於資產所有權"
            elif "單元 3" in unit_choice:
                u_key = "unit_3"
                st.success("▶️ **[微影音播放中] 識別 Discord 假官方空投**\n\n*核心觀念：陌生私訊送免費空投 99% 具備釣魚惡意合約！*")
                q_title = "隨堂考：在 Discord 收到陌生管理員私訊說你中了免費 NFT 空投，點擊連結即可領取，你應該？"
                options = ["立刻點擊連結登入錢包領取", "不理會並檢舉，因為極高機率是釣魚合約", "把自己的 Discord 密碼告訴他"]
                correct_ans = "不理會並檢舉，因為極高機率是釣魚合約"
            elif "單元 4" in unit_choice:
                u_key = "unit_4"
                st.info("▶️ **[微影音播放中] 小心 Permit2 無限授權合約**\n\n*核心觀念：互動前使用 Etherscan 檢查授權額度。*")
                q_title = "隨堂考：與不知名去中心化合約互動時，彈出無限授權請求，正確做法是？"
                options = ["直接盲簽確認", "使用工具自訂修改為剛好需要的授權額度或拒絕", "把電腦重開機"]
                correct_ans = "使用工具自訂修改為剛好需要的授權額度或拒絕"
            else:
                u_key = "unit_5"
                st.success("▶️ **[微影音播放中] 私鑰保管與硬體錢包安全**\n\n*核心觀念：大額數位資產應存放於離線冷錢包。*")
                q_title = "隨堂考：以下哪種方式存放私鑰或助記詞最安全？"
                options = ["用筆抄在實體紙張上並妥善鎖在保險箱", "用手機拍照存在雲端相簿", "發到自己的 LINE 記事本"]
                correct_ans = "用筆抄在實體紙張上並妥善鎖在保險箱"

            if u_key in st.session_state.completed_units:
                st.success("✅ **【本單元測驗已通關】** 您已成功掌握此核心資安觀念！")
            else:
                st.markdown(f"**{q_title}**")
                user_choice = st.radio("請選擇您的答案：", options, key=f"radio_{u_key}")
                
                if st.button("🚀 提交答案領取學習積分 (+50 Coins)", key=f"btn_{u_key}"):
                    if user_choice == correct_ans:
                        st.session_state.user_points += 50
                        st.session_state.completed_units.append(u_key)
                        st.balloons()
                        st.success("🎉 **回答正確！** 恭喜獲得 +50 學習積分！")
                        st.rerun()
                    else:
                        st.error("❌ **回答錯誤！** 請重新思考影片中的核心防禦觀念後再次作答。")

    with col_v2:
        st.markdown("### 📊 微學習成效與防刷分儀表板")
        completed_count = len(st.session_state.completed_units)
        st.metric(label="🏆 已解鎖通關單元數", value=f"{completed_count} / 5 單元")
        st.progress(completed_count / 5)
        
        st.info("🧠 **技術認知與防刷分機制說明**：\n"
                "• **微學習精神**：呼應刑事警察局《30秒虛擬貨幣詐騙out！》短片概念，將複雜資安拆解為短平快宣導。\n"
                "• **防刷分機制**：系統自動透過 Session State 記錄各單元通關狀態，已通關單元無法重複獲取積分，確保學習歷程真實有效。")

# 3. 防詐動態牆
elif menu == "🔍 防詐網址審核與留言牆":
    st.header("🔍 社群防詐網址審核與實況截圖留言牆")
    st.write("直接輸入可疑網址進行系統自動審核，並可留下心得留言與上傳詐騙現場截圖佐證！")
    
    with st.form("report_form", clear_on_submit=True):
        st.subheader("🚨 提交新網址審核與留言通報")
        input_url = st.text_input("輸入要審核的網址 (URL)：", placeholder="例如：https://fake-uniswap-airdrop.com")
        input_comment = st.text_area("防詐心得留言 / 現場狀況說明：", placeholder="例如：點進去要求連接 Metamask 錢包，簽署後 USDT 瞬間被轉走！")
        uploaded_file = st.file_uploader("上傳詐騙現場截圖 (選填，支援 PNG/JPG)：", type=["png", "jpg", "jpeg"])
        
        submitted = st.form_submit_button("🤖 執行網址審核並發布貼文 (賺取 +100 積分)")
        
        if submitted:
            clean_url = input_url.strip()
            clean_comment = input_comment.strip()
            
            if len(clean_url) < 4:
                st.error("⚠️ 請輸入有效的完整網址（至少 4 個字元）！")
            else:
                url_lower = clean_url.lower()
                trusted_official_domains = ["lbank.com", "binance.com", "okx.com", "bybit.com", "coinbase.com"]
                is_trusted = any(domain in url_lower for domain in trusted_official_domains)
                
                if is_trusted:
                    auto_risk = "🟢 合法官方活動/推廣網址"
                else:
                    risk_keywords = ["airdrop-claim", "free-crypto", "connect-wallet", "verify-account", "wallet-fix", "reward-bonus"]
                    match_count = sum(1 for kw in risk_keywords if kw in url_lower)
                    if match_count >= 1 or "-" in url_lower and "lbank" not in url_lower:
                        auto_risk = "🔴 高風險釣魚 (AI自動審核)"
                    else:
                        auto_risk = "🟡 中度疑慮 (需注意)"

                st.session_state.wall_posts.insert(0, {
                    "url": clean_url, 
                    "comment": clean_comment if clean_comment else "無額外留言說明。", 
                    "risk": auto_risk,
                    "reporter": st.session_state.user_id,
                    "image": uploaded_file
                })
                st.session_state.user_points += 100
                st.success(f"✅ 審核完成！系統判定：**{auto_risk}**。貼文已成功發布，積分 +100 點已入帳！")
                st.rerun()

    st.markdown("---")
    st.subheader("🔥 全校防詐動態與審核通報牆（完整公開列表）")
    st.write(f"當前共有 **{len(st.session_state.wall_posts)}** 筆通報與審核紀錄：")
    
    for idx, post in enumerate(st.session_state.wall_posts, 1):
        risk_badge = post.get('risk', '⚠️ 需注意')
        reporter_id = post.get('reporter', '匿名學生')
        comment_text = post.get('comment', '')
        img_file = post.get('image', None)
        
        st.markdown(f"### 📌 通報紀錄 #{idx} ({reporter_id})")
        if "高風險" in risk_badge:
            st.error(f"**審核結果狀態：** {risk_badge}\n\n**檢測網址：** `{post['url']}`")
        elif "合法" in risk_badge:
            st.success(f"**審核結果狀態：** {risk_badge}\n\n**檢測網址：** `{post['url']}`")
        else:
            st.warning(f"**審核結果狀態：** {risk_badge}\n\n**檢測網址：** `{post['url']}`")
            
        st.markdown(f"💬 **使用者留言說明**：\n> {comment_text}")
        if img_file is not None:
            st.image(img_file, caption=f"通報人 {reporter_id} 上傳的現場截圖佐證", use_column_width=True)
        st.markdown("---")

# 4. 幸運餅乾
elif menu == "🥠 幸運餅乾盲盒":
    st.header("🥠 Lucky Cookie - 資安幸運餅乾與防禦運勢")
    st.write("結合趣味盲盒機制的互動遊戲！每位訪客**每日享有 3 次**抽取幸運餅乾的機會。")
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown(f"### 🥠 每日防詐盲盒 (剩餘次數: {3 - st.session_state.cookie_count} / 3)")
        
        if st.session_state.cookie_count < 3:
            if st.button("✨ 咬開幸運餅乾 (獲得 +30 積分)"):
                fortunes = [
                    ("🌟【極品大吉】資安防禦值爆表！", "今天沒有收到任何詐騙私訊，您的帳戶安全無虞，防禦力 +100！"),
                    ("🍀【大吉】空投免疫達人！", "面對陌生私訊的免費空投保持高度警覺，成功守住資產不歸零！"),
                    ("🎯【中吉】冷錢包守護神降臨！", "助記詞切記實體抄寫，絕對不要存放在手機相簿或雲端備份中！"),
                    ("💡【小吉】授權檢視專家！", "每次在互動前，記得檢查授權額度與安全性。"),
                    ("⚠️【小凶提醒】當心釣魚網址！", "近期群組常出現偽造授權網站，簽署交易前請務必核對網域正確性！")
                ]
                res_title, res_desc = random.choice(fortunes)
                st.session_state.cookie_count += 1
                st.session_state.user_points += 30
                st.session_state.cookie_history.append((res_title, res_desc))
                st.balloons()
                st.rerun()
        else:
            st.warning("🔒 您今日的 3 次幸運餅乾額度已全部使用完畢！")
            
        if st.session_state.cookie_history:
            st.markdown("### 📜 您今日抽到的防詐籤文紀錄：")
            for i, (t, d) in enumerate(st.session_state.cookie_history, 1):
                st.info(f"**第 {i} 次抽獎**：{t}\n*{d}*")
    
    with col_g2:
        st.markdown("### 🏆 幸運餅乾機制設計說明")
        st.info("• **次數限制**：每位訪客每日限制 **3 次** 抽獎機會。\n• **多元籤文序列**：內含 5 種不同資安防禦等級的盲盒籤文與積分獎勵。")

# 5. 團隊分工
elif menu == "👥 團隊成員與 WBS 分工":
    st.header("👥 專題團隊成員與 WBS 工作分配")
    st.markdown("""
    * **指導老師**：杜建志 老師
    * **執行單位**：元培醫事科技大學 資訊管理系 (115學年度)
    * **團隊成員與職責分工**：
      1. **林俊磊** (學號：1121408006，電話：0908586559) — 專題總籌、需求分析與防詐指標設定
      2. **吳品毅** (學號：1121408004，電話：0905486080) — 系統介面與影音企劃
      3. **林建愷** (學號：1121408005，電話：0976230162) — 社群防詐動態牆與同儕驗證機制設計
      4. **楊杰斯** (學號：1121408026，電話：0975399476) — 官網與互動模擬系統實作
    """)
