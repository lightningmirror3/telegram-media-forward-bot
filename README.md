# Telegram Media Forward Bot

A simple, robust Telegram bot built using [Pyrogram](https://github.com/pyrogram/pyrogram) to automatically forward specific video media messages from source channels to destination channels.

## 🚀 Features

- Automatically forwards videos from specified source channels to destination channels.
- Handles Telegram API errors gracefully (FloodWait, PeerIdInvalid, ChatWriteForbidden).
- Customizable MIME type filtering.
- Secure handling of sensitive credentials using environment variables.

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

git clone https://github.com/your_username/telegram-media-forward-bot.git
cd telegram-media-forward-bot


### Step 2: Install Dependencies


### Step 3: Set Environment Variables

Create a `.env` file in the project root and add your credentials:
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id
API_HASH=your_api_hash


Replace placeholders with your actual credentials.

### Step 3: Configure Channel Mapping

Edit `config.py` and update the `CHANNEL_MAPPING` dictionary with your channel IDs.

Example: 
CHANNEL_MAPPING = {
-1002386644256: -1002484982348,
-1001597273610: -1001721796359,
# Add more mappings as needed...
}


### Step 4: Run the Bot

python3 bot.py



## 🚀 Deployment (Systemd Service)

Create a systemd service file (`telegram-media-forward-bot.service`) in `/etc/systemd/system/`:

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


Then enable and start the service:

sudo systemctl daemon-reload
sudo systemctl enable telegram-media-forward-bot.service
sudo systemctl start telegram-media-forward-bot.service


Check logs:


## 🛠️ Technologies Used

- Python 3.10+
- Pyrogram (Telegram MTProto API framework)
- Asyncio for concurrency and throttling control

## 📖 License

MIT License © Your Name or Organization Name.








