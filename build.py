import os
import shutil
import json
from jinja2 import Environment, FileSystemLoader

# Directories
SRC_DIR = 'src'
DIST_DIR = 'dist'
IMG_SRC = os.path.join(SRC_DIR, 'images')
IMG_DIST = os.path.join(DIST_DIR, 'images')
CSS_SRC = os.path.join(SRC_DIR, 'css')
CSS_DIST = os.path.join(DIST_DIR, 'css')

# Ensure dist directories exist
os.makedirs(DIST_DIR, exist_ok=True)
os.makedirs(IMG_DIST, exist_ok=True)
os.makedirs(CSS_DIST, exist_ok=True)

# Copy CSS and Images
shutil.copytree(CSS_SRC, CSS_DIST, dirs_exist_ok=True)
shutil.copytree(IMG_SRC, IMG_DIST, dirs_exist_ok=True)

# Jinja Setup
env = Environment(loader=FileSystemLoader(SRC_DIR))
template = env.get_template('template.html')
simple_template = env.get_template('simple.html')

# Data Matrix
pages = [
    {
        "canonical_path": "/market/orange-home-grown/",
        "market_name": "Orange Home Grown",
        "city": "Orange, CA",
        "state_code": "CA",
        "service": "Farmers & Artisans Market",
        "landmark": "Old Towne Orange",
        "primary_benefit": "Fresh local produce and handcrafted artisan goods",
        "h2_1": "Why Choose Orange Home Grown Farmers & Artisans Market?",
        "p_1": "Nestled near Old Towne Orange, this market provides an incredible array of fresh, organic ingredients. Whether you're a culinary enthusiast or simply searching for the freshest local produce, our certified local farmers bring their absolute best. You can taste the expertise in every bite.",
        "p_2": "Our commitment to quality means everything you find here is grown with care and authority in the agricultural field.",
        "h2_2": "Connecting the Community Through Fresh Produce",
        "p_3": "Experience matters. The farmers at Orange Home Grown Farmers & Artisans Market have spent years perfecting their harvest, delivering trustworthy and high-quality goods.",
        "p_4": "From handcrafted artisan goods to the finest seasonal vegetables, trust your local vendors in Orange, CA."
    },
    {
        "canonical_path": "/market/irvine-regional-park/",
        "market_name": "Irvine Regional Park Farmers Market",
        "city": "Orange, CA",
        "state_code": "CA",
        "service": "Regional Park Farmers Market",
        "landmark": "Irvine Regional Park",
        "primary_benefit": "Family-friendly market experience with organic options",
        "h2_1": "A Family-Friendly Regional Park Farmers Market",
        "p_1": "If you're looking for a relaxing weekend outing, the Irvine Regional Park Farmers Market is unmatched. Situated near Irvine Regional Park, this location offers a vibrant atmosphere full of trustworthy farmers and local artisans.",
        "p_2": "Expect nothing but the finest organic options and a welcoming community.",
        "h2_2": "Freshness You Can Trust",
        "p_3": "With generations of experience, our vendors bring an authoritative knowledge of agriculture to your table.",
        "p_4": "Join us to enjoy a family-friendly market experience with organic options in beautiful Orange, CA."
    },
    {
        "canonical_path": "/market/all-aboard/",
        "market_name": "All Aboard Flea & Farmers Market",
        "city": "Orange County, CA",
        "state_code": "CA",
        "service": "Flea & Farmers Market",
        "landmark": "Local Rail Hub",
        "primary_benefit": "Unique vintage finds mixed with fresh farm produce",
        "h2_1": "Discover the All Aboard Flea & Farmers Market",
        "p_1": "Right by the Local Rail Hub, this unique market blends a traditional farmers market with vintage treasures. Trust our curated selection of vendors who offer both fresh farm produce and rare flea market finds.",
        "p_2": "It's an experience built on local expertise and community trust.",
        "h2_2": "More Than Just Produce",
        "p_3": "The All Aboard Flea & Farmers Market is an authoritative source for local goods. Our vendors are carefully selected to ensure the highest quality.",
        "p_4": "Find your unique vintage finds mixed with fresh farm produce right here in Orange County, CA."
    },
    {
        "canonical_path": "/info/sunday-markets/",
        "market_name": "Sunday Markets",
        "city": "Orange, CA",
        "state_code": "CA",
        "service": "Sunday Farmers Markets",
        "landmark": "Central Orange County",
        "primary_benefit": "The best weekend spots for fresh produce",
        "h2_1": "Your Guide to Sunday Farmers Markets in Orange, CA",
        "p_1": "Planning your weekend? Sunday Farmers Markets are the perfect way to spend your morning in Central Orange County. Rely on our extensive local expertise to guide you to the freshest produce available.",
        "p_2": "Our detailed guide ensures you visit only the most trustworthy and high-quality vendors.",
        "h2_2": "Weekend Freshness Guaranteed",
        "p_3": "The best weekend spots for fresh produce aren't hard to find when you know where to look. Let our authoritative insights lead the way.",
        "p_4": "Shop local and support your community every Sunday."
    }
]

