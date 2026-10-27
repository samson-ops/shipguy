"""ZIP-only pickup/delivery fields for the pricing tool (re-applied after the workspace reset).
Run:  python3 zip_lock.py [site_root]
Idempotent: pages that already carry data-zipfield are skipped."""
import sys, os, glob, re

SITE = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/build/shipguy'

def pages():
    out = []
    for p in glob.glob(os.path.join(SITE, '**', '*.html'), recursive=True):
        if '_preview-do-not-deploy' in p: continue
        h = open(p, encoding='utf-8').read()
        if 'id="pqForm"' in h: out.append(p)
    return sorted(out)

ZIP_FN = ("  function zipOk(inp){var er=document.getElementById(inp.id+'-err'); var v=inp.value.replace(/\\D/g,'').slice(0,5); if(v!==inp.value) inp.value=v; "
          "if(/^\\d{5}$/.test(v)){inp.classList.remove('err'); if(er)er.style.display='none'; return true;} inp.classList.add('err'); if(er)er.style.display='block'; return false;}\n"
          "  function locLabel(id,raw){var el=document.getElementById(id),d=el&&el.dataset?el.dataset:{}; raw=(raw||'').trim(); return d.city?(d.city+(d.state?', '+d.state:'')+(d.zip||raw?' '+(d.zip||raw):'')):raw;}\n")

REPL = [
 # --- form markup ---
 ('<input id="pq-pickup" name="pickup" placeholder="Enter city or ZIP code" autocomplete="off" required></div></div>',
  '<input id="pq-pickup" name="pickup" placeholder="Enter 5-digit ZIP code" inputmode="numeric" pattern="[0-9]{5}" maxlength="5" data-zipfield="1" autocomplete="off" required></div>'
  '<div class="pq-zip-hint" id="pq-pickup-hint"></div><div class="pq-zip-err" id="pq-pickup-err">Enter a 5-digit ZIP code.</div></div>', 1),
 ('<input id="pq-delivery" name="delivery" placeholder="Enter city or ZIP code" autocomplete="off" required></div></div>',
  '<input id="pq-delivery" name="delivery" placeholder="Enter 5-digit ZIP code" inputmode="numeric" pattern="[0-9]{5}" maxlength="5" data-zipfield="1" autocomplete="off" required></div>'
  '<div class="pq-zip-hint" id="pq-delivery-hint"></div><div class="pq-zip-err" id="pq-delivery-err">Enter a 5-digit ZIP code.</div></div>', 1),
 # --- validation ---
 ("if(inp.type==='checkbox'){if(!consentOk(inp))ok=false;return;} if(!inp.value.trim())",
  "if(inp.type==='checkbox'){if(!consentOk(inp))ok=false;return;} if(inp.dataset.zipfield){if(!zipOk(inp))ok=false;return;} if(!inp.value.trim())", 1),
 ("if(el.type==='checkbox'){if(!consentOk(el))ok=false;return;} if(!el.value.trim())",
  "if(el.type==='checkbox'){if(!consentOk(el))ok=false;return;} if(el.dataset.zipfield){if(!zipOk(el))ok=false;return;} if(!el.value.trim())", 1),
 ("  function validateAll(){", ZIP_FN + "  function validateAll(){", 1),
 ("  var cbx=document.getElementById('pq-consent'); if(cbx){cbx.addEventListener('change',function(){consentOk(cbx);});}",
  "  var cbx=document.getElementById('pq-consent'); if(cbx){cbx.addEventListener('change',function(){consentOk(cbx);});}\n"
  "  form.querySelectorAll('input[data-zipfield]').forEach(function(z){z.addEventListener('input',function(){var v=z.value.replace(/\\D/g,'').slice(0,5); if(v!==z.value) z.value=v; "
  "var hint=document.getElementById(z.id+'-hint'); if(hint&&!z.dataset.zip) hint.textContent=''; if(/^\\d{5}$/.test(v)){var er=document.getElementById(z.id+'-err'); if(er)er.style.display='none'; z.classList.remove('err');}});});", 1),
 # --- route label on the result card ---
 ("document.getElementById('pqRoute').textContent=(data.pickup||'')+' \\u2192 '+(data.delivery||'')+'  \\u00b7  '+(data.transport||'Open')+' transport';",
  "document.getElementById('pqRoute').textContent=locLabel('pq-pickup',data.pickup)+' \\u2192 '+locLabel('pq-delivery',data.delivery)+'  \\u00b7  '+(data.transport||'Open')+' transport';", 1),
 # --- Google Places: postal codes only; selection writes the ZIP and shows City, ST under the field ---
 ("fields:['address_components','formatted_address'],types:['(regions)']});",
  "fields:['address_components','formatted_address'],types:['postal_code']});", 1),
 ("        el.dataset.zip=zip; el.dataset.city=city; el.dataset.state=state;\n"
  "        el.value = city ? (city+(state?', '+state:'')+(zip?' '+zip:'')) : (zip||p.formatted_address||el.value);\n"
  "        el.classList.remove('err');",
  "        el.dataset.zip=zip; el.dataset.city=city; el.dataset.state=state;\n"
  "        el.value = zip || el.value.replace(/\\D/g,'').slice(0,5);\n"
  "        var hint=document.getElementById(id+'-hint'); if(hint) hint.textContent = city ? (city+(state?', '+state:'')) : '';\n"
  "        var er=document.getElementById(id+'-err'); if(/^\\d{5}$/.test(el.value)){el.classList.remove('err'); if(er)er.style.display='none';}",
  1),
 ("      el.addEventListener('input',function(){el.dataset.zip='';el.dataset.city='';el.dataset.state='';});",
  "      el.addEventListener('input',function(){el.dataset.zip='';el.dataset.city='';el.dataset.state=''; var hint=document.getElementById(id+'-hint'); if(hint) hint.textContent='';});", 1),
 # --- CSS ---
 (".pq-consent-err{display:none;color:#dc2b3d;font-size:13px;font-weight:600;margin-top:8px}",
  ".pq-consent-err{display:none;color:#dc2b3d;font-size:13px;font-weight:600;margin-top:8px}"
  ".pq-zip-hint{font-size:12.5px;color:#5b6478;margin-top:6px;min-height:0}.pq-zip-hint:empty{display:none}.pq-zip-err{display:none;color:#dc2b3d;font-size:12.5px;font-weight:600;margin-top:6px}", 1),
]

done = skipped = 0; problems = []
for p in pages():
    h = open(p, encoding='utf-8').read()
    if 'data-zipfield' in h: skipped += 1; continue
    new = h; bad = []
    for old, rep, n in REPL:
        c = new.count(old)
        if c != n: bad.append((old[:60], c)); continue
        new = new.replace(old, rep)
    if bad:
        problems.append((p.replace(SITE + '/', ''), bad)); continue
    open(p, 'w', encoding='utf-8').write(new); done += 1
print('zip lock applied:', done, '| already had it:', skipped, '| problems:', len(problems))
for p, b in problems: print('  ', p, b)
