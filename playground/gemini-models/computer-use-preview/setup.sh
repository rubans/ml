# Clone the Repository
git clone https://github.com/google/computer-use-preview.git
cd computer-use-preview

# Set up Python Virtual Environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Install system dependencies required by Playwright for Chrome
playwright install-deps chrome
# Install the Chrome browser for Playwright
playwright install chrome