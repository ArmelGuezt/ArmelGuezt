"""Refresh public GitHub data; run with GITHUB_TOKEN in GitHub Actions."""
import json, os, datetime, urllib.request, urllib.error, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; USER='ArmelGuezt'
TOKEN=os.getenv('GITHUB_TOKEN'); HEAD={'Accept':'application/vnd.github+json','User-Agent':'ArmelGuezt-profile','X-GitHub-Api-Version':'2022-11-28'}
if TOKEN: HEAD['Authorization']='Bearer '+TOKEN
def get(url, body=None):
 req=urllib.request.Request(url,headers=HEAD,data=json.dumps(body).encode() if body else None)
 if body: req.add_header('Content-Type','application/json')
 with urllib.request.urlopen(req,timeout=30) as f: return json.load(f)
base='https://api.github.com'; repos=[]; page=1
while True:
 batch=get(f'{base}/users/{USER}/repos?type=owner&per_page=100&page={page}')
 repos.extend(x for x in batch if not x.get('private') and x['owner']['login'].lower()==USER.lower())
 if len(batch)<100:break
 page+=1
# Keep preferred projects first, then other repositories by name.
priority={'git-devops-automation':0,'cicd-multiple-stages-and-dependencies':1,'franka-braiding-salon':2}
repos.sort(key=lambda x:(priority.get(x['name'],3),x['name']))
rows=[]
for repo in repos:
 try: count=len(get(f'{base}/repos/{USER}/{repo["name"]}/commits?per_page=10'))
 except urllib.error.HTTPError as e:
  if e.code==409: count=0 # empty repository
  else: count=None
 except (OSError,ValueError): count=None
 rows.append({'name':repo['name'],'recent_commits':count})
calendar=None
if TOKEN:
 try:
  query='query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date weekday contributionCount}}}}}}'
  res=get(base+'/graphql',{'query':query,'variables':{'login':USER}})
  c=res['data']['user']['contributionsCollection']['contributionCalendar']
  calendar={'total':c['totalContributions'],'weeks':[[{'date':d['date'],'weekday':d['weekday'],'count':d['contributionCount']} for d in w['contributionDays']] for w in c['weeks']]}
 except (KeyError,TypeError,OSError,ValueError): print('Calendar unavailable; displaying explicit fallback.')
# Do not write misleading replacement stats if the repository request failed (it raises above).
result={'date':datetime.datetime.now(datetime.timezone.utc).date().isoformat(),'source':'rest','repos':rows,'stars':sum(x.get('stargazers_count',0) for x in repos),'calendar':calendar}
(ROOT/'data.json').write_text(json.dumps(result,indent=2)+'\n')
subprocess.run([sys.executable,str(ROOT/'scripts/render.py')],check=True)
