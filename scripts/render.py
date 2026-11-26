from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'assets'; A.mkdir(exist_ok=True)
D=json.loads((ROOT/'data.json').read_text())
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
svg('hero.svg',260,s,'Armel Guezem Titio - DevOps, cloud infrastructure and SRE')
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
# data cards
repos=D['repos']; n=len(repos); recent=sum(x['recent_commits'] for x in repos if x.get('recent_commits') is not None); known=sum(x.get('recent_commits') is not None for x in repos); label='Recent commits returned' if D.get('source')=='connector' else 'Recent default-branch commits'; cap='Search results, up to 10 per repo' if D.get('source')=='connector' else 'Up to 10 per public repo'
s=t(24,30,'03 / GITHUB ACTIVITY',13,BLUE,650,'class="mono"')+t(936,30,'AS OF '+D['date'],12,MUTED,500,'text-anchor="end" class="mono"')
metrics=[(n,'Public repositories','Found in GitHub query'),(recent if known else 'N/A',label,cap),(known,'Repositories sampled','Commit data available')]
if D.get('stars') is not None: metrics[2]=(D['stars'],'Stars received','Across public repositories')
for i,(val,lab,sub) in enumerate(metrics):
 x=24+i*310;s+=r(x,50,292,110)+t(x+16,95,val,38,[BLUE,GREEN,PURPLE][i],700)+t(x+16,121,lab,15,WHITE,600)+t(x+16,143,sub,12,MUTED)
s+=t(24,191,'RECENT COMMITS / PUBLIC REPOSITORY SAMPLE',12,MUTED,600,'class="mono"')
for i,repo in enumerate(repos[:8]):
 y=215+i*39;count=repo.get('recent_commits');s+=t(24,y+12,repo['name'][:51],13,WHITE,500,'class="mono"')+r(465,y-1,415,16,PANEL,LINE,5)
 if count is not None and count>0:
  w=415*min(count,10)/10;s+=r(465,y-1,w,16,GREEN,GREEN,5)+f'<rect class="animated" x="465" y="{y-1}" width="{w}" height="16" rx="5" fill="#79e2a3" opacity=".18"><animate attributeName="opacity" values=".08;.4;.08" dur="3s" repeatCount="indefinite"/></rect>'
 s+=t(935,y+12,'N/A' if count is None else count,14,GREEN if count is not None else MUTED,600,'text-anchor="end" class="mono"')
h=256+len(repos[:8])*39;s+=t(24,h-20,'Sample only - not lifetime contributions. '+('Some repositories may be omitted.' if D.get('source')=='connector' else 'Public data only.'),12,MUTED)
svg('activity.svg',h,s,'GitHub repository and recent commit sample statistics dated '+D['date'])
# graph: optional real GitHub calendar, no fabricated cells
cal=D.get('calendar')
if cal:
 days=cal['weeks'];s=t(24,30,'04 / CONTRIBUTION CALENDAR',13,BLUE,650,'class="mono"')+t(936,30,str(cal['total'])+' contributions reported by GitHub',13,GREEN,600,'text-anchor="end"')
 colors=['#21262d','#0e4429','#006d32','#26a641','#39d353']
 for i,week in enumerate(days[-54:]):
  for day in week:
   c=day['count']; level=0 if c==0 else 1 if c<3 else 2 if c<6 else 3 if c<10 else 4
   s+=f'<rect x="{28+i*16.5}" y="{55+day["weekday"]*16.5}" width="13" height="13" rx="3" fill="{colors[level]}"><title>{esc(day["date"])}: {c}</title></rect>'
 s+=t(24,193,'GitHub calendar - visibility depends on profile settings and API access.',12,MUTED)
 svg('calendar.svg',211,s,'Real GitHub contribution calendar')
else:
 s=t(24,30,'04 / CONTRIBUTION CALENDAR',13,BLUE,650,'class="mono"')+t(24,68,'Calendar data not verified yet',22,WHITE,700)+t(24,94,'Open the live GitHub profile to view your contribution history.',14,MUTED)+t(24,119,'The refresh workflow will render the calendar when the API makes it available.',13,MUTED)
 svg('calendar.svg',140,s,'Contribution calendar not yet available')
