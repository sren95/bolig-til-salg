# AGENTS.md

## Purpose

This repository is a private apartment sales notice site for Sundgade 1, 4.th,
6400 Sønderborg. The user wants it to feel like it was built by a professional
real-estate company, while still being honest that it is a private sale.

This file is the Codex equivalent of a `CLAUDE.md`: read it before making
changes, keep it updated, and use it as project memory.

## User Intent

- Build a polished, trustworthy sales page for the apartment.
- Present the apartment with strong visuals, concrete facts, a floor plan, map,
  gallery/slideshow, and clear contact path.
- Keep the tone professional, warm, factual, and not overhyped.
- Reuse useful copy and facts from the old purchase/sales documents, but do not
  present outdated numbers as current.
- Make it easy to publish via GitHub Pages.
- Make it easy to maintain when images or property facts change.

## Current Site Structure

- `index.html`: Main sales page.
- `gallery.html`: Full gallery page with slideshow/popover.
- `style.css`: Shared styling for both pages.
- `bolig-oplysninger-template.md`: Source worksheet for facts, copy, privacy,
  images, documents, and future updates.
- `assets/photos/`: Curated images used on the main page.
- `assets/gallery/`: Web-friendly gallery images used by `gallery.html`.
- `assets/gallery/gallery-manifest.json`: Generated list of actual gallery
  images. `gallery.html` reads this file so deleted images do not show as blank.
- `picture_raw/`: Raw HEIC source photos from the user.
- `scripts/update-gallery-manifest.mjs`: Regenerates the gallery manifest from
  the files that actually exist in `assets/gallery/`.
- `Screenshot 2026-05-13 at 21.04.02.png`: Current floor plan image.

## Current Property Facts

Use these as the currently known facts unless the user changes them:

- Address: Sundgade 1, 4.th, 6400 Sønderborg.
- Type: Ejerlejlighed.
- Floor: 4th floor, no elevator.
- Size: 93 m2 + 6 m2 balcony.
- Tinglyst area: 86 m2 according to 2020 sales material.
- Rooms: 3 rooms, including 2 bedrooms.
- Asking price: 2.600.000 kr.
- Common expenses: 3.650 kr./md.
- Heating: 7.920 kr. aconto / 7.440 kr. used last year, per user input.
- Energy label: C, per user input.
- Takeover: Flexible.
- Pets: Allowed, per user input.
- Parking: Yes; earlier material mentions unnumbered parking.
- Storage/cellar: Yes.
- Bike parking: Yes.
- Internet: Fiber installed.
- Contact: Søren, soren.petersen95@gmail.com.
- Phone should not be shown publicly for now.
- Nearby-distance copy currently uses approximate public data: nearest grocery
  about 500 m, Apoteket Borgen about 600 m, nearest registered daycare about
  550 m, and school districts mentioned as Dybbøl-Skolen/Sønderskov-Skole.
  Treat these as approximate and verify before making them more definitive.
- Institution stats currently shown: about 50 day institutions in Sønderborg
  according to Minly; 37 ground schools in Sønderborg Kommune according to
  DinGeo; Dybbøl-Skolen 829 pupils, wellbeing 3.70, grade average 7.5;
  Sønderskov-Skolen 630 pupils, wellbeing 3.60, grade average 7.0. Treat all
  as public third-party/official-derived data that can change.

## Improvements To Highlight

- Total renovation/total refurbishment in 2018.
- District heating for all apartments in the owners' association in 2022.
- New low-energy windows and new bay window/karnap in 2023.
- New main door to the stairwell in 2024.
- Balcony from 2025 with access through a door in the bay window/karnap.
- Balcony/view over Alssund and the bridge.

## Text And Positioning

Current positioning:

- Apartment by Alssund with balcony and view.
- Open kitchen-living space as the main gathering point.
- View toward Alssund, the bridge, and historic Sønderborg surroundings.
- Area copy can reuse/paraphrase transferable positioning from a nearby
  Nørre Havnegade listing: water-facing everyday life, walks along Alssund,
  proximity to harbor, city center, shopping, cafes/restaurants, bus, doctor,
  Sønderborg Slot and Slotsparken. Do not reuse exact phrasing or transfer
  building-specific facts such as elevator, penthouse, southwest balcony, or
  exact distances unless verified for Sundgade 1.
- Practical layout: kitchen-living room, two bedrooms, bathroom, hallway/entry,
  balcony.
- Relevant to couples, singles, students needing extra space, or a buyer wanting
  a separate office/guest room.

Text reused from older sales material should be paraphrased and updated. The
old sales listing was useful for ideas like:

- View toward water, Sønderborg Slot, and Christian X's Bro.
- Kitchen-living room as the natural gathering point.
- Light fronts, dark counters, integrated appliances/materials.
- Common outdoor areas by the water.
- Cykelskur, vaskerum, cellar/storage, parking.
- Boat spot no. C is mentioned in older material, but must be described as
  historical/unconfirmed unless the user confirms it is current.

