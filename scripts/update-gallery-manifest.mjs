import { readdir, writeFile } from "node:fs/promises";
import path from "node:path";

const galleryDir = path.join(process.cwd(), "assets", "gallery");
const outputPath = path.join(galleryDir, "gallery-manifest.json");
const allowedExtensions = new Set([".jpg", ".jpeg", ".png", ".webp", ".avif"]);
const preferredOrder = [
  "outside-across-water-marked.jpg.png",
  "IMG_2006.jpg",
  "IMG_2381.jpg",
  "IMG_6150.jpg",
  "IMG_6149.PNG",
  "IMG_6129.jpg",
  "IMG_6114.jpg",
  "IMG_2733.jpg",
  "IMG_2754.jpg",
  "IMG_2758.jpg",
  "IMG_2877.jpg",
  "IMG_2878.jpg",
  "IMG_2885.jpg",
  "IMG_2802.jpg",
  "IMG_2826.jpg",
  "IMG_2851.jpg"
];
const preferredRank = new Map(preferredOrder.map((file, index) => [file, index]));

const files = (await readdir(galleryDir))
  .filter((file) => allowedExtensions.has(path.extname(file).toLowerCase()))
  .sort((a, b) => {
    const aRank = preferredRank.get(a) ?? Number.POSITIVE_INFINITY;
    const bRank = preferredRank.get(b) ?? Number.POSITIVE_INFINITY;
    if (aRank !== bRank) return aRank - bRank;
    return a.localeCompare(b, "da", { numeric: true });
  });

const manifest = files.map((file, index) => ({
  src: `assets/gallery/${file}`,
  label: `Billede ${index + 1} af ${files.length}`
}));

await writeFile(outputPath, `${JSON.stringify(manifest, null, 2)}\n`);
console.log(`Wrote ${manifest.length} gallery images to ${outputPath}`);
