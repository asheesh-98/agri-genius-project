setInterval(() => {
  const elems = document.querySelectorAll('[data-price]');
  elems.forEach(el => {
    const base = parseFloat(el.dataset.base) || parseFloat(el.textContent) || 10;
    const change = (Math.sin(Date.now()/5000 + base) + (Math.random()-0.5)) * 0.5;
    const val = Math.max(1, base + change).toFixed(2);
    el.textContent = val;
  });
}, 3000);
