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
- `assets/gallery/plantegning.png`: Gallery copy of the floor plan.
- `picture_raw/`: Raw HEIC source photos from the user.
- `scripts/update-gallery-manifest.mjs`: Regenerates the gallery manifest from
  the files that actually exist in `assets/gallery/`.
- `scripts/generate-qr-code.py`: Regenerates the QR code PNG for the website
  URL.
- `scripts/requirements-qr.txt`: Python dependency for QR generation.
- `salgsopstilling-sundgade-1.html`: Print-ready private sales statement
  source for bank/interested buyers.
- `salgsopstilling-sundgade-1.pdf`: Generated PDF sales statement for sharing
  with interested buyers/banks.
- `qr-code.png`: Current QR code image for the public website URL.
- `Screenshot 2026-05-13 at 21.04.02.png`: Current floor plan image.

## Current Property Facts

Use these as the currently known facts unless the user changes them:

- Address: Sundgade 1, 4.th, 6400 Sønderborg.
- Type: Ejerlejlighed.
- Floor: 4th floor, no elevator.
- Size: 93 m2 + 6 m2 balcony.
- Front-page facts may present this as "100 m2 inkl. altan" / gross area for a
  simple buyer-facing overview, while detailed copy should still preserve the
  known 93 m2 + 6 m2 balcony distinction.
- Tinglyst area: 86 m2 according to 2020 sales material.
- Rooms: 3 rooms, including 2 bedrooms.
- Bad/toilet: 1 bathroom and 1 toilet.
- Plan: 1.
- Asking price: 2.650.000 kr.
- Calculated 5% down payment shown publicly: 132.500 kr.
- Common expenses: 3.650 kr./md.
- Heating: 7.920 kr. aconto / 7.440 kr. used last year, per user input.
- Energy label: C, per user input.
- Takeover: Flexible.
- Pets: Allowed, per user input.
- Kitchen and bathroom brand: AUBO, per user input/template.
- Parking: Private parking option; earlier material mentions unnumbered parking.
- Boat spot: Private boat spot no. C is mentioned in historic material and
  should be confirmed as current before being treated as final.
- Storage/cellar: Private depot/storage room included.
- Bike parking: Yes.
- Internet: Fiber installed.
- Unique feature: remote-controlled skylight/ovenlysvindue with extra daylight
  and easy ventilation.
- Contact: Søren, soren.petersen95@gmail.com.
- Phone should not be shown publicly for now.
- Nearby-distance copy currently uses user-provided public-facing distances:
  about 50 m to bus stop, SDU, Alsion/concert hall and Sønderborg Station, and
  about 300 m to the beach. City life/Borgen/slot/cafés/restaurants are still
  described as over the bridge on the opposite side of Alssund.
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
- Balcony from 2025 hangs directly over Alssund/the water, with view over
  Alssund and the bridge. This is a key sales point and should be emphasized.

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
- Important location orientation: Sundgade 1 is on the opposite side of Alssund
  from the Nørre Havnegade inspiration listing. It is on the same side as
  Alsion/SDU and Sønderborg Station, and opposite Borgen, Sønderborg Slot and
  the bus station. Public copy should describe those opposite-side amenities as
  reached over/across the bridge rather than implying they are on the same side.
- Practical layout: kitchen-living room, two bedrooms, bathroom, hallway/entry,
  balcony.
- Relevant to couples, singles, students needing extra space, or a buyer wanting
  a separate office/guest room.
- Public-facing copy should read like a polished listing, not an internal
  worksheet. Avoid repeated caveats such as "historisk materiale", "tidligere
  oplyst" and "bør bekræftes" on the page itself; keep necessary caution in the
  general disclaimer or internal notes.
- Mention brands such as AUBO only where they add concrete value, not repeatedly
  in headlines and intro copy.

Buyer-message preference:

- For broad first-contact questions such as whether the apartment is still for
  sale, whether viewing is possible, or what the annual/monthly expenses are,
  answer politely and refer to the website plus the sales statement for facts
  and economy before proposing a specific viewing time, unless the user asks to
  suggest a time.

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
- Set `assets/photos/outside-across-water-marked.png` as the primary front-page
  image and added preferred ordering to the gallery manifest script so the
  location/exterior/view images appear first.
- Made front-page images click through to `gallery.html` with an `image`
  parameter so the matching image opens directly in the slideshow.
- Added the floor plan to the gallery as `assets/gallery/plantegning.png`, with
  a custom "Plantegning" label in the manifest.
- Added a bottom gallery strip before the contact section, including balcony,
  living space and floor plan entry points.
