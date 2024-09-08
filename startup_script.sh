# initial
sudo apt update
sudo apt-get install -y git
sudo apt-get install python3-venv=3.9.2-3 
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

git clone https://github.com/mpinchover/soundcloud_scraper.git
python3 -m venv soundcloud_env
source soundcloud_env/bin/activate
pip install -r requirements.txt

# boot
source soundcloud_env/bin/activate
pip install -r soundcloud_scraper/requirements.txt

# not sure
sudo apt-get install -y google-chrome-stable
