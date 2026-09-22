# -*- coding: utf-8 -*-
import html, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from slides import S

import base64
HERE      = pathlib.Path(__file__).resolve().parent      # deck/build
PROJECT   = HERE.parent                                  # deck
LOGODIR   = HERE / 'logos'
POSTERDIR = HERE / 'poster'
OUTFILE   = PROJECT / 'robotics-2026.html'

def datauri_any(path, mime):
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()

LOGO_CDP = 'url("' + datauri_any(LOGODIR/'cdp.png', 'image/png') + '")'
LOGO_HS  = 'url("' + datauri_any(LOGODIR/'headspring.png', 'image/png') + '")'

# Each illustration ships twice: the still frame is embedded in the HTML so the
# deck renders instantly, the ~150-frame loop stays in img/ and is fetched when
# its slide comes up. See CLAUDE.md.
ART, ANIM = {}, {}
for _f in sorted(POSTERDIR.glob('*.webp')):
    _key = _f.stem.split('-', 1)[1]
    ART[_key]  = datauri_any(_f, 'image/webp')
    ANIM[_key] = 'img/' + _f.name
TITLE = "A Look at the Present and Future of Robotics"
FOOT  = "Robotics · present and future"
DATE  = "September 2026"
TOTAL = len(S)
LOGO = ('<div class="logorow">'
        '<div class="lg lg-cdp" role="img" aria-label="CDP"></div>'
        '<span class="lg-rule"></span>'
        '<div class="lg lg-hs" role="img" aria-label="Headspring Executive Development"></div>'
        '</div>')
FOOTLOGO = '<span class="foot-logo" aria-hidden="true"></span>'

NUM = {'golem': '01-golem', 'talos': '02-talos', 'pandora': '03-pandora', 'capek': '04-capek', 'steam': '05-steam', 'arm': '06-arm', 'warehouse': '07-warehouse', 'automaton': '08-automaton', 'brain-gear': '09-brain-gear', 'stage-mud': '10-stage-mud', 'hand-word': '11-hand-word', 'scale': '12-scale', 'pocketwatch': '13-pocketwatch', 'factory': '14-factory', 'lease-cart': '15-lease-cart', 'fishing-net': '16-fishing-net', 'seal': '17-seal'}

def art_block(name):
    uri = ART[name]
    return (f'<div class="art"><img class="art-img" src="{uri}" '
            f'data-anim="{ANIM[name]}" alt=""></div>')

def src_line(s):
    return f'<p class="src">{s["src"]}</p>' if s.get('src') else ''

def render(s, i):
    n, k = i + 1, s['kind']
    cls = ['slide', f'k-{k}'] + (['dark'] if s.get('dark') else [])
    body = ''
    if k == 'cover':
        cls.append('has-art')
        body = (f'<div class="col">{LOGO}'
                f'<h1 class="cover-title">{s["title"]}</h1>'
                f'<p class="cover-meta">{s["who"]}<br><span>{s["date"]}</span></p></div>'
                + art_block(s['art']))
    elif k == 'quote':
        body = f'<blockquote>{s["text"]}</blockquote><p class="attrib">{s["src"]}</p>'
    elif k == 'anchor':
        kick = f'<p class="kicker">{s["kicker"]}</p>' if s.get('kicker') else ''
        wide = ' wide' if s.get('wide') else ''
        body = f'{kick}<p class="anchor{wide}">{s["text"]}</p>'
    elif k == 'data':
        body = (f'<p class="figure">{s["figure"]}</p><p class="figcap">{s["cap"]}</p>'
                + src_line(s))
    elif k == 'video':
        cls.append('k-video')
        body = (f'<div class="vwrap" data-vid="{s["vid"]}" data-slug="{s["slug"]}">'
                f'<h2>{s["title"]}</h2>'
                f'<div class="vstage">'
                f'<video class="vplayer" playsinline preload="metadata">'
                f'<source src="video/{s["slug"]}.mp4" type="video/mp4">'
                f'<source src="video/{s["slug"]}.webm" type="video/webm">'
                f'</video>'
                f'<button class="play" aria-label="Play video"><span></span></button>'
                f'</div>'
                f'<p class="vlabel">{s["label"]}</p>'
                f'<p class="vhint"></p>'
                f'<a class="vlink" href="https://www.youtube.com/watch?v={s["vid"]}" '
                f'target="_blank" rel="noopener">open on youtube &#8599;</a></div>')
    elif k == 'bullets':
        lis = ''.join(f'<li>{b}</li>' for b in s['items'])
        has = bool(s.get('art'))
        if has: cls.append('has-art')
        body = (f'<div class="col"><h2>{s["title"]}</h2><ul>{lis}</ul>{src_line(s)}</div>'
                + (art_block(s['art']) if has else ''))
    elif k == 'close':
        body = (f'<h1 class="cover-title">{s["title"]}</h1>'
                f'<p class="mail"><a href="mailto:{s["mail"]}">{s["mail"]}</a></p>'
                f'<p class="cover-meta">{s["who"]} · {s["org"]}</p>')
    act = s.get('act', '')
    foot = ('' if k in ('cover',) else
            f'<footer><span class="fl-wrap">{FOOTLOGO}{act or FOOT} · {DATE}</span>'
            f'<span>{n} / {TOTAL}</span></footer>')
    return (f'<section class="{" ".join(cls)}" id="s{n}">'
            f'<div class="inner">{body}</div>{foot}</section>')

