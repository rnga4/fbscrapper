const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  page.on('pageerror', err => console.log('BROWSER ERROR:', err));

  await page.goto('http://127.0.0.1:5000');
  
  console.log('Clicking scrape button...');
  await page.click('#btnScrape');
  
  // Wait for either the table to appear, or an alert
  page.on('dialog', async dialog => {
    console.log('ALERT TRIGGERED:', dialog.message());
    await dialog.accept();
  });

  console.log('Waiting for liveStatus to finish...');
  try {
    // Wait until liveStatus display becomes none OR tableWrapper becomes block
    await page.waitForFunction(() => {
      const live = document.getElementById('liveStatus').style.display;
      const table = document.getElementById('tableWrapper').style.display;
      return live === 'none' || table === 'block';
    }, { timeout: 60000 });
  } catch (e) {
    console.log('Wait timeout or error:', e);
  }

  const tableDisplay = await page.evaluate(() => document.getElementById('tableWrapper').style.display);
  const liveStatus = await page.evaluate(() => document.getElementById('liveStatus').style.display);
  const liveStatusText = await page.evaluate(() => document.getElementById('liveStatusText').textContent);
  
  console.log('Table display:', tableDisplay);
  console.log('LiveStatus display:', liveStatus);
  console.log('LiveStatus Text:', liveStatusText);
  
  const html = await page.evaluate(() => document.getElementById('tableBody').innerHTML);
  console.log('Table HTML:', html.substring(0, 200));

  await browser.close();
})();
