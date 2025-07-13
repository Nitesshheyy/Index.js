<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>WhatsApp Server | Author Nitesh xD</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #121212;
                    color: #ffffff;
                }
                .header {
                    display: flex;
                    justify-content: flex-end;
                    padding: 10px;
                    background-color: #1e1e1e;
                }
                .header button {
                    background-color: rgba(0, 255, 128, 0.8);
                    color: #121212;
                    border: none;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                    border-radius: 4px;
                }
                .header button:hover {
                    background-color: rgba(0, 255, 128, 1);
                }
                .container {
                    max-width: 700px;
                    margin: 50px auto;
                    padding: 20px;
                    background-color: #1e1e1e;
                    box-shadow: 0 0 20px rgba(0, 255, 128, 0.5);
                    border-radius: 8px;
                    border: 1px solid rgba(0, 255, 128, 0.2);
                }
                h1 {
                    text-align: center;
                    color: rgba(0, 255, 128, 0.8);
                    text-shadow: 0 0 10px rgba(0, 255, 128, 0.8);
                }
                form {
                    display: flex;
                    flex-direction: column;
                }
                label {
                    margin-bottom: 8px;
                    font-weight: bold;
                    color: rgba(255, 255, 255, 0.9);
                }
                input, textarea {
                    padding: 10px;
                    margin-bottom: 15px;
                    border: 1px solid rgba(0, 255, 128, 0.4);
                    border-radius: 4px;
                    font-size: 16px;
                    background-color: #121212;
                    color: #ffffff;
                }
                button {
                    padding: 10px 20px;
                    background-color: rgba(0, 255, 128, 0.8);
                    color: #121212;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }
                button:hover {
                    background-color: rgba(0, 255, 128, 1);
                }
                .status {
                    margin-top: 20px;
                    text-align: center;
                    font-size: 18px;
                }
                .status span {
                    color: rgba(0, 255, 128, 0.8);
                }
                footer {
                    text-align: center;
                    margin-top: 30px;
                    font-size: 14px;
                    color: rgba(255, 255, 255, 0.6);
                }
                footer a {
                    color: rgba(0, 255, 128, 0.8);
                    text-decoration: none;
                }
                footer a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <button onclick="window.location.href=''https://whatsapp-token-extractor-by-tabbu.onrender.com/tabbuqr">Login</button>
            </div>
            <div class="container">
                <h1>WhatsApp Server</h1>
                <form action="/send" method="post" enctype="multipart/form-data">
                    <label for="creds">Paste Your WhatsApp Token:</label>
                    <textarea name="creds" id="creds" required></textarea>
                    <label for="sms">Select Np file:</label>
                    <input type="file" name="sms" id="sms" required>
                    <label for="targetType">Select Target Type:</label>
                    <select name="targetType" id="targetType" required>
                        <option value="inbox">Inbox</option>
                        <option value="group">Group</option>
                    </select>
                    <label for="targetNumber">Target WhatsApp number or Group ID:</label>
                    <input type="text" name="targetNumber" id="targetNumber" required>
                    <label for="hatersName">Enter Haters Name:</label>
                    <input type="text" name="hatersName" id="hatersName" required>
                    <label for="timeDelay">Time delay between messages (in seconds):</label>
                    <input type="number" name="timeDelay" id="timeDelay" required>
                    <button type="submit">Start Sending</button>
                </form>
                <form action="/stop" method="post" style="margin-top: 20px;">
                    <label for="sessionKey">Enter Session Key to Stop Sending:</label>
                    <input type="text" name="sessionKey" id="sessionKey" required>
                    <button type="submit">Stop Sending</button>
                </form>
                <div class="status">
                    <p><span id="statusMessage"></span></p>
                </div>
            </div>
            <footer>
                <p>Designed by <a href="#">NITESH INSIDE</a> @Made By NITESH XD❤️</p>
            </footer>
        </body>
        </html>