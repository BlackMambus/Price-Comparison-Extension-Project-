document.getElementById('compare').addEventListener('click', () => {
  const product = document.getElementById('product').value;
  fetch(`http://localhost:5000/compare?product=${encodeURIComponent(product)}`)
    .then(res => res.json())
    .then(data => {
      const results = document.getElementById('results');
      results.innerHTML = '';
      data.forEach(site => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="${site.url}" target="_blank">${site.site}: ${site.price}</a>`;
        results.appendChild(li);
      });
    });
});