## Disclaimers And Caution

The site includes a standard disclaimer/forbehold. Preserve it unless the user
asks to change it. The disclaimer should cover:

- Information is for guidance in a private sale.
- Measurements, areas, financial numbers, floor plans, map details, and
  descriptions may be rounded or may change.
- Buyers should verify information in documents, with the owners' association or
  administrator, and with their own advisers before agreement.

Be conservative with old PDF/sales listing data. Prefer wording like:

- "ifølge tidligere salgsopstilling"
- "historisk materiale nævner..."
- "bør bekræftes som aktuel"

Do not use outdated 2020 price, old monthly owner expense, or old energy label
when newer user-provided values exist.

## Gallery Maintenance

The full gallery is manifest-driven. If images are added or deleted in
`assets/gallery/`, run:

```sh
node scripts/update-gallery-manifest.mjs
```

This rewrites `assets/gallery/gallery-manifest.json` so `gallery.html` shows the
correct image count and no missing-image blanks.

Raw HEIC photos are in `picture_raw/`. GitHub Pages cannot display HEIC reliably,
so photos used by the site should be converted to JPG/WebP/PNG before being
referenced.

The main page uses a curated subset in `assets/photos/`. The full gallery uses
`assets/gallery/`.

## Local Preview

For local preview:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Then open:

- Main page: `http://127.0.0.1:8080/`
- Full gallery: `http://127.0.0.1:8080/gallery.html`

Stop the server before finishing if it was started by the agent.

## GitHub Pages

Expected GitHub Pages URL:

```text
https://sren95.github.io/bolig-til-salg/
```

GitHub Pages should be configured as:

- Source: Deploy from a branch.
- Branch: `main`.
- Folder: `/root`.

## How Future Agents Should Work

1. Read this file first.
2. Check `git status --short` before changing files.
3. Treat user edits as intentional. Do not revert or overwrite user changes
   unless explicitly asked.
4. Read the relevant current files before editing:
   - `index.html`
   - `gallery.html`
   - `style.css`
   - `bolig-oplysninger-template.md`
   - `assets/gallery/gallery-manifest.json` when gallery work is involved
5. If the user adds/removes gallery images, regenerate the manifest.
6. If the user changes facts in `bolig-oplysninger-template.md`, update the site
   to match, and update this file if the fact is important project memory.
7. If the user changes the site directly, inspect and preserve their changes.
   Work with them rather than restoring an older version from memory.
8. After meaningful changes, update this file under the relevant sections so the
   next agent has current context.
9. Preview visual changes locally when possible, especially changes to layout,
   images, map, floor plan, or slideshow.
10. Keep public-facing copy professional, precise, and in Danish unless the user
    asks otherwise.

## Progress So Far

- Replaced an accidental `index.html.save` draft with real `index.html` and
  `style.css`.
- Added `.gitignore`.
- Added `bolig-oplysninger-template.md` for structured data capture.
- Filled in property facts from the user's template.
- Added disclaimer/forbehold to page and template.
- Added floor plan section using `Screenshot 2026-05-13 at 21.04.02.png`.
- Added Google Maps preview and link.
- Corrected elevator status to "no elevator".
- Parsed useful facts from old purchase/sales PDF visually because it was
  scanned/image-based.
- Added newer improvements from the user: 2018 renovation, 2022 district
  heating, 2023 windows/karnap, 2024 stairwell main door, 2025 balcony.
- Converted selected HEIC photos to web JPGs for the main page.
- Added curated main-page gallery.
- Added `gallery.html` full gallery page with popover/slideshow.
- Converted raw gallery photos to web-friendly JPGs under `assets/gallery/`.
- Changed gallery from hardcoded 131-image range to manifest-based loading.
- Added `scripts/update-gallery-manifest.mjs`.
- Updated the area/location section with more water-and-city positioning based
  on transferable inspiration from a nearby Nørre Havnegade listing.
- Added an "Udvalgte hverdagsafstande" block for grocery, pharmacy, daycare,
  school district, station/SDU and city life.
- Added an institution/school statistics block for day institutions, ground
  schools and key figures for Dybbøl-Skolen and Sønderskov-Skolen.
- Added a document/sales-information section, expanded room-by-room copy, and
  made the economy/facts section more complete while keeping unknown figures
  marked as to be clarified rather than inventing current values.

## Known Open Items

- More image curation may be useful. There are many raw photos and many gallery
  photos; the user may want to remove duplicates or reorder the best ones.
- Boat spot no. C should remain unconfirmed until the user verifies it.
- Some financial fields remain "oplyses ved henvendelse" or should be verified
  from current documents.
- The site may eventually need downloadable documents, if the user provides
  approved public PDFs.
- If adding new source documents, avoid committing private purchase contracts or
  sensitive personal documents unless the user explicitly asks.