sections = '\n'.join(render(s, i) for i, s in enumerate(S))

CSS = r"""
:root{
  --paper:#F7F4EE; --ink:#1B1B1B; --brass:#B8860B; --rust:#A4441F;
  --grey:#8A8378; --line:#DED6C7;
  --logo-cdp:LOGOCDP;
  --logo-hs:LOGOHS;
  --sans:"Optima","Gill Sans","Gill Sans MT","Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{background:#171512;font-family:var(--sans);color:var(--ink);
  display:flex;align-items:center;justify-content:center;overflow:hidden}
#stage{position:relative;width:1280px;height:720px;transform-origin:center center;flex:none}
.slide{position:absolute;inset:0;background:var(--paper);padding:64px 84px 76px;
  display:none;align-items:center}
.slide.on{display:flex}
.inner{width:100%;display:flex;flex-direction:column;justify-content:center}
.has-art .inner{flex-direction:row;align-items:center;gap:36px}
.inner .col{flex:1 1 55%;min-width:0}
.art{flex:0 1 41%;display:flex;align-items:center;justify-content:center;
  max-height:520px;align-self:center}
.art img,.art svg{width:100%;height:auto;max-height:500px;display:block}
.art-img{display:block;border-radius:2px}
.art-svg{width:100%}

h1.cover-title{font-size:68px;max-width:12ch;line-height:1.04;font-weight:600;letter-spacing:-.02em}
h2{font-size:42px;font-weight:600;line-height:1.1;margin-bottom:34px;letter-spacing:-.01em}
h2::after{content:"";display:block;width:64px;height:3px;background:var(--brass);
  margin-top:18px;border-radius:2px}
.kicker{font-size:15px;letter-spacing:.22em;text-transform:uppercase;color:var(--brass);
  margin-bottom:22px;font-weight:600}
.cover-meta{font-size:22px;color:var(--grey);margin-top:38px;line-height:1.5}
.cover-meta span{font-size:18px}

ul{list-style:none}
li{font-size:27px;line-height:1.38;margin-bottom:19px;padding-left:30px;position:relative;
  max-width:29ch}
.slide:not(.has-art) li{max-width:44ch;font-size:29px;margin-bottom:24px}
li::before{content:"";position:absolute;left:0;top:.72em;width:14px;height:2px;
  background:var(--brass);border-radius:1px}
.slide:not(.has-art) li::before{width:16px;top:.7em}
li b{font-weight:700}
li i{font-style:italic}

.anchor{font-size:58px;line-height:1.18;font-weight:600;letter-spacing:-.015em;max-width:22ch}
.anchor.wide{max-width:none;font-size:50px;line-height:1.24;white-space:nowrap}  /* one sentence per line, no wrapping */
blockquote{font-size:44px;line-height:1.28;font-weight:400;font-style:italic;max-width:24ch}
.attrib{margin-top:34px;font-size:20px;color:var(--grey)}
.figure{font-size:104px;font-weight:700;letter-spacing:-.03em;line-height:1;color:var(--brass)}
.figcap{font-size:30px;line-height:1.35;margin-top:30px;max-width:26ch}
.src{margin-top:30px;font-size:15px;color:var(--grey);letter-spacing:.01em}
.dark{background:var(--ink);color:var(--paper)}
.dark .figure{color:#E2B95C}
.dark .src,.dark footer,.dark .attrib,.dark .cover-meta{color:#9A9287}
.dark li::before{background:#E2B95C}
.dark h2::after{background:#E2B95C}

.k-video .inner{align-items:flex-start}
.vwrap{width:100%}
.vstage{position:relative;margin-top:6px;width:100%;max-width:980px;aspect-ratio:16/9;
  background:#14120F;border-radius:3px;overflow:hidden;display:flex;
  align-items:center;justify-content:center;cursor:pointer}
.vstage.noclip{background:transparent;border:2px solid var(--line);max-width:760px}
.vplayer{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:#14120F}
.vstage.noclip .vplayer{display:none}
.vstage:fullscreen,.vstage:-webkit-full-screen{max-width:none;aspect-ratio:auto;border-radius:0;background:#000;border:0}
.vstage.playing{cursor:default}
.vstage.playing:hover .play{transform:none}
.play{position:relative;z-index:2;width:112px;height:112px;border-radius:50%;
  border:3px solid rgba(247,244,238,.92);background:rgba(20,18,15,.35);cursor:pointer;
  display:flex;align-items:center;justify-content:center;transition:background .18s,transform .18s;
  backdrop-filter:blur(2px)}
.play span{width:0;height:0;border-left:30px solid #F7F4EE;border-top:19px solid transparent;
  border-bottom:19px solid transparent;margin-left:9px}
.vstage:hover .play{background:var(--brass);transform:scale(1.05)}
.vstage.noclip .play{border-color:var(--ink);background:transparent}
.vstage.noclip .play span{border-left-color:var(--ink)}
.vstage.noclip:hover .play span{border-left-color:#F7F4EE}
.vlabel{margin-top:22px;font-size:21px;color:var(--ink);max-width:52ch;line-height:1.4}
.vhint{margin-top:8px;font-size:14px;color:var(--grey);letter-spacing:.03em}
.vhint a{color:var(--grey)}
.vlink{display:inline-block;margin-top:10px;font-size:14px;color:var(--grey);
  letter-spacing:.04em;text-decoration:none;border-bottom:1px solid var(--line)}
.vlink:hover{color:var(--brass);border-color:var(--brass)}
.k-video h2{margin-bottom:22px;font-size:38px}
.k-video h2::after{margin-top:14px}
.mail{margin-top:26px;font-size:34px}
.mail a{color:var(--brass);text-decoration:none;border-bottom:2px solid var(--line)}

footer{position:absolute;left:84px;right:84px;bottom:30px;display:flex;
  justify-content:space-between;font-size:13px;color:var(--grey);
  border-top:1px solid var(--line);padding-top:14px;letter-spacing:.04em}
.dark footer{border-color:#3A362F}


.logorow{display:flex;align-items:center;gap:24px;margin-bottom:38px}
.lg{background-position:left center;background-size:contain;background-repeat:no-repeat}
.lg-cdp{width:79px;height:44px;background-image:var(--logo-cdp)}
.lg-hs{width:171px;height:51px;background-image:var(--logo-hs)}
.lg-rule{width:1px;height:38px;background:var(--line)}
.foot-logo{display:inline-block;width:62px;height:19px;margin-right:13px;
  background:var(--logo-hs) left center/contain no-repeat;opacity:.9}
.dark .foot-logo{background-color:var(--paper);border-radius:2px;
  padding:3px 5px;box-sizing:content-box;opacity:.92}
footer .fl-wrap{display:flex;align-items:center}
#bar{position:fixed;left:0;bottom:0;height:3px;background:var(--brass);
  width:0;transition:width .22s ease;z-index:9}
#help{position:fixed;right:14px;top:12px;font-size:11px;color:#5E5850;
  letter-spacing:.08em;z-index:9;opacity:.75}
@media print{
  body{display:block;background:#fff;overflow:visible}
  #stage{width:auto;height:auto;transform:none!important}
  .slide{position:relative;display:flex!important;width:1280px;height:720px;
    page-break-after:always;break-after:page}
  #bar,#help{display:none}
}
"""

