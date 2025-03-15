# Telegram Media Forward Bot 🚀📹

A simple, robust Telegram bot built using [Pyrogram](https://github.com/pyrogram/pyrogram) to automatically forward specific video media messages from source channels to destination channels.

---

## ✨ Features

- 🎥 **Automated Forwarding**: Automatically forwards videos from specified source channels to destination channels.
- 🛡️ **Error Handling**: Gracefully handles Telegram API errors like FloodWait, PeerIdInvalid, and ChatWriteForbidden.
- 🔍 **MIME Type Filtering**: Allows customizable filtering based on MIME types.
- 🔒 **Secure Credentials**: Sensitive credentials are securely managed using environment variables.

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/your_username/telegram-media-forward-bot.git
cd telegram-media-forward-bot
```

### Step 2: Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Set Environment Variables

Create a `.env` file in the project root and add your credentials:

```plaintext
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id
API_HASH=your_api_hash
```

Replace placeholders with your actual credentials. 🔑

### Step 4: Configure Channel Mapping

Edit `config.py` and update the `CHANNEL_MAPPING` dictionary with your channel IDs:

```python
CHANNEL_MAPPING = {
    -1002386644256: -1002484982348,
    -1001597273610: -1001721796359,
    # Add more mappings as needed...
}
```

### Step 5: Run the Bot

Start the bot using:

```bash
python3 bot.py
```

---

## 🚀 Deployment (Systemd Service)

## Setting Up the Telegram Media Forward Bot Service

 Create and Edit the Service File

1. Open the `.service` file for editing using `nano`:
   ```bash
   sudo nano /etc/systemd/system/telegram-media-forward-bot.service
   ```

2. Paste the following content into the file:
   ```text
   [Unit]
   Description=Telegram Media Forward Bot Service
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/telegram-media-forward-bot
   ExecStart=/usr/bin/python3 bot.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

 Save and Exit

- Press `Ctrl+O` to save the file.
- Press `Enter` to confirm the filename.
- Press `Ctrl+X` to exit the editor.


3. Enable and start the service:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable telegram-media-forward-bot.service
    sudo systemctl start telegram-media-forward-bot.service
    ```

4. Check logs for troubleshooting:

    ```bash
    journalctl -u telegram-media-forward-bot.service -f
    ```

---
## 😓 Bot Misbehave Solution:

Revoke the old token for @your_bot via @BotFather and generate a new one:

Open @BotFather on Telegram.

Use /mybots and select @Myour_bot.

Choose "API Token" → "Revoke Token."

Generate a new token and update it in your .env file.

Delete the old session file after updating the token:


### Delete Session File

To delete the session file associated with your bot, use the following command:

```bash
rm MediaForwardBot.session
```

If you're unsure about the session filename, you can list all `.session` files in your current directory by running:

```bash
ls *.session
```

This will display all session files. You can then delete any `.session` files related to your bot as needed.

---

## 🛠️ Technologies Used

- 🐍 **Python** (3.10+)
- 🤖 **Pyrogram** (Telegram MTProto API framework)
- ⚡ **Asyncio** (Concurrency and throttling control)

---

## 📖 License

📝 MIT License © Your Name or Organization Name.

---

Bot created by- [@asifalex](https://t.me/asifalex). 🎉

