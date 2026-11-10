import streamlit as st
import random

# 頁面配置
st.set_page_config(
    page_title="Tasksnap - 數位資產素養與社群防詐平台",
    page_icon="🛡️",
    layout="wide"
)

# 初始化 Session State 儲存積分與動態牆資料
if 'user_points' not in st.session_state:
    st.session_state.user_points = 150
if 'wall_posts' not in st.session_state:
    st.session_state.wall_posts = [
        {"url": "fake-uniswap-rewards.com", "desc": "假冒 Uniswap 官方發放空投獎勵，要求 Permit 授權。", "votes": 42},
        {"url": "Discord 假官方支援小幫手 (Support#8821)", "desc": "私訊聲稱錢包驗證失敗，要求提供助記詞協助解鎖。", "votes": 38}
    ]

# 頂部導覽列與即時積分狀態
st.title("🛡️ Tasksnap 新興數位資產素養與社群防詐平台")
st.markdown("### 結合影音內容與社群媒體之新興數位資產素養推廣平台設計與經營")
st.success("📌 **115學年度元培醫事科技大學資訊管理系畢業專題** | 指導老師：杜建志 老師 | 組員：林俊磊、吳品毅、林建愷、楊杰斯")

# 積分狀態看板（獨立分開，絕對不擠壓）
st.markdown("---")
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.info("👤 **當前身分**\n\n學生 / 訪客 (ID: 1121408...)")
with col_s2:
    st.warning(f"⭐ **學習積分 (Task Coins)**\n\n{st.session_state.user_points} 點")
with col_s3:
    st.success("🛡️ **資安素養等級**\n\nWeb3 資安防護生 (Lv.2)")

st.markdown("---")

# 側邊欄分頁導覽
menu = st.sidebar.selectbox("🧭 系統功能導覽選單", [
    "🏠 專題核心總覽",
    "🎬 沉浸式短影音學習 (賺積分)",
    "🛡️ 防詐動態牆 (即時通報與投票)",
    "🥠 資安幸運餅乾 (抽獎系統)",
    "👥 團隊成員與 WBS 分工"
])

# 1. 核心總覽
if menu == "🏠 專題核心總覽":
    st.header("🏠 專題系統架構與核心價值")
    st.write("本專題針對大專院校學生與青年世代，打造兼具**「短影音微學習」**與**「社群同儕防詐互助」**的數位資產教育平台 (Tasksnap)。")
    st.success("🌐 您的 Streamlit 線上網址已經成功上線並完成串接！隨時可以展示短影音模擬、防詐動態牆與即時積分系統。")

# 2. 短影音學習
elif menu == "🎬 沉浸式短影音學習 (賺積分)":
    st.header("🎬 直立式短影音微學習專區")
    st.write("觀看專題企劃之硬核資安短影音，完成隨堂挑戰即可賺取學習積分！")
    
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown("### 📱 手機模擬播放器")
        video_choice = st.selectbox("選擇學習單元：", [
            "單元 1：助記詞絕對不上雲端！",
            "單元 2：識別 Discord 假官方空投",
            "單元 3：小心 Permit2 無限授權合約"
        ])
        if "單元 1" in video_choice:
            st.info("▶️ **播放中：助記詞絕對不上雲端**\n\n*核心觀念：私鑰與助記詞為資產完全控制權，絕對不可截圖存於手機相簿！*")
        elif "單元 2" in video_choice:
            st.warning("▶️ **播放中：識別 Discord 假官方空投**\n\n*核心觀念：陌生私訊送免費空投 99% 具備釣魚惡意合約！*")
        else:
            st.success("▶️ **播放中：小心 Permit2 無限授權合約**\n\n*核心觀念：互動前使用 Etherscan 檢查授權額度。*")
            
        if st.button("✅ 完成本單元測驗 (領取 +50 積分)"):
            st.session_state.user_points += 50
            st.balloons()
            st.success("🎉 測驗成功！積分 +50 點已入帳！")
            st.rerun()

    with col_v2:
        st.markdown("### 💡 學習成效與積分累積機制")
        st.write("透過 Z 世代習慣的微學習（Micro-learning）模式，將龐大且艱澀的區塊鏈資安法規與風險，拆解為 30-60 秒易讀易懂的短影音內容，提升學生主動防禦意願。")

