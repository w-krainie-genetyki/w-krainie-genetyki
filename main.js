async function loadData(){
  const res = await fetch('data.json');
  const data = await res.json();
  return data;
}

function renderList(items){
  const container = document.getElementById('items');
  container.innerHTML = '';
  items.forEach(it=>{
    const el = document.createElement('div');
    el.className = 'item';
    el.innerHTML = `<strong>${it.title}</strong><small>${it.date || ''} · ${it.category}</small><div>${it.excerpt||''}</div>`;
    el.addEventListener('click', ()=> loadItem(it));
    container.appendChild(el);
  })
}

async function loadItem(item){
  document.getElementById('item-title').textContent = item.title;
  document.getElementById('item-meta').textContent = `${item.date || ''} · ${item.category}`;
  const res = await fetch(item.path);
  const md = await res.text();
  document.getElementById('item-body').innerHTML = marked.parse(md);
}

function setupSearch(all){
  const input = document.getElementById('search');
  input.addEventListener('input', ()=>{
    const q = input.value.toLowerCase().trim();
    const filtered = all.filter(i=> (i.title + ' ' + (i.excerpt||'') + ' ' + (i.tags||'')).toLowerCase().includes(q));
    renderList(filtered);
  })
}

document.addEventListener('DOMContentLoaded', async ()=>{
  const data = await loadData();
  renderList(data);
  setupSearch(data);
});