- Reworked the main public-facing copy toward a more polished real-estate sales
  tone, with stronger focus on light, view, opholdsmiljø, altan and location,
  while preserving factual private-sale framing.
- Updated the headline and balcony copy to emphasize that the balcony is
  directly over the water/Alssund.
- User prefers the current opening direction: "Penthouse-lejlighed med altan over
  Alssund", stronger emphasis on Sønderborg Slot, cafélivet, bridge opening,
  boat traffic, sunrise behind the city, and a more polished premium listing
  tone.
- Latest user copy also emphasizes Skanserne, stranden, 100 m2 bruttoareal inkl.
  altan/depotrum, and a shorter public contact paragraph without the seller's
  first name in the body text.
- Added a fuller Boligfakta-style detail list using the apartment's own facts:
  udbudsform, plan, bad, toilet, boligareal, bruttoareal and varmekilde. Do not
  copy B energy label, 2008 build year, 3rd floor, 2 rooms, 91 m2 or 10 m2
  balcony from the comparison listing.
- Updated the area/location section with more water-and-city positioning based
  on transferable inspiration from a nearby Nørre Havnegade listing.
- Added an "Udvalgte hverdagsafstande" block for grocery, pharmacy, daycare,
  school district, station/SDU and city life.
- Added an institution/school statistics block for day institutions, ground
  schools and key figures for Dybbøl-Skolen and Sønderskov-Skolen.
- Added a document/sales-information section, expanded room-by-room copy, and
  made the economy/facts section more complete while keeping unknown figures
  marked as to be clarified rather than inventing current values.
- Cleaned public-facing copy to read more like a polished listing: fewer visible
  caveats, AUBO mentioned only where useful, and distance values shown without
  repeated "ca." prefixes.
- Tested responsive preview through a local HTTP server at 360/390 mobile, 768
  tablet, 1366 laptop and 1440 desktop widths. `index.html` and `gallery.html`
  had no broken images and no horizontal overflow after adding a cache-busted
  stylesheet link and tightening mobile nav wrapping.
- Fixed mobile hero image rendering by making the top photo-slot images fill
  their slots absolutely, increasing the two smaller mobile rows, and bumping
  the stylesheet query string to `style.css?v=2026-05-18`.
- Corrected public location copy so Sundgade is described on the Alsion/SDU and
  station side of Alssund, with Borgen, Sønderborg Slot and the bus station on
  the opposite side reached over the bridge.
- Added `scripts/generate-qr-code.py` and `scripts/requirements-qr.txt` so the
  QR code can be regenerated for the GitHub Pages URL. The QR script adds a
  centered "Sundgade 1" label by default; use `--center-text` to change it or
  `--no-center-text` for a plain QR code.
- Created a bank-friendly private sales statement:
  `salgsopstilling-sundgade-1.html` and generated
  `salgsopstilling-sundgade-1.pdf`. The PDF is intended to be sent as the main
  document to interested buyers/banks, with underlying PDFs from
  `documentation/` as supporting attachments.
- Updated the public economy section on `index.html` so the 3.650 kr./md.
  amount is clearly presented as the total monthly owner expense, with
  fællesudgifter, aconto varme, aconto vand and trapperengøring shown as
  sub-items of that same amount. Added annual/other rows for 2025 heat/water
  consumption, property tax, ground tax, insurance information and bumped the
  stylesheet query string to `style.css?v=2026-05-19`.
- Added public download links for `salgsopstilling-sundgade-1.pdf` in the top
  navigation and as a simple button in the contact section. Bumped the
  stylesheet query string to `style.css?v=2026-05-19-2`.
- Added the remote-controlled skylight/ovenlysvindue as a unique feature in the
  public site copy, the PDF sales statement source, and the property-info
  template.

## Known Open Items

- More image curation may be useful. There are many raw photos and many gallery
  photos; the user may want to remove duplicates or reorder the best ones.
- Boat spot no. C should remain unconfirmed until the user verifies it.
- Some financial fields remain "oplyses ved henvendelse" or should be verified
  from current documents.
- The public economy block currently hides unknown/unverified financial rows
  rather than showing placeholders. Add them back only when current numbers are
  available.
- The site may eventually need downloadable documents, if the user provides
  approved public PDFs.
- If adding new source documents, avoid committing private purchase contracts or
  sensitive personal documents unless the user explicitly asks.
- To regenerate the QR code, install the QR dependency if needed:
  `python3 -m pip install -r scripts/requirements-qr.txt`, then run
  `python3 scripts/generate-qr-code.py`.
