import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="centered"
)

load_dotenv()

# ===== CSS =====
st.markdown(
    """
    <style>
    .main > div {
        padding-top: 2rem;
    }

    .main-title {
        font-size: 2.3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 0.95rem;
        color: #6c757d;
        margin-bottom: 1.8rem;
    }

    /* STYLING FORM LANGSUNG */
    div[data-testid="stForm"] {
        background: linear-gradient(135deg, #111827 0%, #020617 100%);
        padding: 1.75rem 1.75rem 1.25rem 1.75rem;
        border-radius: 18px;
        border: 1px solid #1f2937;
        box-shadow: 0 16px 35px rgba(0,0,0,0.65);
    }

    .hint-text {
        font-size: 0.80rem;
        color: #9ca3af;
        margin-top: 0.25rem;
        margin-bottom: 0.3rem;
    }

    .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.15rem 0.65rem;
        border-radius: 999px;
        background: #022c22;
        color: #a7f3d0;
        font-size: 0.75rem;
        margin-bottom: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ===== HEADER =====
st.markdown(
    """
    <div class="main-title">🧳 AI Travel Itinerary Planner</div>
    <div class="subtitle">
        Plan a personalized day trip by simply telling me your destination and what you like.
    </div>
    """,
    unsafe_allow_html=True,
)

# ===== CONTENT =====
col1, col2 = st.columns([1.2, 1])

with col1:
    with st.form("planner_form"):
        city = st.text_input(
            "📍 Destination city",
            placeholder="e.g. Tokyo, Bandung, Paris"
        )
        st.markdown(
            '<div class="hint-text">Use a city name that actually exists for better results.</div>',
            unsafe_allow_html=True,
        )

        interests = st.text_input(
            "🎯 Your interests (comma-separated)",
            placeholder="e.g. coffee shops, art museum, street food, night market"
        )
        st.markdown(
            '<div class="hint-text">Separate with commas so the AI can understand each interest clearly.</div>',
            unsafe_allow_html=True,
        )

        submitted = st.form_submit_button("🚀 Generate itinerary")

        if submitted:
            if city and interests:
                planner = TravelPlanner()
                planner.set_city(city)
                planner.set_interests(interests)

                with st.spinner("Building your personalized itinerary... ⏳"):
                    itinerary = planner.create_itineary()

                st.success("Itinerary generated successfully!")

                st.markdown(
                    f"""
                    <div class="badge">
                        <span>📄</span>
                        <span>Your AI-generated travel plan</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(f"### Here’s your day in **{city}**:")
                st.markdown(itinerary)
            else:
                st.warning("Please fill in both **city** and **interests** to continue 🙂")

with col2:
    st.markdown("#### Quick tips")
    st.markdown(
        """
        - Try something like:  
          `Rome` + `history, coffee, hidden gems`  
        - Or:  
          `Seoul` + `K-Pop, skincare, street food, night view`  
        - The more specific your interests, the smarter the itinerary.
        """
    )
