#!/usr/bin/env python3
"""
Bristol Dental & Orthodontics — Automated WordPress Blog Publisher
Runs weekly via GoDaddy cron job.
Posts rotating SEO-optimised dental blog content to bristol-dental.com
Posts are created as DRAFTS by default — log into wp-admin to review and publish.
"""

import json
import base64
import urllib.request
import urllib.error
import datetime
import logging

# ============================================================
# CONFIGURATION
# ============================================================
import os

WP_SITE_URL     = "https://bristol-dental.com"
WP_USERNAME     = os.environ.get("WP_USERNAME", "")
WP_APP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")
POST_STATUS     = "draft"   # Change to "publish" to go fully automatic
LOG_FILE        = "/tmp/bristol_dental_wp_posts.log"

# ============================================================
# ROTATING BLOG POSTS (12 weeks of content — loops automatically)
# ============================================================
BLOG_POSTS = [
    {
        "title": "5 Signs You Might Need a Dental Implant",
        "content": """<p>Losing a tooth can feel overwhelming, but dental implants have made it possible to restore your smile permanently and naturally. At Bristol Dental &amp; Orthodontics in Santa Ana, CA, Dr. Finley helps patients every week understand whether an implant is the right choice for them.</p>

<h2>Here are 5 signs an implant could be right for you:</h2>

<ol>
<li><strong>You have a missing tooth</strong> — Gaps in your smile don't just affect appearance; they can cause neighboring teeth to shift over time.</li>
<li><strong>Your dentures are uncomfortable</strong> — Implants are fixed in place and feel just like natural teeth, with no slipping or adhesive needed.</li>
<li><strong>You have difficulty chewing</strong> — A missing or failing tooth can make eating painful and affect your diet.</li>
<li><strong>Your jawbone is shrinking</strong> — Tooth loss leads to bone loss. Implants are the only restoration that stimulates the jawbone and prevents deterioration.</li>
<li><strong>You have a cracked or failing tooth</strong> — Sometimes saving a tooth isn't possible. An implant is often the best long-term solution.</li>
</ol>

<p>Dental implants are a long-term investment in your oral health. With proper care, they can last a lifetime.</p>

<p><strong>Serving patients in Santa Ana, Orange County, and surrounding areas.</strong></p>

<p>📞 Call us at <a href="tel:714-874-8579">714-874-8579</a> or <a href="https://bristol-dental.com/services/dental-implants/">learn more about dental implants at Bristol Dental</a>.</p>"""
    },
    {
        "title": "Invisalign vs. Braces: Which Is Right for You?",
        "content": """<p>Thinking about straightening your teeth? You're not alone — orthodontic treatment is one of the most popular dental services we offer at Bristol Dental &amp; Orthodontics in Santa Ana, CA. But with so many options available, how do you choose between Invisalign and traditional braces?</p>

<h2>Invisalign: The Clear Choice for Many Adults</h2>
<p>Invisalign uses a series of custom-made clear aligners that are nearly invisible when worn. They're removable, so you can eat whatever you like and brush and floss normally. Most patients in Santa Ana choose Invisalign for its discreet appearance and comfort.</p>

<h2>Traditional Braces: Tried and Tested</h2>
<p>Braces are fixed to your teeth and use wires and brackets to gradually shift your smile. They're highly effective for complex cases and are often the better choice for younger patients or more significant alignment issues.</p>

<h2>Which Should You Choose?</h2>
<ul>
<li>Choose <strong>Invisalign</strong> if you want a discreet, flexible option and have mild to moderate alignment issues.</li>
<li>Choose <strong>braces</strong> if your case is more complex or you prefer a fixed solution.</li>
</ul>

<p>The best way to find out which is right for you is a consultation with Dr. Finley. We offer orthodontic care for teens and adults throughout Santa Ana and Orange County.</p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> or visit our <a href="https://bristol-dental.com/services/invisalign/">Invisalign page</a> to book a consultation.</p>"""
    },
    {
        "title": "How Often Should You Really Visit the Dentist?",
        "content": """<p>You've probably heard that you should visit the dentist every six months — but is that right for everyone? At Bristol Dental &amp; Orthodontics in Santa Ana, we take a personalised approach to dental checkups based on your individual oral health needs.</p>

<h2>The Standard: Every 6 Months</h2>
<p>For most healthy adults and children, a checkup and professional cleaning every six months is the gold standard. It allows us to catch small problems — like early cavities or gum inflammation — before they become bigger, more expensive issues.</p>

<h2>You Might Need More Frequent Visits If You:</h2>
<ul>
<li>Have a history of gum disease or periodontal problems</li>
<li>Smoke or use tobacco products</li>
<li>Have diabetes, which can affect oral health</li>
<li>Are pregnant (hormonal changes can increase gum sensitivity)</li>
<li>Have a weakened immune system</li>
<li>Are prone to cavities or plaque buildup</li>
</ul>

<h2>Children and Seniors</h2>
<p>Kids and older adults often benefit from more frequent visits too. Growing teeth need monitoring, and seniors may face increased risk of dry mouth, gum disease, and tooth loss.</p>

<p>Not sure how often you should come in? Let Dr. Finley assess your oral health and build a schedule that works for you.</p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> or <a href="https://bristol-dental.com/contact/">book your checkup online</a> — serving Santa Ana and all of Orange County.</p>"""
    },
    {
        "title": "Teeth Whitening in Santa Ana: What Are Your Options?",
        "content": """<p>A brighter smile can make a huge difference in your confidence — and it's one of the most requested cosmetic dental treatments we offer at Bristol Dental &amp; Orthodontics in Santa Ana, CA. But with so many whitening products on the market, what actually works?</p>

<h2>Professional Whitening vs. Over-the-Counter Products</h2>
<p>Drugstore whitening strips and toothpastes can offer mild improvement, but professional teeth whitening at our Santa Ana dental office delivers dramatically better results — often several shades lighter in a single visit.</p>

<h2>In-Office Whitening</h2>
<p>Our in-office whitening treatment uses a professional-strength gel activated by a special light. Most patients see results of 4–8 shades lighter in about an hour. It's safe, fast, and done under the supervision of Dr. Finley.</p>

<h2>Take-Home Whitening Kits</h2>
<p>We also offer custom-fitted whitening trays you can use at home at your own pace. These deliver professional results more gradually and are great for maintaining your whitened smile after an in-office treatment.</p>

<h2>Is Whitening Right for You?</h2>
<p>Whitening works best on natural tooth enamel. It won't change the colour of crowns, veneers, or fillings. We'll assess your smile and recommend the best option at your consultation.</p>

<p>📞 Ready for a brighter smile? <a href="tel:714-874-8579">Call us at 714-874-8579</a> or explore our <a href="https://bristol-dental.com/services/cosmetic-dentistry/">cosmetic dentistry services</a>.</p>"""
    },
    {
        "title": "What Is Periodontal Disease — and How Do We Treat It?",
        "content": """<p>Gum disease is one of the most common oral health conditions in the United States — and one of the most underdiagnosed. At Bristol Dental &amp; Orthodontics in Santa Ana, CA, we help patients understand, prevent, and treat periodontal disease at every stage.</p>

<h2>What Is Periodontal Disease?</h2>
<p>Periodontal disease (gum disease) is an infection of the gums and the bone that supports your teeth. It starts as gingivitis — mild inflammation caused by plaque buildup — and can progress to periodontitis if left untreated, which can lead to tooth loss.</p>

<h2>Warning Signs to Watch For:</h2>
<ul>
<li>Gums that bleed when you brush or floss</li>
<li>Red, swollen, or tender gums</li>
<li>Persistent bad breath</li>
<li>Gums pulling away from your teeth</li>
<li>Loose or shifting teeth</li>
</ul>

<h2>How We Treat Gum Disease</h2>
<p>Early-stage gum disease can often be reversed with a professional deep cleaning (scaling and root planing) combined with improved at-home care. More advanced cases may require additional treatment or referral to a periodontist.</p>

<p>The good news: caught early, gum disease is very manageable. Regular checkups at our Santa Ana office are the best prevention.</p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> or learn more about <a href="https://bristol-dental.com/services/periodontal-disease-treatment/">periodontal treatment at Bristol Dental</a>.</p>"""
    },
    {
        "title": "Emergency Dentist in Santa Ana — What to Do When Dental Pain Strikes",
        "content": """<p>Dental emergencies don't wait for a convenient moment. Whether it's a sudden toothache, a knocked-out tooth, or a broken crown, knowing what to do — and where to go — can make all the difference. Bristol Dental &amp; Orthodontics in Santa Ana, CA offers same-day emergency dental care for patients throughout Orange County.</p>

<h2>Common Dental Emergencies We Treat:</h2>
<ul>
<li><strong>Severe toothache</strong> — Pain that doesn't go away is a sign something is wrong. Don't wait.</li>
<li><strong>Knocked-out tooth</strong> — Keep the tooth moist (in milk or saliva) and get to us within an hour for the best chance of saving it.</li>
<li><strong>Cracked or broken tooth</strong> — Rinse your mouth with warm water and call us immediately.</li>
<li><strong>Lost crown or filling</strong> — Cover the exposed area with dental cement from a pharmacy and call us right away.</li>
<li><strong>Abscess or swelling</strong> — A dental abscess is a serious infection that needs immediate attention.</li>
</ul>

<h2>What to Do First</h2>
<p>Call our Santa Ana office as soon as possible. We keep time in our schedule for emergency patients and will do everything we can to see you the same day.</p>

<p>📞 <strong>Call us now: <a href="tel:714-874-8579">714-874-8579</a></strong> — or learn more about <a href="https://bristol-dental.com/services/emergency-dentistry/">emergency dentistry at Bristol Dental</a>.</p>"""
    },
    {
        "title": "Family Dentistry in Santa Ana: Care for Every Age",
        "content": """<p>Finding a dental home for your whole family — from toddlers to grandparents — makes dental care simpler, more consistent, and a lot less stressful. At Bristol Dental &amp; Orthodontics in Santa Ana, CA, we welcome patients of all ages and pride ourselves on creating a warm, comfortable experience for every member of your family.</p>

<h2>Why Choose a Family Dentist?</h2>
<p>A family dentist builds a long-term relationship with your household. We get to know your family's dental history, track changes over time, and provide continuity of care that a specialist-only practice can't offer.</p>

<h2>What We Offer for Every Stage of Life:</h2>
<ul>
<li><strong>Children</strong> — Gentle first visits, sealants, fluoride treatments, and cavity prevention education</li>
<li><strong>Teens</strong> — Orthodontic consultations, wisdom tooth monitoring, sports mouthguards</li>
<li><strong>Adults</strong> — Routine cleanings, cosmetic treatments, Invisalign, implants</li>
<li><strong>Seniors</strong> — Dentures, implants, dry mouth management, and periodontal care</li>
</ul>

<h2>Conveniently Located in Santa Ana</h2>
<p>We're located at 2835 S Bristol St, Suite A, Santa Ana, CA — easy to reach for families across Orange County.</p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> to book appointments for the whole family, or explore our <a href="https://bristol-dental.com/services/family-dentistry/">family dentistry services</a>.</p>"""
    },
    {
        "title": "The Truth About Wisdom Teeth: Do They Always Need to Come Out?",
        "content": """<p>Wisdom teeth — the third molars that typically emerge in your late teens or early twenties — are one of the most common reasons people visit an oral surgeon or dentist. But do they always need to be removed? At Bristol Dental &amp; Orthodontics in Santa Ana, we get this question a lot.</p>

<h2>Not Always — But Often Yes</h2>
<p>Some people's wisdom teeth come in perfectly straight and cause no problems at all. But for most people, the jaw doesn't have enough room to accommodate them, which leads to:</p>

<ul>
<li><strong>Impaction</strong> — The tooth gets stuck below the gum line or grows at an angle</li>
<li><strong>Crowding</strong> — Wisdom teeth push against neighboring teeth and shift your smile</li>
<li><strong>Infection</strong> — Partially erupted wisdom teeth are hard to clean and are prone to gum infection</li>
<li><strong>Cysts</strong> — In rare cases, fluid-filled sacs can form around impacted teeth and damage surrounding bone</li>
</ul>

<h2>How Do You Know If Yours Need to Come Out?</h2>
<p>X-rays at your regular dental checkup are the best way to monitor wisdom teeth. Dr. Finley will track their development and advise you before problems arise — ideally before symptoms start.</p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> or learn more about <a href="https://bristol-dental.com/services/wisdom-teeth-extractions/">wisdom tooth extractions at Bristol Dental</a> in Santa Ana.</p>"""
    },
    {
        "title": "What Is Sedation Dentistry — and Is It Right for You?",
        "content": """<p>Dental anxiety is more common than you might think. Millions of Americans avoid the dentist due to fear or anxiety — and that avoidance can lead to serious oral health problems over time. At Bristol Dental &amp; Orthodontics in Santa Ana, CA, sedation dentistry helps patients get the care they need in a calm, comfortable way.</p>

<h2>What Is Sedation Dentistry?</h2>
<p>Sedation dentistry uses medication to help patients relax during dental procedures. It ranges from mild relaxation to deeper sedation depending on the patient's needs.</p>

<h2>Types of Sedation We Offer:</h2>
<ul>
<li><strong>Nitrous oxide (laughing gas)</strong> — Mild and fast-acting, wears off quickly so you can drive home afterward</li>
<li><strong>Oral sedation</strong> — A pill taken before your appointment that leaves you deeply relaxed but awake</li>
<li><strong>IV sedation</strong> — Administered directly into the bloodstream for deeper sedation during longer procedures</li>
</ul>

<h2>Who Is Sedation Dentistry For?</h2>
<ul>
<li>Patients with dental anxiety or phobia</li>
<li>Those with a strong gag reflex</li>
<li>Patients who need multiple procedures in one visit</li>
<li>People with sensitivity to dental sounds or smells</li>
</ul>

<p>You deserve to feel comfortable in the dental chair. Let's talk about your options.</p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> or visit our <a href="https://bristol-dental.com/services/sedation-dentistry/">sedation dentistry page</a> to learn more.</p>"""
    },
    {
        "title": "Sleep Apnea and Your Dentist: How Oral Appliances Can Help",
        "content": """<p>Did you know your dentist can help treat sleep apnea? Many people are surprised to learn that Bristol Dental &amp; Orthodontics in Santa Ana, CA offers sleep apnea treatment — and for some patients, it's a life-changing alternative to a CPAP machine.</p>

<h2>What Is Sleep Apnea?</h2>
<p>Sleep apnea is a condition where breathing repeatedly stops and starts during sleep. The most common type — obstructive sleep apnea — happens when the throat muscles relax and block the airway. It causes loud snoring, gasping during sleep, and daytime fatigue.</p>

<h2>How Can a Dentist Help?</h2>
<p>For mild to moderate sleep apnea, a custom oral appliance (also called a mandibular advancement device) can be highly effective. It fits like a mouthguard and gently repositions the jaw to keep the airway open during sleep.</p>

<h2>Benefits of Oral Appliance Therapy:</h2>
<ul>
<li>Small and portable — great for travel</li>
<li>Quiet — no machine noise</li>
<li>Easy to wear and maintain</li>
<li>Often covered by medical insurance</li>
</ul>

<p>If you've been told you snore or have been diagnosed with sleep apnea, talk to Dr. Finley about whether an oral appliance might be right for you.</p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> or explore our <a href="https://bristol-dental.com/services/sleep-apnea-treatment/">sleep apnea treatment options</a>.</p>"""
    },
    {
        "title": "Restorative Dentistry in Santa Ana: Crowns, Bridges, and More",
        "content": """<p>A damaged or missing tooth doesn't have to be permanent. At Bristol Dental &amp; Orthodontics in Santa Ana, CA, our restorative dentistry services are designed to bring your smile back to full health — both in function and appearance.</p>

<h2>What Is Restorative Dentistry?</h2>
<p>Restorative dentistry covers any treatment that repairs or replaces damaged, decayed, or missing teeth. The goal is to restore your ability to eat, speak, and smile comfortably.</p>

<h2>Common Restorative Treatments We Offer:</h2>
<ul>
<li><strong>Dental crowns</strong> — A cap placed over a damaged tooth to restore its shape, strength, and appearance</li>
<li><strong>Dental bridges</strong> — A fixed restoration that fills the gap left by one or more missing teeth</li>
<li><strong>Tooth-coloured fillings</strong> — Natural-looking composite resin used to repair cavities</li>
<li><strong>Dentures</strong> — Removable replacements for multiple missing teeth</li>
<li><strong>Dental implants</strong> — The gold standard for replacing missing teeth permanently</li>
</ul>

<h2>Why Restore Damaged Teeth?</h2>
<p>Leaving damaged or missing teeth untreated can lead to shifting teeth, bone loss, bite problems, and additional decay. Restorative treatment protects your long-term oral health.</p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> or visit our <a href="https://bristol-dental.com/services/restorative-dentistry/">restorative dentistry page</a> to learn what's right for you.</p>"""
    },
    {
        "title": "New Patient Special: $59 Exam & X-Ray at Bristol Dental, Santa Ana",
        "content": """<p>Looking for a new dentist in Santa Ana, CA? We'd love to welcome you to the Bristol Dental &amp; Orthodontics family — and we're making it easy to get started.</p>

<h2>New Patient Offer: $59 Exam &amp; X-Ray*</h2>
<p>New patients without insurance can take advantage of our special introductory offer: a comprehensive dental exam and full X-rays for just $59. It's our way of saying welcome, and making sure there's no barrier to getting the dental care you deserve.</p>

<h2>What's Included:</h2>
<ul>
<li>Full dental examination with Dr. Andrew Finley</li>
<li>Dental X-rays to assess your oral health</li>
<li>Personalised treatment plan if needed</li>
<li>A friendly, pressure-free experience</li>
</ul>

<h2>Why Choose Bristol Dental &amp; Orthodontics?</h2>
<p>We're a top-rated Santa Ana dental practice with 280+ five-star reviews. Dr. Finley and our team are committed to making every visit comfortable, clear, and tailored to your needs. We offer everything from routine cleanings to Invisalign, dental implants, and cosmetic dentistry — all under one roof.</p>

<p><em>*Offer for new patients without dental insurance only.</em></p>

<p>📞 <a href="tel:714-874-8579">Call 714-874-8579</a> or <a href="https://bristol-dental.com/exam-x-ray/">claim your $59 new patient offer today</a>.</p>"""
    },
]

