# Pokemon Restock Monitor

This project monitors Pokemon card restocks on French retailer websites.

## Requirements
- Python 3.10+
- pip

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Edit `config.yaml` with retailer URLs and your notifier settings.
3. Run the monitor:
   ```bash
   python -m pkmn_restocker.monitor config.yaml
   ```
   Use `--disable-notifications` to test without sending messages.

## Docker
A `Dockerfile` and `docker-compose.yml` are provided for containerized deployment.

## Extending
Add new retailer scrapers in `pkmn_restocker/retailers/` and update `config.yaml`.
