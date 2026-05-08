import streamlit as st
import pandas as pd
from urllib.parse import quote

st.set_page_config(page_title="Indica Computers & Web Square", page_icon="💻", layout="wide")

SHOP_NAME = "Indica Computers & Web Square"
WHATSAPP_NUMBER = "919486827765"
EMAIL = "info@indicacomputers.com"
CATEGORIES = [
    "All",
    "Laptops",
    "Desktops",
    "All in One PC",
    "Printers",
    "CCTV",
    "Ethernet Cables",
    "Monitors",
    "Mouse",
    "Keyboards",
    "Adapters",
    "SSD",
    "RAM",
    "Routers",
    "Modem",
]

@st.cache_data
def load_products():
    df = pd.read_csv("products.csv")
    for col in ["category", "brand", "model", "title", "description", "specs", "stock_status", "location", "image_url"]:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str)
    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
    return df

def wa_link(product_name):
    text = f"Hello, I am interested in {product_name} from {SHOP_NAME}. Please share price and availability."
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(text)}"

def email_link(product_name):
    subject = quote(f"Enquiry for {product_name}")
    body = quote(f"Hello {SHOP_NAME},\n\nI am interested in {product_name}. Please share price, stock, and details.\n\nRegards,")
    return f"mailto:{EMAIL}?subject={subject}&body={body}"

st.title(f"{SHOP_NAME}")
st.caption("Warehouse product catalog with WhatsApp and email enquiries")

st.info("Browse products now. Online payment can be added later. Use the filters to find items quickly.")

df = load_products()

with st.sidebar:
    st.header("Search & Filter")
    search = st.text_input("Search products", placeholder="Laptop, printer, CCTV, SSD...")
    category = st.selectbox("Category", CATEGORIES)
    stock_only = st.checkbox("In stock only", value=False)

filtered = df.copy()

if category != "All":
    filtered = filtered[filtered["category"].str.lower() == category.lower()]

if search:
    q = search.lower()
    mask = (
        filtered["title"].str.lower().str.contains(q, na=False)
        | filtered["brand"].str.lower().str.contains(q, na=False)
        | filtered["model"].str.lower().str.contains(q, na=False)
        | filtered["description"].str.lower().str.contains(q, na=False)
        | filtered["specs"].str.lower().str.contains(q, na=False)
    )
    filtered = filtered[mask]

if stock_only:
    filtered = filtered[filtered["stock_status"].str.lower().isin(["in stock", "available", "ready"])]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Products", len(df))
c2.metric("Showing", len(filtered))
c3.metric("Categories", df["category"].nunique())
c4.metric("Contact", "WhatsApp")

st.divider()

if filtered.empty:
    st.warning("No products found. Try a different search or category.")
else:
    for _, row in filtered.iterrows():
        with st.container(border=True):
            left, right = st.columns([1, 3])
            with left:
                img = str(row.get("image_url", "")).strip()
                if img:
                    st.image(img, use_container_width=True)
                else:
                    st.markdown("### 📦")
                st.link_button("Inquire on WhatsApp", wa_link(row['title']))
                st.link_button("Email Quote", email_link(row['title']))
            with right:
                title = row.get("title", "")
                st.subheader(title)
                brand = row.get("brand", "")
                model = row.get("model", "")
                cat = row.get("category", "")
                price = row.get("price", "")
                stock_status = row.get("stock_status", "")
                location = row.get("location", "")
                desc = row.get("description", "")
                specs = row.get("specs", "")
                info = []
                if brand: info.append(f"**Brand:** {brand}")
                if model: info.append(f"**Model:** {model}")
                if cat: info.append(f"**Category:** {cat}")
                if not pd.isna(price) and price != "": info.append(f"**Price:** ₹{int(price):,}" if float(price).is_integer() else f"**Price:** ₹{price}")
                if stock_status: info.append(f"**Stock:** {stock_status}")
                if location: info.append(f"**Location:** {location}")
                st.markdown(" | ".join(info))
                if desc:
                    st.write(desc)
                if specs:
                    st.caption(f"Specs: {specs}")

st.divider()
st.subheader("Quick Contact")
col1, col2 = st.columns(2)
with col1:
    st.link_button("Chat on WhatsApp", f"https://wa.me/{WHATSAPP_NUMBER}")
with col2:
    st.link_button("Send Email", f"mailto:{EMAIL}")

st.caption("Built for catalog browsing, enquiries, and future e-commerce expansion.")
