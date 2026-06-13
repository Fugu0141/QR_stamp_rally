# QR Stamp Rally

A simple QR code stamp rally app for real-world events.

Participants scan QR codes with their smartphones to collect stamps. When they collect all stamps, they can show the completion page to staff and receive a prize or reward.

This project runs as a static website, so it can be hosted on GitHub Pages, Netlify, Vercel, Cloudflare Pages, or any ordinary web server.

The default sample is a **5-stamp rally**, but you can change the number of stamps by editing `config.js`.

## Sample

A sample page is available here:

[![Live Sample](https://img.shields.io/badge/Live%20Sample-open-blue)](https://fugu0141.github.io/stamp-rally/)

## Features

- Designed for real-world stamp rally events
- Smartphone-friendly layout
- Static HTML/CSS/JavaScript only
- No backend required
- Works with any static web hosting service
- One reusable QR landing page: `stamp-get.html?id=1`
- Easy customization through `config.js`
- Completion page for showing a prize/reward message
- Optional QR code generation script

## How it works

Each QR code points to a stamp collection URL like this:

```txt
https://example.com/stamp-get.html?id=1
```

When a participant opens that URL on their phone, the app saves the stamp ID in the browser's `localStorage`.

The stamp book page reads the saved data and shows the participant's progress.

## File structure

```txt
.
├─ index.html                  # Home page and test links
├─ stamp.html                  # Stamp book page
├─ stamp-get.html              # QR landing page. Use ?id=1, ?id=2, etc.
├─ goal.html                   # Completion/prize page
├─ config.js                   # Main customization file
├─ assets/
│  ├─ css/
│  │  └─ style.css             # Shared design
│  └─ js/
│     ├─ stamp-core.js         # Stamp storage and common functions
│     ├─ index.js              # Home page rendering
│     ├─ stamp-page.js         # Stamp book rendering
│     ├─ stamp-get-page.js     # QR landing page rendering
│     └─ goal-page.js          # Completion page rendering
└─ tools/
   └─ generate_qr.py           # Optional QR code generator
```

## Quick start

1. Download or fork this repository.
2. Edit `config.js` for your event.
3. Publish the files to any static web hosting service.
4. Create QR codes for each `stamp-get.html?id=...` URL.
5. Print the QR codes and place them around your event venue.
6. Ask participants to scan the QR codes with their smartphones.

## Customizing the event

Most changes should be made in `config.js`.

### Change the app name

```js
appName: "My Event Stamp Rally",
logoText: "MY EVENT",
storageKey: "my_event_stamp_rally_v1",
```

`storageKey` is important. If you reuse the same browser for testing different events, changing this value keeps each event's stamp data separate.

### Change colors

```js
theme: {
  primary: "#0284c7",
  secondary: "#7c3aed",
  success: "#16a34a",
  background: "#f0f4f8",
  text: "#0f172a",
  muted: "#64748b"
},
```

### Change the stamps

The default version has 5 stamps:

```js
stamps: [
  { id: "1", icon: "🌟", title: "Stamp 1", message: "First stamp collected!" },
  { id: "2", icon: "🎈", title: "Stamp 2", message: "Nice progress!" },
  { id: "3", icon: "🧭", title: "Stamp 3", message: "More than halfway there!" },
  { id: "4", icon: "🎁", title: "Stamp 4", message: "Almost done!" },
  { id: "5", icon: "🏆", title: "Stamp 5", message: "You collected every stamp!" }
],
```

You can add or remove items. The stamp count updates automatically.

For example, a 3-stamp rally would look like this:

```js
stamps: [
  { id: "1", icon: "🍎", title: "Apple", message: "You found the apple spot!" },
  { id: "2", icon: "🍊", title: "Orange", message: "You found the orange spot!" },
  { id: "3", icon: "🍇", title: "Grape", message: "You found the grape spot!" }
],
```

Then your QR URLs would be:

```txt
stamp-get.html?id=1
stamp-get.html?id=2
stamp-get.html?id=3
```

## Hosting

You can host this project on any service that can publish static HTML files.

Examples:

- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages
- Your own web server

### Option 1: GitHub Pages

1. Create a new public GitHub repository.
2. Upload these files to the repository.
3. Open the repository's **Settings**.
4. Go to **Pages**.
5. Set **Source** to `Deploy from a branch`.
6. Select the `main` branch and `/root` folder.
7. Save.

After a short time, GitHub Pages will give you a URL like this:

```txt
https://your-name.github.io/your-repository/
```

Your stamp book will be here:

```txt
https://your-name.github.io/your-repository/stamp.html
```

Your first QR stamp URL will be here:

```txt
https://your-name.github.io/your-repository/stamp-get.html?id=1
```

### Option 2: Other static hosting services

Upload all project files to your hosting service.

The important point is that these files must be accessible through public URLs:

```txt
stamp.html
stamp-get.html?id=1
goal.html
config.js
assets/
```

For example, if your site is hosted at:

```txt
https://example.com/
```

Your first stamp URL will be:

```txt
https://example.com/stamp-get.html?id=1
```

## Creating QR codes

You can use any QR code generator. Each QR code should point to one stamp URL.

Example for a 5-stamp rally:

```txt
https://example.com/stamp-get.html?id=1
https://example.com/stamp-get.html?id=2
https://example.com/stamp-get.html?id=3
https://example.com/stamp-get.html?id=4
https://example.com/stamp-get.html?id=5
```

If you use GitHub Pages, replace `https://example.com/` with your GitHub Pages URL.

### Optional: generate QR codes with Python

Install the dependency:

```bash
pip install qrcode[pil]
```

Run this command from the project root:

```bash
python tools/generate_qr.py --base-url https://example.com/
```

The script creates:

```txt
qr-codes/       # QR PNG images
qr-print.html   # Printable QR code page
```

Open `qr-print.html` in your browser and print it.

## Testing locally

Because this is a static site, you can open `index.html` directly in a browser.

For more reliable testing, run a local server:

```bash
python -m http.server 8000
```

Then open:

```txt
http://localhost:8000/
```

Test the stamp URLs like this:

```txt
http://localhost:8000/stamp-get.html?id=1
http://localhost:8000/stamp-get.html?id=2
http://localhost:8000/stamp-get.html?id=3
http://localhost:8000/stamp-get.html?id=4
http://localhost:8000/stamp-get.html?id=5
```

## Resetting progress

The stamp book page includes a reset button. This is useful for testing before the event.

Participants' progress is stored only in their own browser. Resetting your own device does not reset other participants' devices.

## Important limitations

This app uses `localStorage`, so it is intentionally simple.

- Progress is saved per browser and per device.
- Progress is not synced across phones.
- Clearing browser data removes the stamps.
- There is no server-side anti-cheat system.
- A participant could technically open the stamp URLs manually if they know them.

For school events, small festivals, exhibitions, open campuses, club activities, or casual prize exchanges, this is usually enough.

If you need strict identity checks, one-time prize redemption, account-based progress, or stronger fraud prevention, you will need a backend system.

## Recommended event operation

For a casual event:

1. Print one QR code per stamp.
2. Place QR codes at different booths or locations.
3. Ask participants to open the stamp book page on their phone.
4. Participants scan QR codes to collect stamps.
5. When they collect all stamps, they show the completion page to staff.
6. Staff checks the screen and gives the prize.

## Suggested repository description

```txt
A simple QR code stamp rally app for real-world events.
```

## License

MIT License. You can modify and reuse this project for personal, school, or event projects.
