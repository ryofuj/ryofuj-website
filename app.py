from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Example dynamic data for tiles
    tiles = [
        {"size": "large", "content": "<h1 class='logo'>Maison</h1>"},
        {"size": "medium", "content": "<img src='https://via.placeholder.com/300' alt='Luxury Villa'><p class='subtext'>Discover exclusive villas with breathtaking views</p>"},
        {"size": "small", "content": "<p class='subtext'>Experience luxury living like never before</p>"},
        {"size": "medium", "content": "<p>Color Palette</p><div class='color-palette'><div class='color-swatch' style='background-color: #f4efe8;'></div><div class='color-swatch' style='background-color: #d7b99e;'></div><div class='color-swatch' style='background-color: #000;'></div><div class='color-swatch' style='background-color: #333;'></div></div>"},
        {"size": "small", "content": "<p>Download Our App</p><div class='cta'><a href='#'>Google Play</a><a href='#'>App Store</a></div>"},
        {"size": "large", "content": "<img src='https://via.placeholder.com/300' alt='Interior Design'>"},
        {"size": "small", "content": "<img src='https://via.placeholder.com/200' alt='Amenities'><p class='subtext'>World-class amenities</p>"},
        {"size": "small", "content": "<p>Exclusive Locations</p><p class='subtext'>Explore our properties around the globe</p>"},
        {"size": "medium", "content": "<img src='https://via.placeholder.com/400' alt='Luxury Interior'><p class='subtext'>Luxury Interiors that inspire</p>"},
        {"size": "small", "content": "<p>Contact Us</p><p class='subtext'>Reach out for personalized assistance</p>"},
        {"size": "small", "content": "<p>More Offers</p><p class='subtext'>Discover our seasonal promotions</p>"},
        {"size": "medium", "content": "<img src='https://via.placeholder.com/400' alt='Outdoor Spaces'><p class='subtext'>Beautiful outdoor spaces to enjoy</p>"},
        {"size": "small", "content": "<p>Membership</p><p class='subtext'>Join our exclusive member program</p>"}
    ]
    return render_template('index.html', tiles=tiles)

if __name__ == '__main__':
    app.run(debug=True)
