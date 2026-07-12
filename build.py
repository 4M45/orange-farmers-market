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
BLOG_DIST = os.path.join(DIST_DIR, 'blog')

# Ensure dist directories exist
os.makedirs(DIST_DIR, exist_ok=True)
os.makedirs(IMG_DIST, exist_ok=True)
os.makedirs(CSS_DIST, exist_ok=True)
os.makedirs(BLOG_DIST, exist_ok=True)

# Copy CSS and Images
shutil.copytree(CSS_SRC, CSS_DIST, dirs_exist_ok=True)
shutil.copytree(IMG_SRC, IMG_DIST, dirs_exist_ok=True)

# Jinja Setup
env = Environment(loader=FileSystemLoader(SRC_DIR))
template = env.get_template('template.html')
simple_template = env.get_template('simple.html')
blog_post_template = env.get_template('blog_post.html')

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

# Blog Data
blog_data = [
    {
        "slug": "ultimate-guide-dates-hours",
        "title": "The Ultimate Guide to Orange Farmers Market Dates & Hours",
        "description": "Find the perfect time to visit the market. Discover orange farmers market dates, seasonal changes, and find an orange farmers market near me.",
        "date": "July 12, 2026",
        "hero_image": "/images/blog_dates_hero.webp",
        "hero_alt": "Calendar surrounded by fresh organic vegetables showing orange farmers market dates",
        "content": "<p>When planning your weekly grocery shopping, knowing the exact <strong>orange farmers market dates</strong> is essential for getting the freshest local produce. Whether you're searching for an <em>orange farmers market near me</em> or just trying to beat the weekend rush, we've got you covered.</p><h2>Understanding the Market Schedule</h2><p>Our local vendors operate on a strict schedule designed to bring you goods at peak freshness. Generally, the core markets open at 9:00 AM and run until 1:00 PM. Arriving early guarantees you the best selection of organic fruits, artisanal cheeses, and fresh-baked breads.</p><img src='/images/inline_produce.webp' alt='Dew-covered organic kale and radishes available at the orange farmers market' style='width:100%; border-radius:8px; margin: 1rem 0;' loading='lazy' width='800' height='533'><p>Many residents frequently ask, \"When does the seasonal produce change?\" You'll find that our certified local farmers rotate their crops quarterly. By checking the official dates, you ensure that you never miss out on the short-lived strawberry season or the autumn pumpkin harvests.</p><h2>Navigating 'Near Me' Searches</h2><p>If you're constantly typing \"orange farmers market near me\" into your phone, consider making the Irvine Regional Park or Old Towne Orange locations your go-to hubs. Both offer ample parking if you arrive before 10:00 AM, making your weekend trip completely stress-free.</p><p>Remember, true agricultural quality is worth the trip. Experience the vibrant community and authoritative expertise of our vendors this weekend!</p>"
    },
    {
        "slug": "why-sunday-is-the-best-day",
        "title": "Why Sunday is the Best Day for Orange Markets",
        "description": "Explore why orange markets sunday events are the highlight of the week for fresh produce and meeting orange farmers.",
        "date": "July 15, 2026",
        "hero_image": "/images/blog_sunday_hero.webp",
        "hero_alt": "Bustling sunday morning crowd at the orange markets with fresh produce and wicker baskets",
        "content": "<p>There is a special energy that buzzes through the air during <strong>orange markets sunday</strong> events. While Saturday markets are bustling and fast-paced, Sunday offers a uniquely relaxed vibe that families and culinary enthusiasts absolutely love.</p><h2>Meeting the Orange Farmers</h2><p>Sundays are traditionally the days when the most experienced <em>orange farmers</em> bring out their specialty items. Because the frantic rush of Saturday has passed, farmers have more time to chat, share recipes, and explain their organic growing processes. This direct interaction is the cornerstone of trust in local agriculture.</p><img src='/images/inline_artisan.webp' alt='Glass jars filled with raw honey and artisan jams from local orange farmers' style='width:100%; border-radius:8px; margin: 1rem 0;' loading='lazy' width='800' height='533'><p>From heirloom tomatoes to raw honey, Sunday vendors take pride in their authoritative knowledge of sustainable farming. When you buy on a Sunday, you're not just purchasing food; you're investing in the local economy and learning directly from the experts.</p><h2>The Weekend Vibe</h2><p>Why else should you prioritize a Sunday visit? The crowds are manageable, live acoustic music often fills the air, and you have the leisure to sip a fresh-pressed green juice while you stroll. It is the ultimate weekend wind-down, perfectly blending community connection with premium natural ingredients.</p>"
    },
    {
        "slug": "meet-the-vendors-spotlight",
        "title": "Meet the Vendors: A Spotlight on Orange Grove Organic Food Markets",
        "description": "Get an inside look at orange farmers market vendors, the role of orange farmers market inc, and what makes orange grove organic food markets special.",
        "date": "July 18, 2026",
        "hero_image": "/images/blog_vendors_hero.webp",
        "hero_alt": "Local artisan farmer holding a crate of fresh organic heirloom tomatoes at orange grove organic food markets",
        "content": "<p>Behind every vibrant stall and overflowing wooden crate of fresh greens is a dedicated small business. Today, we're spotlighting the incredible <strong>orange farmers market vendors</strong> who make our weekends so delicious, with a special focus on the renowned <em>orange grove organic food markets</em>.</p><h2>The Standard of Organic Excellence</h2><p>When you visit the <strong>orange grove organic food markets</strong>, you are experiencing the pinnacle of sustainable agriculture. These vendors are carefully vetted by <em>orange farmers market inc</em>, the organizing body that ensures every participant meets strict, authoritative standards for organic certification and local sourcing.</p><img src='/images/inline_produce.webp' alt='Close-up of fresh organic produce sold by orange farmers market vendors' style='width:100%; border-radius:8px; margin: 1rem 0;' loading='lazy' width='800' height='533'><p>Our certified technicians of the soil—the farmers—spend decades perfecting their craft. This expertise translates directly into the robust flavors and nutritional density of the produce you take home.</p><h2>Supporting the Orange Farmers Market Inc Network</h2><p>By shopping with these vendors, you are directly supporting the initiatives of Orange Farmers Market Inc. Their mission goes beyond commerce; they strive to educate the public on the environmental benefits of organic farming and provide a reliable, trustworthy marketplace.</p><p>Next time you visit, ask your vendor about their growing practices. You'll be amazed by the deep well of knowledge they possess and the incredible care that goes into every single harvest.</p>"
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

# Generate Blog Posts
blog_cards_html = ""
for post in blog_data:
    # Render individual post
    html = blog_post_template.render(**post)
    file_path = os.path.join(BLOG_DIST, f"{post['slug']}.html")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    url_list.append(f"https://orangefarmersmarket.com/blog/{post['slug']}.html")
    
    # Generate HTML card for the index page
    blog_cards_html += f"""
    <div style='padding:1.5rem; background: var(--glass-bg); border:var(--glass-border); border-radius:12px; box-shadow:var(--glass-shadow);'>
        <p style='color: var(--color-primary-dark); font-size: 0.85rem; font-weight:bold;'>{post['date']}</p>
        <h3 style='margin-bottom:0.5rem;'><a href='/blog/{post['slug']}.html' style='color: var(--color-text);'>{post['title']}</a></h3>
        <p style='font-size: 0.95rem; color: var(--color-text-muted);'>{post['description']}</p>
        <a href='/blog/{post['slug']}.html' class='btn' style='margin-top:1rem; padding: 0.5rem 1rem; font-size: 0.9rem;'>Read More</a>
    </div>
    """

# Generate Home Page
home_data = pages[0].copy()
home_data['canonical_path'] = '/'
home_html = template.render(**home_data)
with open(os.path.join(DIST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(home_html)
url_list.append("https://orangefarmersmarket.com/")

# Generate AdSense Required Pages (Privacy, Terms, About, Contact) and Blog Index
static_pages = {
    "blog.html": {
        "title": "Our Blog",
        "description": "Read the latest news and updates from Orange Farmers Market.",
        "content": f"<p>Welcome to our blog! Stay tuned for seasonal recipes, farmer spotlights, and market updates.</p><div style='display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;'>{blog_cards_html}</div>"
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
