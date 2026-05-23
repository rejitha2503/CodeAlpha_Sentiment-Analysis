import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import re
import warnings
warnings.filterwarnings("ignore")
from textblob import TextBlob

# ── Load & Process ────────────────────────────────
print("Loading data...")
df = pd.read_csv("amazon.csv")

def split_reviews(text):
    if pd.isna(text): return []
    text = re.sub(r'https?://\S+', '', str(text))
    return [p.strip() for p in text.split(',') if len(p.strip()) > 8]

rows = []
for _, row in df.iterrows():
    cat = str(row['category']).split('|')[0].strip()
    for rev in list(set(
        split_reviews(row['review_title']) +
        split_reviews(row['review_content']))):
        score = TextBlob(rev).sentiment.polarity
        sent  = ('Positive' if score > 0.05
                 else 'Negative' if score < -0.05
                 else 'Neutral')
        rows.append({'category':cat, 'review':rev,
                     'sentiment':sent, 'score':round(score,3),
                     'product':str(row['product_name'])})

rdf = pd.DataFrame(rows)
total = len(rdf)
pos   = (rdf['sentiment']=='Positive').sum()
neu   = (rdf['sentiment']=='Neutral').sum()
neg   = (rdf['sentiment']=='Negative').sum()
avg   = rdf['score'].mean()

print(f"Total: {total:,} | Pos: {pos:,} | Neu: {neu:,} | Neg: {neg:,}")

# ── Colors ────────────────────────────────────────
BG     = '#060606'
CARD   = '#111111'
CARD2  = '#1A1A1A'
RED    = '#FF2020'
RED2   = '#BB0000'
RED4   = '#660000'
GREEN  = '#00E676'
GREEN2 = '#00A152'
YELLOW = '#FFD600'
WHITE  = '#FFFFFF'
GRAY   = '#888888'
LGRAY  = '#BBBBBB'
DGRAY  = '#1E1E1E'

# ════════════════════════════════════════════════════
# FIGURE  26×17
# ════════════════════════════════════════════════════
fig = plt.figure(figsize=(26, 17), facecolor=BG)

# ── Top red bar ───────────────────────────────────
fig.add_axes([0,0.974,1,0.026]).set_facecolor(RED2)
plt.gca().axis('off')

# ── TITLE ─────────────────────────────────────────
fig.text(0.5, 0.947,
    'AMAZON REVIEWS  —  SENTIMENT ANALYSIS',
    ha='center', fontsize=33, fontweight='bold',
    color=WHITE, zorder=5,
    path_effects=[pe.withStroke(linewidth=12, foreground=RED2)])

fig.text(0.5, 0.918,
    f'TextBlob NLP  ●  {total:,} Reviews Analyzed  ●  9 Categories  ●  Positive  /  Neutral  /  Negative  Classification',
    ha='center', fontsize=11.5, color=GRAY)

# Gradient divider
for i,a in enumerate(np.linspace(0,1,60)):
    fig.add_artist(mpatches.Rectangle(
        (i/60,0.909),1/60,0.004,
        facecolor=RED,alpha=a*0.9,
        transform=fig.transFigure,clip_on=False,zorder=4))
for i,a in enumerate(np.linspace(1,0,60)):
    fig.add_artist(mpatches.Rectangle(
        (0.5+i/60,0.909),1/60,0.004,
        facecolor=RED,alpha=a*0.9,
        transform=fig.transFigure,clip_on=False,zorder=4))

# ── KPI CARDS ─────────────────────────────────────
kpis = [
    (f"{total:,}", "TOTAL REVIEWS",  "Analyzed",              '#FFFFFF'),
    (f"{pos:,}",   "POSITIVE",       f"{pos/total*100:.1f}%", GREEN),
    (f"{neu:,}",   "NEUTRAL",        f"{neu/total*100:.1f}%", YELLOW),
    (f"{neg:,}",   "NEGATIVE",       f"{neg/total*100:.1f}%", RED),
    (f"{avg:.2f}", "AVG SCORE",      "Polarity Index",        LGRAY),
]
cw,ch = 0.162,0.078
cy    = 0.820
xs    = [0.030,0.205,0.380,0.555,0.730]

