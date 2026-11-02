import base64


def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def load_css():

    bg = get_base64("assets/inventory_bg.jpg")

    css = f"""
    <style>

    /* Main App Background */

    .stApp {{
        background-image: linear-gradient(
            rgba(10,15,30,0.85),
            rgba(10,15,30,0.85)
        ),
        url("data:image/jpg;base64,{bg}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Sidebar */

    section[data-testid="stSidebar"] {{
        background: rgba(12,25,45,0.92);
        border-right:1px solid #355c7d;
    }}

    /* Headers */

    h1,h2,h3 {{
        color:#5EC8FF;
    }}

    /* Paragraph */

    p,label {{
        color:white;
    }}

    /* Metric Cards */

    div[data-testid="metric-container"] {{

        background:#16263e;
        border-radius:15px;
        padding:15px;
        border:1px solid #2d8cff;

    }}

    /* Buttons */

    .stButton>button {{

        width:100%;
        background:#0E76FD;
        color:white;
        border-radius:10px;
        height:50px;
        font-size:18px;
        font-weight:bold;
        border:none;

    }}

    .stButton>button:hover {{
        background:#0059d6;
    }}

    /* Inputs */

    .stNumberInput,
    .stSelectbox{{
        border-radius:10px;
    }}

    </style>
    """

    return css