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

To deploy the bot as a systemd service:

1. Create a systemd service file (`telegram-media-forward-bot.service`) in `/etc/systemd/system/`:

    ```plaintext
    [Unit]
    Description=Telegram Media Forward Bot Service
    After=network.target

    [Service]
    User=ubuntu # replace with your VPS username if different
    WorkingDirectory=/path/to/telegram-media-forward-bot # replace with actual path
    ExecStart=/usr/bin/python3 bot.py
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```

2. Enable and start the service:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable telegram-media-forward-bot.service
    sudo systemctl start telegram-media-forward-bot.service
    ```

3. Check logs for troubleshooting:

    ```bash
    journalctl -u telegram-media-forward-bot.service -f
    ```

---

## 🛠️ Technologies Used

- 🐍 **Python** (3.10+)
- 🤖 **Pyrogram** (Telegram MTProto API framework)
- ⚡ **Asyncio** (Concurrency and throttling control)

---

## 📖 License

📝 MIT License © Your Name or Organization Name.

---

Bot created by Telegram [@asifalex](https://t.me/asifalex). 🎉

Citations:
[1] https://emojipedia.org/github
[2] https://doakio.com/blog/emojis-in-tech-docs-fad-or-future/
[3] https://blog.invidelabs.com/21-emojis-every-developer-should-be-using/
[4] https://jimit105.github.io/github-emoji-cheatsheet/
[5] https://texta.ai/blog/google-docs/emojify-your-documents-unleash-the-power-of-emojis-in-google-docs
[6] https://www.myintervals.com/blog/introducing-emojis-for-tasks-projects-and-more/
[7] https://gist.github.com/roachhd/1f029bd4b50b8a524f3c
[8] https://dev.to/devshreeom/how-to-boost-your-productivity-as-a-developer-with-emojis-4aff
[9] https://www.linkedin.com/pulse/most-common-100-professional-emojis-linkedin-please-copy-erhan-eren
[10] https://github.com/onmyway133/emoji
[11] https://www.process.st/emoji-in-business-documents/
[12] https://www.freepik.com/free-photos-vectors/technology-emoji
[13] https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md
[14] https://www.linkedin.com/pulse/cracking-code-leveraging-emojis-enhanced-marketing-deeper-jandal-jvvxc
[15] https://www.reddit.com/r/todoist/comments/endlvg/what_handy_emojis_do_you_use_for_quick_visual/
[16] https://github.com/ikatyang/emoji-cheat-sheet
[17] https://iconscout.com/blog/enhancing-design-emojis-add-playfulness-expression-creations
[18] https://blog.hubspot.com/marketing/best-emojis
[19] https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia
[20] https://emojidb.org/technology-project-emojis

---
Answer from Perplexity: pplx.ai/share