for i,(val,lbl,sub,accent) in enumerate(kpis):
    cx = xs[i]
    # Glow
    fig.add_artist(mpatches.FancyBboxPatch(
        (cx+0.003,cy-0.004),cw,ch,
        boxstyle="round,pad=0.01",
        facecolor=accent if accent!=WHITE else RED2,
        alpha=0.15,linewidth=0,
        transform=fig.transFigure,clip_on=False,zorder=2))
    # Card
    fig.add_artist(mpatches.FancyBboxPatch(
        (cx,cy),cw,ch,
        boxstyle="round,pad=0.01",
        facecolor=CARD2,
        edgecolor=accent,linewidth=2.2,
        transform=fig.transFigure,clip_on=False,zorder=3))
    # Top strip
    fig.add_artist(mpatches.Rectangle(
        (cx+0.004,cy+ch-0.010),cw-0.008,0.010,
        facecolor=accent,
        transform=fig.transFigure,clip_on=False,zorder=4))
    # Value
    fig.text(cx+cw/2,cy+ch*0.62,val,
        ha='center',va='center',
        fontsize=22,fontweight='bold',color=accent,
        transform=fig.transFigure,zorder=5)
    # Label
    fig.text(cx+cw/2,cy+ch*0.32,lbl,
        ha='center',va='center',
        fontsize=9,fontweight='bold',color=WHITE,
        transform=fig.transFigure,zorder=5)
    # Sub
    fig.text(cx+cw/2,cy+ch*0.10,sub,
        ha='center',va='center',
        fontsize=8,color=GRAY,
        transform=fig.transFigure,zorder=5)

# ── GRID  3×4 ─────────────────────────────────────
gs = gridspec.GridSpec(3,4,figure=fig,
    hspace=0.60,wspace=0.38,
    top=0.795,bottom=0.065,
    left=0.048,right=0.978)

def style(ax,title,color=RED2):
    ax.set_facecolor(CARD)
    for sp in ax.spines.values():
        sp.set_edgecolor('#2A0000')
        sp.set_linewidth(1.3)
    ax.tick_params(colors=LGRAY,labelsize=9)
    ax.set_axisbelow(True)
    ax.grid(color='#1C1C1C',linewidth=0.9,
            linestyle='-',alpha=1)
    ax.set_title('  '+title,color=WHITE,
        fontsize=11,fontweight='bold',
        pad=2,loc='left',
        backgroundcolor=color)
    ax.xaxis.label.set_color(GRAY)
    ax.yaxis.label.set_color(GRAY)

# ════════════════════════════════════════════════════
# ROW 1  — Story: Overview
# ════════════════════════════════════════════════════

# C1 — Donut
ax1 = fig.add_subplot(gs[0,0])
style(ax1,'Overall Sentiment')
ax1.pie([pos,neu,neg],
    labels=['Positive','Neutral','Negative'],
    autopct='%1.1f%%',
    colors=[GREEN,YELLOW,RED],
    startangle=90,
    wedgeprops={'edgecolor':BG,'linewidth':3.5,'width':0.60},
    textprops={'color':WHITE,'fontsize':10.5,'fontweight':'bold'},
    pctdistance=0.75,labeldistance=1.18)
ax1.text(0,0.08,f'{total:,}',ha='center',va='center',
         fontsize=13,fontweight='bold',color=WHITE)
ax1.text(0,-0.12,'Reviews',ha='center',va='center',
         fontsize=9,color=GRAY)

# C2 — Sentiment by Category grouped bar
ax2 = fig.add_subplot(gs[0,1:3])
style(ax2,'Sentiment by Product Category','#1A0000')
cs = rdf.groupby(['category','sentiment'])\
        .size().unstack(fill_value=0)
for c in ['Positive','Neutral','Negative']:
    if c not in cs.columns: cs[c]=0
cs = cs[['Positive','Neutral','Negative']]\
       .sort_values('Positive',ascending=False)
