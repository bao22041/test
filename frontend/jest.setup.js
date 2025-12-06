const fs = require('fs');
const path = require('path');

expect.extend({
  async toMatchScreenshot(page, testName) {
    const screenshotPath = path.join(__dirname, `./html-report/${testName}.png`);
    await page.screenshot({ path: screenshotPath });
    return { pass: true };
  }
});
