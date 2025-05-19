const express = require('express');
const app = express();
const port = process.env.PORT || 3001; // Allow port to be set via environment variable

app.get('/time', (req, res) => {
    const offsetHours = parseInt(req.query.offset_hours) || 0;
    const now = new Date();
    now.setUTCHours(now.getUTCHours() + offsetHours);
    res.json({
        gmt_time: now.toISOString(),
        offset_applied_hours: offsetHours
    });
});

app.listen(port, () => {
    console.log(`MCP Time Service listening on port ${port}`);
}); 