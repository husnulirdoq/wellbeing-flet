# wellbeing-flet
create dir wellbeing-flet

echo "# wellbeing-flet" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/husnulirdoq/wellbeing-flet.git
git push -u origin main

mkdir frontend
mkdir backend
mkdir admin

sudo apt update && sudo apt upgrade -y

sudo apt install python3.11 python3.11-venv -y

python3 -m venv venv
source venv/bin/activate

backend: FastAPI, connect ke PostgreSQL lewat DATABASE_URL.
admin: Streamlit, connect ke backend API.
frontend: Flet, connect ke backend API + Firebase config.
db: PostgreSQL, data disimpan di volume db_data.
Firebase: config file (firebase.json atau google-services.json) dimount ke container frontend/backend, lalu dipakai di kode Python.