x2 = np.arange(len(cs))
w  = 0.26
for i,(col,clr) in enumerate(zip(
        ['Positive','Neutral','Negative'],
        [GREEN,YELLOW,RED])):
    b = ax2.bar(x2+i*w-w,cs[col],
                width=w,color=clr,
                edgecolor='none',alpha=0.9,label=col)
    for bar in b:
        if bar.get_height() > 100:
            ax2.text(bar.get_x()+bar.get_width()/2,
                     bar.get_height()+30,
                     str(int(bar.get_height())),
                     ha='center',color=WHITE,
                     fontsize=7.5,fontweight='bold')
ax2.set_xticks(x2)
ax2.set_xticklabels(cs.index,rotation=15,
    ha='right',color=WHITE,fontsize=9.5)
ax2.set_ylabel('Number of Reviews',fontsize=9)
ax2.legend(fontsize=9,facecolor=CARD2,
           labelcolor=WHITE,edgecolor='#330000',
           loc='upper right')

# C3 — Score Distribution
ax3 = fig.add_subplot(gs[0,3])
style(ax3,'Score Distribution')
for sent,clr,al in zip(
        ['Positive','Neutral','Negative'],
        [GREEN,YELLOW,RED],[0.85,0.75,0.85]):
    data = rdf[rdf['sentiment']==sent]['score']
    ax3.hist(data,bins=20,color=clr,
             alpha=al,edgecolor='none',label=sent)
ax3.axvline(0.05,color=WHITE,linewidth=1.2,
            linestyle='--',alpha=0.5,label='Threshold')
ax3.axvline(-0.05,color=WHITE,linewidth=1.2,
            linestyle='--',alpha=0.5)
ax3.set_xlabel('Polarity Score (-1 to +1)',fontsize=8.5)
ax3.set_ylabel('Count',fontsize=8.5)
ax3.legend(fontsize=8,facecolor=CARD2,
           labelcolor=WHITE,edgecolor='#330000')

# ════════════════════════════════════════════════════
# ROW 2  — Story: Products
# ════════════════════════════════════════════════════

# C4 — Top Positive Products
ax4 = fig.add_subplot(gs[1,0:2])
style(ax4,'Top 10 Highly Positive Products',GREEN2)
pp = rdf[rdf['sentiment']=='Positive']\
    .groupby('product')['score']\
    .mean().sort_values(ascending=False).head(10)
short4 = [n[:38]+'...' if len(n)>38 else n
          for n in pp.index]
norm4  = plt.Normalize(pp.min(),pp.max())
clrs4  = [plt.cm.Greens(0.45+0.5*norm4(v))
          for v in pp.values]
b4 = ax4.barh(short4,pp.values,
              color=clrs4,edgecolor='none',height=0.62)
ax4.invert_yaxis()
ax4.set_xlabel('Avg Polarity Score',fontsize=9)
ax4.set_xlim(0,1.18)
ax4.tick_params(axis='y',colors=WHITE,labelsize=9)
for b in b4:
    ax4.text(b.get_width()+0.01,
             b.get_y()+b.get_height()/2,
             f'{b.get_width():.2f}',
             va='center',color=WHITE,
             fontsize=9.5,fontweight='bold')

# C5 — Top Negative Products
ax5 = fig.add_subplot(gs[1,2:4])
style(ax5,'Top 10 Most Negative Products',RED4)
np_ = rdf[rdf['sentiment']=='Negative']\
     .groupby('product')['score']\
     .mean().sort_values(ascending=True).head(10)
short5 = [n[:38]+'...' if len(n)>38 else n
          for n in np_.index]
norm5  = plt.Normalize(np_.min(),np_.max())
clrs5  = [plt.cm.Reds(0.45+0.45*norm5(abs(v)))
          for v in np_.values]
b5 = ax5.barh(short5,np_.values,
              color=clrs5,edgecolor='none',height=0.62)
ax5.invert_yaxis()
ax5.set_xlabel('Avg Polarity Score',fontsize=9)
ax5.tick_params(axis='y',colors=WHITE,labelsize=9)
ax5.axvline(0,color=WHITE,linewidth=1,alpha=0.3)
for b in b5:
    ax5.text(b.get_width()-0.01,
             b.get_y()+b.get_height()/2,
             f'{b.get_width():.2f}',
             va='center',ha='right',
             color=WHITE,fontsize=9.5,fontweight='bold')

