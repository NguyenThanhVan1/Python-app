"""Món quà 20/10 - phiên bản web Streamlit."""

import base64
from html import escape
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).parent
FEATURED_IMAGE = APP_DIR / "350a140c-676b-42d8-a6c1-d5bdfe03f5e3.jpg"
DEFAULT_RECIPIENT = "em yêu"
DEFAULT_SENDER = "anh"
DEFAULT_MESSAGE = (
    "Cảm ơn em vì đã đến bên anh. Chỉ cần em luôn vui vẻ, bình an và "
    "mỉm cười, với anh đó đã là một điều thật tuyệt vời."
)


def setup_page() -> None:
    st.set_page_config(
        page_title="Món Quà Nhỏ Dành Cho Em ❤️",
        page_icon="💖",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Pacifico&display=swap');
        :root { --pink: #ff3f78; --deep: #a71455; --ink: #702044; }
        .stApp {
            background:
                radial-gradient(circle at 8% 12%, #fff 0 3%, transparent 20%),
                radial-gradient(circle at 92% 10%, #ffd2e3 0 2%, transparent 22%),
                linear-gradient(135deg, #fff7f9 0%, #ffe0ec 48%, #ffd0e5 100%);
            color: var(--ink);
        }
        .stApp, .stApp button, .stApp input, .stApp textarea {
            font-family: 'Be Vietnam Pro', sans-serif;
        }
        .block-container { max-width: 920px; padding-top: 2rem; padding-bottom: 4rem; }
        h1, h2, h3 { color: var(--deep); font-weight: 800; }
        h1 { text-shadow: 0 4px 22px rgba(255, 63, 120, .25); }
        .hero {
            position: relative; overflow: hidden; text-align: center;
            padding: 2.3rem 1.2rem 2rem; margin-bottom: 1.2rem;
            border: 1px solid rgba(255,255,255,.8); border-radius: 32px;
            background: linear-gradient(135deg, rgba(255,255,255,.8), rgba(255,215,230,.72));
            box-shadow: 0 18px 55px rgba(166, 20, 85, .15);
        }
        .hero h1 { margin: .3rem 0 .4rem; font-family: 'Pacifico', cursive; font-size: clamp(2rem, 7vw, 4rem); color: #c21d60; }
        .hero p { margin: 0; color: #8d4566; font-size: 1.05rem; }
        .hero-image {
            display: block; width: min(100%, 460px); max-height: 330px; object-fit: cover;
            margin: 1.5rem auto .4rem; border: 8px solid white; border-radius: 24px;
            box-shadow: 0 12px 35px rgba(167, 20, 85, .22);
            animation: image-glow 2.2s ease-in-out infinite alternate;
        }
        .gift-card {
            background: rgba(255,255,255,.76); border: 1px solid rgba(255,160,195,.7);
            border-radius: 24px; padding: 1.5rem 1.8rem; color: var(--ink);
            line-height: 1.85; box-shadow: 0 12px 35px rgba(184,59,98,.1);
            backdrop-filter: blur(8px);
        }
        .subtitle { color: #8e5369; text-align: center; margin: -.7rem 0 1.5rem; }
        .heart-field { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
        .heart-field span { position: absolute; bottom: -60px; color: #ff4f86; opacity: 0;
            animation: float-heart 8s linear infinite; filter: drop-shadow(0 0 8px #ff8fb4); }
        .heart-field span:nth-child(1) { left: 7%; animation-delay: .2s; font-size: 24px; }
        .heart-field span:nth-child(2) { left: 18%; animation-delay: 2.4s; font-size: 42px; color: #ff9bc0; }
        .heart-field span:nth-child(3) { left: 33%; animation-delay: 4s; font-size: 20px; }
        .heart-field span:nth-child(4) { left: 52%; animation-delay: 1.2s; font-size: 35px; color: #e9276d; }
        .heart-field span:nth-child(5) { left: 71%; animation-delay: 3.2s; font-size: 28px; }
        .heart-field span:nth-child(6) { left: 88%; animation-delay: 5s; font-size: 46px; color: #ff9bc0; }
        .sparkles { position: fixed; inset: 0; pointer-events: none; z-index: 0; }
        .sparkles::before, .sparkles::after { content: '✦  ✧  ✦  ✧  ✦'; position: absolute;
            color: #ffb0ce; letter-spacing: 2.5rem; animation: sparkle 2s ease-in-out infinite alternate; }
        .sparkles::before { top: 13%; left: 3%; } .sparkles::after { right: 2%; bottom: 16%; animation-delay: 1s; }
        .stApp > header, .block-container { position: relative; z-index: 1; }
        div.stButton > button {
            border: 0; border-radius: 999px; color: white; font-weight: 700;
            background: linear-gradient(135deg, #ff3f78, #c51661);
            box-shadow: 0 7px 18px rgba(197,22,97,.25); transition: transform .2s, box-shadow .2s;
        }
        div.stButton > button:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 11px 25px rgba(197,22,97,.38); color: white; }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, #fff4f8, #ffe4ef); }
        @keyframes float-heart { 0% { transform: translateY(0) rotate(0) scale(.65); opacity: 0; }
            12% { opacity: .9; } 80% { opacity: .75; } 100% { transform: translateY(-115vh) rotate(35deg) scale(1.25); opacity: 0; } }
        @keyframes sparkle { from { opacity: .25; transform: scale(.8) rotate(-8deg); } to { opacity: 1; transform: scale(1.15) rotate(8deg); } }
        @keyframes image-glow { from { box-shadow: 0 12px 35px rgba(167,20,85,.22); } to { box-shadow: 0 12px 45px rgba(255,63,120,.5); } }
        </style>
        <div class="heart-field"><span>♥</span><span>♡</span><span>♥</span><span>❤</span><span>♡</span><span>♥</span></div>
        <div class="sparkles"></div>
        """,
        unsafe_allow_html=True,
    )


def initialize_state() -> None:
    defaults = {
        "page": "welcome",
        "recipient": DEFAULT_RECIPIENT,
        "sender": DEFAULT_SENDER,
        "custom_message": DEFAULT_MESSAGE,
        "photos": [],
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def go_to(page: str) -> None:
    st.session_state.page = page


def letter_text() -> str:
    return (
        f"{st.session_state.recipient} à,\n\n"
        "Chúc em một ngày 20/10 thật vui vẻ, xinh đẹp và hạnh phúc. "
        "Mong em luôn được yêu thương, trân trọng và có thật nhiều nụ cười.\n\n"
        f"{st.session_state.custom_message}\n\n"
        "Anh không phải lúc nào cũng giỏi nói lời ngọt ngào, "
        "nhưng anh luôn trân trọng những khoảnh khắc có em trong cuộc đời mình.\n\n"
        f"Thương em nhiều,\n{st.session_state.sender} ❤️"
    )


def ending_text() -> str:
    return (
        f"Chúc {st.session_state.recipient} yêu của anh một ngày 20/10 thật vui vẻ "
        "và hạnh phúc nhé ❤️🌷\n\n"
        "Anh mong em sẽ luôn xinh đẹp, bình an, luôn mỉm cười và gặp thật nhiều "
        "điều tốt đẹp trong cuộc sống. Anh biết đôi khi anh không phải là người "
        "giỏi nói những lời ngọt ngào, nhưng anh muốn em biết rằng em là một "
        "người rất đặc biệt đối với anh.\n\n"
        "Cảm ơn em vì đã xuất hiện trong cuộc đời anh, vì những niềm vui, những "
        "khoảnh khắc đáng nhớ và cả những điều nhỏ bé mà em mang đến mỗi ngày. "
        "Anh không hứa sẽ khiến mọi ngày của em đều hoàn hảo, nhưng anh sẽ cố "
        "gắng để khi em mệt mỏi, em có một người để sẻ chia; khi em buồn, em "
        "có một người để dựa vào; và khi em hạnh phúc, anh sẽ luôn là người vui cùng em.\n\n"
        "Mong rằng không chỉ riêng ngày 20/10 mà cả những ngày bình thường sau "
        "này, em đều cảm nhận được mình được yêu thương, trân trọng và nâng niu. "
        f"Anh thương em nhiều lắm! ❤️🥰\n\n— {st.session_state.sender}"
    )


def render_settings() -> None:
    with st.sidebar:
        st.header("⚙️ Tùy chỉnh món quà")
        with st.form("settings_form"):
            recipient = st.text_input("Tên người nhận", value=st.session_state.recipient)
            sender = st.text_input("Tên người tặng", value=st.session_state.sender)
            message = st.text_area("Lời nhắn riêng", value=st.session_state.custom_message, height=130)
            saved = st.form_submit_button("💾 Lưu thay đổi", use_container_width=True)
        if saved:
            st.session_state.recipient = recipient.strip() or DEFAULT_RECIPIENT
            st.session_state.sender = sender.strip() or DEFAULT_SENDER
            st.session_state.custom_message = message.strip() or DEFAULT_MESSAGE
            st.success("Đã lưu thay đổi 💗")


def render_navigation() -> None:
    labels = {"welcome": "🏠 Trang đầu", "letter": "💌 Bức thư", "secret": "✨ Điều muốn nói", "album": "📷 Album", "ending": "🌷 Lời kết"}
    selected = st.radio("Đi đến", list(labels), format_func=labels.get, index=list(labels).index(st.session_state.page), horizontal=True, label_visibility="collapsed")
    if selected != st.session_state.page:
        go_to(selected)
        st.rerun()


def render_welcome() -> None:
    image_html = ""
    if FEATURED_IMAGE.exists():
        encoded_image = base64.b64encode(FEATURED_IMAGE.read_bytes()).decode("ascii")
        image_html = f'<img class="hero-image" src="data:image/jpeg;base64,{encoded_image}" />'
    st.markdown(
        f'<section class="hero"><div style="font-size:2.8rem;animation:sparkle 1.4s infinite alternate">💖 ✨ 💖</div>'
        '<h1>Món Quà Nhỏ Dành Cho Em</h1>'
        '<p>🌹 Một bất ngờ rực rỡ, được viết riêng bằng tất cả yêu thương 🌹</p>'
        f"{image_html}</section>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="gift-card" style="text-align:center">Món quà này dành riêng cho '
        f'<b>{escape(st.session_state.recipient)}</b> — người đặc biệt nhất trong tim anh 💞</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("🎁 MỞ QUÀ NGAY ✨", type="primary", use_container_width=True):
        go_to("letter")
        st.rerun()


def render_letter() -> None:
    st.header("💌 Một bức thư nhỏ gửi đến em")
    st.caption(f"Gửi {st.session_state.recipient} — từ {st.session_state.sender}")
    st.markdown(f'<div class="gift-card">{escape(letter_text()).replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
    first, second = st.columns(2)
    with first:
        if st.button("✨ Điều anh muốn nói…", use_container_width=True):
            go_to("secret")
            st.rerun()
    with second:
        if st.button("📷 Album kỷ niệm", use_container_width=True):
            go_to("album")
            st.rerun()


def render_secret() -> None:
    st.header("✨ Điều anh muốn nói…")
    st.markdown(
        '<div class="gift-card">Nếu có một điều anh muốn em luôn nhớ, thì đó là:<br><br>'
        "Em không cần phải trở thành ai khác để được yêu thương. Em của hiện tại "
        "đã rất đáng quý rồi. Cảm ơn em vì đã là chính em và vì đã cho anh cơ hội "
        "được đồng hành cùng em. 💗</div>",
        unsafe_allow_html=True,
    )
    if st.button("Mở album kỷ niệm 📷", use_container_width=True):
        go_to("album")
        st.rerun()


def render_album() -> None:
    st.header("📷 Album kỷ niệm của chúng mình")
    st.caption("Thêm những khoảnh khắc khiến em mỉm cười nhé")
    uploaded = st.file_uploader("Thêm ảnh từ thiết bị", type=["png", "jpg", "jpeg", "gif", "bmp"], accept_multiple_files=True)
    if uploaded:
        st.session_state.photos = uploaded
    photos = st.session_state.photos
    if photos:
        st.success(f"Album đã có {len(photos)} ảnh kỷ niệm 💕")
        columns = st.columns(min(3, len(photos)))
        for index, photo in enumerate(photos):
            with columns[index % len(columns)]:
                st.image(photo, caption=photo.name, use_container_width=True)
    else:
        st.info("Album đang chờ những kỷ niệm của chúng mình 🌷")
    first, second = st.columns(2)
    with first:
        if st.button("Quay lại thư", use_container_width=True):
            go_to("letter")
            st.rerun()
    with second:
        if st.button("Lời kết ❤️", use_container_width=True):
            go_to("ending")
            st.rerun()


def render_ending() -> None:
    st.header("🌷 Dành riêng cho cô gái anh thương")
    st.markdown(f'<div class="gift-card">{escape(ending_text()).replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
    if st.button("Xem lại từ đầu ↻", use_container_width=True):
        go_to("welcome")
        st.rerun()


def main() -> None:
    setup_page()
    initialize_state()
    render_settings()
    render_navigation()
    pages = {"welcome": render_welcome, "letter": render_letter, "secret": render_secret, "album": render_album, "ending": render_ending}
    pages[st.session_state.page]()


if __name__ == "__main__":
    main()
