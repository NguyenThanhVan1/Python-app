"""Phiên bản web Streamlit của món quà 20/10."""

import streamlit as st


DEFAULT_RECIPIENT = "em yêu"
DEFAULT_SENDER = "anh"
DEFAULT_MESSAGE = (
    "Cảm ơn em vì đã đến bên anh. Chỉ cần em luôn vui vẻ, bình an và "
    "mỉm cười, với anh đó đã là một điều thật tuyệt vời."
)


def setup_page() -> None:
    st.set_page_config(
        page_title="Món Quà Nhỏ Dành Cho Em ❤️",
        page_icon="💗",
        layout="centered",
    )
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #fff7f3 0%, #ffe7ef 100%);
        }
        .block-container {
            max-width: 820px;
            padding-top: 2.5rem;
            padding-bottom: 3rem;
        }
        h1, h2, h3 { color: #b83b62; }
        .gift-card {
            background: rgba(255, 255, 255, .82);
            border: 1px solid #f4c5d3;
            border-radius: 20px;
            padding: 1.5rem 1.8rem;
            color: #71354d;
            line-height: 1.8;
            box-shadow: 0 8px 24px rgba(184, 59, 98, .08);
        }
        .subtitle {
            color: #8e5369;
            text-align: center;
            margin-top: -1rem;
            margin-bottom: 2rem;
        }
        </style>
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
        st.header("⚙ Tùy chỉnh món quà")
        with st.form("settings_form"):
            recipient = st.text_input("Tên người nhận", value=st.session_state.recipient)
            sender = st.text_input("Tên người tặng", value=st.session_state.sender)
            message = st.text_area(
                "Lời nhắn riêng",
                value=st.session_state.custom_message,
                height=130,
            )
            saved = st.form_submit_button("Lưu thay đổi", use_container_width=True)
        if saved:
            st.session_state.recipient = recipient.strip() or DEFAULT_RECIPIENT
            st.session_state.sender = sender.strip() or DEFAULT_SENDER
            st.session_state.custom_message = message.strip() or DEFAULT_MESSAGE
            st.success("Đã lưu thay đổi.")


def render_navigation() -> None:
    labels = {
        "welcome": "🏠 Trang đầu",
        "letter": "💌 Bức thư",
        "secret": "✨ Điều muốn nói",
        "album": "📷 Album",
        "ending": "🌷 Lời kết",
    }
    selected = st.radio(
        "Đi đến",
        options=list(labels),
        format_func=labels.get,
        index=list(labels).index(st.session_state.page),
        horizontal=True,
        label_visibility="collapsed",
    )
    if selected != st.session_state.page:
        go_to(selected)
        st.rerun()


def render_welcome() -> None:
    st.title("MÓN QUÀ NHỎ\nDÀNH CHO EM ❤️")
    st.markdown(
        '<p class="subtitle">Anh có một món quà nhỏ dành riêng cho em… 💗</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="gift-card" style="text-align:center">'
        "Một món quà nhỏ, nhưng chứa thật nhiều yêu thương dành cho "
        f"<b>{st.session_state.recipient}</b>."
        "</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("🎁 MỞ QUÀ NGAY", type="primary", use_container_width=True):
        go_to("letter")
        st.rerun()


def render_letter() -> None:
    st.header("Một bức thư nhỏ gửi đến em 💌")
    st.caption(f"Gửi {st.session_state.recipient} — từ {st.session_state.sender}")
    st.markdown(
        f'<div class="gift-card">{letter_text().replace(chr(10), "<br>")}</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    first, second = st.columns(2)
    with first:
        if st.button("Điều anh muốn nói…", use_container_width=True):
            go_to("secret")
            st.rerun()
    with second:
        if st.button("Album 📷", use_container_width=True):
            go_to("album")
            st.rerun()


def render_secret() -> None:
    st.header("Điều anh muốn nói… ✨")
    st.markdown(
        '<div class="gift-card">Nếu có một điều anh muốn em luôn nhớ, thì đó là:<br><br>'
        "Em không cần phải trở thành ai khác để được yêu thương. Em của hiện tại "
        "đã rất đáng quý rồi. Cảm ơn em vì đã là chính em và vì đã cho anh cơ hội "
        "được đồng hành cùng em. 💗</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Mở album kỷ niệm 📷", use_container_width=True):
        go_to("album")
        st.rerun()


def render_album() -> None:
    st.header("Album kỷ niệm của chúng mình 📷")
    st.caption("Thêm những khoảnh khắc khiến em mỉm cười nhé")
    uploaded = st.file_uploader(
        "Thêm ảnh từ thiết bị",
        type=["png", "jpg", "jpeg", "gif", "bmp"],
        accept_multiple_files=True,
    )
    if uploaded:
        st.session_state.photos = uploaded
    if st.session_state.photos:
        st.success(f"Album đã có {len(st.session_state.photos)} ảnh kỷ niệm.")
        columns = st.columns(min(3, len(st.session_state.photos)))
        for index, photo in enumerate(st.session_state.photos):
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
    st.header("Dành riêng cho cô gái anh thương 🌷")
    st.markdown(
        f'<div class="gift-card">{ending_text().replace(chr(10), "<br>")}</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Xem lại từ đầu ↻", use_container_width=True):
        go_to("welcome")
        st.rerun()


def main() -> None:
    setup_page()
    initialize_state()
    render_settings()
    render_navigation()
    {
        "welcome": render_welcome,
        "letter": render_letter,
        "secret": render_secret,
        "album": render_album,
        "ending": render_ending,
    }[st.session_state.page]()


if __name__ == "__main__":
    main()