# ============================================================
# WORDPRESS API FUNCTIONS
# ============================================================

def get_auth_header(username, app_password):
    """Generate Basic Auth header for WordPress REST API."""
    credentials = f"{username}:{app_password}"
    token = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    return f"Basic {token}"


def create_wp_post(title, content, status="draft"):
    """Create a post via the WordPress REST API."""
    url = f"{WP_SITE_URL}/wp-json/wp/v2/posts"

    payload = json.dumps({
        "title":   title,
        "content": content,
        "status":  status,
    }).encode("utf-8")

    headers = {
        "Authorization": get_auth_header(WP_USERNAME, WP_APP_PASSWORD),
        "Content-Type":  "application/json",
    }

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
            return {"success": True, "post_id": result.get("id"), "link": result.get("link")}
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        return {"success": False, "error": f"HTTP {e.code}: {error_body}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


# ============================================================
# MAIN
# ============================================================

def main():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s",
    )

    # Pick this week's post using ISO week number (rotates through all 12)
    week_number = datetime.date.today().isocalendar()[1]
    post_index  = (week_number - 1) % len(BLOG_POSTS)
    post        = BLOG_POSTS[post_index]

    logging.info(f"Week {week_number} — Posting: '{post['title']}'")
    print(f"Posting: {post['title']}")

    result = create_wp_post(
        title   = post["title"],
        content = post["content"],
        status  = POST_STATUS,
    )

    if result["success"]:
        msg = f"SUCCESS — Post ID {result['post_id']} created as '{POST_STATUS}'. URL: {result['link']}"
        logging.info(msg)
        print(msg)
    else:
        msg = f"FAILED — {result['error']}"
        logging.error(msg)
        print(msg)


if __name__ == "__main__":
    main()
