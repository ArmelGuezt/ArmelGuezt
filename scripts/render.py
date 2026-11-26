from pathlib import Path
import html
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'assets'; A.mkdir(exist_ok=True)
BG='#0d1117'; PANEL='#161b22'; LINE='#30363d'; BLUE='#58a6ff'; GREEN='#3fb950'; WHITE='#f0f6fc'; MUTED='#a6b3c2'; PURPLE='#bc8cff'
def esc(s): return html.escape(str(s),quote=True)
def t(x,y,s,size=16,color=WHITE,weight=400,extra=''):
 return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" {extra}>{esc(s)}</text>'
def r(x,y,w,h,fill=PANEL,stroke=LINE,rad=8,extra=''):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rad}" fill="{fill}" stroke="{stroke}" {extra}/>'
def svg(name,h,content,desc):
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{h}" viewBox="0 0 960 {h}" role="img" aria-label="{esc(desc)}" font-family="system-ui, -apple-system, Segoe UI, sans-serif"><title>{esc(desc)}</title><style>.mono{{font-family:ui-monospace, SFMono-Regular, Consolas, monospace}} @media(prefers-reduced-motion:reduce){{.animated{{display:none}}}}</style>{r(1,1,958,h-2,BG,LINE,12)}{content}</svg>'''
 (A/name).write_text(s+'\n')
# hero
s='''<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" stroke="#263747" opacity=".45" fill="none"/></pattern><clipPath id="edge"><rect x="1" y="1" width="958" height="258" rx="12"/></clipPath><linearGradient id="beam"><stop stop-color="#58a6ff" stop-opacity="0"/><stop offset=".5" stop-color="#58a6ff" stop-opacity=".13"/><stop offset="1" stop-color="#58a6ff" stop-opacity="0"/></linearGradient></defs><g clip-path="url(#edge)"><rect x="1" y="1" width="958" height="258" fill="url(#grid)"/><rect class="animated" x="-180" y="1" width="180" height="258" fill="url(#beam)"><animate attributeName="x" from="-180" to="960" dur="8s" repeatCount="indefinite"/></rect></g>'''
s+=r(24,24,912,212,BG,LINE,10)+''.join(f'<circle cx="{42+i*15}" cy="42" r="4" fill="{c}"/>' for i,c in enumerate(['#f85149','#e3b341',GREEN]))
s+=t(99,47,'armelguezt@engineering:~',12,MUTED,500,'class="mono"')+t(48,85,'$ whoami',15,GREEN,600,'class="mono"')+t(46,137,'Armel Guezem Titio',46,WHITE,750)+t(48,168,'DEVOPS / CLOUD INFRASTRUCTURE / SRE',16,BLUE,650,'class="mono"')+t(48,202,'Build. Automate. Scale. Keep it reliable.',16,MUTED)
s+=r(722,72,187,134,PANEL,LINE,8)+t(738,95,'ENGINEERING FOCUS',11,MUTED,650,'class="mono"')
for i,(lab,col) in enumerate([('AUTOMATION',BLUE),('DELIVERY',GREEN),('RELIABILITY',PURPLE)]):
 y=121+i*27;s+=f'<circle cx="744" cy="{y-4}" r="4" fill="{col}"/>'+t(757,y,lab,12,WHITE,500,'class="mono"')
s+='''<circle class="animated" cx="744" cy="117" r="7" fill="none" stroke="#58a6ff"><animate attributeName="r" values="5;13;5" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0;.7" dur="2s" repeatCount="indefinite"/></circle><rect class="animated" x="129" y="72" width="8" height="15" fill="#3fb950"><animate attributeName="opacity" values="1;1;0;0;1" dur="1.5s" repeatCount="indefinite"/></rect>'''
svg('hero-v2-full-name.svg',260,s,'Armel Guezem Titio - DevOps, cloud infrastructure and SRE')
# toolbox
s=t(24,30,'01 / ENGINEERING TOOLBOX',13,BLUE,650,'class="mono"')+t(936,30,'LEARNING & HANDS-ON PRACTICE',12,MUTED,500,'text-anchor="end" class="mono"')
for i,(title,items,col) in enumerate([('Systems',['Linux','Bash','Python','Git'],BLUE),('Delivery',['Docker','Kubernetes','Helm','GitHub Actions'],GREEN),('Cloud & IaC',['AWS','Azure','Terraform','OpenTofu'],PURPLE),('Reliability',['Observability','SLI / SLO','Incident response'], '#e3b341')]):
 x=24+i*232;s+=r(x,50,216,160)+r(x+13,64,5,19,col,col,2)+t(x+28,79,title,17,WHITE,650)
 for j,it in enumerate(items):s+=t(x+17,108+j*23,'+ '+it,14,MUTED,500,'class="mono"')
svg('toolbox.svg',230,s,'Engineering toolbox - areas of learning and hands-on practice')
# pipeline
s=t(24,30,'02 / CONTINUOUS DELIVERY',13,BLUE,650,'class="mono"')+t(936,30,'REFERENCE LAB ARCHITECTURE',12,MUTED,500,'text-anchor="end" class="mono"')
for i,(n,lab,sub,col) in enumerate([('01','CODE','Git',BLUE),('02','BUILD','CI/CD',BLUE),('03','PACKAGE','Docker',PURPLE),('04','DEPLOY','Kubernetes',GREEN),('05','OBSERVE','SRE',GREEN)]):
 x=24+i*184;s+=r(x,57,168,92)+t(x+13,78,n,11,col,650,'class="mono"')+t(x+13,104,lab,17,WHITE,700)+t(x+13,127,sub,13,MUTED)
 if i<4:s+=f'<path d="M{x+168} 102h16" stroke="{LINE}" stroke-width="2"/><circle class="animated" cx="{x+170}" cy="102" r="3" fill="{col}"><animate attributeName="cx" values="{x+169};{x+183}" dur="1.4s" begin="{i*.25}s" repeatCount="indefinite"/></circle>'
s+=t(24,179,'Feedback loop: monitor, measure, learn, improve.',14,MUTED)
svg('pipeline.svg',200,s,'Reference CI/CD lab workflow, not a claim of production deployments')
