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

# Generate AdSense Required Pages (Privacy, Terms, About, Contact) and Blog
static_pages = {
    "blog.html": {
        "title": "Our Blog",
        "description": "Read the latest news and updates from Orange Farmers Market.",
        "content": "<p>Welcome to our blog! Stay tuned for seasonal recipes, farmer spotlights, and market updates.</p><div style='display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 2rem;'><div style='padding:1rem; border:1px solid #ccc; border-radius:8px;'><h4>Spring Harvest is Here</h4><p>Discover the freshest spring greens available this weekend.</p></div><div style='padding:1rem; border:1px solid #ccc; border-radius:8px;'><h4>Meet Our Artisans</h4><p>An inside look at the people behind our handcrafted goods.</p></div></div>"
    },
    "about.html": {
        "title": "About Us",
        "description": "Learn about the mission and history of Orange Farmers Market.",
        "content": "<div class='content-section'><h2>Our Mission</h2><p>Orange Farmers Market was established with a singular mission: to connect our community with the freshest, highest-quality local produce and artisan goods. We believe in sustainable agriculture, supporting local small businesses, and providing a vibrant, family-friendly marketplace for everyone to enjoy.</p><h2>What We Do</h2><p>We serve as the digital hub for local farmers markets in the Orange area. Our directory helps residents and visitors easily locate weekend markets, discover new vendors, and learn about the benefits of eating locally grown, organic food.</p><h2>Community First</h2><p>By bringing together certified local farmers and passionate artisans, we foster a community built on trust and agricultural excellence. We are dedicated to providing accurate, authoritative information to help you make the best choices for your family's table.</p></div>"
    },
    "contact.html": {
        "title": "Contact Us",
        "description": "Get in touch with Orange Farmers Market for vendor inquiries or general questions.",
        "content": "<div class='content-section'><p>Whether you have a question about our market locations, want to become a vendor, or just want to say hello, we would love to hear from you!</p><div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;'><div><h3>Get in Touch</h3><p><strong>Email:</strong> contact@orangefarmersmarket.com</p><p><strong>Phone:</strong> +1 (800) 555-FARM</p><p><strong>Mailing Address:</strong><br>123 Market Street, Suite 100<br>Orange, CA 92866</p></div><div><form style='display:flex;flex-direction:column;gap:1rem;'><input type='text' placeholder='Your Name' required style='padding:0.75rem; border:1px solid #ccc; border-radius:4px; font-family:inherit;'><input type='email' placeholder='Your Email' required style='padding:0.75rem; border:1px solid #ccc; border-radius:4px; font-family:inherit;'><input type='text' placeholder='Subject' required style='padding:0.75rem; border:1px solid #ccc; border-radius:4px; font-family:inherit;'><textarea placeholder='Your Message' rows='5' required style='padding:0.75rem; border:1px solid #ccc; border-radius:4px; font-family:inherit;'></textarea><button type='submit' class='btn' style='align-self:flex-start; border:none; cursor:pointer;'>Send Message</button></form></div></div></div>"
    },
    "privacy.html": {
        "title": "Privacy Policy",
        "description": "Privacy policy and cookie usage details for Orange Farmers Market.",
        "content": "<div class='content-section'><p><strong>Last updated: July 2026</strong></p><p>At Orange Farmers Market (orangefarmersmarket.com), the privacy of our visitors is of extreme importance to us. This privacy policy document outlines the types of personal information that is received and collected by our site and how it is used.</p><h2>Log Files</h2><p>Like many other Web sites, we make use of log files. The information inside the log files includes internet protocol (IP) addresses, type of browser, Internet Service Provider (ISP), date/time stamp, referring/exit pages, and number of clicks to analyze trends, administer the site, track user's movement around the site, and gather demographic information. IP addresses and other such information are not linked to any information that is personally identifiable.</p><h2>Cookies and Web Beacons</h2><p>We use cookies to store information about visitors' preferences, to record user-specific information on which pages the site visitor accesses or visits, and to personalize or customize our web page content based upon visitors' browser type or other information that the visitor sends via their browser.</p><h2>Google AdSense and DoubleClick DART Cookie</h2><ul><li>Third party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites.</li><li>Google's use of advertising cookies enables it and its partners to serve ads to our users based on their visit to our sites and/or other sites on the Internet.</li><li>Users may opt out of personalized advertising by visiting <a href='https://myadcenter.google.com/' target='_blank' rel='noopener noreferrer'>Google Ads Settings</a>. Alternatively, users can opt out of a third-party vendor's use of cookies for personalized advertising by visiting <a href='https://www.aboutads.info' target='_blank' rel='noopener noreferrer'>www.aboutads.info</a>.</li></ul><h2>Consent</h2><p>By using our website, you hereby consent to our privacy policy and agree to its terms. If you require any more information or have any questions about our privacy policy, please feel free to contact us by email at contact@orangefarmersmarket.com.</p></div>"
    },
    "terms.html": {
        "title": "Terms of Service",
        "description": "Terms of service and user agreements for Orange Farmers Market.",
        "content": "<div class='content-section'><p><strong>Last updated: July 2026</strong></p><h2>1. Acceptance of Terms</h2><p>By accessing and using Orange Farmers Market (orangefarmersmarket.com), you accept and agree to be bound by the terms and provision of this agreement. If you do not agree to abide by these terms, please do not use this service.</p><h2>2. Informational Purposes Only</h2><p>All content provided on this website is for informational purposes only. The owners of this website make no representations as to the accuracy or completeness of any information on this site or found by following any link on this site. The owners will not be liable for any errors or omissions in this information nor for the availability of this information.</p><h2>3. Intellectual Property Rights</h2><p>The site and its original content, features, and functionality are owned by Orange Farmers Market and are protected by international copyright, trademark, patent, trade secret, and other intellectual property or proprietary rights laws.</p><h2>4. External Links</h2><p>Our website may contain links to third-party web sites or services that are not owned or controlled by Orange Farmers Market. We have no control over, and assume no responsibility for, the content, privacy policies, or practices of any third party web sites or services.</p><h2>5. Changes to Terms</h2><p>We reserve the right, at our sole discretion, to modify or replace these Terms at any time. We will try to provide at least 30 days' notice prior to any new terms taking effect.</p></div>"
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