# Generate PSEO Pages
url_list = []
for page in pages:
    html = template.render(**page)
    # Ensure directory exists
    dir_path = os.path.join(DIST_DIR, page['canonical_path'].strip('/'))
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, 'index.html')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    url_list.append(f"https://orangefarmersmarket.com{page['canonical_path']}")

# Generate Home Page (Root index.html)
# We will just re-use the first market page as the home page for now, 
# or a slightly modified version.
home_data = pages[0].copy()
home_data['canonical_path'] = '/'
home_html = template.render(**home_data)
with open(os.path.join(DIST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(home_html)
url_list.append("https://orangefarmersmarket.com/")

# Generate AdSense Required Pages (Privacy, Terms, About, Contact)
static_pages = {
    "about.html": {
        "title": "About Us",
        "description": "Learn about Orange Farmers Market.",
        "content": "<p>We are dedicated to bringing the freshest local produce to Orange, CA. Our network of farmers markets ensures quality, sustainability, and community support.</p>"
    },
    "contact.html": {
        "title": "Contact Us",
        "description": "Get in touch with Orange Farmers Market.",
        "content": "<p>Have questions or want to become a vendor? Please reach out!</p><form style='display:flex;flex-direction:column;gap:1rem;'><input type='text' placeholder='Name' required style='padding:0.5rem;'><input type='email' placeholder='Email' required style='padding:0.5rem;'><textarea placeholder='Message' rows='5' required style='padding:0.5rem;'></textarea><button type='submit' class='btn' style='align-self:flex-start;'>Send Message</button></form>"
    },
    "privacy.html": {
        "title": "Privacy Policy",
        "description": "Privacy policy for Orange Farmers Market.",
        "content": "<p>Your privacy is important to us. This privacy policy explains what data we collect and how it is used. We do not sell your personal data. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to your website or other websites.</p>"
    },
    "terms.html": {
        "title": "Terms of Service",
        "description": "Terms of service for Orange Farmers Market.",
        "content": "<p>By accessing our website, you agree to our terms of service. Content is for informational purposes only.</p>"
    }
}

for filename, data in static_pages.items():
    html = simple_template.render(**data)
    with open(os.path.join(DIST_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(html)
    url_list.append(f"https://orangefarmersmarket.com/{filename}")

# Generate robots.txt
robots_content = """User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: *
Allow: /

Sitemap: https://orangefarmersmarket.com/sitemap.xml
"""
with open(os.path.join(DIST_DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)

# Generate sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in url_list:
    sitemap_content += f"  <url>\n    <loc>{url}</loc>\n  </url>\n"
sitemap_content += "</urlset>"
with open(os.path.join(DIST_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print("Build completed successfully!")
