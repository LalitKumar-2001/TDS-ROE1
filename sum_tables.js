const { chromium } = require('playwright');

async function sumNumbersFromPage(url) {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(url);

  // Get all numbers from all tables
  const sum = await page.evaluate(() => {
    let total = 0;
    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
      const cells = table.querySelectorAll('td');
      cells.forEach(cell => {
        const num = parseFloat(cell.textContent.replace(/[^0-9.\-]+/g, ''));
        if (!isNaN(num)) total += num;
      });
    });
    return total;
  });

  await browser.close();
  return sum;
}

(async () => {
  const urls = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=72",
    "https://sanand0.github.io/tdsdata/js_table/?seed=73",
    "https://sanand0.github.io/tdsdata/js_table/?seed=74",
    "https://sanand0.github.io/tdsdata/js_table/?seed=75",
    "https://sanand0.github.io/tdsdata/js_table/?seed=76",
    "https://sanand0.github.io/tdsdata/js_table/?seed=77",
    "https://sanand0.github.io/tdsdata/js_table/?seed=78",
    "https://sanand0.github.io/tdsdata/js_table/?seed=79",
    "https://sanand0.github.io/tdsdata/js_table/?seed=80",
    "https://sanand0.github.io/tdsdata/js_table/?seed=81"
  ];

  let grandTotal = 0;
  for (const url of urls) {
    const subtotal = await sumNumbersFromPage(url);
    grandTotal += subtotal;
  }
  console.log(`Grand Total: ${grandTotal}`);
})();