JS = r"""
const slides=[...document.querySelectorAll('.slide')];let i=0;
const bar=document.getElementById('bar'),stage=document.getElementById('stage');
function fit(){const s=Math.min(innerWidth/1280,innerHeight/720);stage.style.transform='scale('+s+')';}
function fitSlide(s){
  const inner=s.querySelector('.inner'); if(!inner) return;
  inner.style.zoom=1;
  const avail=s.clientHeight-parseFloat(getComputedStyle(s).paddingTop)
             -parseFloat(getComputedStyle(s).paddingBottom);
  let k=1;
  while(inner.scrollHeight*k>avail && k>0.62){k-=0.02;}
  if(k<1) inner.style.zoom=k.toFixed(2);
}
// ---- illustrations: still frame is embedded, the animated loop lives in img/ ----
// Each loop is fetched once, then swapped in. show() fetches the current and next
// slide at once; prefetchAll() then walks the whole deck one file at a time so every
// loop is cached long before its slide comes up, even on hotel wifi.
function animate(n,done){
  const s=slides[n]; if(!s){done&&done();return;}
  const img=s.querySelector('.art-img[data-anim]'); if(!img){done&&done();return;}
  const url=img.dataset.anim; delete img.dataset.anim;
  const pre=new Image();
  pre.onload=()=>{img.src=url; done&&done();};
  pre.onerror=()=>{done&&done();};   // no img/ next to the deck: the still stays
  pre.src=url;
}
let prefetching=false;
function prefetchAll(){
  if(prefetching) return; prefetching=true;
  const order=[]; for(let k=0;k<slides.length;k++) order.push((i+k)%slides.length);
  const next=()=>{ const n=order.shift(); if(n===undefined) return; animate(n,next); };
  next();
}
function show(n){
  i=Math.max(0,Math.min(slides.length-1,n));
  slides.forEach((s,k)=>s.classList.toggle('on',k===i));
  fitSlide(slides[i]);
  animate(i); animate(i+1);
  bar.style.width=((i+1)/slides.length*100)+'%';
  location.hash='#s'+(i+1);
  document.querySelectorAll('.ytframe').forEach(f=>{
    if(!f.closest('.slide').classList.contains('on')) f.remove();});
  document.querySelectorAll('.vplayer').forEach(v=>{
    if(!v.closest('.slide').classList.contains('on')){try{v.pause()}catch(e){}}});
  document.querySelectorAll('.vwrap .play').forEach(p=>{
    if(!p.closest('.vstage').querySelector('.ytframe')) p.style.display='flex';});
}
// ---- video ----
const FILE = location.protocol === 'file:';
function fsStage(){ const el=document.fullscreenElement||document.webkitFullscreenElement;
  return el && el.classList && el.classList.contains('vstage') ? el : null; }
function stopVideo(stage){
  const v=stage.querySelector('.vplayer'); if(v){try{v.pause()}catch(e){} v.controls=false;}
  stage.querySelectorAll('.ytframe').forEach(f=>f.remove());
  stage.classList.remove('playing');
  const p=stage.querySelector('.play'); if(p) p.style.display='flex';
  const w=stage.closest('.vwrap'); if(w) w.querySelector('.vhint').textContent =
    (v && v.readyState>0) ? 'press v · local clip, plays full screen'
    : FILE ? 'press v · opens on youtube, full screen' : 'press v · plays here, full screen';
}
function goFull(el){
  const r=el.requestFullscreen||el.webkitRequestFullscreen;
  if(r){ try{ const p=r.call(el); if(p&&p.catch) p.catch(()=>{}); }catch(e){} }
}
document.addEventListener('fullscreenchange',()=>{
  if(!fsStage()) document.querySelectorAll('.vstage.playing').forEach(stopVideo);
});
document.querySelectorAll('.vwrap').forEach(w=>{
  const v=w.querySelector('.vplayer'), stage=w.querySelector('.vstage'),
        hint=w.querySelector('.vhint');
  v.addEventListener('error',()=>{
    stage.classList.add('noclip');
    hint.textContent = FILE
      ? 'press v · opens on youtube, full screen'
      : 'press v · plays here, full screen';
  },true);
  v.addEventListener('loadedmetadata',()=>{
    stage.classList.remove('noclip'); hint.textContent='press v · local clip, plays full screen';
  });
  v.addEventListener('ended',()=>{ if(fsStage()===stage){ (document.exitFullscreen||document.webkitExitFullscreen).call(document); } else stopVideo(stage); });
});
function playVideo(w){
  const v=w.querySelector('.vplayer'), stage=w.querySelector('.vstage');
  if(stage.classList.contains('playing')){          // already running: toggle pause
    if(v && v.readyState>0 && !stage.querySelector('.ytframe')){ v.paused?v.play():v.pause(); }
    return;
  }
  // 1. local clip in video/  -> plays inside the deck, full screen, offline
  if(!stage.classList.contains('noclip') && v.readyState>0){
    stage.classList.add('playing'); w.querySelector('.play').style.display='none';
    v.controls=true; v.currentTime=0;
    goFull(stage); const p=v.play(); if(p&&p.catch) p.catch(()=>{});
    w.querySelector('.vhint').textContent='space pause · ← → seek · esc stop';
    return;
  }
  // 2. no local clip, served over http(s) -> embedded YouTube player, full screen
  const url='https://www.youtube.com/watch?v='+w.dataset.vid;
  if(!FILE){
    const f=document.createElement('iframe');
    let ok=false;
    f.className='ytframe';f.allow='autoplay; encrypted-media; fullscreen; picture-in-picture';
    f.allowFullscreen=true;f.style.cssText='position:absolute;inset:0;width:100%;height:100%;border:0';
    f.addEventListener('load',()=>{ok=true});
    f.src='https://www.youtube-nocookie.com/embed/'+w.dataset.vid+'?autoplay=1&rel=0&modestbranding=1&playsinline=1';
    stage.classList.remove('noclip'); stage.classList.add('playing'); stage.appendChild(f);
    w.querySelector('.play').style.display='none';
    w.querySelector('.vhint').textContent='youtube player · esc stop';
    goFull(stage);
    setTimeout(()=>{ if(!ok){ stopVideo(stage); stage.classList.add('noclip');
      w.querySelector('.vhint').textContent='embedding blocked here · opening youtube';
      window.open(url,'_blank','noopener'); } },3500);
    return;
  }
  // 3. opened as a file:// with no local clip -> browsers block the embed, open YouTube
  window.open(url,'_blank','noopener');
}
addEventListener('keydown',e=>{
  const ps=slides[i].querySelector('.vstage.playing');
  if(ps){                                            // a video is on: keys drive it
    const v=ps.querySelector('.vplayer'), yt=ps.querySelector('.ytframe');
    if(e.key===' '||e.key==='k'||e.key==='v'){ e.preventDefault(); if(v&&!yt){v.paused?v.play():v.pause();} }
    if(e.key==='ArrowRight'&&v&&!yt){ e.preventDefault(); v.currentTime=Math.min(v.duration||1e9,v.currentTime+10); }
    if(e.key==='ArrowLeft'&&v&&!yt){ e.preventDefault(); v.currentTime=Math.max(0,v.currentTime-10); }
    if(e.key==='Escape'){                            // leaving fullscreen stops it too (fullscreenchange)
      if(fsStage()) (document.exitFullscreen||document.webkitExitFullscreen).call(document);
      else stopVideo(ps); }
    return;
  }
  if(['ArrowRight','PageDown',' ','Enter','n'].includes(e.key)){e.preventDefault();show(i+1)}
  if(['ArrowLeft','PageUp','p'].includes(e.key)){e.preventDefault();show(i-1)}
  if(e.key==='Home')show(0); if(e.key==='End')show(slides.length-1);
  if(e.key==='v'){const w=slides[i].querySelector('.vwrap'); if(w){e.preventDefault();playVideo(w)}}
  if(e.key==='f'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
});
addEventListener('resize',fit);
document.addEventListener('click',e=>{
  const st=e.target.closest('.vstage');
  if(st){ if(!st.classList.contains('playing')) playVideo(st.closest('.vwrap')); return; }
  if(e.target.closest('a'))return;
  show(i+ (e.clientX < innerWidth*0.28 ? -1 : 1));
});
fit();
show(location.hash?parseInt(location.hash.slice(2))-1||0:0);
setTimeout(prefetchAll,1500);
"""

CSS = CSS.replace('LOGOCDP', LOGO_CDP).replace('LOGOHS', LOGO_HS)

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)} — Javier Fuentes Ibáñez</title>
<style>{CSS}</style>
</head>
<body>
<div id="stage">
{sections}
</div>
<div id="bar"></div>
<div id="help">← → navigate · f fullscreen</div>
<script>{JS}</script>
</body>
</html>
"""
OUTFILE.write_text(doc, encoding='utf-8')
# index.html so the GitHub Pages URL works without the file name; keeps the #sN hash.
(PROJECT / 'index.html').write_text(
    '<!doctype html><meta charset="utf-8"><title>' + html.escape(TITLE) + '</title>\n'
    '<meta http-equiv="refresh" content="0; url=robotics-2026.html">\n'
    '<script>location.replace("robotics-2026.html"+location.hash)</script>\n'
    '<a href="robotics-2026.html">' + html.escape(TITLE) + '</a>\n', encoding='utf-8')
print(f'wrote {OUTFILE}  {len(doc)/1024:.0f} KB  {TOTAL} slides')
