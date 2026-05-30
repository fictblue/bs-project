# BS (Baraya Salawasna) Website

Website tongkrongan Baraya Salawasna dengan fitur lengkap!

## 🚀 Tech Stack

- **Backend**: Django 5.0.4
- **Frontend**: Django Templates + HTML + TailwindCSS + JavaScript
- **Database**: SQLite (development)
- **AI**: OpenAI API (GPT-3.5-turbo)
- **Hosting**: Ngrok (development)

## 📋 Fitur

### Phase 1 (Completed)
- ✅ Homepage dengan stats, quote harian, dan foto random
- ✅ Member System dengan profile, skills, badges
- ✅ Gallery & Memories dengan upload foto
- ✅ Hidden Admin Panel di `/baraya-core`

### Phase 2 (Completed)
- ✅ Event System dengan agenda dan participants
- ✅ Achievement System dengan berbagai kategori
- ✅ BS Lore Archive untuk sejarah dan quotes

### Phase 3 (Completed)
- ✅ AI BS Assistant dengan OpenAI integration
- ✅ AI Memory System untuk belajar lore baru
- ⏳ Leaderboard (coming soon)

### Phase 4 (Coming Soon)
- ⏳ Real-time features
- ⏳ Mobile optimization

## 🛠️ Installation

1. Clone repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Setup environment variables:
```bash
cp .env.example .env
# Edit .env and add your values
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

7. Access website at `http://127.0.0.1:8000`

## 📁 Project Structure

```
bs_project/
├── core/           # Homepage dan daily quote
├── members/        # Member system
├── gallery/        # Gallery & memories
├── events/         # Event system
├── achievements/   # Achievement system
├── ai_assistant/   # AI BS Assistant
├── lore/           # BS Lore Archive
└── dashboard/      # Hidden admin panel
```

## 🔐 Admin Panel

- **Hidden Admin**: `/baraya-core/` (requires login)
- **Django Admin**: `/admin/` (requires superuser)

## 🤖 AI Assistant

AI BS Assistant bisa:
- Cari member berdasarkan skill
- Ceritain lore dan sejarah BS
- Info event yang akan datang
- Random roast member (santai aja)
- Jawab pertanyaan tentang BS

Untuk mengaktifkan AI, tambahkan `OPENAI_API_KEY` di `.env`

## 📝 Usage

1. **Tambah Member**: Login ke admin panel, tambah member dengan photo, skills, bio
2. **Upload Foto**: Upload foto ke gallery dengan caption dan kategori
3. **Buat Event**: Buat event dengan tanggal, lokasi, dan participants
4. **Tambah Achievement**: Tambah achievement untuk member yang berprestasi
5. **Lore Archive**: Tambah quotes, kejadian absurd, meme internal
6. **AI Memory**: Tambah lore baru agar AI belajar dan berkembang

## 🎨 Customization

- Ubah warna di `static/css/style.css`
- Ubah layout di `templates/base.html`
- Tambah custom logic di views masing-masing app

## 🚀 Deployment (Ngrok)

Untuk hosting dengan Ngrok:

1. Install Ngrok
2. Run: `ngrok http 8000`
3. Share URL dengan teman-teman

## 📝 Notes

- Password validation diaktifkan secara default
- Media files diupload ke `media/` folder
- Static files di `static/` folder
- Timezone: Asia/Jakarta
- Language: Indonesian

## 🎯 Roadmap

- [ ] Leaderboard untuk games
- [ ] Talent Showcase section
- [ ] Real-time notifications
- [ ] Mobile app version
- [ ] Dark mode
- [ ] Export data feature

---

Made with ❤️ by Baraya Salawasna