# ════════════════════════════════════════════════════
# ROW 3  — Story: Insights
# ════════════════════════════════════════════════════

# C6 — Marketing Insights (horizontal)
ax6 = fig.add_subplot(gs[2,0:2])
style(ax6,'Marketing Insights — Avg Score by Category','#003300')
ms = rdf.groupby('category')['score']\
        .mean().sort_values(ascending=True)
clrs6 = [GREEN if v>0.25 else
         YELLOW if v>0.15 else RED
         for v in ms.values]
b6 = ax6.barh(ms.index,ms.values,
              color=clrs6,edgecolor='none',height=0.62)
ax6.invert_yaxis()
ax6.set_xlabel('Avg Polarity Score',fontsize=9)
ax6.tick_params(axis='y',colors=WHITE,labelsize=10)
ax6.set_xlim(0,0.43)
for b in b6:
    v = b.get_width()
    sentiment_label = ('🟢 Positive' if v>0.25
                       else '🟡 Neutral' if v>0.15
                       else '🔴 Negative')
    ax6.text(v+0.004,
             b.get_y()+b.get_height()/2,
             f'{v:.3f}  {sentiment_label}',
             va='center',color=WHITE,
             fontsize=9,fontweight='bold')

# C7 — Stacked by Category
ax7 = fig.add_subplot(gs[2,2:4])
style(ax7,'Sentiment Breakdown — All Categories','#1A0000')
st = rdf.groupby(['category','sentiment'])\
        .size().unstack(fill_value=0)
for c in ['Positive','Neutral','Negative']:
    if c not in st.columns: st[c]=0
st = st[['Positive','Neutral','Negative']]\
       .sort_values('Positive',ascending=False)
bot = np.zeros(len(st))
for col,clr in zip(
        ['Positive','Neutral','Negative'],
        [GREEN,YELLOW,RED]):
    vals = st[col].values
    ax7.bar(range(len(st)),vals,bottom=bot,
            color=clr,edgecolor=BG,
            linewidth=0.8,width=0.65,
            label=col,alpha=0.92)
    for j,(v,b) in enumerate(zip(vals,bot)):
        if v > 300:
            ax7.text(j,b+v/2,f'{v:,}',
                     ha='center',color=WHITE,
                     fontsize=8.5,fontweight='bold')
    bot += vals
ax7.set_xticks(range(len(st)))
ax7.set_xticklabels(st.index,rotation=15,
    ha='right',color=WHITE,fontsize=9.5)
ax7.set_ylabel('Number of Reviews',fontsize=9)
ax7.legend(fontsize=9,facecolor=CARD2,
           labelcolor=WHITE,edgecolor='#330000')
ax7.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x,p: f'{int(x):,}'))

# ── Bottom bar ────────────────────────────────────
bot_ax = fig.add_axes([0,0.018,1,0.012])
bot_ax.set_facecolor(RED2); bot_ax.axis('off')
fig.text(0.5,0.007,
    'CodeAlpha Data Analytics Internship   ●   Task 4 : Sentiment Analysis   ●   Rejitha E   ●   CA/DF1/85415   ●   May 2026',
    ha='center',fontsize=9,color=LGRAY)

plt.savefig('task4_sentiment_dashboard.png',
            dpi=170,bbox_inches='tight',facecolor=BG)

print("\n✅ Dashboard saved!")
print(f"\n{'='*50}")
print("   AMAZON SENTIMENT - FINAL SUMMARY")
print(f"{'='*50}")
print(f"📊 Total Reviews   : {total:,}")
print(f"✅ Positive        : {pos:,} ({pos/total*100:.1f}%)")
print(f"⚪ Neutral         : {neu:,} ({neu/total*100:.1f}%)")
print(f"❌ Negative        : {neg:,} ({neg/total*100:.1f}%)")
print(f"📈 Avg Score       : {avg:.3f}")
best = rdf.groupby('category')['score'].mean().idxmax()
worst= rdf.groupby('category')['score'].mean().idxmin()
print(f"\n💡 Best Category   : {best}")
print(f"⚠️  Worst Category  : {worst}")
print(f"\n✅ Task 4 Complete!")