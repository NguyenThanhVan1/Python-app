"""Món quà 20/10 - phiên bản web Streamlit."""

import base64
from html import escape
import math
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).parent
FEATURED_IMAGE = APP_DIR / "350a140c-676b-42d8-a6c1-d5bdfe03f5e3.jpg"
DEFAULT_RECIPIENT = "em bé yêu"
DEFAULT_SENDER = "anh"
DEFAULT_MESSAGE = (
    "Cảm ơn em vì đã bước vào cuộc đời anh và làm cho những ngày bình thường "
    "trở nên ấm áp, ý nghĩa hơn. Anh chúc em luôn giữ được sự dịu dàng, bản lĩnh "
    "và niềm tin vào những điều tốt đẹp; mong mọi ước mơ của em đều từng bước "
    "trở thành hiện thực."
)


def build_flower_heart() -> str:
    flowers = []
    flower_count = 138
    for index in range(flower_count):
        angle = (index / flower_count) * math.tau
        layer = 0.82 + (index % 4) * 0.06
        x = 50 + 47 * layer * math.sin(angle) ** 3
        y = 47 - 41 * layer * (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) / 17
        size = 13 + (index % 6) * 2
        delay = (index % 24) * -0.11
        drift = 5 + (index % 7)
        rotation = (index * 29) % 360
        flowers.append(
            f'<i class="flower" style="--x:{x:.2f}%;--y:{y:.2f}%;--size:{size}px;'
            f'--delay:{delay:.2f}s;--drift:{drift}px;--rotation:{rotation}deg"></i>'
        )
    return "".join(flowers)


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
        .flower-heart {
            position: relative; width: min(98vw, 700px); height: 480px; margin: -.2rem auto .8rem;
            filter: drop-shadow(0 0 22px rgba(255, 64, 131, .82)) drop-shadow(0 0 48px rgba(255, 152, 195, .65));
        }
        .flower-heart .flower {
            position: absolute; left: var(--x); top: var(--y); width: var(--size); height: var(--size);
            border-radius: 50%; transform: rotate(var(--rotation));
            background:
                radial-gradient(ellipse at 50% 17%, #fff 0 23%, transparent 25%),
                radial-gradient(ellipse at 83% 42%, #ffb1cb 0 25%, transparent 27%),
                radial-gradient(ellipse at 67% 82%, #ff5c91 0 25%, transparent 27%),
                radial-gradient(ellipse at 33% 82%, #ff7eaa 0 25%, transparent 27%),
                radial-gradient(ellipse at 17% 42%, #ffb1cb 0 25%, transparent 27%),
                radial-gradient(circle, #ffd86e 0 14%, transparent 16%);
            filter: drop-shadow(0 0 3px #fff) drop-shadow(0 0 9px #ff4e89);
            animation: flower-dance 2.1s ease-in-out var(--delay) infinite alternate,
                flower-twinkle 1.35s ease-in-out var(--delay) infinite;
        }
        .flower-heart::after {
            content: '✨'; position: absolute; left: 50%; top: 51%; transform: translate(-50%, -50%);
            font-size: 3.6rem; opacity: .98; text-shadow: 0 0 14px #fff, 0 0 32px #ff3f89, 0 0 55px #ffb0ce;
            animation: sparkle .7s ease-in-out infinite alternate;
        }
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
        @keyframes flower-dance {
            0% { transform: translate(calc(var(--drift) * -1), 10px) rotate(var(--rotation)) scale(.55); opacity: .3; }
            35% { transform: translate(var(--drift), -15px) rotate(calc(var(--rotation) + 18deg)) scale(1.3); opacity: 1; }
            70% { transform: translate(calc(var(--drift) * -1), 5px) rotate(calc(var(--rotation) - 14deg)) scale(.82); opacity: .68; }
            100% { transform: translate(var(--drift), -9px) rotate(calc(var(--rotation) + 28deg)) scale(1.12); opacity: .96; }
        }
        @keyframes flower-twinkle {
            0%, 100% { filter: brightness(1) drop-shadow(0 0 3px #fff) drop-shadow(0 0 8px #ff4e89); }
            50% { filter: brightness(1.9) drop-shadow(0 0 7px #fff) drop-shadow(0 0 18px #ff4e89); }
        }
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
        "Nhân ngày Phụ nữ Việt Nam 20/10, anh trân trọng gửi đến em những lời "
        "chúc tốt đẹp và chân thành nhất. Chúc em luôn mạnh khỏe, bình an, tự tin "
        "và hạnh phúc trên mọi chặng đường của cuộc sống. Mong rằng mỗi ngày mới "
        "đều mang đến cho em một niềm vui, một cơ hội đẹp và thêm nhiều lý do để "
        "mỉm cười.\n\n"
        f"{st.session_state.custom_message}\n\n"
        "Anh không phải lúc nào cũng giỏi nói những lời hoa mỹ, nhưng anh luôn "
        "trân trọng sự hiện diện của em và biết ơn từng khoảnh khắc được đồng hành "
        "cùng em. Chúc cho những dự định, ước mơ và nỗ lực của em luôn được đền "
        "đáp xứng đáng; và dù cuộc sống có đôi lúc thử thách, em vẫn luôn giữ "
        "được trái tim ấm áp cùng ánh sáng riêng của mình.\n\n"
        f"Thương em nhiều,\n{st.session_state.sender} ❤️"
    )


def ending_text() -> str:
    return (
        f"Nhân ngày Phụ nữ Việt Nam 20/10, anh kính chúc {st.session_state.recipient} "
        "luôn dồi dào sức khỏe, giữ trong tim thật nhiều bình an và đón nhận mọi "
        "điều tốt đẹp bằng nụ cười rạng rỡ nhất. Chúc em luôn tự tin theo đuổi "
        "những điều mình yêu thích, đủ nghị lực trước mọi thử thách và đủ dịu dàng "
        "để tận hưởng những niềm vui giản dị trong cuộc sống. ❤️🌷\n\n"
        "Anh cảm ơn em vì đã xuất hiện, vì những khoảnh khắc đáng nhớ, vì sự ấm áp "
        "và những điều nhỏ bé nhưng quý giá mà em đã mang đến mỗi ngày. Sự hiện "
        "diện của em khiến cuộc sống trở nên nhiều màu sắc hơn, và với anh, em "
        "luôn là một người đặc biệt, xứng đáng được yêu thương, tôn trọng và nâng niu.\n\n"
        "Anh không dám hứa rằng mọi ngày phía trước sẽ luôn hoàn hảo, nhưng anh "
        "mong mình có thể luôn chân thành, kiên nhẫn và đủ vững vàng để đồng hành "
        "cùng em. Khi em mệt mỏi, mong em biết rằng em luôn có một người sẵn sàng "
        "lắng nghe; khi em buồn, em có một bờ vai để sẻ chia; và khi em hạnh phúc, "
        "anh sẽ luôn vui cùng em bằng tất cả sự tự hào và yêu thương.\n\n"
        "Mong rằng không chỉ riêng ngày 20/10, mà trong tất cả những ngày bình "
        "thường sau này, em đều cảm nhận được giá trị của bản thân và biết rằng "
        "em xứng đáng với những điều tử tế nhất. Chúc em có một hành trình thật "
        "đẹp, nhiều thành công, nhiều yêu thương và luôn giữ được ánh sáng rực "
        f"rỡ trong tâm hồn. Anh thương em thật nhiều! ❤️🥰\n\n— {st.session_state.sender}"
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
        '<p>🌹 Một lời chúc trang trọng, được viết riêng bằng tất cả yêu thương 🌹</p>'
        f'<div class="flower-heart" aria-label="Trái tim tạo từ những cánh hoa">{build_flower_heart()}</div>'
        '<p style="font-size:.9rem;color:#c21d60;font-weight:600">Trái tim anh được kết thành từ những cánh hoa rực rỡ dành cho em 🌸✨</p>'
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