# 3. 防詐動態牆
elif menu == "🛡️ 防詐動態牆 (即時通報與投票)":
    st.header("🛡️ 社群防詐警報通報與同儕驗證動態牆")
    st.write("集結社群同儕智慧，即時通報疑慮連結與詐騙手法！")
    
    with st.form("report_form"):
        st.subheader("🚨 發起新的社群防詐通報")
        input_url = st.text_input("可疑網址 / 詐騙帳號名稱：", placeholder="例如：fake-opensea-airdrop.io")
        input_desc = st.text_area("詐騙手法描述：", placeholder="例如：聲稱抽中免費 NFT，連接錢包後立刻被轉走...")
        submitted = st.form_submit_button("立即發布通報 (賺取 +100 積分)")
        
        if submitted:
            if input_url:
                st.session_state.wall_posts.insert(0, {"url": input_url, "desc": input_desc, "votes": 1})
                st.session_state.user_points += 100
                st.success(f"✅ 成功發布通報「{input_url}」！社群防詐積分 +100 點已入帳！")
            else:
                st.error("⚠️ 請輸入可疑網址或帳號名稱！")

    st.markdown("---")
    st.subheader("🔥 當前社群熱門防詐通報清單")
    for idx, post in enumerate(st.session_state.wall_posts):
        col_p1, col_p2 = st.columns([3, 1])
        with col_p1:
            st.error(f"🚨 **{post['url']}**\n\n描述：{post['desc']}")
        with col_p2:
            if st.button(f"👍 確實是詐騙 ({post['votes']})", key=f"vote_{idx}"):
                st.session_state.wall_posts[idx]['votes'] += 1
                st.session_state.user_points += 10
                st.success("👍 驗證投票成功！積分 +10 點！")
                st.rerun()

# 4. 幸運餅乾
elif menu == "🥠 資安幸運餅乾 (抽獎系統)":
    st.header("🥠 Lucky Cookie Bite - Web3 資安幸運餅乾")
    st.write("抽取今日專屬的區塊鏈資安籤文，測試防禦運勢並賺取積分！")
    
    fortunes = [
        "【大吉】今天沒有收到任何詐騙 Discord 私訊，資安防禦值爆表！",
        "【中吉】助記詞千萬不要存手機相簿裡，實體抄寫最安全！",
        "【小吉】每次授權合約（Permit）前看清楚權限，資產絕對不歸零。",
        "【吉】冷錢包是資產最後防線，大額資產放冷錢包最安心！"
    ]
    
    if st.button("抽取今日資安籤文 🥠 (賺取 +30 積分)"):
        res = random.choice(fortunes)
        st.session_state.user_points += 30
        st.success(f"🎉 抽獎成功！獲得積分 +30 點！\n\n### {res}")
        st.balloons()
        st.rerun()

# 5. 團隊分工
elif menu == "👥 團隊成員與 WBS 分工":
    st.header("👥 專題團隊成員與 WBS 工作分配")
    st.markdown("""
    * **指導老師**：杜建志 老師
    * **執行單位**：元培醫事科技大學 資訊管理系 (115學年度)
    * **團隊成員與職責分工**：
      1. **林俊磊** (學號：1121408006，電話：0908586559) — 專題總籌, 需求分析與防詐指標設定
      2. **吳品毅** (學號：1121408004，電話：0905486080) — UI/UX 原型設計, 短影音腳本企劃
      3. **林建愷** (學號：1121408005，電話：0976230162) — 社群防詐動態牆與同儕驗證機制設計
      4. **楊杰斯** (學號：1121408026，電話：0975399476) — Python 官網與互動模擬系統實作
    """)
