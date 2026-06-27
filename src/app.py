import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="CLV Intelligence", layout="wide", page_icon="◈")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
header[data-testid="stHeader"] { display: none !important; }
div[data-testid="stToolbar"] { display: none !important; }
#MainMenu { display: none !important; }
footer { display: none !important; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #080c18; color: #e2e8f0; }
.stApp { background: linear-gradient(135deg, #080c18 0%, #0d1428 50%, #080c18 100%); }
.stApp > header { display: none; }
div[data-testid="stDecoration"] { display: none; }
.block-container { padding: 0.5rem 2.5rem 1.5rem 2.5rem !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { background: #0a0f1e !important; border-right: 1px solid #1a2440; }
section[data-testid="stSidebar"] .block-container { padding: 1.5rem 1rem !important; }
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] > div { display: flex; flex-direction: column; gap: 4px; }
div[data-testid="stRadio"] > div > label { display: flex !important; align-items: center; padding: 10px 12px !important; border-radius: 10px !important; font-size: 13px !important; color: #4a6080 !important; cursor: pointer !important; transition: all 0.15s !important; border: none !important; background: transparent !important; }
div[data-testid="stRadio"] > div > label:hover { background: rgba(124,140,255,0.08) !important; color: #a0aec0 !important; }
div[data-testid="stRadio"] > div > label[aria-checked="true"] { background: rgba(124,140,255,0.12) !important; color: #7c8cff !important; font-weight: 600 !important; }
div[data-testid="stRadio"] > div > label > div:first-child { display: none !important; }
div[data-testid="stRadio"] > div > label > div:last-child { font-size: 13px !important; padding: 0 !important; }
.metric-card { background: linear-gradient(135deg, #0f1729 0%, #131e35 100%); border: 1px solid #1a2440; border-radius: 16px; padding: 1.2rem 1.4rem; position: relative; overflow: hidden; }
.metric-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, #7c8cff, #a78bfa); border-radius: 16px 16px 0 0; }
.metric-label { font-size: 11px; font-weight: 500; color: #4a6080; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
.metric-value { font-size: 26px; font-weight: 700; color: #ffffff; line-height: 1; margin-bottom: 6px; }
.metric-accent { background: linear-gradient(90deg, #7c8cff, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.metric-change { font-size: 11px; color: #4ecdc4; }
.card { background: linear-gradient(135deg, #0f1729 0%, #131e35 100%); border: 1px solid #1a2440; border-radius: 16px; padding: 1.4rem 1.6rem; margin-bottom: 1rem; }
.card-title { font-size: 13px; font-weight: 600; color: #7c8cff; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: center; }
.card-title span { font-size: 11px; color: #4a6080; text-transform: none; letter-spacing: 0; font-weight: 400; }
.segment-row { display: flex; align-items: center; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #1a2440; }
.segment-row:last-child { border-bottom: none; }
.segment-dot { width: 8px; height: 8px; border-radius: 50%; margin-right: 10px; flex-shrink: 0; }
.segment-name { font-size: 13px; color: #c8d6e8; font-weight: 500; display: flex; align-items: center; }
.segment-bar-wrap { flex: 1; margin: 0 16px; background: #1a2440; border-radius: 4px; height: 4px; }
.segment-bar { height: 4px; border-radius: 4px; }
.result-wrap { background: linear-gradient(135deg, #0f1729 0%, #131e35 100%); border: 1px solid #1a2440; border-radius: 16px; padding: 1.6rem; margin-top: 1rem; }
.cust-avatar { width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 700; flex-shrink: 0; }
.stat-mini-label { font-size: 10px; color: #4a6080; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
.stat-mini-value { font-size: 20px; font-weight: 700; color: #ffffff; }
.rec-box { border-radius: 12px; padding: 12px 16px; margin-top: 1rem; display: flex; align-items: flex-start; gap: 10px; }
.rec-box-label { font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 3px; }
.tech-pill { display: inline-block; background: rgba(124,140,255,0.08); border: 1px solid rgba(124,140,255,0.2); color: #7c8cff; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: 500; margin: 4px; }
.step-num { width: 32px; height: 32px; border-radius: 10px; background: rgba(124,140,255,0.12); color: #7c8cff; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; flex-shrink: 0; }
.step-title { font-size: 14px; font-weight: 600; color: #e2e8f0; margin-bottom: 3px; }
.step-desc { font-size: 12px; color: #4a6080; line-height: 1.5; }
div[data-testid="stNumberInput"] input { background: #0a0f1e !important; border: 1px solid #1a2440 !important; border-radius: 10px !important; color: #e2e8f0 !important; font-family: 'Inter', sans-serif !important; }
.stButton button { background: linear-gradient(135deg, #7c8cff, #5a6fd6) !important; border: none !important; border-radius: 10px !important; color: white !important; font-weight: 600 !important; font-size: 13px !important; height: 42px !important; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    final = pd.read_csv('../data/processed/final_customer_segments.csv')
    transactions = pd.read_csv('../data/processed/clean_transactions.csv', parse_dates=['InvoiceDate'])
    return final, transactions

final, transactions = load_data()

CHART_THEME = dict(
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#4a6080', family='Inter', size=11),
    margin=dict(t=10, b=10, l=0, r=0),
)
SEG_COLORS = {'Champion': '#7c8cff', 'Loyal': '#4ecdc4', 'At Risk': '#f7b731', 'Lost': '#ff6b6b'}
SEG_FILL = {'Champion': 'rgba(124,140,255,0.12)', 'Loyal': 'rgba(78,205,196,0.12)', 'At Risk': 'rgba(247,183,49,0.12)', 'Lost': 'rgba(255,107,107,0.12)'}
SEG_REC = {
    'Champion': ('◆', 'Prioritize retention. Offer exclusive loyalty rewards and early access to new products.'),
    'Loyal': ('●', 'Nurture with personalized offers. Upsell higher-value product lines.'),
    'At Risk': ('▲', 'Re-engagement campaign recommended within 30 days. Offer a time-limited discount.'),
    'Lost': ('○', 'Low ROI to pursue aggressively. Consider a single win-back email with a strong incentive.')
}

with st.sidebar:
    st.markdown("""
    <div style="padding:0.5rem 0 1.5rem 0;">
      <div style="font-size:18px;font-weight:700;color:#7c8cff;letter-spacing:-0.5px;margin-bottom:2px;">◈ CLVIntelligence</div>
      <div style="font-size:11px;color:#2a3a55;">Probabilistic ML Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["▦  Dashboard", "◎  Segments", "◈  Customer Lookup", "△  Model Info", "○  About"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div style="background:rgba(124,140,255,0.08);border:1px solid rgba(124,140,255,0.2);border-radius:12px;padding:1rem;margin-top:1.5rem;">
      <div style="font-size:11px;font-weight:600;color:#7c8cff;margin-bottom:6px;">MODEL INFO</div>
      <div style="font-size:11px;color:#4a6080;line-height:1.6;">BG/NBD + Gamma-Gamma<br>Trained on 2010–2011<br>Horizon: 12 months<br>Customers scored: 2,790</div>
    </div>
    """, unsafe_allow_html=True)

seg_order = ['Champion', 'Loyal', 'At Risk', 'Lost']

if "Dashboard" in page:
    hour = datetime.now().hour
    greeting = "Good morning" if hour < 12 else "Good afternoon" if hour < 17 else "Good evening"
    st.markdown(f"""
    <div style="font-size:28px;font-weight:700;color:#fff;letter-spacing:-0.5px;margin-bottom:4px;padding-top:1rem;">
      {greeting}, <span style="background:linear-gradient(90deg,#7c8cff,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Analyst.</span>
    </div>
    <div style="font-size:14px;color:#4a6080;margin-bottom:1.5rem;">Here's your customer lifetime value intelligence for today.</div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    total = len(final)
    champ_count = (final['Segment'] == 'Champion').sum()
    with c1:
        st.markdown(f"""<div class="metric-card"><div class="metric-label">Total Customers</div><div class="metric-value">{total:,}</div><div class="metric-change">▲ with CLV scores</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="metric-card"><div class="metric-label">Avg CLV · 12 months</div><div class="metric-value metric-accent">£{final['CLV'].mean():,.0f}</div><div class="metric-change">▲ per customer</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="metric-card"><div class="metric-label">Top Customer CLV</div><div class="metric-value">£{final['CLV'].max():,.0f}</div><div class="metric-change">▲ highest predicted</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="metric-card"><div class="metric-label">Champions</div><div class="metric-value">{champ_count:,}</div><div class="metric-change">▲ {champ_count/total*100:.1f}% of base</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1.1, 0.9])

    with col_left:
        st.markdown('<div class="card"><div class="card-title">CLV Overview <span>by segment · avg value</span></div>', unsafe_allow_html=True)
        seg_avgs = [final[final['Segment'] == s]['CLV'].mean() for s in seg_order]
        seg_counts = [final[final['Segment'] == s].shape[0] for s in seg_order]
        max_avg = max(seg_avgs)
        for seg, avg, cnt in zip(seg_order, seg_avgs, seg_counts):
            color = SEG_COLORS[seg]
            pct = avg / max_avg * 100
            st.markdown(f"""
            <div class="segment-row">
              <div class="segment-name"><div class="segment-dot" style="background:{color}"></div>{seg}</div>
              <div class="segment-bar-wrap"><div class="segment-bar" style="width:{pct:.0f}%;background:{color};"></div></div>
              <div style="display:flex;gap:16px;align-items:center;">
                <div style="font-size:11px;color:#4a6080;min-width:40px;text-align:right;">{cnt}</div>
                <div style="font-size:13px;font-weight:600;color:{color};min-width:60px;text-align:right;">£{avg:,.0f}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">CLV Distribution <span>all customers</span></div>', unsafe_allow_html=True)
        fig_hist = go.Figure()
        for seg in seg_order:
            d = final[final['Segment'] == seg]['CLV']
            fig_hist.add_trace(go.Histogram(x=d, name=seg, marker_color=SEG_COLORS[seg], opacity=0.8, nbinsx=30))
        fig_hist.update_layout(**CHART_THEME, height=200, barmode='overlay',
                               legend=dict(orientation='h', y=1.1, x=0, font=dict(size=10, color='#4a6080')),
                               xaxis=dict(gridcolor='#1a2440', linecolor='#1a2440', title='CLV (£)'),
                               yaxis=dict(gridcolor='#1a2440', linecolor='#1a2440', title='Customers'))
        st.plotly_chart(fig_hist, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="card"><div class="card-title">Top Customers <span>by predicted CLV</span></div>', unsafe_allow_html=True)
        top8 = final.nlargest(8, 'CLV')[['Customer ID', 'CLV', 'Segment', 'frequency']].reset_index(drop=True)
        for _, row in top8.iterrows():
            color = SEG_COLORS.get(row['Segment'], '#7c8cff')
            fill = SEG_FILL.get(row['Segment'], 'rgba(124,140,255,0.12)')
            st.markdown(f"""
            <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid #1a2440;">
              <div style="display:flex;align-items:center;gap:10px;">
                <div style="width:34px;height:34px;border-radius:10px;background:{fill};display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:{color};">{str(int(row['Customer ID']))[:3]}</div>
                <div>
                  <div style="font-size:13px;font-weight:500;color:#c8d6e8;">ID {int(row['Customer ID'])}</div>
                  <div style="font-size:10px;color:#4a6080;">{int(row['frequency'])} orders</div>
                </div>
              </div>
              <div style="text-align:right;">
                <div style="font-size:14px;font-weight:700;color:{color};">£{row['CLV']:,.0f}</div>
                <div style="font-size:10px;background:{fill};color:{color};padding:1px 8px;border-radius:10px;display:inline-block;">{row['Segment']}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif "Segments" in page:
    st.markdown("""<div style="font-size:28px;font-weight:700;color:#fff;margin-bottom:4px;padding-top:1rem;">Segment Analysis</div>
    <div style="font-size:14px;color:#4a6080;margin-bottom:1.5rem;">Deep dive into each customer tier.</div>""", unsafe_allow_html=True)

    cols = st.columns(4)
    for i, seg in enumerate(seg_order):
        d = final[final['Segment'] == seg]
        color = SEG_COLORS[seg]
        with cols[i]:
            st.markdown(f"""
            <div class="metric-card" style="border-top:2px solid {color};">
              <div style="font-size:11px;font-weight:600;color:{color};text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">{seg}</div>
              <div style="font-size:24px;font-weight:700;color:#fff;margin-bottom:4px;">{len(d):,}</div>
              <div style="font-size:11px;color:#4a6080;margin-bottom:10px;">{len(d)/len(final)*100:.1f}% of customers</div>
              <div style="border-top:1px solid #1a2440;padding-top:10px;">
                <div style="font-size:10px;color:#4a6080;margin-bottom:2px;">Avg CLV</div>
                <div style="font-size:16px;font-weight:700;color:{color};">£{d['CLV'].mean():,.0f}</div>
              </div>
              <div style="margin-top:8px;">
                <div style="font-size:10px;color:#4a6080;margin-bottom:2px;">Avg Orders</div>
                <div style="font-size:16px;font-weight:700;color:#e2e8f0;">{d['frequency'].mean():.1f}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><div class="card-title">CLV by Segment <span>distribution</span></div>', unsafe_allow_html=True)
        fig_box = go.Figure()
        for seg in seg_order:
            d = final[final['Segment'] == seg]['CLV']
            fig_box.add_trace(go.Box(y=d, name=seg, marker_color=SEG_COLORS[seg],
                                     line_color=SEG_COLORS[seg], fillcolor=SEG_FILL[seg], boxmean=True))
        fig_box.update_layout(**CHART_THEME, height=300,
                              xaxis=dict(gridcolor='#1a2440', linecolor='#1a2440'),
                              yaxis=dict(gridcolor='#1a2440', linecolor='#1a2440', tickprefix='£'),
                              showlegend=False)
        st.plotly_chart(fig_box, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><div class="card-title">Recency vs Frequency <span>by segment</span></div>', unsafe_allow_html=True)
        fig_scatter = go.Figure()
        for seg in seg_order:
            d = final[final['Segment'] == seg]
            fig_scatter.add_trace(go.Scatter(x=d['recency'], y=d['frequency'], mode='markers', name=seg,
                                             marker=dict(color=SEG_COLORS[seg], size=5, opacity=0.6)))
        fig_scatter.update_layout(**CHART_THEME, height=300,
                                  xaxis=dict(gridcolor='#1a2440', linecolor='#1a2440', title='Recency (days)'),
                                  yaxis=dict(gridcolor='#1a2440', linecolor='#1a2440', title='Frequency'),
                                  legend=dict(font=dict(size=10, color='#4a6080')))
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif "Customer Lookup" in page:
    st.markdown("""<div style="font-size:28px;font-weight:700;color:#fff;margin-bottom:4px;padding-top:1rem;">Customer Lookup</div>
    <div style="font-size:14px;color:#4a6080;margin-bottom:1.5rem;">Enter a customer ID to see their CLV, segment, and purchase history.</div>""", unsafe_allow_html=True)

    st.markdown('<div class="card"><div class="card-title">Search <span>by customer ID</span></div>', unsafe_allow_html=True)
    col_in, col_btn = st.columns([5, 1])
    with col_in:
        customer_id = st.number_input("Customer ID", min_value=int(final['Customer ID'].min()),
                                      max_value=int(final['Customer ID'].max()), value=14646, label_visibility="collapsed")
    with col_btn:
        search = st.button("Analyse ↗")
    st.markdown("</div>", unsafe_allow_html=True)

    if search:
        customer = final[final['Customer ID'] == customer_id]
        if len(customer) == 0:
            st.error("Customer not found or was a one-time buyer.")
        else:
            c = customer.iloc[0]
            seg = c['Segment']
            color = SEG_COLORS.get(seg, '#7c8cff')
            fill = SEG_FILL.get(seg, 'rgba(124,140,255,0.12)')
            icon, rec_text = SEG_REC.get(seg, ('●', ''))
            st.markdown(f"""
            <div class="result-wrap">
              <div style="display:flex;align-items:center;gap:14px;margin-bottom:1.4rem;padding-bottom:1.2rem;border-bottom:1px solid #1a2440;">
                <div class="cust-avatar" style="background:{fill};color:{color};">{str(int(customer_id))[:2]}</div>
                <div>
                  <div style="font-size:16px;font-weight:600;color:#fff;margin-bottom:4px;">Customer {int(customer_id)}</div>
                  <span style="background:{fill};color:{color};padding:3px 12px;border-radius:20px;font-size:10px;font-weight:600;letter-spacing:0.5px;">{seg}</span>
                </div>
              </div>
              <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem;margin-bottom:1rem;">
                <div><div class="stat-mini-label">Predicted CLV</div><div class="stat-mini-value" style="color:{color};">£{c['CLV']:,.0f}</div></div>
                <div><div class="stat-mini-label">Total Orders</div><div class="stat-mini-value">{int(c['frequency'])}</div></div>
                <div><div class="stat-mini-label">Avg Order Value</div><div class="stat-mini-value">£{c['monetary']:.2f}</div></div>
                <div><div class="stat-mini-label">Days Since Purchase</div><div class="stat-mini-value">{int(c['recency'])}</div></div>
              </div>
              <div class="rec-box" style="background:{fill};border:1px solid {color}33;">
                <div style="font-size:16px;color:{color};">{icon}</div>
                <div>
                  <div class="rec-box-label" style="color:{color};">Business Recommendation</div>
                  <div style="font-size:13px;color:#c8d6e8;line-height:1.5;">{rec_text}</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="card"><div class="card-title">Purchase History <span>daily revenue over time</span></div>', unsafe_allow_html=True)
            history = transactions[transactions['Customer ID'] == customer_id].copy().sort_values('InvoiceDate')
            daily = history.groupby(history['InvoiceDate'].dt.date)['Revenue'].sum().reset_index()
            daily.columns = ['Date', 'Revenue']
            fig3 = go.Figure()
            fig3.add_trace(go.Scatter(x=daily['Date'], y=daily['Revenue'], mode='lines+markers',
                                      line=dict(color=color, width=2), marker=dict(color=color, size=5),
                                      fill='tozeroy', fillcolor=fill))
            fig3.update_layout(**CHART_THEME, height=220,
                               xaxis=dict(gridcolor='#1a2440', linecolor='#1a2440'),
                               yaxis=dict(gridcolor='#1a2440', linecolor='#1a2440', tickprefix='£'))
            st.plotly_chart(fig3, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

elif "Model Info" in page:
    st.markdown("""<div style="font-size:28px;font-weight:700;color:#fff;margin-bottom:4px;padding-top:1rem;">Model Info</div>
    <div style="font-size:14px;color:#4a6080;margin-bottom:1.5rem;">How the CLV predictions are generated.</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="card">
          <div class="card-title">BG/NBD Model <span>purchase frequency</span></div>
          <div style="font-size:13px;color:#c8d6e8;line-height:1.7;margin-bottom:1rem;">The Beta-Geometric / Negative Binomial Distribution model predicts how many future purchases a customer will make. It models two processes simultaneously — how often a customer buys while active, and when they churn.</div>
          <div style="border-top:1px solid #1a2440;padding-top:1rem;">
            <div style="font-size:11px;color:#4a6080;margin-bottom:8px;text-transform:uppercase;letter-spacing:1px;">Inputs</div>
            <div style="font-size:12px;color:#7c8cff;">Recency · Frequency · Customer Age (T)</div>
          </div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="card">
          <div class="card-title">Gamma-Gamma Model <span>monetary value</span></div>
          <div style="font-size:13px;color:#c8d6e8;line-height:1.7;margin-bottom:1rem;">The Gamma-Gamma model predicts the average transaction value of future purchases. It assumes monetary value is independent of purchase frequency — a key statistical assumption verified on this dataset.</div>
          <div style="border-top:1px solid #1a2440;padding-top:1rem;">
            <div style="font-size:11px;color:#4a6080;margin-bottom:8px;text-transform:uppercase;letter-spacing:1px;">Inputs</div>
            <div style="font-size:12px;color:#4ecdc4;">Frequency · Average Monetary Value</div>
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
      <div class="card-title">CLV Formula <span>how the final score is computed</span></div>
      <div style="background:#0a0f1e;border:1px solid #1a2440;border-radius:12px;padding:1.2rem;font-family:monospace;font-size:14px;color:#7c8cff;text-align:center;margin-bottom:1rem;">
        CLV = BG/NBD(predicted purchases) × Gamma-Gamma(avg order value) × 12 months
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;">
        <div style="text-align:center;padding:1rem;background:#0a0f1e;border-radius:12px;border:1px solid #1a2440;">
          <div style="font-size:11px;color:#4a6080;margin-bottom:4px;">Raw Dataset</div>
          <div style="font-size:15px;font-weight:600;color:#fff;">541,910 rows</div>
        </div>
        <div style="text-align:center;padding:1rem;background:#0a0f1e;border-radius:12px;border:1px solid #1a2440;">
          <div style="font-size:11px;color:#4a6080;margin-bottom:4px;">After Cleaning</div>
          <div style="font-size:15px;font-weight:600;color:#fff;">397,885 rows</div>
        </div>
        <div style="text-align:center;padding:1rem;background:#0a0f1e;border-radius:12px;border:1px solid #1a2440;">
          <div style="font-size:11px;color:#4a6080;margin-bottom:4px;">Customers Scored</div>
          <div style="font-size:15px;font-weight:600;color:#7c8cff;">2,790</div>
        </div>
      </div>
    </div>""", unsafe_allow_html=True)

elif "About" in page:
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0f1729 0%,#131e35 100%);border:1px solid #1a2440;border-radius:20px;padding:2.5rem;margin-bottom:1.5rem;text-align:center;margin-top:1rem;">
      <div style="display:inline-block;background:rgba(124,140,255,0.12);color:#7c8cff;padding:4px 14px;border-radius:20px;font-size:11px;font-weight:600;letter-spacing:1px;margin-bottom:1rem;">◈ Portfolio Project</div>
      <div style="font-size:28px;font-weight:700;color:#ffffff;margin-bottom:0.75rem;">Customer Lifetime Value Intelligence</div>
      <div style="font-size:14px;color:#4a6080;line-height:1.7;max-width:600px;margin:0 auto;">
        A production-grade probabilistic ML system that predicts how much revenue each customer will generate over the next 12 months —
        built on real e-commerce transaction data using statistical models trusted by companies like Spotify, Amazon, and Shopify.
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="card">
          <div class="card-title">What is CLV?</div>
          <div style="font-size:13px;color:#c8d6e8;line-height:1.7;">Customer Lifetime Value predicts the total revenue a business can expect from a single customer. Instead of treating all customers equally, CLV lets businesses invest marketing budgets where they'll generate the highest return — retaining Champions, re-engaging At Risk customers, and avoiding spend on Lost ones.</div>
        </div>""", unsafe_allow_html=True)

        st.markdown("""<div class="card">
          <div class="card-title">Tech Stack</div>
          <div style="margin-top:0.5rem;">
            <span class="tech-pill">Python</span><span class="tech-pill">Pandas</span>
            <span class="tech-pill">Lifetimes</span><span class="tech-pill">BG/NBD</span>
            <span class="tech-pill">Gamma-Gamma</span><span class="tech-pill">Plotly</span>
            <span class="tech-pill">Streamlit</span><span class="tech-pill">Scikit-learn</span>
            <span class="tech-pill">NumPy</span><span class="tech-pill">Git</span>
          </div>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="card">
          <div class="card-title">How It Was Built</div>
          <div style="display:flex;flex-direction:column;gap:14px;margin-top:0.5rem;">
            <div style="display:flex;gap:12px;align-items:flex-start;">
              <div class="step-num">1</div>
              <div><div class="step-title">Data Cleaning</div><div class="step-desc">541k raw transactions cleaned — nulls, cancellations, and bad values removed to produce 397k valid rows.</div></div>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start;">
              <div class="step-num">2</div>
              <div><div class="step-title">RFM Feature Engineering</div><div class="step-desc">Recency, Frequency, and Monetary value computed per customer as model inputs.</div></div>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start;">
              <div class="step-num">3</div>
              <div><div class="step-title">Probabilistic Modelling</div><div class="step-desc">BG/NBD fitted for purchase prediction. Gamma-Gamma fitted for spend estimation.</div></div>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start;">
              <div class="step-num">4</div>
              <div><div class="step-title">Segmentation</div><div class="step-desc">2,790 customers segmented into Champion, Loyal, At Risk, and Lost tiers using CLV quartiles.</div></div>
            </div>
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="text-align:center;padding:2rem;">
      <div style="font-size:13px;color:#4a6080;margin-bottom:0.5rem;">Built by</div>
      <div style="font-size:20px;font-weight:700;color:#fff;">Gayathri Menon</div>
    </div>
    """, unsafe_allow_html=True)
