from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['travel_website']

# 1. Insert State
ap_state_doc = {"name": "Andhra Pradesh"}
ap_state_id = db.states.insert_one(ap_state_doc).inserted_id

jk_state_doc = {"name": "Jammu and Kashmir"}
jk_state_id = db.states.insert_one(jk_state_doc).inserted_id

up_state_doc = {"name": "Uttar Pradesh"}
up_state_id = db.states.insert_one(up_state_doc).inserted_id

rs_state_doc = {"name": "Rajasthan"}
rs_state_id = db.states.insert_one(rs_state_doc).inserted_id

kl_state_doc = {"name": "Kerala"}
kl_state_id = db.states.insert_one(kl_state_doc).inserted_id

as_state_doc = {"name": "Assam"}
as_state_id = db.states.insert_one(as_state_doc).inserted_id

ks_state_doc = {"name": "Karnataka"}
ks_state_id = db.states.insert_one(ks_state_doc).inserted_id

city_guwahati = {
    "state_id": as_state_id,
    "name": "Guwahati",
    "popular_places": [
        {
            "name": "Guwahati",
            "history": {
                "text": "Guwahati, Assam’s largest city on the Brahmaputra, traces its roots to ancient Kamarupa (4th–12th centuries), mentioned in the Mahabharata and Sanskrit texts with legends of Narakasura, Bhagadatta, and epic battles. It served as the capital for many dynasties; Dighalipukhuri and ancient temples reflect a legacy of culture and politics. During the medieval era, Pragjyotishpur was famous for scholarship, Tantrism, and the Kamakhya Temple; later, Guwahati was a fort for the Ahom rulers and British administrative HQ before it moved to Shillong.",
                "image": "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, aloo pitika, fish/duck curry, bamboo shoot, greens, pitha) at restaurants/markets; street snacks: puri sabzi, samosa, jalebi, bhaji, laru; fish tenga (tangy curry), duck/pigeon dishes; Assam black tea at roadside cafés.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Visit Kamakhya Temple, Ambubachi Mela (major pilgrimage event); tour Assam State Museum (art, archaeology, history); explore Srimanta Sankardev Kalakshetra, river cruises, evening markets; experience Bihu/Sattriya dance, folk music festivals, handloom/textile markets; day trips to Navagraha, Umananda, Basistha, ancient shrines.",
                    "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Bring cash—digital payments grow, but small shops/temples often cash-only."},
                {"tip": "Dress modestly for temples; remove footwear, cover shoulders/legs."},
                {"tip": "Drink bottled water; watch street food hygiene in markets."},
                {"tip": "Use registered guides for temples/museums/hill tours."},
                {"tip": "Stay alert in festival crowds; secure valuables."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Pobitora Wildlife Sanctuary (rhinos, birding, 48 km away); Majuli Island (river island, monasteries, crafts); Hajo (multi-faith pilgrimage site); Sualkuchi (silk weaving/muga saris); Chandubi Lake (lagoon, eco-tours, boating, birdwatching, picnics).",
                    "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_jorhat = {
    "state_id": as_state_id,
    "name": "Jorhat",
    "popular_places": [
        {
            "name": "Jorhat",
            "history": {
                "text": "Jorhat, famed as the 'Tea Capital of India' and the cultural center of Upper Assam, was the last Ahom Kingdom capital (ruled Assam for ~600 years, 1228–1826 AD). The capital moved here in 1794 by King Gaurinath Singha. Jorhat played a strategic role in the Moamoria rebellion, Burmese invasions (1817–24), and British colonial expansion. Landmarks like Raja Maidam (royal tomb), Garh Ali, and colonial buildings reflect its heritage. The 19th-century tea industry reshaped Jorhat into a key center for production, research, and trade.",
                "image": "https://images.unsplash.com/photo-1594736797933-d0300ee91e77?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, aloo pitika, fish curry, duck curry, bamboo shoot, greens) in city restaurants/tea estates; pitha, laru, payas at festivals/homestays; street snacks (samosa, puri sabzi, jalebi, fritters from markets); fresh Assam tea in garden cafes.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Tea garden/factory tours (harvesting, tea making); explore Raja Maidam, Garh Ali, colonial sites; visit Tocklai Tea Research Institute (world’s oldest/largest for tea science); attend cultural fests, music, Asam Sahitya Sabha events; boat trips to Majuli Island for monasteries, crafts, birdwatching.",
                    "image": "https://images.unsplash.com/photo-1594736797933-d0300ee91e77?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash for markets/eateries—digital payments growing, not universal."},
                {"tip": "Dress modest/comfortable for tours; monsoon—bring rain gear."},
                {"tip": "Confirm guide credentials for tea/river excursions."},
                {"tip": "Drink bottled water, check street food hygiene."},
                {"tip": "Guard from mosquitoes in tea gardens/riversides."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Majuli Island (largest river island—monasteries, crafts, sites); Sivasagar (Ahom temples, palaces); Gibbon Wildlife Sanctuary (India’s only gibbon preserve, forest walks); Dhekiakhowa Bornamghar (Vaishnavite prayer hall); Naga Hills (hiking, tribes, vistas).",
                    "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_kaziranga = {
    "state_id": as_state_id,
    "name": "Kaziranga National Park",
    "popular_places": [
        {
            "name": "Kaziranga Wildlife Sanctuary",
            "history": {
                "text": "Kaziranga National Park in Assam, spanning Golaghat and Nagaon districts, began conservation in 1904 after Baroness Mary Curzon’s famed rhino search. The area became Kaziranga Proposed Reserve Forest (1905), then expanded east to the Brahmaputra. Kaziranga Game Sanctuary (1916), Wildlife Sanctuary (1950), and official National Park (1974, 430 km²) followed. The park is home to two-thirds of the world’s one-horned rhinoceroses and became a UNESCO World Heritage Site in 1985. Today it is an Iconic Tourist Site of India and a designated Tiger Reserve.",
                "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, aloo pitika, fish curry, bamboo shoot, duck/chicken curry) at forest lodges/eco-resorts; pitha, laru, payas in homestays/festivals; street food (puri sabzi, samosa, jalebi, bhaji from stalls); black tea from regional estates.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Jeep/elephant safaris for wildlife—one-horned rhinoceros, elephants, swamp deer, tigers, buffalo; birdwatching (rare fishing eagle, pelican, storks); forest watchtowers, riverine walks, photo tours (sunrise/sunset); Kaziranga Orchid/Biodiversity Park, tea estate tours; music/dance/artisan crafts in villages.",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Best visit: Nov–Apr for safaris; area closes during monsoons/floods."},
                {"tip": "Book safaris early—use licensed operators/forest guides."},
                {"tip": "Carry cash for entry/snacks/shopping—digital payment limited."},
                {"tip": "Dress full-coverage, use insect repellent against mosquitoes."},
                {"tip": "Stay in vehicles/on marked trails; respect wildlife space."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Majuli Island (world’s largest river island—culture/biodiversity); Hoollongapar Gibbon Sanctuary (India’s only ape species); Nameri National Park (birding, rafting); Golaghat tea gardens (guided tours/tastings); Kakochang Waterfalls (scenic getaway near Bokakhat).",
                    "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}


city_kamakhya_temple = {
    "state_id": as_state_id,
    "name": "Kamakhya Temple",
    "popular_places": [
        {
            "name": "Kamakhya Temple",
            "history": {
                "text": "Kamakhya Temple, atop Nilachal Hill in Guwahati, Assam, is among India's oldest and most revered Shakti shrines. Said to mark where the womb of Goddess Sati fell, it is a chief Shakti Peetha and Tantric center. The sanctum holds a yoni-shaped stone, naturally moist from a spring, symbolizing the goddess's creative force. Origins trace to tribal/pre-Aryan roots, but today's temple was rebuilt by King Naranarayan of Koch dynasty (1555–1565 AD) after destruction by Kalapahar. Ahom kings, especially Rajeshwar Singha, expanded and restored structures, building the Natamandira. Its design fuses Nagara, Assamese, and Islamic styles.",
                "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, aloo pitika, fish curry, veg curries) from local eateries/temple kitchens; pitha (rice cakes), laru (sweet coconut balls), payas (rice pudding) at festivals; street snacks (puri sabzi, samosa, jalebi near steps); tea and simple dhaba meals.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Participate in Ambubachi Mela (June, goddess's menstruation, rituals/music/fair); guided temple chamber tours for carvings, relics, and sanctum; bhajan/folk music performances; visiting shrines for Shiva, Vishnu, Mahavidyas; shopping for ritual items and souvenirs in Nilachal Hill markets.",
                    "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly; remove shoes before entering the complex."},
                {"tip": "Carry cash—vendors/donation counters rarely accept cards."},
                {"tip": "Photography restricted in sanctum, allowed outside—ask permission."},
                {"tip": "During puja/festivals (Ambubachi) expect crowds—keep valuables secure."},
                {"tip": "Stay hydrated/use sun protection while touring hilly grounds."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Umananda Temple (Brahmaputra river island, Shiva shrine); Navagraha Temple (astrology-themed hill temple); Assam State Museum (heritage/artifacts); Pobitora Wildlife Sanctuary (rhinos, birding, eco-tours); Guwahati markets (textiles, crafts, food).",
                    "image": "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}
city_manas = {
    "state_id": as_state_id,
    "name": "Manas National Park",
    "popular_places": [
        {
            "name": "Manas National Park",
            "history": {
                "text": "Manas National Park, at the Himalayan foothills on the Assam-Bhutan border, named for the Manas River (Brahmaputra tributary), was once a royal hunting preserve for Cooch Behar and Gauripur kings. Post-Duar War (1865), it became British territory and was set up as a sanctuary in 1928. Named a Tiger Reserve (1973) and UNESCO World Heritage Site (1985), Manas covers 500 sq km today. Despite decades of conflict and poaching (1980s–2003), conservation revived wildlife—especially rhinos—earning global praise. It is also a Biosphere and Elephant Reserve.",
                "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, aloo pitika, fish/poultry/bamboo shoot/wild greens) at park lodges/villages; pitha, laru, payas in homestays; street snacks: samosa, puri sabzi, jalebi, Assam black tea.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Wildlife safaris (jeep/elephant)—Bengal tiger, rhino, wild buffalo, golden langur, pygmy hog, hispid hare, clouded leopard; birdwatching (450+ species: Bengal florican, hornbill, black-necked stork); landscape photography; village walks/cultural exchanges with Bodo communities; forest watchtowers, river picnics, butterfly walks.",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Visit Nov–April; park closed in monsoon."},
                {"tip": "Carry cash—digital payments limited rural."},
                {"tip": "Dress earth-toned/full-sleeved for safaris; use insect repellent."},
                {"tip": "Stay in vehicles/guided safaris—do not enter forest alone."},
                {"tip": "Book safaris early with registered operators."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Bhutan’s Royal Manas National Park (cross-border wildlife); Barpeta (Satras, monasteries); Hajo (pilgrimage site for Hindus/Buddhists/Muslims); Pobitora Sanctuary (rhinos, near Guwahati); Bodo villages (culture, crafts).",
                    "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_haflong = {
    "state_id": as_state_id,
    "name": "Haflong",
    "popular_places": [
        {
            "name": "Haflong",
            "history": {
                "text": "Haflong, Assam’s only hill station, is in Dima Hasao district and was once the capital of the Dimacha (Dimasa) Kingdom before joining Assam post-independence. The name ‘Haflong’ means ‘ant hill’ in Dimasa, reflecting deep tribal ties to the land. The region includes Maibong—capital of the Kachari kingdom (16th–18th centuries)—its ruins echoing royal legacy and resilience. Haflong is famed for scenic hills, vibrant festivals, and sustainable tourism blending indigenous and colonial influences.",
                "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Dimasa dishes: namsu (fermented fish), smoked pork/chicken with bamboo shoot, khar-based delicacies; Judima (rice wine, copper bowl); tribal foods: silkworm chutney, weaver ants, forest greens; Assamese cuisine (rice meals, Laksa, khar); pitha/sweets at festivals; Assam tea daily.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Trekking/nature walks—Haflong Lake, Hatisor/Jatinga waterfalls; visiting tribal villages for textiles, handicrafts, festival immersion; birdwatching in Jatinga (famed bird phenomena); exploring Maibong ruins (Ramchandi Temple, stone houses); paragliding/camping/adventure sports in hills; sampling local food and Judima in markets.",
                    "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—digital payments rare in rural hill areas."},
                {"tip": "Dress light/modest; bring warm layers for evenings/mornings."},
                {"tip": "Use mosquito repellent for hikes; bottled water is safest."},
                {"tip": "Hire local guides for villages/adventure and tribal custom insight."},
                {"tip": "Roads are slow—book lodgings early (busy festival seasons)."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Maibong (Kachari ruins, Ramchandi, stones); Jatinga (bird mystery, waterfalls); Umrangso (hydro power station, reservoirs); Silchar (Barak Valley gateway); Panimoor Waterfalls (majestic falls, Dima Hasao).",
                    "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_tezpur = {
    "state_id": as_state_id,
    "name": "Tezpur",
    "popular_places": [
        {
            "name": "Tezpur",
            "history": {
                "text": "Tezpur, known as the 'City of Blood,' dates to ancient legend—the epic love story of Usha and Aniruddha led to a war between Banasura and Krishna, giving Tezpur its name. Archaeological finds point to settlements from the 4th century, with ruins mostly from the 9th–12th centuries (notably at Bamuni Hills). The Asura dynasty ruled Tezpur historically; later, Ahoms and the British arrived. The city’s monuments, like Da Parbatia’s Gupta-era doorway, Mahabhairab Temple, and Hazara Pukhuri tank, echo its rich heritage as Assam’s cultural hub.",
                "image": "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, aloo pitika, fish/bamboo shoot/local greens) in restaurants/family kitchens; pitha, laru, payas at festivals; samosa, puri sabzi, jalebi, bhaji stalls; Assamese black tea at cafés/tea estates.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Tour Agnigarh Hill (sculptures, views, Usha-Aniruddha legend); explore Bamuni Hills/Da Parbatia (sculptural ruins, architecture); visit Mahabhairab Temple (Shiva shrine); relax/boat at Cole Park (Chitralekha Udyan, artifacts); outings at Padum Pukhuri/Hazara Pukhuri lakes; museums: District, Jyoti Bharti.",
                    "image": "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—digital payment not standard at small shops/sites."},
                {"tip": "Dress light/modest for temples/parks; humid climate."},
                {"tip": "Drink bottled water; check hygiene for street food."},
                {"tip": "Guard valuables in crowds/festivals."},
                {"tip": "Respect norms: shoes off in temples, ask before photos in heritage sites."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Bura-Chapori Wildlife Sanctuary (birding, wildlife tours); Nameri National Park (rafting, birds, elephants); Kaziranga National Park (rhino safaris, ~2 hours away); Haleswar Temple (historic Shiva, 10km north); Silghat (Kolia Bhomora Setu bridge, Nagaon link).",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_majuli = {
    "state_id": as_state_id,
    "name": "Majuli Island",
    "popular_places": [
        {
            "name": "Majuli",
            "history": {
                "text": "Majuli, the world’s largest inhabited river island, lies in the Brahmaputra River (Assam), formed over centuries by earthquakes, floods, and shifting channels. In the 16th century, Neo-Vaishnavite reformer Srimanta Sankardev founded satras for the spread of Vaishnavite art, culture, and spirituality—making Majuli a cultural hub. Important during Ahom rule, the Moamoria rebellion, and under the British, it’s now India’s first river island district (since 2016). Majuli’s inhabitants (Mishing, Deori, Sonowal Kachari) live in bamboo houses adapted to a waterbound landscape.",
                "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, aloo pitika, fish/duck curry, bamboo shoots); pitha, laru, payas at homestays/festivals; fresh fish, local greens, Mishing ethnic dishes (apong rice beer); puri sabzi, samosa, jalebi from market stalls; Assam tea at tea shops.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Visit historic satras (Auniati, Kamalabari, Dakhinpat) for Sattriya dance, mask making, music, ritual; attend Raas Mahotsav festival; explore tribal villages, bamboo houses, handloom weaving; birdwatching (migratory/Siberian birds); cycling, ferry rides, walking wetlands/beels/paddy fields.",
                    "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Best visit: Nov–March; avoid monsoon (floods, erosion)."},
                {"tip": "Main access by ferry from Jorhat—verify schedules."},
                {"tip": "Carry cash—digital payments rare."},
                {"tip": "Respect satra/village customs (shoes off, modest dress)."},
                {"tip": "Use bottled water; consult homestays about food/safety."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Jorhat (tea capital, Tocklai research); Sivasagar (Ahom city, monuments, temples, tanks); Gibbon Wildlife Sanctuary (forest, wildlife); Dhekiakhowa Bornamghar (Vaishnavite monastery); Nimati Ghat (ferry market, Assam mainland link).",
                    "image": "https://images.unsplash.com/photo-1594736797933-d0300ee91e77?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_sualkuchi = {
    "state_id": as_state_id,
    "name": "Sualkuchi",
    "popular_places": [
        {
            "name": "Sualkuchi",
            "history": {
                "text": "Sualkuchi, the 'Manchester of the East,' is a historic silk-weaving village on the Brahmaputra, about 30–35 km from Guwahati. Its roots trace to Suvarnakudya (Arthashastra, 4th c. BCE) and Pala king Dharma Pal, who settled weaving families here in the 10th–11th centuries. Under the Ahoms in the 17th century, it became Assam’s weaving center. Silk weaving—Muga, Eri, Pat—flourished, and WWII expansion made Sualkuchi the heart of Assam’s textile tradition. Nearly every home now has a loom, with craftspeople from many districts.",
                "image": "https://images.unsplash.com/photo-1594736797933-d0300ee91e77?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, fish curry, aloo pitika, bamboo shoots, local veg) in village kitchens; pitha, laru, payas at festivals; puri sabzi, samosa, chai from stalls; meals and black tea with weaving families.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Walk lanes to see traditional looms/weaving (Muga, Eri, Pat silk); tour workshops, try weaving, learn about dye/motifs; shop for Mekhela Chadar, sarees, scarf, textiles direct from weavers; photograph village, market, and festival scenes; attend Bihu and weaving festivals (music, crafts).",
                    "image": "https://images.unsplash.com/photo-1594736797933-d0300ee91e77?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—few shops/looms take cards."},
                {"tip": "Wear light/clothing with covered shoulders for village/shops."},
                {"tip": "Ask to photograph artisans in workshops."},
                {"tip": "Drink bottled water, check food hygiene for home/market stalls."},
                {"tip": "Lanes are narrow and humid—bring hats/hydration."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Guwahati (Kamakhya Temple, markets, cruises); Hajo (multi-faith pilgrimage site); Pobitora Wildlife Sanctuary (rhinos, birds); Chandubi Lake (eco-tours, boating, picnics); Bijoynagar (crafts, river scenery).",
                    "image": "https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_tinsukia = {
    "state_id": as_state_id,
    "name": "Tinsukia",
    "hidden_gem_places": [
        {
            "name": "Tinsukia",
            "history": {
                "text": "Tinsukia, in Upper Assam, was formerly Bengmara—capital of the Matak Kingdom in the late 18th century under King Sarbananda Singha. The Muttock dynasty is known for sacred tanks; the heritage is visible in historic lakes and monuments. British rule increased Tinsukia’s importance—location on WWII Stilwell (Ledo) Road (to Myanmar/China), and became a tea industry hub. Today it’s Assam’s 'business capital,' with royal/colonial landmarks, bungalows, markets, and industrial sites.",
                "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, fish/duck curry, bamboo shoot, greens) at restaurants/markets; street snacks (samosa, puri sabzi, kachori, jalebi, chai at chowks); sweets: pitha, laru (coconut), payas (festivals, local bakeries); Assam tea from local estates.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Wildlife safaris at Dibru Saikhowa National Park (rare species, river dolphins, birds); heritage walks at Na-Pukhuri Park (historic ponds by Muttock kings); visit Tilinga Mandir (bell temple with thousands of bells); boating/photography at lakes; explore Bherjan-Borjan-Padumoni Wildlife Sanctuary; shop tea, handicrafts, produce at bustling markets.",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—small shops/parks may not accept digital payment."},
                {"tip": "Dress comfortable/modest for temples/nature sites."},
                {"tip": "Use bottled water/sun protection; humid summers, pleasant winters."},
                {"tip": "Book wildlife tours/safaris with licensed operators."},
                {"tip": "Follow rules for parks/heritage sites; respect local customs."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Digboi (oldest oil refinery, WWII cemetery, bungalows); Sadiya (Chutia Kingdom historic capital); Ledo (Stilwell Road, coalfields, WWII memorial); Margherita ('Coal Queen', museums, Arunachali cuisine); Dehing Patkai Wildlife Sanctuary (eco-tourism, jungle walks).",
                    "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}
city_pabitora = {
    "state_id": as_state_id,
    "name": "Pabitora Wildlife Sanctuary",
    "hidden_gem_places": [
        {
            "name": "Pabitora Wildlife Sanctuary",
            "history": {
                "text": "Pabitora Wildlife Sanctuary (Morigaon, Assam), also called Pobitora, is a marshland on the Brahmaputra’s southern bank, ~30 km from Guwahati. Once a village-protected swamp, it became a reserved forest in 1971 after rhino sightings, then a wildlife sanctuary in 1987 (38.81 km²). Known as 'Mini Kaziranga,' it hosts the world’s highest Indian one-horned rhino density; it’s an Important Bird Area with thousands of migratory birds, 22 mammals, 27 reptiles, and 80 butterflies.",
                "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, fish/bamboo shoot/local veg) at nearby dhabas; pitha, laru, payas from village homes/festivals; street snacks—samosa, puri sabzi, jalebi near sanctuary; Assam black tea.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Jeep/elephant safaris to see one-horned rhinos and megafauna; birdwatching (200+ resident/migratory species); wildlife/floodplain photography; village walks (Mayong ethnic communities); explore hillocks; join cultural/awareness programs at festival time.",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—rural shops/entry mostly cash-only."},
                {"tip": "Wear sturdy shoes/full sleeves—marshland can be slippery."},
                {"tip": "Don’t leave safari vehicles; obey guides."},
                {"tip": "Respect wildlife—keep distance from rhinos/buffaloes."},
                {"tip": "Drink bottled water; check stall/dhaba hygiene before eating."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Guwahati (Kamakhya Temple, Brahmaputra cruises); Mayong (magic heritage, village culture); Hajo (temple/mosque/Buddhist pilgrimage site); Chandubi Lake (eco-tours, boating, birdwatching); Manas & Kaziranga National Parks (UNESCO wildlife areas in Assam).",
                    "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}
city_digboi = {
    "state_id": as_state_id,
    "name": "Digboi",
    "hidden_gem_places": [
        {
            "name": "Digboi",
            "history": {
                "text": "Digboi (Tinsukia, Upper Assam), the 'Oil City of Assam,' is famed as India’s oil industry birthplace. British engineers yelled 'dig, boy, dig' when searching for oil in the 19th century, giving Digboi its name. Oil was found in the late 1860s, and Asia's first oil refinery opened here in 1901, still the world’s oldest functional refinery. Colonial bungalows, tea gardens, and clubs lend Digboi a rich industrial heritage.",
                "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali—rice, dal, aloo pitika, fish curry, greens, bamboo shoots at restaurants/homestays; street snacks—samosa, kachori, puri sabzi, jalebi, masala chai from markets; Arunachali tribal dishes (Gahori with Lai Hak) in Margherita; Assam tea, pitha, laru, payas (sweets).",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Guided tours of Digboi Oil Refinery and Museum (Asia’s oil history, engineering); visit Digboi War Cemetery (WWII history, memorials); historic golf on the 18-hole estate course; heritage walks among Victorian bungalows and Centenary Environment Park; nearby tea gardens, biodiversity park (birdwatching, nature trails).",
                    "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—digital payments less common."},
                {"tip": "Dress comfortable/modest for tours, walks, parks."},
                {"tip": "Book transport/lodgings early—busy in peak seasons."},
                {"tip": "Respect etiquette at cemetery/refinery—check photo rules."},
                {"tip": "Use bottled water, check hygiene for market street food."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Dibru Saikhowa National Park (wildlife, birding, ~25–30km away); Margherita (coal museum, Arunachali cuisine); Powai Tea Estate (garden tours, bungalow stays); Ridge Point (panoramic overlook); Dhola-Sadiya Bridge (India’s longest; gateway to Arunachal Pradesh).",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_panimur = {
    "state_id": as_state_id,
    "name": "Panimur Waterfalls",
    "hidden_gem_places": [
        {
            "name": "Panimur Waterfalls",
            "history": {
                "text": "Panimur Waterfalls, known as the 'Niagara of Northeast,' is a spectacular natural attraction in Dima Hasao district, Assam, formed by the Kopili River plunging over rocky terrain. Set in the Barail range, ~120 km from Haflong, Panimur has been a revered Dimasa tribal pilgrimage site since the Dimasa kingdom era. Annual rituals and holy baths are held during Maghi Purnima, with prayers for peace and well-being. The site is culturally connected to regional legends and tribal traditions.",
                "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, fish/chicken curry, bamboo shoots, greens) from village eateries; tribal snacks: pitha, laru, roasted meats, wild honey; masala chai/simple meals at dhabas; spicy chutneys, smoked pork, seasonal fruit.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Sightseeing, picnicking, photography at waterfalls/turquoise pools (post-monsoon/winter best); adventure: river crossing, rafting, rappelling, night trekking; hiking rocky trails, sunset views over cascades; engage with Dimasa culture through festivals/stories/rituals; fishing in natural pools, forest camping.",
                    "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Wear sturdy, non-slip shoes; carry extra clothes—area very wet/rocky."},
                {"tip": "Carry cash—remote villages/camps don't accept digital payment."},
                {"tip": "Don't swim in fast streams/climb wet rocks; extra care with children."},
                {"tip": "Don't litter; respect tribal customs/holy sites."},
                {"tip": "Use sunscreen, hats, insect protection for humidity."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Haflong (Assam's hill station—trekking, camping, lake); Maibong (ruins, Ramchandi temple, Mahur river); Jatinga (bird mystery, birdwatching); Umrangso (hydroelectric project, tea gardens, herbal trails); Diphu Hills (Karbi Anglong scenic hills, district capital).",
                    "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}


city_dibru_saikhowa = {
    "state_id": as_state_id,
    "name": "Dibru Saikhowa",
    "hidden_gem_places": [
        {
            "name": "Dibru Saikhowa National Park",
            "history": {
                "text": "Dibru Saikhowa National Park (Dibrugarh/Tinsukia, Assam) began as Dibru Reserved Forest (1890), expanded through the 20th century, joined with Saikhowa Reserved Forest (1929), became a wildlife sanctuary (1986), and a biosphere reserve (1997, 765km²; core 340km²). Declared a national park in 1999, these floodplains are protected for rare/endangered species, especially the white-winged wood duck. The park is famous for salix swamp forests, grasslands, and rich biodiversity.",
                "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali: rice, dal, fish curry, bamboo shoot, duck/chicken, local veg at eco lodges/markets; pitha, laru, payas in homestays/festivals; street snacks—puri sabzi, samosa, jalebi near park; locally brewed tea/wild honey from villages.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Wildlife safaris: search for white-winged wood duck, Bengal tiger, clouded leopard, gangetic dolphin, wild buffalo, capped langur, hoolock gibbon, feral horses; birdwatching—400+ species (adjutant stork, pelican, parrotbill, babbler); boat cruises, forest walks among floodplains/river islands/swamps; wetland/wild horse photography; engage with indigenous Mishing, Deori, Sonowal Kachari crafts/culture.",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Best visit: Nov–Apr; park prone to flooding/closure in monsoon."},
                {"tip": "Carry cash (entry, guides, food, crafts)—digital payments rare."},
                {"tip": "Wear full sleeves/earth-tones; use mosquito repellent for safaris/walks."},
                {"tip": "Travel with licensed guides—do not enter restricted/sensitive zones alone."},
                {"tip": "Drink bottled water/check food hygiene in stalls/homestays."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Dibrugarh (tea estates, city markets); Tinsukia (gateway town—heritage, crafts); Maguri Beel (birding/wetlands, near park); Sadiya (historic trading outpost, Brahmaputra's eastern edge); Jeypore Rainforest (Dehing Patkai—wild elephants, biodiversity).",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_kasi = {
    "state_id": up_state_id,
    "name": "Varanasi (Kasi)",
    "popular_places": [
        {
            "name": "Varanasi (Kasi/Benares)",
            "history": {
                "text": "Varanasi—Kasi/Benares—is among the world's oldest cities, existing over 3,000 years. A spiritual and cultural hub since Vedic times, it endured destruction and revival through Mughal, Maratha, and British eras. The city is sacred to Shiva and remains a magnet for pilgrims seeking salvation at its ghats and Kashi Vishwanath Temple.",
                "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Kachori sabzi, jalebi, Banarasi paan, lassi, thandai, chaat (tamatar chaat, dahi-puri), samosa, malaiyo, launglata, rabri, peda.",
                    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Attend evening Ganga Aarti at Dashashwamedh Ghat, sunrise boat rides, explore Kashi Vishwanath and other temples, visit saree/textile markets, wall art walks, and tour Sarnath and heritage museums.",
                    "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly, especially at temples and ghats; often remove footwear."},
                {"tip": "Crowded places: watch valuables and avoid touts/false guides."},
                {"tip": "Use bottled or filtered water; be wary about street food hygiene."},
                {"tip": "Carry cash for small purchases; digital acceptance variable in the old city."},
                {"tip": "Respect religious practices—ask before taking photos at temples, rituals, or ghats."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Sarnath (Buddhist site), Ramnagar Fort (vintage, royal palace), Bharat Kala Bhavan (BHU art museum), Tulsi Manas Temple, Durga Kund, weavers’ villages for silk brocade and crafts.",
                    "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_taj_mahal = {
    "state_id": up_state_id,
    "name": "Agra (Taj Mahal)",
    "popular_places": [
        {
            "name": "Taj Mahal",
            "history": {
                "text": "The Taj Mahal in Agra, commissioned by Mughal Emperor Shah Jahan in memory of Mumtaz Mahal, was built 1632–1653 by 20,000 artisans led by chief architect Ustad Ahmad Lahauri. Its famous white marble mausoleum, gardens, and the celestial symbolism within the complex reflect the peak of Mughal art and devotion, earning UNESCO status in 1983.",
                "image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Mughlai dishes (biryani, kebabs, Mughlai parathas), Agra petha, bedai & jalebi, dalmoth snack, tandoori chai, and street savories near the Taj and in Agra markets.",
                    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Guided tours of the mausoleum and mosque, watch marble inlay/color changes, photography of inlay/calligraphy, stroll Mughal gardens and reflection pools, visit Agra Fort, Mehtab Bagh, and crafts markets.",
                    "image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Buy official tickets only—avoid touts and unauthorized guides."},
                {"tip": "Dress modestly and follow decorum; photography restricted in some areas."},
                {"tip": "Carry cash for food/souvenirs; digital payments may be limited."},
                {"tip": "Entry is closed after sunset—visit early to avoid crowds."},
                {"tip": "Use hydration and sun protection due to Agra's heat."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Agra Fort (UNESCO), Mehtab Bagh (rear view), Tomb of Itimad-ud-Daulah ('Baby Taj'), Fatehpur Sikri (grand Mughal capital), Sikandra (Akbar’s tomb).",
                    "image": "https://images.unsplash.com/photo-1598977123668-b4deb4ff0ec1?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_mathura = {
    "state_id": up_state_id,
    "name": "Mathura",
    "popular_places": [
        {
            "name": "Mathura",
            "history": {
                "text": "Mathura, over 2,500 years old, is renowned as the birthplace of Krishna and was the Surasena capital. Referenced in epics and ancient Buddhist, Jain, and Hindu texts, it flourished under Maurya, Kushan, and Gupta rulers, endured temple destruction and revivals, and remains a top Krishna pilgrimage center today.",
                "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Kachori-sabzi, lassi, handi-thandai, Mathura peda, rabri, vegetarian thalis and simple North Indian fare.",
                    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Visit Krishna Janmabhoomi temple, attend aarti at Vishram Ghat, explore Government Museum, experience Holi and Janmashtami festivals, take day trips to Vrindavan, Barsana, Gokul.",
                    "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Dress conservatively for temples; remove shoes as required."},
                {"tip": "Drink only bottled water."},
                {"tip": "Carry cash for shops, donations, and purchases."},
                {"tip": "Watch out for touts—fix guide rates beforehand."},
                {"tip": "Respect photo restrictions for rituals and cremation ghats."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Vrindavan (major Krishna temples/ashrams), Barsana (Holi, Radha temples), Govardhan Hill (parikrama), Gokul (Krishna childhood legends), Kusum Sarovar & Radha Kund (pilgrimage ponds, temples).",
                    "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_sarnath = {
    "state_id": up_state_id,
    "name": "Sarnath",
    "popular_places": [
        {
            "name": "Sarnath",
            "history": {
                "text": "Sarnath, 10 km from Varanasi, is where Gautama Buddha gave his first sermon after enlightenment around 528 BCE, outlining the Four Noble Truths and Eightfold Path. Marked by Ashoka’s lion-capital pillar and monumental stupas, it remains a top Buddhist pilgrimage site and archaeological landmark.",
                "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "North Indian/UP specialties (kachori-sabzi, lassi, samosa, chaat), vegetarian meals (dal, rice, sabzi) in monasteries, fresh fruit and sweets (peda, rabri), and Buddhist cuisines (momos, noodle soups).",
                    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Explore Dhamek/Chaukhandi Stupa, Ashokan pillars, Sarnath Archaeological Museum, meditate in Deer Park, join teachings at Mulagandhakuti Vihara, visit international Buddhist/Jain temples.",
                    "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly at sites/shrines; footwear may be restricted in temples."},
                {"tip": "Carry cash for market and entry fees."},
                {"tip": "Respect photo rules in museums/temples."},
                {"tip": "Drink only bottled/filtered water; be cautious about food hygiene."},
                {"tip": "Sarnath is quieter than Varanasi but watch belongings at festivals/busy sites."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Varanasi (ghats, Kashi Vishwanath Temple), Ramnagar Fort, Bharat Mata Temple, Chunar Fort, Kaushambi (Buddhist site).",
                    "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_fatehpur_sikri = {
    "state_id": up_state_id,
    "name": "Fatehpur Sikri",
    "popular_places": [
        {
            "name": "Fatehpur Sikri",
            "history": {
                "text": "Fatehpur Sikri was built as Akbar’s imperial capital from 1571–85, inspired by Sufi saint Salim Chishti. It flourished as a center of Mughal administration and pluralistic dialogue, featuring syncretic architecture and impressive palaces, but was abandoned soon after—now a UNESCO World Heritage 'ghost city.'",
                "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Mughlai (seekh kebab, biryani, spicy curries), bedai and jalebi (breakfast), petha (sweet souvenir), dal moth, samosa, tandoori chai.",
                    "image": "https://images.unsplash.com/photo-1563379091339-03246963d511?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Guided tours of palaces (Jodha Bai Mahal), Diwan-i-Am/Khas, Panch Mahal, Jama Masjid, Buland Darwaza, Salim Chishti tomb, plus sunset photography and exploring red sandstone ruins.",
                    "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Visit Oct–March for best weather; summers are very hot."},
                {"tip": "Carry cash for tickets, snacks, crafts; digital/online payments may be limited."},
                {"tip": "Use only official guides; beware touts."},
                {"tip": "Dress modestly and remove shoes for mosque/shrine."},
                {"tip": "Respect photo restrictions inside the tomb and palace interiors."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Agra Fort, Taj Mahal, Itimad-ud-Daulah’s Tomb (Baby Taj), Bharatpur Bird Sanctuary, Jodha Bai Mahal, Hiran Minar.",
                    "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_ayodhya = {
    "state_id": up_state_id,
    "name": "Ayodhya",
    "popular_places": [
        {
            "name": "Ayodhya",
            "history": {
                "text": "Ayodhya on the Sarayu River is known as the birthplace of Lord Rama and was the ancient capital of Kosala. It appears in epics and Jain/Buddhist texts and was shaped by Maurya, Gupta, Mughal, and colonial eras. The Ram Mandir, consecrated in 2024, stands at the traditionally recognized spot of Rama’s birth.",
                "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Kachori sabzi, jalebi, lassi, thandai, Banarasi sweets (peda, rabri), samosa, chaat, breads, and prasadam from temples.",
                    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Visit Ram Janmabhoomi Temple, Hanuman Garhi, Kanak Bhawan; attend Diwali/Ram Navami festivals; walk along Sarayu ghats, see rituals and aarti, explore Guptar Ghat, Ramkot Fort, and enjoy temple performances.",
                    "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly and respectfully in religious areas; some temples require head covering."},
                {"tip": "Use bottled water; be careful with street food."},
                {"tip": "Carry cash; limited digital acceptance."},
                {"tip": "Watch belongings in crowds/markets."},
                {"tip": "Ask before photographing ceremonies/shrines."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Hanuman Garhi, Kanak Bhawan, Guptar Ghat, Ramkot Fort, Naya Ghat (all along Sarayu River, key for pilgrims/rituals).",
                    "image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_prayagraj = {
    "state_id": up_state_id,
    "name": "Prayagraj",
    "popular_places": [
        {
            "name": "Prayagraj (Allahabad)",
            "history": {
                "text": "Prayagraj, one of India’s oldest and holiest cities, sits at the Triveni Sangam and was renamed Allahabad by Akbar in 1583. Its Vedic, Mughal, and British past includes Akbar’s Fort, Anand Bhawan, All Saints Cathedral, and the world’s largest religious festival—the Kumbh Mela.",
                "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Kachori sabzi, lassi, thandai, chaat, samosa, jalebi, Allahabadi guava (fresh or in sweets), vegetarian thalis, peda, rabri.",
                    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Attend Ganga Aarti at Sangam, boat rides/bathing, explore Akbar’s Fort, Ashoka Pillar, Anand Bhawan museum, visit All Saints Cathedral, Jami Masjid, enjoy festivals (Kumbh, Magh Mela, Diwali), shop handicrafts and sweets.",
                    "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Dress conservatively at ghats, temples, mosques."},
                {"tip": "Drink bottled water; watch street food hygiene."},
                {"tip": "Carry cash for small purchases."},
                {"tip": "Watch belongings in crowds/pilgrimage areas."},
                {"tip": "Respect local customs and photography restrictions at rituals, temples, cremation sites."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Triveni Sangam (Kumbh), Anand Bhawan, All Saints Cathedral, Kaushambi (Buddhist ruins), Shringverpur (mythical village, river legends).",
                    "image": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_dudhwa_national_park = {
    "state_id": up_state_id,
    "name": "Dudhwa National Park",
    "popular_places": [
        {
            "name": "Dudhwa National Park",
            "history": {
                "text": "Dudhwa National Park in Lakhimpur Kheri near Nepal was created as a sanctuary in 1958, expanded to a national park in 1977 thanks to Billy Arjan Singh. Now part of Dudhwa Tiger Reserve, it protects Bengal tigers, rhinos, elephants, and swamp deer across grasslands, swamps, and dense forests.",
                "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Simple North Indian fare (dal, sabzi, chapati, rice) at lodges/camps, fresh market vegetables, wild honey, samosas/pakoras, tea, and sweets in local villages.",
                    "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Jeep and elephant safaris, bird watching (450+ species), nature walks, photography, visit endangered species sites and Tharu villages; scenic drives along rivers and marshes, Suheli barrage for waterbirds.",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Visit Nov–May; avoid monsoons for flooding/closed roads."},
                {"tip": "Carry cash—digital payment rare at gates/markets."},
                {"tip": "Obey park rules; no noise/litter; follow guide on wildlife."},
                {"tip": "Wear covered shoes/clothing—ticks/leeches in wet grass."},
                {"tip": "Respect Tharu customs; ask before photographing people/homes."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Kishanpur Sanctuary, Katarniaghat Sanctuary, Frog Temple (Oel), Suheli Barrage, Indo-Nepal border villages for cross-cultural birding.",
                    "image": "https://images.unsplash.com/photo-1564024840715-5c3c7d87eede?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_agra_fort = {
    "state_id": up_state_id,
    "name": "Agra Fort",
    "popular_places": [
        {
            "name": "Agra Fort",
            "history": {
                "text": "Agra Fort, a UNESCO World Heritage site on the Yamuna River, was built by Akbar from 1565–1573 over an older site and expanded by Jahangir, Shah Jahan, and Aurangzeb. It was the imperial Mughal residence until 1638 and features grand sandstone and marble palaces, halls, mosques, and gardens.",
                "image": "https://images.unsplash.com/photo-1598977123668-b4deb4ff0ec1?w=800&auto=format&fit=crop"
            },
            "localCuisine": [
                {
                    "name": "Mughlai (seekh kebab, biryani, tandoori naan), Agra petha, bedai and aloo sabzi, dalmoth, tandoori chai, jalebi from street stalls near the fort.",
                    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&auto=format&fit=crop"
                }
            ],
            "activities": [
                {
                    "name": "Take guided walks of the fort’s halls, mosques, and palaces; see the Taj Mahal from fort balconies; study Mughal architecture; explore Amar Singh and Delhi gates, in-fort gardens, and occasional light shows.",
                    "image": "https://images.unsplash.com/photo-1598977123668-b4deb4ff0ec1?w=800&auto=format&fit=crop"
                }
            ],
            "safetyTips": [
                {"tip": "Buy tickets only at official counters or online; beware touts and unofficial guides."},
                {"tip": "Dress modestly; wear shoes suitable for long walks/summer heat."},
                {"tip": "Carry cash for local snacks, shops; digital payment is limited."},
                {"tip": "Confirm photography permissions—mosque sections may restrict."},
                {"tip": "Evening visits are cooler and less crowded than midday."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Taj Mahal, Mehtab Bagh, Itimad-ud-Daulah’s Tomb (Baby Taj), Fatehpur Sikri, Jama Masjid Agra.",
                    "image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&auto=format&fit=crop"
                }
            ]
        }
    ]
}

city_lucknow = {
    "state_id": up_state_id,
    "name": "Lucknow",
    "popular_places": [
        {
            "name": "Lucknow",
            "history": {
                "text": "Lucknow, the capital of Uttar Pradesh, is famed for Awadhi culture, arts, cuisine, and its role as the Nawabi capital after the fall of the Mughal Empire. Known for its Mughal-Persian-British heritage, the city’s icons include Bara Imambara, Rumi Darwaza, and the British Residency, synonymous with 1857 rebellion history.",
                "image": "https://yourbucket.com/lucknow-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Awadhi biryani, Galouti/Tunday/Kakori kebabs, Nihari, basket chaat, samosa, chole bhature, kulfi, malai-makkhan, sweets from Chowk/Aminabad.",
                    "image": "https://yourbucket.com/galouti-kebab.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Heritage walks to Bara Imambara (Bhul Bhulaiya labyrinth), Chhota Imambara, Rumi Darwaza, British Residency, Hussainabad Clock Tower, shop for Chikankari, attend Kathak/music events, visit Kaiserbagh Palace, Safed Baradari, Sikandar Bagh gardens.",
                    "image": "https://yourbucket.com/bara-imambara.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly at shrines/historic sites."},
                {"tip": "Carry cash for market purchases; digital acceptance variable."},
                {"tip": "Use government-certified tour guides; beware touts near landmarks."},
                {"tip": "Drink bottled water, check street food hygiene."},
                {"tip": "Ask permission before photographs of people/religious activities."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Dewa Sharif (Sufi shrine, Barabanki), Nawabganj Bird Sanctuary, Bithoor (pilgrimage town), Kakori Memorial, Kanpur (industrial/cultural city).",
                    "image": "https://yourbucket.com/rumi-darwaza.jpg"
                }
            ]
        }
    ]
}

city_chitrakoot = {
    "state_id": up_state_id,
    "name": "Chitrakoot",
    " hidden_gem_places": [
        {
            "name": "Chitrakoot",
            "history": {
                "text": "Chitrakoot, on the UP-MP border, is renowned as the Ramayana site where Lord Rama, Sita, and Lakshmana spent their exile. Ancient and sacred, its sites (Kamadgiri Hill, Ramghat, Janki Kund) attract pilgrims and were celebrated by Bundelas and Marathas, remaining central in India’s spiritual poetry/geography.",
                "image": "https://yourbucket.com/chitrakoot-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Sattvic thali (chapati, rice, dal, sabzi, halwa), malpua, khoya ladoos, besan halwa, ram dana laddoos, street snacks (kachori sabzi, poha, jalebi, samosa, sabudana khichdi, fruit chaat), litti chokha, til laddoos, makhana fry, boondi, gur sweets.",
                    "image": "https://yourbucket.com/chitrakoot-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Ritual dips at Ramghat, Kamadgiri Hill parikrama, explore Janki Kund, Sphatik Shila, Hanuman Dhara, Satna forest trails, visit ashrams, enjoy festival music, street food, local markets, and Chitrakoot Mela.",
                    "image": "https://yourbucket.com/kamadgiri-hill.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly in temples/ghats; remove footwear inside sacred spaces."},
                {"tip": "Eat early—restaurants often close after sunset; drink filtered/boiled water."},
                {"tip": "Carry cash, as digital payments are rare."},
                {"tip": "Respect temple customs, ask before photos, don’t display valuables."},
                {"tip": "Crowded/riverside sites—observe precautions in festival periods."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Kamadgiri Hill (parikrama, shrines), Janki Kund (Sita’s bathing spot), Sphatik Shila (legendary boulder), Hanuman Dhara (waterfall/shrine), Gupt Godavari Caves (underground river), Bharatkoop (sacred well).",
                    "image": "https://yourbucket.com/gupt-godavari-caves.jpg"
                }
            ]
        }
    ]
}

city_chunar_fort = {
    "state_id": up_state_id,
    "name": "Chunar Fort",
    " hidden_gem_places": [
        {
            "name": "Chunar Fort",
            "history": {
                "text": "Chunar Fort sits above the Ganges in Mirzapur district and dates back to at least the 1st century BCE. Fortified and named variously, it changed hands from King Sahadeo to Mughal and British rulers. It served as depot, prison, and residence, protected today as a culture site celebrated in literature and folklore.",
                "image": "https://yourbucket.com/chunar-fort-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Samosas, pakoras, North Indian thalis (chapati, dal, sabzi, sweets), malaiyo, milk sweets, tea, and snacks near river/fort entrance.",
                    "image": "https://yourbucket.com/malaiyo.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Explore ramparts, gates (Iftikhar Khan), Sonwa Mandap, ancient wells/stepwells, Aurangzeb’s mosque; fort photography, legends, walk old Mirzapur markets for crafts.",
                    "image": "https://yourbucket.com/sonwa-mandap.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Wear sturdy shoes—many steps/tunnels, uneven terrain."},
                {"tip": "Carry cash; vendors/guides rarely accept digital payments."},
                {"tip": "Drink bottled water; be mindful with food in crowds/heat."},
                {"tip": "Follow local customs—remove shoes in mosque/burj/shrine areas."},
                {"tip": "Check/confirm photo rules in sacred/interior spaces."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Vindhyachal (pilgrimage town/temple, 25 km), Varanasi (spiritual city, 40 km downstream), Sonwa Mandap & Bhairo Burj (fort highlights), Kali Khoh/caves (legendary sites), Mirzapur (ghats, carpets, lakes).",
                    "image": "https://yourbucket.com/mirzapur-ghat.jpg"
                }
            ]
        }
    ]
}


city_ramnagar = {
    "state_id": up_state_id,
    "name": "Ramnagar",
    " hidden_gem_places": [
        {
            "name": "Ramnagar",
            "history": {
                "text": "Ramnagar, on the east bank of the Ganges near Varanasi, centers on Ramnagar Fort (built 18th-century by Maharaja Balwant Singh/Kashi Naresh). The sandstone fort, mixing Mughal and Indian styles, houses the royal family, legacy events, and the famous Dussehra Ram Leela festival.",
                "image": "https://yourbucket.com/ramnagar-fort-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Samosas, pakoras, North Indian thalis (dal, chapati, sabzi, local sweets), jalebi, malaiyo, rabri, peda, fruit chaat, lassi.",
                    "image": "https://yourbucket.com/ramnagar-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Tour Ramnagar Fort’s museum (cars, weapons, clocks, costumes), attend Ram Leela festival (Dussehra), visit fort temples (Vyasa, Hanuman), walk gardens/towers, boat rides with Ganges/Varanasi views, experience royal traditions/festivals.",
                    "image": "https://yourbucket.com/ram-leela.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly for temples/museums/royal interiors."},
                {"tip": "Cash preferred at stalls/guides; digital options rare."},
                {"tip": "Stairs/terrain uneven—wear sturdy shoes."},
                {"tip": "Check photography rules in museum/living quarters."},
                {"tip": "Expect crowds/security during Dussehra and major festivals."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Varanasi (ghats, temple, bazaars), Tulsi Ghat (cultural hub, opposite river), Sarnath (Buddhist pilgrimage), Chunar Fort (downstream), Vindhyachal (pilgrimage, market).",
                    "image": "https://yourbucket.com/tulsi-ghat.jpg"
                }
            ]
        }
    ]
}


city_rani_mahal = {
    "state_id": up_state_id,
    "name": "Rani Mahal (Varanasi)",
    " hidden_gem_places": [
        {
            "name": "Rani Mahal (Rana Mahal)",
            "history": {
                "text": "Rani Mahal (Rana Mahal) at Causatthi Ghat was built around 1670 by Maharana Jagat Singh of Udaipur as his Kashi pilgrimage residence. The Rajasthani-style palace features river-view porches, intricate stone windows, and water-access platforms, symbolizing Mewar-Kashi spiritual ties.",
                "image": "https://yourbucket.com/rana-mahal-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Samosa, jalebi, kachori sabzi, lassi, thandai, rabri, malaiyo, peda, North Indian vegetarian thalis at riverside and palace hotels.",
                    "image": "https://yourbucket.com/ghat-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Tour Rana Mahal's river views, Rajasthani architecture, porches; photograph stone-lattice windows; boat rides for sunrise/sunset palace views; visit Vakratunda Vinayaka shrine, Causatthi Ghat; stay at heritage hotels (Palace on Steps, Hotel Elena).",
                    "image": "https://yourbucket.com/rana-mahal-architecture.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly at ghats/palaces/temples; remove shoes at shrines."},
                {"tip": "Carry cash—vendors/hotels prefer cash payments."},
                {"tip": "Be careful on wet/slippery steps and platforms."},
                {"tip": "Check photography rules in palace interiors/temples."},
                {"tip": "Festival crowds—watch valuables, follow local advice."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Causatthi Ghat (historic bathing/ceremonies), Darbhanga Ghat (ornate palace), Kashi Vishwanath Temple, Tulsi Ghat (rituals, music), Ramnagar Fort (royal museum across river).",
                    "image": "https://yourbucket.com/causatthi-ghat.jpg"
                }
            ]
        }
    ]
}


city_katarniaghat = {
    "state_id": up_state_id,
    "name": "Katarniaghat Wildlife Sanctuary",
    " hidden_gem_places": [
        {
            "name": "Katarniaghat",
            "history": {
                "text": "Katarniaghat Wildlife Sanctuary in Bahraich near Nepal is a key floodplain, forest, and wetland reserve founded in 1975, part of Dudhwa Tiger Reserve since 1987. It preserves vital wildlife corridors, habitats, and species along the Ghagra, having evolved from British hunting grounds into a top conservation area.",
                "image": "https://yourbucket.com/katarniaghat-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Simple North Indian vegetarian fare (dal, sabzi, chapati, rice) at eco-camps/Forest Rest Houses, samosas/pakoras/tea in villages, wild honey, seasonal fruit. Carry packaged snacks for treks/safaris.",
                    "image": "https://yourbucket.com/eco-camp-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Jeep/boat safaris (tigers, leopards, gharials, dolphins, elephants, birds), nature walks, butterfly watching, guided tours, river birding, visit Tharu villages for crafts/culture.",
                    "image": "https://yourbucket.com/katarniaghat-safari.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Visit Nov–May; sanctuary closes and rivers flood during monsoon."},
                {"tip": "Carry cash, card payment rarely possible at gates/stalls."},
                {"tip": "Wear shoes, long pants, insect repellent—grasslands harbor ticks/leeches/mosquitoes."},
                {"tip": "Obey guides/park rules—no loud noise, litter, or approaching wildlife."},
                {"tip": "Respect Tharu customs; ask before photos or entering private hamlets."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Dudhwa National Park, Kishanpur Wildlife Sanctuary (bird/mammal wetlands), Frog Temple (Oel), Indo-Nepal border villages (birding/culture), Suheli Barrage (riverscape/birdwatching).",
                    "image": "https://yourbucket.com/frog-temple.jpg"
                }
            ]
        }
    ]
}

city_hawa_mahal = {
    "state_id": rs_state_id,
    "name": "Hawa Mahal",
    "popular_places": [
        {
            "name": "Hawa Mahal",
            "history": {
                "text": "Hawa Mahal ('Palace of Winds') was built in 1799 by Maharaja Sawai Pratap Singh as part of Jaipur’s City Palace. Designed by Lal Chand Ustad, its five stories—953 lattice windows—let royal women observe life below under purdah. The pink sandstone masterpiece reflects Rajput-Mughal, Jaipur Pink City legacy, and careful restoration up to the present.",
                "image": "https://yourbucket.com/hawa-mahal-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri), rooftop sweets (ghevar, mawa kachori, rabri), snacks/chaat (Johari Bazaar), masala chai, samosas in historic cafes.",
                    "image": "https://yourbucket.com/ghevar.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Tour the palace’s 953 jharokhas/lattices and balconies, photograph at sunrise/sunset for Pink City views, museum visit, shop handicrafts/jewelry/textiles at Johari Bazaar, climb to upper floors for views of Jantar Mantar, City Palace, Jaipur.",
                    "image": "https://yourbucket.com/hawa-mahal-jharokha.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Buy tickets at official counters, avoid touts/guides."},
                {"tip": "Carry cash for markets/food stalls, digital may be limited."},
                {"tip": "Wear modest, respectful attire in busy bazaars."},
                {"tip": "Sturdy shoes needed for floors/ramps."},
                {"tip": "Photography usually allowed in public, but check rules in museum sections."}
            ],
            "nearbyAttractions": [
                {
                    "name": "City Palace (Mughal-Rajput museums), Jantar Mantar (UNESCO observatory), Johari Bazaar (jewels, food), Albert Hall Museum (Indo-Saracenic art), Nahargarh Fort (city/sunset views).",
                    "image": "https://yourbucket.com/city-palace.jpg"
                }
            ]
        }
    ]
}

city_udaipur_city_palace = {
    "state_id": rs_state_id,
    "name": "Udaipur City Palace",
    "popular_places": [
        {
            "name": "Udaipur City Palace",
            "history": {
                "text": "Udaipur City Palace, Rajasthan’s largest, was begun by Maharana Udai Singh II in 1559 and expanded for 400 years by his Sisodia Rajput successors. It merges Rajput, Mughal, European, and Chinese styles on Lake Pichola’s bank, housing private palaces, courtyards (Mor Chowk), royal museums, and a tradition of Mewar cultural patronage.",
                "image": "https://yourbucket.com/udaipur-palace-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri, spicy curries), sweets (ghevar, rabri, mawa kachori), masala chai, samosas, street snacks/chaat near City Palace/Jagdish Chowk.",
                    "image": "https://yourbucket.com/udaipur-ghevar.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Tour Sheesh Mahal, Mor Chowk, Zenana Mahal, art galleries, photograph lake panoramas, Badi Mahal gardens, visit Palace Museum (armory, textiles, royal artifacts), attend cultural shows/weddings, shop palace bazaars.",
                    "image": "https://yourbucket.com/city-palace-balcony.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Buy tickets/camera passes at official counters, avoid touts."},
                {"tip": "Cash preferred for entry, shopping, and food; digital not always available."},
                {"tip": "Dress modestly—respectful attire for palace interiors."},
                {"tip": "Wear comfortable shoes for marble stairs, corridors."},
                {"tip": "Check photo restrictions in museum/art galleries."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Lake Pichola (boat rides, Jag Mandir, Lake Palace), Jagdish Temple, Bagore Ki Haveli (museum, Gangaur Ghat), Saheliyon-ki-Bari (lotus gardens/pavilions), Sajjangarh (Monsoon Palace, for sunset views).",
                    "image": "https://yourbucket.com/lake-pichola.jpg"
                }
            ]
        }
    ]
}

city_mehrangarh_fort = {
    "state_id": rs_state_id,
    "name": "Mehrangarh Fort",
    "popular_places": [
        {
            "name": "Mehrangarh Fort",
            "history": {
                "text": "Mehrangarh Fort, founded by Rao Jodha in 1459, dominates Jodhpur from a 400-foot hilltop. Over 500 years, it was expanded by Rathore rulers as a mighty fortress, palace center, and spiritual site. Legends (Cheeria Nathji's curse) and folk celebrations are part of its storied history.",
                "image": "https://yourbucket.com/mehrangarh-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri, spicy curries), sweets (ghevar, mawa kachori, rabri), samosa, mirchi vada, masala chai, makhaniya lassi.",
                    "image": "https://yourbucket.com/mehrangarh-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Tour palaces (Moti Mahal, Phool Mahal, Sheesh Mahal), walk through 7 gates (Jai Pol, Fateh Pol, Loha Pol with sati handprints), view Dedh Kangra Pol, fort ramparts (Jodhpur panorama), Chamunda Mataji Temple, Mehrangarh Museum, enjoy Rajasthan Folk and Sacred Spirit Festivals.",
                    "image": "https://yourbucket.com/mehrangarh-rampart.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Buy official tickets only; avoid touts/unofficial guides."},
                {"tip": "Wear strong footwear for ramps and stone paths."},
                {"tip": "Cash preferred for market purchases; digital not universal."},
                {"tip": "Dress modestly in the fort and historic areas."},
                {"tip": "Keep valuables secure; follow museum rules for photography."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Jaswant Thada (marble memorial), Umaid Bhawan Palace (museum/hotel), Mandore Gardens (old capital temples/cenotaphs), Ghanta Ghar & Sardar Market (Jodhpur bazaar), Rao Jodha Desert Rock Park (native flora park).",
                    "image": "https://yourbucket.com/jaswant-thada.jpg"
                }
            ]
        }
    ]
}


city_jaisalmer_fort = {
    "state_id": rs_state_id,
    "name": "Jaisalmer Fort",
    "popular_places": [
        {
            "name": "Jaisalmer Fort (Sonar Quila)",
            "history": {
                "text": "Jaisalmer Fort, or Sonar Quila, was built in 1156 AD by Rawal Jaisal on Trikuta Hill. One of the few living forts with a resident population, it played a strategic Silk Route role and reflects Rajput, Mughal, and desert heritage through its radiant stone, ramparts, and palaces. Today a UNESCO site, it's famed for vibrant traditions.",
                "image": "https://yourbucket.com/jaisalmer-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri), sweets (ghevar, mawa kachori, rabri), samosa, mirchi vada, Jaisalmer bhujia, masala chai, pyaz ki kachori.",
                    "image": "https://yourbucket.com/jaisalmer-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Tour ramparts and gates (Akhai Pol, Ganesh Pol, Suraj Pol, Hawa Pol), explore Raj Mahal, Jain temples, merchant havelis, shop for crafts in fort alleys, puppet shows, folk festivals, sunset from ramparts.",
                    "image": "https://yourbucket.com/sonar-quila-rampart.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Tickets at official counters only; avoid touts/unofficial guides."},
                {"tip": "Cash preferred in fort shops/markets."},
                {"tip": "Wear modest clothing, sturdy shoes for uneven climbs."},
                {"tip": "Ask before photographing in palace/temple rooms."},
                {"tip": "Watch belongings in busy alleys; respect local conduct."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Patwon ki Haveli, Salim Singh ki Haveli, Nathmal ki Haveli, Gadisar Lake, Bada Bagh, Desert National Park, Kuldhara ghost village.",
                    "image": "https://yourbucket.com/gadisar-lake.jpg"
                }
            ]
        }
    ]
}
city_ranthambore_national_park = {
    "state_id": rs_state_id,
    "name": "Ranthambore National Park",
    "popular_places": [
        {
            "name": "Ranthambore National Park",
            "history": {
                "text": "Ranthambore National Park, near Sawai Madhopur, was a game sanctuary from 1955, became a Project Tiger reserve in 1973, and national park in 1980. Merging Aravali and Vindhya ranges, it features ruins, lakes, and the 10th-century Ranthambore Fort (UNESCO), shaping both wildlife and regional heritage.",
                "image": "https://yourbucket.com/ranthambore-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri), mirchi vada, pyaz ki kachori, samosa (roadside stalls), rabri, ghevar, mawa kachori, masala chai, heavy breakfasts.",
                    "image": "https://yourbucket.com/ranthambore-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Jeep/canter safaris for tiger sightings, birdwatching (320+ species: serpent eagle, paradise flycatcher, waterfowl), photography at lakes/ruins/fort, sunset at Ranthambore Fort, visit Ranthambore Museum, enjoy local cultural events.",
                    "image": "https://yourbucket.com/ranthambore-safari.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash for local vendors/guides, digital options limited."},
                {"tip": "Book safaris in advance with registered operators, especially in peak season."},
                {"tip": "Dress in neutral colours/full-coverage; bring water, hats, sunscreen, camera."},
                {"tip": "Never step out of vehicles during safaris; follow wildlife safety rules."},
                {"tip": "Photography allowed in public areas, but check museum/fort restrictions."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Ranthambore Fort, Surwal Lake (birding), Trinetra Ganesh Temple (in fort), Khandar Fort, village safaris (local crafts, artisans, sustainability).",
                    "image": "https://yourbucket.com/ranthambore-fort.jpg"
                }
            ]
        }
    ]
}

city_pushkar = {
    "state_id": rs_state_id,
    "name": "Pushkar",
    "popular_places": [
        {
            "name": "Pushkar",
            "history": {
                "text": "Pushkar, perched beside a mythic lake created by Brahma’s lotus, is among Hinduism’s five holiest towns. Its antiquity goes back to Gupta times, and after periods of destruction (Aurangzeb) was revived by Marwar and local devotees. Celebrated for its Brahma Temple (one of a kind), lively bazaar, and Camel Fair.",
                "image": "https://yourbucket.com/pushkar-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, ker sangri, gatte ki sabzi), malpua, rabri, kachori, mirchi vada, poha, chai, lassi, chaats.",
                    "image": "https://yourbucket.com/pushkar-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Walk around Pushkar Lake, bathe at 52 ghats, explore Brahma Temple and other ashrams, attend Camel Fair (races, music, markets), sunset hike to Savitri Temple, shop for crafts in bazaar.",
                    "image": "https://yourbucket.com/camel-fair.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly at temples/ghats; remove shoes in sacred areas."},
                {"tip": "Bottled water advised; use caution with street food."},
                {"tip": "Cash preferred at stalls; some cafes take digital payment."},
                {"tip": "Watch crowds/touts during fairs/festivals; protect valuables."},
                {"tip": "Ask permission before photos in ceremonies/portraits."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Ajmer (Dargah Sharif, forts), Savitri Temple (Ratnagiri Hill, sunset views), Kishangarh (Bani Thani art, marble), rose gardens/desert villages, Nag Pahar (sacred hill/cave).",
                    "image": "https://yourbucket.com/pushkar-lake.jpg"
                }
            ]
        }
    ]
}

city_junagarh_fort = {
    "state_id": rs_state_id,
    "name": "Junagarh Fort (Bikaner)",
    "popular_places": [
        {
            "name": "Junagarh Fort",
            "history": {
                "text": "Junagarh Fort, originally called Chintamani, was built between 1589–1594 by Raja Rai Singh in Bikaner’s city center. Never conquered except briefly, it showcases 400 years of Mughal, Rajput, and revivalist architecture. Rich in palaces, pavilions, and mirrorwork, it chronicles Bikaner’s valor, culture, and history.",
                "image": "https://yourbucket.com/junagarh-fort-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri), Bikaneri bhujia, rasgulla, kachori, ghevar, mawa kachori, samosa, mirchi vada, masala chai.",
                    "image": "https://yourbucket.com/bikaneri-bhujia.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Tour palaces (Anup, Phool, Chandra, Badal, Karan Mahals), Prachina Museum, see Daulat Pol handprints, explore mirrorwork/murals, photograph courtyards and balconies, shop Bikaner crafts at main gates.",
                    "image": "https://yourbucket.com/anup-mahal.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Get tickets at official counters, use registered guides."},
                {"tip": "Carry cash for shops/stalls; digital is rare."},
                {"tip": "Dress comfortably/modestly; sturdy shoes needed for stones."},
                {"tip": "Follow photography rules inside palaces/museums."},
                {"tip": "Use caution on fort steps and during monsoon/busy times."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Lalgarh Palace (museum/hotel), Karni Mata Temple (rat temple, Deshnok), Ganga Golden Jubilee Museum, National Research Centre on Camels, Rampuriya Havelis (merchant mansions).",
                    "image": "https://yourbucket.com/lalgarh-palace.jpg"
                }
            ]
        }
    ]
}

city_ajmer_dargah = {
    "state_id": rs_state_id,
    "name": "Ajmer Dargah",
    "popular_places": [
        {
            "name": "Ajmer Dargah (Khwaja Moinuddin Chishti)",
            "history": {
                "text": "Ajmer Dargah is the Sufi shrine of Khwaja Moinuddin Chishti, who arrived in Ajmer in 1192 and spent his life teaching and serving. The shrine, built after 1236 and expanded by Delhi Sultanate and Mughals (esp. Akbar), features Indo-Islamic architecture, marble domes, silver railings, and courtyards. It is a symbol of Sufi peace, inclusivity, and service.",
                "image": "https://yourbucket.com/ajmer-dargah-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Langar (community meals), Ajmeri kachori, samosa, mirchi bada (street sellers around the shrine), mawa kachori, rabri (sweet shops), Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri) at nearby eateries.",
                    "image": "https://yourbucket.com/ajmer-langar.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Visit shrine/prayer, present chadar, attend qawwali evenings, Urs festival (music, rituals, shared food), explore dargah complex/architecture, shop for Sufi crafts and beads, visit Akbari Masjid/Nizam Gate.",
                    "image": "https://yourbucket.com/ajmer-qawwali.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly/carry scarf; cover arms/legs for entry."},
                {"tip": "Cash recommended—stalls/donation counters rarely take cards."},
                {"tip": "Remove shoes on shrine premises; observe prayer etiquette."},
                {"tip": "Crowds during Urs/festivals—keep valuables secure."},
                {"tip": "Photography allowed in outside areas, ask permission in prayer halls/tomb."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Ana Sagar Lake (scenic boat rides/walks), Akbari Fort & Museum, Adhai Din Ka Jhonpra (old mosque/arches), Taragarh Fort (city views), Pushkar (Brahma Temple, short drive from Ajmer).",
                    "image": "https://yourbucket.com/ana-sagar.jpg"
                }
            ]
        }
    ]
}

city_mount_abu = {
    "state_id": rs_state_id,
    "name": "Mount Abu",
    "popular_places": [
        {
            "name": "Mount Abu",
            "history": {
                "text": "Mount Abu (Arbudaranya) is Rajasthan’s only hill station, rich in ancient lore, Rajput refuge, and saintly retreat. Sage Vashistha, Rajput clan origins, Nandi’s rescue, and Jain/tribal legend all converge here. Dilwara Temples (11th–13th c.) and Guru Shikhar (highest Aravalli peak) are highlights, alongside colonial and tribal history.",
                "image": "https://yourbucket.com/mount-abu-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri), Jain veg meals, malai ghewar, rabri, mawa kachori, kachori, samosa, chaas, chana jor garam, bhutta, ice cream (Nakki Lake).",
                    "image": "https://yourbucket.com/mount-abu-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Visit Dilwara Temples (marble carving), boat/picnic/stroll at Nakki Lake, trek to Guru Shikhar (views, shrine), explore Achalgarh Fort, shop tribal handicrafts, wander Mount Abu bazaar.",
                    "image": "https://yourbucket.com/dilwara-temple.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Mountain weather is changeable; carry light jackets/rain gear."},
                {"tip": "Cash is best for small shops/stalls, though digital payment is growing."},
                {"tip": "Dress comfortably/modestly, esp. for temples (cover arms/legs)."},
                {"tip": "Wear good shoes; terrain is rocky/steep in places."},
                {"tip": "At viewpoints/lakes, keep valuables safe during crowds/festivals."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Dilwara Temples (2.5 km), Achalgarh Fort/hill temples, Guru Shikhar (peak), Trevor’s Tank (picnic, birdwatch), Arbuda Devi Temple (rock-cut cave/shrine).",
                    "image": "https://yourbucket.com/nakki-lake.jpg"
                }
            ]
        }
    ]
}

city_chittorgarh_fort = {
    "state_id": rs_state_id,
    "name": "Chittorgarh Fort",
    "popular_places": [
        {
            "name": "Chittorgarh Fort (Chitrakut)",
            "history": {
                "text": "Chittorgarh Fort was founded by Chitrangada Mori (7th c.), seized by Bappa Rawal (8th c., Mewar) and became India’s largest fort. Notable sieges by Alauddin Khilji, Bahadur Shah, Akbar marked it as a symbol of Rajput valor and tragedy. Its UNESCO listing and folklore affirm its pride and historic stature.",
                "image": "https://yourbucket.com/chittorgarh-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri), mirchi vada, pyaz ki kachori, samosa, masala chai, rabri, ghevar, mawa kachori, buttermilk, lassi.",
                    "image": "https://yourbucket.com/chittorgarh-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Walk through seven pols (gateways), historic palaces (Rana Kumbha Mahal, Rani Padmini’s Palace), Vijay/Kirti Stambh (towers), temple visits (Rajput/Sultanate architecture), explore reservoirs/views/ramparts, shop local handicrafts, miniature paintings, silver jewelry.",
                    "image": "https://yourbucket.com/vijay-stambh.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Cash is handy—stalls/guides may not take cards."},
                {"tip": "Wear sturdy shoes for uneven/steep stone walks."},
                {"tip": "Dress modestly at temples/palaces."},
                {"tip": "Hydrate and use sunscreen in summer heat."},
                {"tip": "Respect signage for restricted/ruin/temple areas."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Ratan Singh Palace (lakeside), Fateh Prakash Palace (museum), Sanwariya Seth Temple (Mandfia), Bhainsrorgarh Fort (hilltop, 50 km), Menal (temple+waterfall, Bundi route).",
                    "image": "https://yourbucket.com/ratan-singh-palace.jpg"
                }
            ]
        }
    ]
}



city_khimsar = {
    "state_id": rs_state_id,
    "name": "Khimsar",
    " hidden_gem_places": [
        {
            "name": "Khimsar Fort",
            "history": {
                "text": "Khimsar, on the Thar Desert’s edge, is famed for Khimsar Fort (built 1523 by Rao Karamsji, son of Rao Jodha), first a military post then expanded as a royal palace in the 18th c. Its quadrangular, horizontal layout features ramparts, palaces, shrines, armory and antique decor. Now a heritage hotel, Khimsar also displays village temples and scenic sand dunes.",
                "image": "https://yourbucket.com/khimsar-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri, local curries), kachori, mirchi vada, samosa, ghevar, mawa kachori, rabri, masala chai, hearty breakfast staples.",
                    "image": "https://yourbucket.com/khimsar-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Heritage walks/guided tours inside fort (palaces, courtyards, armory), camel safaris, jeep rides, desert sunsets/bonfire dinners at Sand Dune Village, visit Black Buck Reserve, Dhawa Doli Sanctuary, temple tours, shop crafts/see folk dance.",
                    "image": "https://yourbucket.com/khimsar-fort-courtyard.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash; digital payment uncommon in villages."},
                {"tip": "Dress for heat (cotton), bring layers for cool evenings."},
                {"tip": "Sturdy footwear for fort/desert walks/safaris."},
                {"tip": "Drink bottled water, be careful with street snacks."},
                {"tip": "Observe safety instructions for camel/jeep rides and wildlife tours."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Nagaur Fort (murals, temples, palaces), Black Buck Reserve, Dhawa Doli Sanctuary (bird/wildlife), Jain/Hindu shrines in Khimsar, Sand Dune Village (eco-resort in desert).",
                    "image": "https://yourbucket.com/nagaur-fort.jpg"
                }
            ]
        }
    ]
}

city_osian = {
    "state_id": rs_state_id,
    "name": "Osian",
    " hidden_gem_places": [
        {
            "name": "Osian Temples",
            "history": {
                "text": "Osian, the 'Khajuraho of Rajasthan', flourished as a Silk Route hub under Gurjara-Pratihara rule (8th–12th c.). Over 100 Hindu/Jain temples once stood—about 20 survive, highlighting art and architecture (Sachiya Mata, Mahavira Jain temples). The town’s trade and culture faded after invasions, but it is a major heritage and pilgrimage site.",
                "image": "https://yourbucket.com/osian-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri), sweets (rabri, mawa kachori, ghevar), kachori, mirchi vada, samosa, masala chai, lassi, bajra roti (millet).",
                    "image": "https://yourbucket.com/osian-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Visit Sachiya Mata and Mahavira Jain temples (carvings, sculptures), wander ruined temple clusters/gateways, desert camel safaris (sunset), photograph reliefs/murals/views, join Navratri temple festivities.",
                    "image": "https://yourbucket.com/sachiya-mata-temple.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Cash only—local vendors rarely accept cards."},
                {"tip": "Dress modestly; bring shawls/scarves for temples."},
                {"tip": "Shoes needed for stone/step walks."},
                {"tip": "Do not climb/touch fragile carvings; obey heritage signs."},
                {"tip": "Desert sun: sunscreen/hat/water always needed."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Jodhpur (Blue City, Mehrangarh Fort), Khimsar (fort/sand dunes/black buck), Nagaur (fort/cattle fair), Mandore (gardens/cenotaphs), camel camps/villages (desert life/culture).",
                    "image": "https://yourbucket.com/jodhpur-fort.jpg"
                }
            ]
        }
    ]
}


city_mandawa = {
    "state_id": rs_state_id,
    "name": "Mandawa",
    " hidden_gem_places ": [
        {
            "name": "Mandawa",
            "history": {
                "text": "Mandawa, in Shekhawati, was founded in the 18th century as a Silk Route tradepost. Developed by merchant and Rajput rulers (Mandu Jat, Thakur Nawal Singh), it flourished with havelis, forts, and palaces blending Rajput, Mughal, and European details. The town’s mansions, frescoes, and painted walls are an open-air art gallery, known as the highlight of Shekhawati.",
                "image": "https://yourbucket.com/mandawa-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, ker sangri, gatte ki sabzi), kachori, samosa, mirchi vada, masala chai, rabri, mawa kachori, ghevar, veg curries, millet rotis.",
                    "image": "https://yourbucket.com/mandawa-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Tour Mandawa Fort (arches, antique rooms, rooftop views), heritage walks to top havelis (Chokhani, Jhunjhunwala, Ladia, Goenka Double, Binsidhar Newatia), photograph murals/art/architecture, join art/camel/teej festivals, shop village handicrafts.",
                    "image": "https://yourbucket.com/mandawa-fort.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash; digital payment is limited at small shops/dhabas."},
                {"tip": "Dress modestly/light cottons; best for climate and decorum at havelis/temples."},
                {"tip": "Comfortable shoes needed for cobbled/uneven streets/steps."},
                {"tip": "Keep hydrated/sunscreen in hot months."},
                {"tip": "Authorized local guides give accurate tours of historic art."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Nawalgarh, Fatehpur, Mahansar (other Shekhawati haveli towns), Dundlod (fort, haveli complexes), Jhunjhunu (Khetri Mahal, Rani Sati Temple), Bikaner (Junagarh Fort, markets), Jaipur (Pink City, 3–3.5 hours).",
                    "image": "https://yourbucket.com/chokhani-haveli.jpg"
                }
            ]
        }
    ]
}


city_khuri_dunes = {
    "state_id": rs_state_id,
    "name": "Khuri Dunes",
    "hidden_gem_places": [
        {
            "name": "Khuri Dunes",
            "history": {
                "text": "Khuri is a tranquil desert village southwest of Jaisalmer, once a Silk Route stop. Its mud/thatch houses, folk music, and desert crafts reflect centuries of Rajput and nomadic culture shaped by ancient trade with Persia and Arabia. Khuri remains a living bastion of authentic Marwar desert tradition.",
                "image": "https://yourbucket.com/khuri-dunes-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, ker sangri, gatte ki sabzi), millet rotis, bajra khichdi, kachori, samosa, mirchi vada, masala chai, rabri, mawa sweets.",
                    "image": "https://yourbucket.com/khuri-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Camel safaris on sand dunes, desert camping (folk music/bonfire/Kalbeliya dance), sunrise/sunset on dunes, stargazing, sandboarding, jeep safaris, dune bashing, photography of vibrant desert life.",
                    "image": "https://yourbucket.com/khuri-camel-safari.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Bring cash—camps/shops rarely take digital payment."},
                {"tip": "Pack sunscreen, hat, sunglasses, and water."},
                {"tip": "Wear lightweight, full-sleeved clothing for sun/sand."},
                {"tip": "Book camel/camp through trusted operators for safety."},
                {"tip": "Protect electronics from dust, heed local wildlife advice."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Jaisalmer (Fort, havelis, bazaars), Sam Sand Dunes, Desert National Park (Great Indian Bustard), Kuldhara (abandoned village), Lodhurva (Jain temples, ruins).",
                    "image": "https://yourbucket.com/sam-dunes.jpg"
                }
            ]
        }
    ]
}


city_narlai = {
    "state_id": rs_state_id,
    "name": "Narlai",
    "hidden_gem_places": [
        {
            "name": "Narlai",
            "history": {
                "text": "Narlai in the Aravalli Hills of Pali, between Jodhpur and Udaipur, was a centuries-old trade outpost and royal hunting lodge. The village is famed for Rawla Narlai (now a hotel), 300+ intricate Hindu/Jain temples, sacred hills, stepwells, and its peaceful, tradition-rich life.",
                "image": "https://yourbucket.com/narlai-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajasthani thali (dal baati churma, gatte ki sabzi, ker sangri, bajra rotis, veg curries), millet breads, fresh dairy, rabri, mawa, kachori, samosa, masala chai, stepwell dinners by candlelight.",
                    "image": "https://yourbucket.com/narlai-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Explore 300+ temples (Jain, Hindu), Lord Adinath Jain Temple, climb Elephant Hill (Shiva cave/700+ steps/views), village walks, crafts/markets, horse/camel safari, stepwell dinners, folk music, wildlife/nature walks, leopard safaris.",
                    "image": "https://yourbucket.com/elephant-hill.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—digital payment rare in villages."},
                {"tip": "Dress modestly for temples; good shoes for walks/hikes."},
                {"tip": "Hydrate/use sun protection for outdoor trips."},
                {"tip": "Respect customs—ask before photos in temples/cultural events."},
                {"tip": "Book safaris through reputable guides/hotels."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Ranakpur Jain Temples (32 km; marble marvels), Kumbhalgarh Fort (36 km; UNESCO hill-fort), Nadol (Aashapura Mata Temple), Jawai (leopard/dam), Ghanerao (temples, stepwells).",
                    "image": "https://yourbucket.com/ranakpur-temple.jpg"
                }
            ]
        }
    ]
}

city_hampi = {
    "state_id": ks_state_id,
    "name": "Hampi",
    "popular_places": [
        {
            "name": "Hampi Ruins",
            "history": {
                "text": "Hampi (on the Tungabhadra River) was the Vijayanagara Empire capital from the 14th–16th centuries and at its peak one of the world’s richest cities. It thrived under Krishnadevaraya and others, was sacked in 1565 (Battle of Talikota), then abandoned. Today, haunting ruins (Virupaksha, Vittala temples, royal enclosures, bazaars) are UNESCO listed and draw global travelers.",
                "image": "https://thefederal.com/file/2022/09/Hampi.jpg"
            },
            "localCuisine": [
                {
                    "name": "South Indian cuisine (idli, dosa, paddu, poori, Bisi Bele Bath, rice dishes), North Karnataka options (jowar rotti, ennegayi, ragi mudde, Maddur vada, Neer dosa, thalis), breakfast (idli/sambar, dosa, lemon rice, puliyogare, filter coffee/chai), paddu, local thalis (Hampi Bazaar). Limited non-veg available on Hippie Island.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVmzPI9oLaX4GV4M56oALV4Og_fUbmrkHruA&s"
                }
            ],
            "activities": [
                {
                    "name": "Heritage walks/guided tours to Virupaksha, Vittala, Achyutaraya Temples, Royal Enclosure, Hampi Bazaar, elephant stables, monoliths; sunrise/sunset hikes to Hemakuta, Matanga, Anjanadri Hills; coracle rides, cycling, rock climbing, lake swims, explore Hippie Island (cafes, global food).",
                    "image": "https://www.plantheunplanned.com/_next/image?url=https%3A%2F%2Flogout.world%2Fmedia%2Fevent%2F1743%2FExplore-Hampi-Plan-The-Unplanned-1.jpeg&w=3840&q=75"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—vendors/guesthouses may lack card/ATM availability."},
                {"tip": "Dress modestly; remove shoes at temples."},
                {"tip": "Protect belongings in ruins/bazaars."},
                {"tip": "Hydrate, use sunscreen/hats for sun."},
                {"tip": "Respect signage, don’t climb fragile ruins; guides recommended for large/remote sites."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Anegundi (across river, caves/fort/Hanuman Temple), Daroji Sloth Bear Sanctuary, Tungabhadra Dam (scenic reservoir/Hospet), Hospet (colonial-era gateway/parks).",
                    "image": "https://yourbucket.com/tungabhadra-dam.jpg"
                }
            ]
        }
    ]
}

city_mysore_palace = {
    "state_id": ks_state_id,
    "name": "Mysore Palace",
    "popular_places": [
        {
            "name": "Mysore Palace (Amba Vilas Palace)",
            "history": {
                "text": "Mysore Palace, or Amba Vilas Palace, is the royal seat of the Wodeyars in Mysuru. First built in the 14th century, rebuilt after lightning, Tipu Sultan’s demolition, and a major fire, the current Indo-Saracenic marvel (by Henry Irwin) rose in 1912. The Palace is famed for Dasara festivities, grand architecture, treasures, and art.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNo-wfIXfAQK7eivtdQSMkIP-45CGmE1x-Vw&s"
            },
            "localCuisine": [
                {
                    "name": "Mysore masala dosa, idli sambar, vada, South Indian thali (rice, sambar, rasam, curry, curd), Mysore pak (ghee sweet), filter coffee, ragi mudde (millet balls).",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUOKLgc3iUEa_THzpezmBO99Tz2JO5ugIwyA&s"
                }
            ],
            "activities": [
                {
                    "name": "Tour palace interiors (Durbar Hall, Kalyana Mantapa, Doll’s Pavilion, gold throne at Dasara), gardens/temples, attend Dasara festival (illuminations, cultural shows), exterior photo walks, silk/sandal markets shopping.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKs5CwfF1DMl24gKNHmbBojYuoRbprEE78fw&s"
                }
            ],
            "safetyTips": [
                {"tip": "Tickets at official counters; no photography inside palace."},
                {"tip": "Cash needed for entry/markets/vendors."},
                {"tip": "Dress modestly; remove shoes at shrines; follow festival crowd signs."},
                {"tip": "Hydrate and use sun protection during the day."},
                {"tip": "Audio-guided/multilingual tours; guard valuables in crowds."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Jaganmohan Palace (art gallery), Chamundi Hill (temple/view), Brindavan Gardens (illuminated fountains), St. Philomena’s Cathedral, Mysore Zoo.",
                    "image": "https://yourbucket.com/chamundi-hill.jpg"
                }
            ]
        }
    ]
}

city_mughal_garden = {
    "state_id": jk_state_id,
    "name": "Mughal Gardens (Srinagar)",
    "popular_places": [
        {
            "name": "Mughal Gardens (Shalimar Bagh, Nishat Bagh, Chashma Shahi)",
            "history": {
                "text": "Srinagar's Mughal Gardens—Shalimar Bagh, Nishat Bagh, Chashma Shahi—were developed in the 17th century, with Shalimar built in 1619 by Emperor Jahangir for Nur Jahan and expanded by Shah Jahan. Their charbagh Persian-inspired design was adapted to Kashmir’s landscape: terraced layouts, marble fountains, and water channels. Sikh and Dogra rulers improved the gardens, which became royal summer homes and court venues; public access and electrification arrived in the 20th century.",
                "image": "https://tse3.mm.bing.net/th/id/OIP.xruioRkUKqo15GVncow0yQHaKl?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Kashmiri wazwan dishes—Rogan Josh, Gustaba, Yakhni, Dum Aloo—at Dal Lake restaurants; noon chai (salt tea), kahwa (spiced tea), girda (bread) from vendors; fresh apples/cherries and spring snacks during garden festivals.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.dSTTPQyjo0wHLEJGkf8MjgHaHa?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Stroll historic terraces, marble pavilions, chinar/almond tree lanes, and over 400 fountains in Shalimar Bagh; photography/nature walks (spring blossom/tulip season); attend cultural shows/festivals (music, dance, folk) in amphitheaters; visit Dal Lake by shikara, explore Pari Mahal and Hazratbal Shrine nearby.",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.XD65xEZwt2fiwY3FwhFDpQHaD3?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Visit March–June for blooms, October for foliage; winter is chilly/gardens less colorful."},
                {"tip": "Stick to walkways—fountain pools/channels slippery."},
                {"tip": "Carry cash—some vendors/garden entry may not accept cards."},
                {"tip": "Observe photography/garden rules—pavilion entry restrictions."},
                {"tip": "Use sunscreen/drink water—spring/summer sun can be intense."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Dal Lake (houseboats, shikara, floating market); Pari Mahal (terraced palace, views); Hazratbal Shrine (mosque, lake north shore); Tulip Garden (Asia’s biggest, near Mughal gardens); Old Srinagar (heritage, markets, jama Masjid).",
                    "image": "https://www.masala.com/cloud/2024/12/20/Dal-lake-400x266.jpg"
                }
            ]
        }
    ]
}


city_gokarna = {
    "state_id": ks_state_id,
    "name": "Gokarna",
    "popular_places": [
        {
            "name": "Gokarna & Mahabaleshwar Temple",
            "history": {
                "text": "Gokarna is a sacred coastal town and major Shaivaite site in Uttara Kannada. Legend says Shiva emerged here from a cow’s ear ('Go' + 'Karna'). Ravana brought Shiva’s Atmalinga from Kailash, but Ganesha tricked him and it was established in the soil (in Mahabaleshwar Temple). The complex, mostly Vijayanagara, is revered as 'Dakshin Kashi.'",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvWNs1kwPHwVbdcPYKXedbDDKM_2O3_nFlgA&s"
            },
            "localCuisine": [
                {
                    "name": "Udupi/North Karnataka cuisine (idli, dosa, paddu, Bisi Bele Bath, jowar roti, ragi mudde), vegetarian thali with coconut, fresh greens, seafood/shack fare (prawn fry, fish curry, calamari near Kudle/Om), Mysore pak, peni, holige, fruit desserts, chai/coffee.",
                    "image": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqU4-5fbW0ecAN45AESSmrk0Z2-bt-6HW6olXr8UhybwdUxbQ1pJloH0nj0VYk-IRQ8OZZfVyaYlhZI-uleJmOPvT7fOOMPvN76kPUjIDgpmcwTHYvm_MzlUVgEhImzLG3GkJJbD_pf6lh/s1600/P1010008-1.JPG"
                }
            ],
            "activities": [
                {
                    "name": "Temple darshan at Mahabaleshwar, Bhadrakali, attend festivals (Mahashivaratri), heritage walks, vibrant market, beach-hopping (Main, Kudle, Om, Half Moon, Paradise), swimming, yoga, trekking to Yana Caves, water sports, coracle rides, music/yoga workshops.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpDcYaaD2XmkJhk84K7t7IZdvSSmvZ84_x0g&s"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash for temples/markets/shacks; digital payment limited to some cafes/hotels."},
                {"tip": "Dress modestly at temples/in town; beachwear is OK at beaches."},
                {"tip": "Observe beach safety, currents, heed lifeguards."},
                {"tip": "Keep valuables safe in crowded areas."},
                {"tip": "Follow footwear/behavior norms at sacred spots."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Yana Caves (limestone/forest trails), Murudeshwara (Shiva statue/sea temple), Honnavar (mangroves/river tours), Karwar (museum/beaches/watersport), Apsarakonda (waterfall/beach, Kumta).",
                    "image": "https://yourbucket.com/murudeshwara.jpg"
                }
            ]
        }
    ]
}

city_coorg = {
    "state_id": ks_state_id,
    "name": "Coorg (Kodagu)",
    "popular_places": [
        {
            "name": "Coorg (Kodagu District)",
            "history": {
                "text": "Coorg (Kodagu), the 'Scotland of India,' is a lush Western Ghats district famed for its hills, coffee estates, and Kodava warrior culture. It was shaped by dynasties like Kadambas, Gangas, Cholas, Hoysalas, Haleri kings, and the British, with a unique tradition of independence, clan system, and martial heritage.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKvl9Hp5y3lzFfc70Uv9kR3bCP_Xa9xRIIFQ&s"
            },
            "localCuisine": [
                {
                    "name": "Kodava food: pandi curry, kadumbuttu, noolputtu, bamboo shoot curry, akki rotti, fish fry, koli curry, veg specialties (paputtu, kosambari, thoppu payasa), seasonal fruits, estate filter coffee.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeQsr96uhHEGuIWt90CzFmcCrrbcny3L1vVQ&s"
                }
            ],
            "activities": [
                {
                    "name": "Plantation tours/homestays (coffee/spice), trekking (Tadiandamol, Brahmagiri, Abbey Falls), river rafting (Barapole), Talakaveri temple, Omkareshwara, Raja’s Seat, nature at wildlife sanctuaries (Nagarhole/Pushpagiri), festivals (Kailpodh, Puthari, Kodava weddings).",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi5BJSyfwfN6K16Spgm5VK2EgmPEM4Y29ntQ&s"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash; ATMs exist in towns but not villages."},
                {"tip": "Light layers for weather; respect temple attire."},
                {"tip": "Use insect repellent; watch for leeches on forest treks."},
                {"tip": "Confirm guides/permission for reserves/tours."},
                {"tip": "Plan for monsoon rains (June–Sep) affecting outdoor activities."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Nagarhole National Park (safaris), Dubare Elephant Camp, Bylakuppe (Tibetan monastery), Iruppu & Mallalli Falls, Talakaveri (spring/temple/origin of Kaveri).",
                    "image": "https://yourbucket.com/dubare-elephant-camp.jpg"
                }
            ]
        }
    ]
}

city_badami = {
    "state_id": ks_state_id,
    "name": "Badami",
    "popular_places": [
        {
            "name": "Badami Cave Temples & Town",
            "history": {
                "text": "Badami (ancient Vatapi) was the 6th–8th c. Chalukya capital and cradle of South Indian temple architecture. Its grandeur includes iconic cave temples cut into sandstone cliffs (since 6th c.), hundreds of Malaprabha valley shrines, and a legacy of architectural and religious innovation now recognized for World Heritage.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIx9N_eM2XHmcwgEB97LfYvpihiJ5WVdQwPg&s"
            },
            "localCuisine": [
                {
                    "name": "North Karnataka thali (jowar roti, brinjal curry, sambar, rasam, chutneys, kosambari), akki rotti, paddu, Mysore pak, karadantu, idli, dosa, vada, poori, lemon rice, filter coffee, pakora, bhajji, masala chai, simple non-veg curries in select guesthouses.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2BZiHDVK_4ccDUqtMet5PsJN-dQaWXfGHUg&s"
                }
            ],
            "activities": [
                {
                    "name": "Tour Badami cave temples (Hindu/Jain/Buddhist), see Nataraja icon and Vishnu halls, Bhutanatha Temple on Agastya Lake, hilltop fort, ancient inscriptions/carvings, trek/scramble on cliffs (views, photo ops), shop crafts/textiles/jewelry in the markets.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUA8Mu_poncfWsdVUWNyj0e0b-xqK86ZofeQ&s"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash for shops, tickets, food stalls."},
                {"tip": "Dress modestly for temples; remove shoes before entering shrines/caves."},
                {"tip": "Comfortable footwear for steps/rocky terrain."},
                {"tip": "Hydrate, use sunscreen; hot/dry midday."},
                {"tip": "Licensed guides recommended for context and navigating the site."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Pattadakal (World Heritage, temple styles), Aihole (early temples), Mahakuta (temple+tank), Banashankari (pilgrimage/fair), Guledgudda (saree/textiles).",
                    "image": "https://yourbucket.com/pattadakal.jpg"
                }
            ]
        }
    ]
}

city_belur = {
    "state_id": ks_state_id,
    "name": "Belur",
    "popular_places": [
        {
            "name": "Belur (Chennakeshava Temple)",
            "history": {
                "text": "Belur, on the Yagachi River, was the Hoysala capital and epicenter of 11th–14th c. art and architecture. King Vishnuvardhana built the Chennakeshava Temple (1117 AD), a Hoysala masterpiece famed for Madanika sculptures and intricate soapstone carvings. Later rulers added shrines and mantapas, leaving a rich legacy now acclaimed by travelers and historians.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStfdG9lOYmvSs5ohj1HzSD0k67muOaTXfwtA&s"
            },
            "localCuisine": [
                {
                    "name": "Karnataka veg thalis (jowar roti, saaru, sambar, kosambari, chutneys, payasa), idli, vada, dosa, upma, poori-sabzi, filter coffee, Mysore pak, karadantu, fruits, bhajji, bonda.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEd7PZNa-rltm9kdZT2TTi5AJNvUSKpL3bQw&s"
                }
            ],
            "activities": [
                {
                    "name": "Tour Chennakeshava Temple (pillars, Madanikas, myth reliefs), smaller temples (Kappe Chennigaraya, Shankareshvara, Pathaleshwara), pushkarini tank, historical walks guided by locals, shop stone/silk crafts in bazaar, visit poet Raghavanka’s samadhi.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQi0TZyVGbATcIQYuLeis0E3O4u45SD9pP3Tw&s"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—digital payment rare in rural areas."},
                {"tip": "Dress modestly; remove shoes before entering temples."},
                {"tip": "Use hats/sunscreen/water; it gets hot outside."},
                {"tip": "Photography okay outside but may be restricted inside—check or ask."},
                {"tip": "Beware monkeys; secure belongings near temples."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Halebidu (twin Hoysaleswara temple, monuments, 16 km), Shravanabelagola (Jain pilgrimage, statue), Chikmagalur (hill station, coffee), Yagachi Dam (boating, picnics), Hassan (dist. HQ, museums, transit).",
                    "image": "https://yourbucket.com/halebidu-temple.jpg"
                }
            ]
        }
    ]
}

city_kabini_wildlife = {
    "state_id": ks_state_id,
    "name": "Kabini Wildlife Sanctuary",
    "popular_places": [
        {
            "name": "Kabini Wildlife Sanctuary",
            "history": {
                "text": "Kabini, at the edge of Nagarhole National Park (Karnataka), served as historic hunting grounds for Mysore royalty and the British. Protection as a wildlife sanctuary began in the 1950s/70s; trophy hunting/khedda ended and conservation flourished. Now, Kabini is known for tigers, leopards, elephants, black panther, birds, safaris, and eco-lodges on the river.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY8Zc52axM87hcEJV4_rh_D1xu9CQGh-wd5g&s"
            },
            "localCuisine": [
                {
                    "name": "South Indian thali (rice, sambar, rasam, curries, chutney, dosa), North Karnataka (jowar roti, brinjal curry, kosambari), river fish (fried/steamed), vada, idli, poori, Mysore pak, filter coffee, seasonal fruits.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSNXClR0sVlYaNKL2mNc-UfMgFTZzmz892dg&s"
                }
            ],
            "activities": [
                {
                    "name": "Jeep/boat safaris to see tigers/leopards/elephants/gaur/birds, birdwatching/photo at reservoir, nature walks, village cycling, heritage forest lodges (spas/ayurveda), see summer elephant gatherings, relax in royal lodge settings.",
                    "image": "https://www.indiabirdwatching.com/wp-content/uploads/2022/07/painted-stork-India-Bird-Watching.jpg.webp"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash; digital may be unreliable for local guides/vendors."},
                {"tip": "Dress full-sleeved/earth-toned for safari; hats/sunscreen/insect spray."},
                {"tip": "Follow guide instructions—never exit safari vehicles or walk off-trail."},
                {"tip": "Avoid monsoon (flooding); Nov–Apr is best."},
                {"tip": "Pre-book licensed safaris/lodges; keep valuables secure."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Nagarhole National Park (adjacent), Bandipur National Park (across river), Mysore (palaces/art museums, 80km), Wayanad (trekking/caves/waterfalls, Kerala), Ranganathittu Bird Sanctuary (migratory waterbirds).",
                    "image": "https://yourbucket.com/nagarhole.jpg"
                }
            ]
        }
    ]
}

city_nandi_hills = {
    "state_id": ks_state_id,
    "name": "Nandi Hills",
    "popular_places": [
        {
            "name": "Nandi Hills (Nandidurga)",
            "history": {
                "text": "Nandi Hills, near Bengaluru, dates to the 11th century (Ganga dynasty) and was later fortified by Cholas, Hoysalas, Vijayanagara, Tipu Sultan, Marathas, and the British. Tipu and colonial rulers made it a summer retreat. Its temples (Yoganandishwara, Bhoga Nandeeshwara), fort ruins, and dramatic cliffs preserve deep strategic, historic, and sacred value.",
                "image": "https://s7ap1.scene7.com/is/image/incredibleindia/nandi-hills-bangalore-karnataka-attr-about?qlt=82&ts=1742165056977"
            },
            "localCuisine": [
                {
                    "name": "South Indian tiffin/thali (idli, vada, dosa, sambar, lemon rice, curd rice), filter coffee, masala chai, fruits, veg snacks, simple veg curries, akki rotti, bisi bele bath, bhajji, pakora, Mysore pak.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZq0ieF02mxlOp8lSsGiCbS7BZ7guWI5h0JA&s"
                }
            ],
            "activities": [
                {
                    "name": "Walks to Yoganandishwara & Bhoga Nandeeshwara Temples, Nandi Fort ruins, Tipu’s Drop, Amrit Sarovar, sunrise treks, cycling, paragliding, visit colonial retreats, birdwatching, tree/sky photography.",
                    "image": "https://dq1q7qkthxkc0.cloudfront.net/StaticMedia/2587c129-c713-4c10-963a-46c8369705cd.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—digital payment limited for entry/snacks."},
                {"tip": "Dress in layers; sturdy shoes for hilly terrain."},
                {"tip": "Obey cliff/trail/fort signage; don’t risk edges."},
                {"tip": "Watch out for monkeys—guard food/valuables."},
                {"tip": "Hydrate and use sun protection in midday sun."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Bhoga Nandeeshwara Temple (Nandi village), Skandagiri (trekking/sea of clouds), Muddenahalli (Sir Visvesvaraya museum), Lepakshi (Vijayanagara temples/art), Chikkaballapur (coffee, markets, reservoirs).",
                    "image": "https://yourbucket.com/skandagiri.jpg"
                }
            ]
        }
    ]
}

city_chikmagalur = {
    "state_id": ks_state_id,
    "name": "Chikmagalur",
    "popular_places": [
        {
            "name": "Chikmagalur",
            "history": {
                "text": "Chikmagalur, 'Younger Daughter’s Village,' was gifted to a chief’s daughter in legend and is where coffee was first planted in India (Baba Budan Giri hills, 17th c.). Famed for coffee estates, wildlife sanctuaries, and trekking, it was shaped by Hoysala and regional rulers who left temples, lakes, and agricultural traditions.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxnLLzmxhnUfzvUTDSsYtXDgurqDcH50MRJA&s"
            },
            "localCuisine": [
                {
                    "name": "Malnad food (akki rotti, neer dosa, pathrode, pundi), Karntaka thali, jowar roti, coconut curries, filter coffee, sweets (payasa, halwa), idli, dosa, chutneys.",
                    "image": "https://i.ytimg.com/vi/_fygF5SB9V8/mqdefault.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trek Mullayanagiri, Baba Budangiri, Kemmanagundi, visit waterfalls (Hebbe, Manikyadhara, Kalhatti, Kadambi), safaris (Bhadra/Kudremukh), coffee estate tours/tasting, Coffee Museum, Sharadamba/Annapoorneshwari/Veera Narayana temples, boating at Hirekolale, walks in tea estates.",
                    "image": "https://www.thehosteller.com/_next/image/?url=https%3A%2F%2Fstatic.thehosteller.com%2Fhostel%2Fimages%2Fbchjn.jpg%2Fbchjn-1724932718652.jpg&w=2048&q=75"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash for rural/entry/market needs; digital is limited."},
                {"tip": "Layer clothes; good shoes for hiking/estate walks."},
                {"tip": "Insect repellent for forests/river areas."},
                {"tip": "Book guides/permits for wildlife/estate tours."},
                {"tip": "Best time: October–April (avoid monsoon rains)."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Belur/Halebidu (Hoysala temples), Sringeri (Sharadamba Math, Vaishnavite history), Kudremukh NP, Bhadra Dam/lake, Hirekolale Lake (sunset/nature picnic).",
                    "image": "https://yourbucket.com/halebidu-temple.jpg"
                }
            ]
        }
    ]
}

city_srirangapatna = {
    "state_id": ks_state_id,
    "name": "Srirangapatna",
    "popular_places": [
        {
            "name": "Srirangapatna",
            "history": {
                "text": "Srirangapatna is a historic Cauvery island town that served as the Mysore capital under Tipu Sultan and the Wodeyars, most noted for 18th-century Anglo-Mysore wars with the British. Pillars of heritage are the Ranganathaswamy Temple (9th c.), Daria Daulat Bagh, Gumbaz mausoleum, fortress, dungeons, and colonial remnants. Tipu’s 1799 defeat ended the town’s royal era, but it remains a vibrant site for culture, history, and pilgrimage.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4khNMf8fZKQuOaIhFcIrkIlXHIVcC9CWr8A&s"
            },
            "localCuisine": [
                {
                    "name": "Masala dosa, set dosa, idli-vada, maddur vada, ragi mudde, bisibele bath, puliyogare, pav bhaji, pani puri, vada pav, papdi chaat, ragda patties, bhel puri, lemon rice, veg thali, coffee, Mysore pak, holige, donne biryani, mutton fry, spicy sagu.",
                    "image": "https://media-assets.swiggy.com/swiggy/image/upload/f_auto,q_auto,fl_lossy/l0i9yxnpdaaitn82rzxy"
                }
            ],
            "activities": [
                {
                    "name": "Tour Ranganathaswamy Temple, Daria Daulat Bagh, Gumbaz, fortress, ramparts, river causeways, Tipu’s/Colonel Bailey’s dungeons, museums; cycle by Cauvery; birdwatch at Ranganathittu, shop local crafts/textiles/snacks.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWH7tOVk82WlUKKzfydQ8H4FsaQOOh80x_gQ&s"
                }
            ],
            "safetyTips": [
                {"tip": "Cash for street food, tickets, guides; digital limited."},
                {"tip": "Dress modestly for temples; shoes off at shrines."},
                {"tip": "Carry water/sunscreen for walking tours."},
                {"tip": "Use local guides for historic/river tours."},
                {"tip": "Don’t climb on ruins; valuables secure in crowds."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Mysore (palace, zoo, market), Ranganathittu Bird Sanctuary (boats/birds), Somanathapura (Hoysala temple), Balmuri/Edmuri Falls (picnic), Shivanasamudra (major waterfalls).",
                    "image": "https://yourbucket.com/gumbaz-mausoleum.jpg"
                }
            ]
        }
    ]
}



city_agumbe = {
    "state_id": ks_state_id,
    "name": "Agumbe",
    "hidden_gem_places": [
        {
            "name": "Agumbe",
            "history": {
                "text": "Agumbe, the 'Cherrapunji of South India,' is a Malnad village known for heavy rain, rainforests, and biodiversity. Home to the Agumbe Rainforest Research Station (king cobra study), its colonial traveler’s choultry, ghat roads, and Malgudi Days filming locations are highlights. The region is famed for eco/conservation tourism, cottage industry, and local healing plant lore.",
                "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/d1/95/cc/g0202010-1459865467901.jpg?w=900&h=500&s=1"
            },
            "localCuisine": [
                {
                    "name": "Malnad cuisine: akki rotti, neer dosa, pundi, coconut curries, thali at homestays, Maddur vada, chutney, filter coffee, wild honey, local fruits, simple home-style sweets, light non-veg at guesthouses.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfNWYgEOH1hPkXzL4MyvY-nbABzgwvMZvZig&s"
                }
            ],
            "activities": [
                {
                    "name": "Trek Narasimha Parvatha/peaks (Kundadri), explore Barkana/Jogi Gundi/Onake Abbi waterfalls, birdwatch/herpetology at Rainforest Research Station, relive Malgudi Days, sunset view/photography of rainforests/clouds.",
                    "image": "https://d26dp53kz39178.cloudfront.net/media/uploads/products/1-1721158210249.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Bring cash; digital payment limited in rural/homestay/roadside stalls."},
                {"tip": "Light rain gear/sturdy shoes for trekking/monsoon."},
                {"tip": "Use guides for forest/wildlife treks—never solo in monsoon."},
                {"tip": "Drink bottled water and check food hygiene."},
                {"tip": "Respect forest rules and don’t disturb wildlife—especially snakes."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Someshwara Wildlife Sanctuary, Kudremukh National Park, Sringeri (Sharadamba Temple), Udupi (temples/cuisine), Barkana/Jogigundi waterfalls.",
                    "image": "https://yourbucket.com/kudremukh.jpg"
                }
            ]
        }
    ]
}

city_st_marys_islands = {
    "state_id": ks_state_id,
    "name": "St. Mary’s Islands",
    "hidden_gem_places": [
        {
            "name": "St. Mary’s Islands (Coconut Island)",
            "history": {
                "text": "St. Mary’s Islands, off Malpe (Udupi, Arabian Sea), are a cluster of four small uninhabited isles famed for unique hexagonal basalt columns formed by volcanic activity 88 million years ago (when India split from Madagascar). Vasco da Gama landed here in 1498, naming it for the Virgin Mary. Now a National Geological Monument and rare coastal wonder.",
                "image": "https://myholidayhappiness.com/uploads/st-marys-island-closed-9113.jpg"
            },
            "localCuisine": [
                {
                    "name": "Fresh coconut water, tropical fruit snacks (seasonal, Malpe boats/stalls), coastal Karnataka cuisine (fish curry, rava fry, prawn, neer dosa, ghee roast), veg tiffin (idli, dosa, vada, upma, coffee), churmuri (puffed rice), masala chai, mango desserts (beach cafes).",
                    "image": "https://theyummydelights.com/wp-content/uploads/2019/03/chicken-ghee-roast.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Ferry from Malpe Beach; panoramic sea views; beachcombing, sunbathing, shell collecting at Shell Beach; explore/photograph basalt rocks, tide pools, coconut groves; birdwatching/picnics; sunset photo ops; see Geological Museum (Malpe).",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLILB7znXstjQYDmIQGlC2RUmMWtw9oHkSGQ&s"
                }
            ],
            "safetyTips": [
                {"tip": "Bring cash for ferries/snacks—digital is limited."},
                {"tip": "No overnight stays—these are day trip islands only."},
                {"tip": "Sun protection and water essential; shade is minimal."},
                {"tip": "Obey signs—no climbing on basalt columns."},
                {"tip": "Monsoon (June–Sep): ferries may not run; best visit Oct–Feb."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Malpe Beach (watersports, sea walk, foods, sunrises/sunsets), Udupi (Krishna temple, markets), Manipal (science/university museums), Kodi Beach/Kapu Lighthouse (quiet beaches), Salumarada Timmakka Tree Park (Udupi green space).",
                    "image": "https://yourbucket.com/kapu-lighthouse.jpg"
                }
            ]
        }
    ]
}


city_apsara_konda = {
    "state_id": ks_state_id,
    "name": "Apsara Konda",
    "hidden_gem_places": [
        {
            "name": "Apsara Konda",
            "history": {
                "text": "Apsara Konda is a scenic spot near Honnavar, named 'Pond of Angels' after local legend that nymphs bathed there. It features a 50-foot waterfall, natural pond, forested park, and mythic Pandava caves (Mahabharata exile stories). The neighboring temples, beach, and lagoon combine spiritual, historic, and coastal allure for visitors.",
                "image": "https://honavarboating.com/wp-content/uploads/2025/04/Apsarakonda-waterfall-honnavar-2.jpg"
            },
            "localCuisine": [
                {
                    "name": "Coastal food: rice, dal, fish curry, prawn fry, bamboo shoot, veg thali, puri sabzi, chai, coconut water, fresh seafood, pitha (rice cake), laru (coconut balls), payas (rice pudding), tropical fruits, home-style sweets.",
                    "image": "https://cdn.vegetariantimes.com/wp-content/uploads/2011/12/bamboo-shoot-mushroom-and-long-bean-stir-fry-dec-2011-crop.jpg?width=730"
                }
            ],
            "activities": [
                {
                    "name": "Visit Apsara Konda waterfall, bathe in the pond, see Pandava caves, walk to Maha Ganapati/Ugra Narasimha temples & Ramachandra Mutt, relax on Apsara Konda beach/Kelginoor lagoon, photography/picnics in forest park, join festivals and nature walks in the Marine Park.",
                    "image": "https://i0.wp.com/eindiatourism.in/wp-content/uploads/2024/04/Pandava_caves.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Bring cash—digital rarely accepted for entry/snacks/temples."},
                {"tip": "Sturdy footwear for rocky/wet paths."},
                {"tip": "Swim only in safe/marked areas; avoid cave climbs alone."},
                {"tip": "Guard belongings from monkeys/crowds—respect rules/signage."},
                {"tip": "Sunscreen/hat/insect repellent—site is sunny and buggy."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Honnavar town/seafood markets, Murudeshwar (Shiva statue/temple), Kasarkod Beach, Idagunji Ganapati Temple, Basavaraja Durga island fort (boat trip).",
                    "image": "https://yourbucket.com/kasarkod-beach.jpg"
                }
            ]
        }
    ]
}


city_kudremukh = {
    "state_id": ks_state_id,
    "name": "Kudremukh",
    "hidden_gem_places": [
        {
            "name": "Kudremukh National Park",
            "history": {
                "text": "Kudremukh ('horse-face') is Karnataka’s second largest wildlife park in the lush Western Ghats, named for the mountain’s profile. Once a mining area, it was declared a national park in 1987. Now a UNESCO hotspot, it protects lion-tailed macaques and rich biodiversity, with rivers that feed southern India.",
                "image": "https://res.cloudinary.com/dyiffrkzh/image/upload/c_fill,f_auto,fl_progressive.strip_profile,g_center,h_400,q_auto,w_700/v1702447807/bbj/yjygfj9q19iaw3ynyvyv.jpg"
            },
            "localCuisine": [
                {
                    "name": "Malnad thali (akki rotti, neer dosa, pundi, coconut curries), veg at homestays/lodges, South Indian classics (idli, dosa, vada, sambar, chutney, filter coffee), river fish, Maddur vada, rice cakes.",
                    "image": "https://www.cookwithkushi.com/wp-content/uploads/2021/11/IMG_4516k.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trek to Kudremukh peak/Kadambi Falls/shola grasslands, wildlife safaris/walks to see tigers, leopards, wild dogs, lion-tailed macaques, gaurs, birds; explore Bhagavathi Nature Camp/caves/Varaha shrines; birdwatch/photo; picnic by rivers.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiPIlF4hnBY_4TFcXNJgrogPdNDEga3f4Imw&s"
                }
            ],
            "safetyTips": [
                {"tip": "Bring cash; digital payment is limited beyond main villages/resorts."},
                {"tip": "Wear shoes, rainwear, earth tones for trekking/wildlife."},
                {"tip": "Get permits/guides via forest office for all treks."},
                {"tip": "Respect park rules, no litter/noise/disturbing wildlife."},
                {"tip": "Best: Oct–May; avoid monsoon (rain, leeches)."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Kalasa (Bhadra/Sri Kalaseshwara Temple), Hornadu (Annapoorneshwari Temple), Sringeri (Tunga river Matha), Bhadra Wildlife Sanctuary, Mullayanagiri (trekking/highest peak near Chikmagalur).",
                    "image": "https://yourbucket.com/bhadra-wildlife.jpg"
                }
            ]
        }
    ]
}


city_chamundi_hills = {
    "state_id": ks_state_id,
    "name": "Chamundi Hills",
    "hidden_gem_places": [
        {
            "name": "Chamundi Hills",
            "history": {
                "text": "Chamundi Hills rise to 1,000m outside Mysore and are famous for the Chamundeshwari Temple (12th c. Hoysala, expanded by Wodeyars), with its Dravidian gopuram and fierce Mahishasura Mardini idol. The huge Nandi statue (17th c.), Mahabaleswara temple, and Rajendra Vilas Palace crown a landscape rich in legend, pilgrimage, and Dasara festival traditions.",
                "image": "https://www.sandeshtheprince.com/wp-content/uploads/2020/07/chamundihills.jpg"
            },
            "localCuisine": [
                {
                    "name": "Karnataka thali (rice, sambar, rasam, bisi bele bath, poori, chutneys), South Indian tiffin (idli-vada, masala/rava dosa, upma, filter coffee), Mysore pak and milk sweets, lemon rice, fried chaat, coconut water, fruit from hilltop markets.",
                    "image": "https://www.shreemithai.com/cdn/shop/products/spl-mysore-pak-206182.jpg?v=1707820107"
                }
            ],
            "activities": [
                {
                    "name": "Pilgrimage/guided tours to Chamundeshwari, Mahabaleshwara Temple, Nandi statue, 1,000-step trek, attend Navaratri/Dasara/Ashada Fridays festivals, explore Rajendra Vilas Palace, Devikere pond, Mahishasura statue, and photo-vistas of Mysore plain.",
                    "image": "https://i0.wp.com/yatrikaone.com/wp-content/uploads/travel/destination/India/Karnataka/Mysore/india-mysore-chamundi-hills-mahishasura-10-26-19-1822-rs-wm.jpg?fit=700%2C1050&ssl=1&w=640"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—digital limited for snacks/taxis/tickets/temple donations."},
                {"tip": "Cool weather/few crowds: visit early morning/late afternoon."},
                {"tip": "Dress modestly, remove shoes for temples, watch valuables/monkeys."},
                {"tip": "Hydrate, sun protection for hilltop; little shade."},
                {"tip": "Obey festival guides/rules and hire certified guides for walks."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Mysore Palace (Dasara), Brindavan Gardens (fountains), St. Philomena’s Cathedral, Karanji Lake (bird park), Ranganathittu Bird Sanctuary (boat safaris).",
                    "image": "https://yourbucket.com/brindavan-gardens.jpg"
                }
            ]
        }
    ]
}


city_sivasagar = {
    "state_id": as_state_id,
    "name": "Sivasagar",
    "popular_places": [
        {
            "name": "Sivasagar",
            "history": {
                "text": "Sivasagar (formerly Rangpur) was capital of the Ahom Kingdom from 1699 to 1788, earning the title 'Land of Ahoms.' The Ahoms ruled Assam for nearly 600 years (1228–1826), making Sivasagar an administrative, architectural, and cultural center. Sivasagar is named after the Sivasagar tank ('Shiva’s lake'), around which temples and monuments like Sivadol, Devi Dol, Vishnu Dol, Rang Ghar, Talatal Ghar, and Kareng Palace cluster. After Burmese invasions (1819) and British annexation (1826), the city declined but remains renowned for its palaces, tanks, and temples.",
                "image": "https://yourbucket.com/sivasagar-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Assamese thali (rice, dal, aloo pitika, fish/duck curry, bamboo shoot, greens) at restaurants/homes; sweet pithas, laru, payas, puri sabzi from stalls; masor tenga (tangy fish curry), other specialties with herbs; Assam black tea in cafés.",
                    "image": "https://yourbucket.com/sivasagar-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Explore Rang Ghar, Talatal Ghar (palaces, tunnels), Kareng Palace (royal residence), Charaideo Maidams (burial mounds); visit Sivadol (tall Shiva temple), Vishnu Dol, Devi Dol by Sivasagar tank; heritage walks of Ahom monuments/tanks/maidans/colonial sites; attend festivities at temples; see Ahom Museum (artifacts, armory, culture).",
                    "image": "https://yourbucket.com/sivasagar-monuments.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash for bazaars, temples, transport—digital payments limited rural."},
                {"tip": "Dress modestly—remove shoes for shrines/temples."},
                {"tip": "Drink bottled water; check street stall hygiene."},
                {"tip": "Authorized guides best for complex site interpretation."},
                {"tip": "Use sun protection/light clothing during humid weather."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Jorhat (tea gardens, Tocklai research, culture); Majuli Island (river island, satras, crafts); Gibbon Wildlife Sanctuary (forest walks, primates); Dhekiakhowa Bornamghar (Vaishnavite prayer hall); Charaideo (burial mounds, Ahom monuments).",
                    "image": "https://yourbucket.com/rang-ghar.jpg"
                }
            ]
        }
    ]
}



city_kochi = {
    "state_id": kl_state_id,
    "name": "Kochi",
    "popular_places": [
        {
            "name": "Kochi",
            "history": {
                "text": "Kochi (Cochin), the 'Queen of the Arabian Sea,' became a key port after Kodungallur’s destruction in 1341. Its global significance drew Arabs, Chinese, Portuguese (the first European settlement in India), Dutch, and British traders/rulers, each leaving their mark—Kerala Jews, Saint Thomas Christians, mosques, and European forts all remain. Multicultural heritage appears in Fort Kochi’s colonial lanes, Chinese fishing nets, Mattancherry Palace, and vibrant markets, making the city a center of trade, tradition, and cosmopolitan life.",
                "image": "https://yourbucket.com/kochi-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala cuisine—appam with stew, meen (fish) curry, prawn fry, Malabar parotta/beef fry, spicy Kerala biryani, kappa (tapioca)/fish curry; street snacks: banana chips, pazham pori, unnakaya; Kochi-style seafood (crab roast, squid fry, karimeen) at harborfront; tropical fruit juice, coconut water, filter coffee.",
                    "image": "https://yourbucket.com/kochi-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Explore Fort Kochi’s lanes, colonial buildings, Chinese nets; visit Mattancherry Palace, Paradesi Synagogue, St. Francis Church, Santa Cruz Cathedral; see Kathakali/Theyyam/Kalaripayattu shows; take houseboat/canoe on lake/backwaters; shop antiques, spices, handicrafts in Jew Town and Broadway.",
                    "image": "https://yourbucket.com/fort-kochi.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly, especially in religious sites."},
                {"tip": "Drink bottled water; street food—watch hygiene."},
                {"tip": "Carry cash for market purchases; digital payments common at large shops."},
                {"tip": "Watch local traffic—crosswalks and signals may not be strictly followed."},
                {"tip": "Respect heritage/protected sites’ rules and photography guidelines."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Cherai Beach (swimming, dolphins, north of city); Vypin Island (backwaters, fishing); Kumbalangi (eco-tourism, rural/crab farming); Kodanad Elephant Centre (family day trip); Athirappilly Waterfalls (lush rainforest falls nearby).",
                    "image": "https://yourbucket.com/cherai-beach.jpg"
                }
            ]
        }
    ]
}

city_alleppey = {
    "state_id": kl_state_id,
    "name": "Alleppey",
    "popular_places": [
        {
            "name": "Alleppey",
            "history": {
                "text": "Alleppey (Alappuzha), the 'Venice of the East,' is famed for its scenic backwaters and canals. Its history goes back to the Sangam era (literature/archaeology), known for rice cultivation, trade, and maritime links—spice shipped to Greece, Rome, Arabia, and China. Modern Alleppey was developed in the mid-18th century by Diwan Rajakesavadas of Travancore, who built canals, roads, and port infrastructure. Under British rule, houseboat and coir industries grew, making Alleppey the Coir Capital of Kerala. Historic homes, warehouses, and waterways are still vital, and events like the Nehru Trophy Boat Race draw worldwide visitors.",
                "image": "https://yourbucket.com/alleppey-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala sadya (veg feast), appam/stew, puttu/kadala curry, fish molee at homestays/backwater eateries; prawn roast/crab fry fresh from lake; banana chips, pazham pori, Alleppey biryani, palpayasam from Ambalapuzha Temple, coir worker snacks at markets.",
                    "image": "https://yourbucket.com/alleppey-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Houseboat/canoe cruises on backwaters/canals—see paddy fields and village life; Nehru Trophy Boat Race (snake boats/music); heritage sites: Lighthouse (1862), Mullakkal Temple, St. Mary’s Church, Krishnapuram Palace; beach walks, birdwatching (Pathiramanal), cycling along waterside lanes; shop for coir, spices, handicrafts.",
                    "image": "https://yourbucket.com/alleppey-boat.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash—small shops/homestays may not take cards."},
                {"tip": "Use bottled water/care with street food (fried snacks/seafood)."},
                {"tip": "Wear sunscreen/light clothes for humid weather; insect repellent in backwaters."},
                {"tip": "Check safety/cleanliness standards before boarding houseboats; use approved guides."},
                {"tip": "Ask before photographing people, especially in churches/temples."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Ambalapuzha Sree Krishna Temple (palpayasam, fests); Krishnapuram Palace (museum, Gajendra Moksha mural); Pathiramanal Island (birdlife, boat access); Marari Beach (coastal getaway north); Kuttanad (Kerala’s rice bowl—village tours, paddy fields).",
                    "image": "https://yourbucket.com/krishnapuram-palace.jpg"
                }
            ]
        }
    ]
}


city_wayanad = {
    "state_id": kl_state_id,
    "name": "Wayanad",
    "popular_places": [
        {
            "name": "Wayanad",
            "history": {
                "text": "Wayanad—'land of paddy fields'—is Kerala’s only plateau. Habitation dates back to the Neolithic era—Edakkal cave petroglyphs (6,000 years old) prove this. Known as Mayakshetra, then Mayanad, ruled by the Veda tribe then the Gangas (10th c., 'Bayalnad'), Kadambas (11th c.), and later Vijayanagara, Mysore Wodeyars, and Pazhassi Rajas. Strategic passes connected Deccan and Malabar, attracting traders/invaders. Modern district formed in 1980.",
                "image": "https://yourbucket.com/wayanad-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Malabar parotta with spicy Kerala-style chicken/beef curry; bamboo rice dishes endemic to tribal communities/resorts; Kerala sadya (veg feast) and fish moilee (coconut stew); jackfruit chips, pazham pori, honey treats; fresh coffee, homemade chocolate from estates.",
                    "image": "https://yourbucket.com/wayanad-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trek to Chembra Peak, Banasura Sagar dam, explore Edakkal Caves; jeep/wildlife safaris in Wayanad Wildlife Sanctuary for elephants/gaurs/leopards; boating/bamboo rafting at Pookode Lake; visit Jain temples, tribal villages, spice/coffee estates; ziplining, waterfall bathing (Soochipara, Meenmutty), shop for spices/handicrafts.",
                    "image": "https://yourbucket.com/wayanad-trekking.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Wear sturdy shoes/insect repellent for treks/safaris; forest leeches/ticks common especially during monsoon."},
                {"tip": "Carry cash—card access can be unreliable in rural/tribal areas."},
                {"tip": "Drink bottled/filtered water; use permitted guides for jungle treks/night safaris."},
                {"tip": "Do not stray into core wildlife zones alone—follow forest regulations."},
                {"tip": "Observe local etiquette; some tribal hamlets/shrines require permission or have photo restrictions."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Edakkal Caves (prehistoric art/panoramic views); Banasura Sagar Dam (largest earthen dam); Kuruva Dweep (forested river island, birding, eco-walks); Tholpetty/Muthanga wildlife zones (safaris); Sultan Bathery (Jain temples, shopping, base for Ghats).",
                    "image": "https://yourbucket.com/edakkal-caves.jpg"
                }
            ]
        }
    ]
}
city_kovalam = {
    "state_id": kl_state_id,
    "name": "Kovalam",
    "popular_places": [
        {
            "name": "Kovalam",
            "history": {
                "text": "Kovalam, meaning 'grove of coconut trees,' was a quiet fishing village for centuries until Regent Maharani Sethu Lakshmi Bayi of Travancore built Halcyon Castle in the 1920s, attracting European visitors. In the 1970s, it gained national and global fame as part of the hippie trail, transforming into India’s coastal getaway. Its 1929 lighthouse is a symbol of Kovalam’s maritime history and tourism boom.",
                "image": "https://yourbucket.com/kovalam-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala seafood curries with fish, prawns, or crab from beach shacks; appam with stew, puttu/kadala curry, sadya (veg feast); banana fritters, spicy mixture, toddy, coconut water from stalls; continental/global fare at resorts.",
                    "image": "https://yourbucket.com/kovalam-seafood.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Beach bathing, swimming, sunbathing beneath coconut groves; climbing the lighthouse for views; surfing, catamaran rides, kayaking, parasailing, water skiing; Ayurvedic massages, yoga, spa therapy at resorts; festivals, village fairs, seafood barbecues on the beach.",
                    "image": "https://yourbucket.com/kovalam-beach.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Best time to visit: Sept–March for dry weather/sea safety."},
                {"tip": "Swim only in supervised areas—watch for undertow seasonally."},
                {"tip": "Dress light/modestly in public."},
                {"tip": "Carry cash for stalls, but most shops accept digital payment."},
                {"tip": "Sunscreen/use caution for valuables near sand/water."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Vizhinjam (fishing port, temples, new seaport); Poovar (backwater boating, birdwatching); Thiruvananthapuram (Kerala capital—museums, Padmanabhaswamy Temple); Vellayani Lake (picnic, boating); Neyyar Dam/Wildlife Sanctuary (treks, elephant center day trips).",
                    "image": "https://yourbucket.com/vizhinjam-port.jpg"
                }
            ]
        }
    ]
}

city_silent_valley = {
    "state_id": kl_state_id,
    "name": "Silent Valley",
    "hidden_gem_places": [
        {
            "name": "Silent Valley National Park",
            "history": {
                "text": "Silent Valley National Park, located in Palakkad district, Kerala, preserves India's last major undisturbed stretch of tropical evergreen rainforests in the Western Ghats. Discovered by botanist Robert Wight in 1847, it was declared a reserve forest in 1914. In the 1970s, a hydro-dam proposal threatened these habitats, sparking India's first major conservation movement—Save Silent Valley—which saved the region and led to its National Park status in 1984, launched in 1985 by PM Rajiv Gandhi. It is now a UNESCO Nilgiri Biosphere core zone.",
                "image": "https://yourbucket.com/silentvalley-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala vegetarian thali (rice, sambar, avial, veg curries) at forest rest houses/dhabas; banana chips, pazham pori, homemade pickle from nearby villages; filter coffee, Palakkad sweets; bring snacks/bottled water—minimal park facilities.",
                    "image": "https://yourbucket.com/silentvalley-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Guided nature walks and jeep safaris to see lion-tailed macaque, Nilgiri tahr, Malabar giant squirrel; birdwatching (over 200 species, great hornbill, whistling thrush); visit Sairandhri center/trek to Kunthipuzha River outlook; rainforest hiking, orchid/frog/butterfly photography; learn conservation history in park exhibits.",
                    "image": "https://yourbucket.com/silentvalley-trek.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Entry only with forest department permit—book all walks/safaris/guides in advance."},
                {"tip": "Best visit: Nov–March (dry); avoid monsoon (slippery/restricted trails)."},
                {"tip": "Dress full coverage; use insect repellent—leeches/mosquitos common."},
                {"tip": "Carry cash for park fees, snacks, and transport; digital payment rare rural."},
                {"tip": "Strict eco-rules: no litter/loud noise/wildlife disturbance; animal photography may require permit."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Nilambur (teak plantations/Conolly’s Plot); Attappadi (tribal reserve, eco-villages); Mannarkkad (town/accommodation/cuisine); Parambikulam Tiger Reserve (wildlife park); Ooty (hill station, Western Ghats travel).",
                    "image": "https://yourbucket.com/nilambur-teak.jpg"
                }
            ]
        }
    ]
}


city_athirappilly = {
    "state_id": kl_state_id,
    "name": "Athirappilly Falls",
    "hidden_gem_places": [
        {
            "name": "Athirappilly Falls",
            "history": {
                "text": "Athirappilly Falls, called the 'Niagara of South India,' is Kerala’s largest waterfall, located in Athirappilly Panchayat, Chalakudy Taluk, Thrissur district, on the Chalakudy River (from Western Ghats’ Sholayar ranges). Its lush rainforest region is famed for biodiversity, notably hornbill species and endangered flora/fauna. Sacred to indigenous tribes, the falls appear in folklore and films. Since the 1990s, environmental movements have protected Athirappilly from hydroelectric projects, preserving its pristine ecosystem.",
                "image": "https://yourbucket.com/athirappilly-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala fish curry, vegetarian sadya at forest lodges/eco-resorts; banana chips, pazham pori, spicy mixture from roadside stalls; fresh coconut water, tea, filter coffee available in markets.",
                    "image": "https://yourbucket.com/athirappilly-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Guided walks/treks through Vazhachal Forest and Sholayar ranges (waterfalls, rapids, wildlife); birdwatching for endangered hornbills and other rare birds; photography at Athirappilly, Vazhachal, Charpa Falls; explore bathing pools, observation points, river picnics; ecological site visits, learn local conservation/tribal heritage.",
                    "image": "https://yourbucket.com/athirappilly-trek.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Best time: June–Feb for high flow and pleasant weather."},
                {"tip": "Wear sturdy shoes, insect repellent for hikes; rocks slippery/forests dense."},
                {"tip": "Carry cash for tickets/snacks/local purchases; digital payments rare in remote areas."},
                {"tip": "Follow trails, respect boundaries; swim only in marked safe areas."},
                {"tip": "Check photography rules in tribal/protected zones."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Vazhachal Falls (trek amidst forests); Charpa Falls (seasonal, close by); Sholayar Reserve Forest (biodiversity/eco-tours); Thumboormuzhi Dam & Butterfly Park (gardens, river views); Malakkapara (tea estates, mountain drives).",
                    "image": "https://yourbucket.com/vazhachal-falls.jpg"
                }
            ]
        }
    ]
}


city_kolukkumalai = {
    "state_id": kl_state_id,
    "name": "Kolukkumalai",
    "hidden_gem_places": [
        {
            "name": "Kolukkumalai Tea Estate",
            "history": {
                "text": "Kolukkumalai tea estate, near Suryanelli (Kerala) on the border with Tamil Nadu, sits at 7,130 feet—making it the world’s highest tea plantation. Established in the early 20th century under British colonial rule, the estate uses its original factory’s orthodox (traditional) tea processing for distinct flavor and strong brew. Its history includes jeep routes, colonial-era worker quarters, and a shift to sustainable practices.",
                "image": "https://yourbucket.com/kolukkumalai-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Fresh Kolukkumalai tea, handpicked and traditionally processed; Kerala-style vegetarian sadya at local lodges/guesthouses; South Indian snacks (idli, dosa, vada, spicy chutneys) at estate canteens; mountain honey and homemade chocolates from eco-camps.",
                    "image": "https://yourbucket.com/kolukkumalai-tea.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Jeep safaris along rugged mountain trails with panoramic views of Tamil Nadu plains and Kerala hills; factory tours of old-fashioned tea processing and tastings; trekking/hiking among misty trails (waterfalls, wild orchids); sunrise/sunset photography at estate viewpoints; overnight stays for immersive mountain experience.",
                    "image": "https://yourbucket.com/kolukkumalai-jeeps.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Access via local jeep—expect rough, bumpy rides/limited road access."},
                {"tip": "Dress in layers—cold mornings/evenings."},
                {"tip": "Carry cash—card payments often not accepted at remote estates."},
                {"tip": "Confirm guide/driver certifications—self-driving not advised."},
                {"tip": "Take water/snacks/rain-wear, especially in monsoon (Aug–Oct)."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Meesapulimala Peak (treks); Devikulam & Chinnar Wildlife Sanctuary (wildlife/scenery); Munnar (hill station hub, tea museums, markets, waterfalls); Thekkady (Periyar Reserve, eco-trails); Kambam & Theni (cardamom/spice market towns).",
                    "image": "https://yourbucket.com/meesapulimala-peak.jpg"
                }
            ]
        }
    ]
}


city_marayoor = {
    "state_id": kl_state_id,
    "name": "Marayoor",
    "hidden_gem_places": [
        {
            "name": "Marayoor",
            "history": {
                "text": "Marayoor, about 40 km from Munnar in Idukki, is famous for Kerala’s only natural sandalwood forest (65,000+ trees) and its rich prehistoric heritage. The Forest Department manages a major sandalwood depot here. Megalithic dolmens (Muniyara)—over 2,000 years old—served as ancient burial chambers and show Marayoor’s archaeological significance. Ezhuthupara cave paintings are unique in Kerala. Local lore links the area to the Pandavas (Mahabharata), making Marayoor a ‘hidden land’ of Tamil/Malayalam legend.",
                "image": "https://yourbucket.com/marayoor-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Marayoor sarkara (special jaggery from sugarcane); simple Kerala vegetarian fare (rice, dal, sambar, vegetable curries—local dhabas/eateries); fresh sugarcane juice/bakery snacks from stalls; banana chips, pazham pori, homemade pickle in homestays.",
                    "image": "https://yourbucket.com/marayoor-sarkara.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trekking and walks in sandalwood forests, Muniyara dolmens/burial sites; visit Ezhuthupara for cave paintings; parks beneath banyan trees, enjoy Pambar River; witness sugarcane harvest/jaggery making (if in season); day trips to Thoovanam Waterfalls (Chinnar Sanctuary), wildlife viewing.",
                    "image": "https://yourbucket.com/marayoor-trekking.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Enter sandalwood forests only with local permission/guides—protection is strict."},
                {"tip": "Carry cash for local purchases; digital payments rare."},
                {"tip": "Wear sturdy shoes/bring sun protection for rocky terrain and outdoor activities."},
                {"tip": "Respect archaeological sites—don’t damage dolmens/cave art."},
                {"tip": "Drink bottled/filtered water; check with locals about safe food stalls."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Kanthalloor (fruit orchards, dolmens); Chinnar Wildlife Sanctuary (treks, wildlife, Thoovanam Falls); Amaravathi Dam & Crocodile Farm (Tamil Nadu, India’s largest crocodile nursery); Pambar River (nature walks); Muniyara Park (megalithic monuments, archaeology).",
                    "image": "https://yourbucket.com/chinnar-wildlife.jpg"
                }
            ]
        }
    ]
}


city_gavi = {
    "state_id": kl_state_id,
    "name": "Gavi",
    "hidden_gem_places": [
        {
            "name": "Gavi",
            "history": {
                "text": "Gavi, a serene village in Kerala’s Pathanamthitta district, lies within the Ranni reserve forest and forms part of the Periyar Tiger Reserve. Once known only to locals and tribal communities, Gavi appeared in the spotlight after the 2012 Malayalam film 'Ordinary.' Surrounded by untouched evergreen forests, it’s a recognized biodiversity hotspot and a model for Kerala’s eco-tourism since the early 2000s, focusing on low-impact, community-driven tourism. Gavi now wins awards for sustainable visitor management and wildlife conservation.",
                "image": "https://yourbucket.com/gavi-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala vegetarian thali (rice, sambar, avial, vegetable curries) at eco-camps and Forest guesthouses; local snacks—banana chips, pazham pori, spicy mixture from village shops; fresh filter coffee, black tea, coconut water at camps; simple homemade dosas, idli, sambhar for breakfast; regional pickles and local fruit.",
                    "image": "https://yourbucket.com/gavi-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Jeep safaris/nature drives in Periyar forests for elephants, gaur, Nilgiri langur, 200+ bird species; trekking to Meenar, Chenthamara Kokka, Sabarimala viewpoint/scenic overlooks; boating on Gavi lake; camping at eco-lodges/tented sites; birdwatching, butterfly walks, cardamom plantation stops; tribal village visits, nature education, photography expeditions.",
                    "image": "https://yourbucket.com/gavi-trekking.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Best visit: Sept–Feb (cool/dry); monsoon (Jun–Aug) brings heavy rain/hard travel."},
                {"tip": "Reserve entry permits and accommodation ahead through Kerala Forest Development Corp."},
                {"tip": "Carry cash for fees, snacks, guides; digital payment limited."},
                {"tip": "Only travel with licensed guides/official jeeps; no solo forest walks allowed."},
                {"tip": "Wear sturdy/light clothes, insect repellent; guard valuables from rain/humidity."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Periyar Tiger Reserve (safaris, rafting, treks); Sabarimala (hill shrine/pilgrimage, trekking trails); Vandiperiyar (plantations, tea/cardamom/spices); Kumily (market town/gateway to Thekkady); Seethathode/Meenar (hill hamlets, forest drives).",
                    "image": "https://yourbucket.com/periyar-tiger.jpg"
                }
            ]
        }
    ]
}



city_munnar = {
    "state_id": kl_state_id,
    "name": "Munnar",
    "popular_places": [
        {
            "name": "Munnar",
            "history": {
                "text": "Munnar in Idukki, Kerala, sits at 1,600m elevation and was once inhabited by Malayarayan and Muthuvan tribes. British planters led by J.D. Munro leased land from the Poonjar royal family in the late 1800s, founding tea, coffee, and cardamom estates. British companies like Kannan Devan Hills built the town and infrastructure, booming in the early 20th century. After independence, Tata-Finlay took over most holdings. Munnar is famed as ‘South India’s Kashmir’ for colonial bungalows, cool climate, and scenic hills.",
                "image": "https://yourbucket.com/munnar-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Appam with stew, puttu/kadala curry, sadhya on banana leaf; local parotta, Kerala fish curry, spicy chicken roast, cardamom sweets; plantation tea, bhajji, banana chips, home-made chocolate from stalls; mountain honey and farm cheese in cafés.",
                    "image": "https://yourbucket.com/munnar-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trekking, walks among tea estates and cardamom hills (Kolukkumalai—the world’s highest tea estate); wildlife spotting (Nilgiri tahr at Eravikulam National Park, birdwatching at Thattekad/forests); tea factory/museum tours; waterfalls (Attukal, Lakkam, Chinnakanal); boating at Mattupetty Dam; jeep safaris; tea/spice/crafts shopping at market.",
                    "image": "https://yourbucket.com/munnar-trekking.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash for purchases—ATMs/card use unreliable in hills."},
                {"tip": "Wear sturdy shoes for plantation/forest walks; mist/rain is frequent."},
                {"tip": "Drink bottled water, be selective with street food hygiene."},
                {"tip": "Dress in layers—days mild, nights chilly (especially in winter)."},
                {"tip": "Follow park/guide rules for wildlife, photography, trekking."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Eravikulam National Park (Nilgiri tahr, Neelakurinji flowers); Top Station (Western Ghat panoramas/valley views); Mattupetty Dam (boating/walks/views); Anamudi (South India’s highest peak); Marayoor (sandalwood forests, ancient dolmens).",
                    "image": "https://yourbucket.com/eravikulam-national-park.jpg"
                }
            ]
        }
    ]
}


city_kozhikode = {
    "state_id": kl_state_id,
    "name": "Kozhikode",
    "popular_places": [
        {
            "name": "Kozhikode",
            "history": {
                "text": "Kozhikode (Calicut), on Kerala’s Malabar coast, is famed as the 'City of Spices.' It was an ancient trade hub with Arabs by the 7th century, and later capital of the Zamorin kingdom. Vasco da Gama arrived in 1498, opening the sea route to Europe and drawing Portuguese, Dutch, and British interest. As a cotton center, Calicut gave 'calico' to the world, and was a multicultural trade nexus. After eras of Mysorean occupation, colonial rule, and independence, Kozhikode remains North Kerala’s economic and cultural heart.",
                "image": "https://yourbucket.com/kozhikode-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Malabar biryani, Kozhikode halwa (brown/black wheat sweet), banana chips, Kerala sadhya (vegetarian feast), fiery fish curries, parotta with beef/chicken roast; street snacks: kallummakkaya (mussels fry), unnakaya (banana stuffed fritter), pathiri (rice pancake).",
                    "image": "https://yourbucket.com/kozhikode-food.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Stroll Kozhikode Beach, visit lighthouse/pier; explore Mananchira Square and ancient Tali Shiva Temple; shop SM Street for sweets/spices/textiles; see Beypore’s handbuilt 'Uru' ships and port; nature walks at Kadalundi Bird Sanctuary, canoe rides on backwaters.",
                    "image": "https://yourbucket.com/kozhikode-beach.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly, especially at religious sites—light cottons suit Kerala’s climate."},
                {"tip": "Carry cash for small shops/stalls; digital payments accepted at larger venues."},
                {"tip": "Drink bottled water—avoid tap water in rural/market areas."},
                {"tip": "Beware strong tides during monsoon (June–Sep) at beaches."},
                {"tip": "Respect cultural norms and ask before photographing people/sites."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Beypore (wooden shipbuilding, fishing harbor); Kappad Beach (Vasco da Gama landing site); Kadalundi Bird Sanctuary (wetlands/birds); Thusharagiri Waterfalls (jungle plantation escape); Wayanad (wildlife, caves, spice plantations, accessible from Kozhikode).",
                    "image": "https://yourbucket.com/beypore-port.jpg"
                }
            ]
        }
    ]
}


city_periyar = {
    "state_id": kl_state_id,
    "name": "Periyar Tiger Reserve",
    "popular_places": [
        {
            "name": "Periyar Tiger Reserve",
            "history": {
                "text": "Periyar Tiger Reserve in Kerala's Western Ghats (Idukki district) was once ruled by Madurai's Pandyas, then Travancore kings—used as royal hunting grounds. Mullaperiyar Dam (1895) created Periyar Lake, the sanctuary’s heart. Maharaja Chithira Thirunal set aside land as Nellikkampatty Game Sanctuary (1934), then the Periyar Wildlife Sanctuary (1950), re-designated as Tiger Reserve under Project Tiger (1978). Now 925+ sq km, Periyar is renowned for Bengal tigers, elephants, gaurs, and rare birds.",
                "image": "https://yourbucket.com/periyar-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala vegetarian thali (rice, sambar, avial, curries) at lodges; appam/stew, idiyappam, puttu/kadala curry in Thekkady/Kumily; banana fritters, Kerala chips, black tea at camps; fish curry (karimeen, tilapia) at lake-edge guesthouses.",
                    "image": "https://yourbucket.com/periyar-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Jeep/boat safaris on Periyar Lake for spotting tigers, elephants, gaurs, water birds; guided walks, bamboo rafting, birdwatching (265+ species), butterfly trails; night patrol/eco-treks with tribal guides; Tribal Heritage Museum; local craft/village culture; spice, ayurveda, tea shopping in Thekkady markets.",
                    "image": "https://yourbucket.com/periyar-safari.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Visit Nov–May for easy wildlife viewing; monsoon brings rain and bugs."},
                {"tip": "Carry cash—digital payment options limited in forest areas."},
                {"tip": "Obey guides, stay on trails, avoid loud noises/littering."},
                {"tip": "Wear full-coverage clothes, insect repellent, sturdy shoes for hikes."},
                {"tip": "Photography may be restricted in tribal/research sites—always ask."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Thekkady (main town—hotels, plantations, walks); Mangala Devi Temple (ancient forest temple, open select days); Gavi Forest (deep eco-trekking and camping); Kumily (market town for spices, ayurveda); Cardamom Hills (scenic treks/drives).",
                    "image": "https://yourbucket.com/thekkady-town.jpg"
                }
            ]
        }
    ]
}


city_sabarimala = {
    "state_id": kl_state_id,
    "name": "Sabarimala",
    "popular_places": [
        {
            "name": "Sabarimala Temple",
            "history": {
                "text": "Sabarimala Temple in Kerala is a famous Hindu pilgrimage devoted to Lord Ayyappa, son of Shiva and Vishnu (Mohini). Set atop Sabarimala hill in the Periyar Tiger Reserve, legend ties it to Ayyappa’s victory over a demon and meditation at this spot. Built originally by King Rajashekara of Pandalam, with the idol believed installed by Parasurama on Makara Sankranti, the shrine became widely visited after the 12th century, surviving destruction and restoration. The temple opens only on select days, drawing millions for Mandala Pooja, Makara Vilakku, Sankranti, and the start of each Malayalam month.",
                "image": "https://yourbucket.com/sabarimala-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala vegetarian thali and sweet payasam prasad; idli, dosa, vada, upma at pilgrim rest houses/forest camps; banana chips, pazham pori, Kerala mixture from local stalls; filter coffee/coconut water at Pamba base camp and Erumeli.",
                    "image": "https://yourbucket.com/sabarimala-prasad.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Pilgrimage trek (4+km forest hike from Pamba), ritual river bathing, ascent of 18 sacred steps; sunrise viewing and Makara Jyothi sacred light festival (Jan); darshan of Lord Ayyappa idol, shrines to Malikappurathamma and Vavar; rituals after 41 days vratham (austerity); exploring Periyar forest, participating in festivals and music.",
                    "image": "https://yourbucket.com/sabarimala-trek.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Pilgrimage is a tough trek—ensure fitness and good shoes."},
                {"tip": "Strict rules: Only men and women over 50/below 10 allowed (check current updates)."},
                {"tip": "Follow dress code: black/blue dhoti, no shirts, bead necklace for vratham."},
                {"tip": "Carry cash; cards rarely accepted in forest/temple area."},
                {"tip": "Avoid valuables; observe bathing/worship rules, photography restricted inside temple."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Pamba River (sacred bathing camp); Erumeli (start of forest pilgrimage route); Periyar Tiger Reserve (wildlife/forest trips); Pandalam (royal palace/shrines); Nilackal and Vavar Shrine (historic pilgrimage waypoints).",
                    "image": "https://yourbucket.com/pamba-river.jpg"
                }
            ]
        }
    ]
}


city_kumarakom_bird_sanctuary = {
    "state_id": kl_state_id,
    "name": "Kumarakom Bird Sanctuary",
    "popular_places": [
        {
            "name": "Kumarakom Bird Sanctuary",
            "history": {
                "text": "Kumarakom Bird Sanctuary (Vembanad Bird Sanctuary) on Vembanad Lake, Kottayam, began as 'Baker’s Estate' in 1847 when George Alfred Baker planted mangroves, creating a haven for native/migratory birds. The estate became a formal bird sanctuary (now 14 acres, Kerala Tourism managed), recognized as India’s first scientifically preserved bird site, supporting 180+ bird species.",
                "image": "https://yourbucket.com/kumarakom-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala specialties—karimeen (pearl spot) fry, fish curry, appam, traditional veg sadya at guesthouses/lakeside eateries; banana chips, pazham pori, spicy mixtures for snacks; toddy, coconut water, filter coffee from lake shacks.",
                    "image": "https://yourbucket.com/karimeen-fry.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Birdwatching: spot waterfowl, egrets, herons, cormorants, moorhen, darters, brahminy kite, Siberian stork, gulls, teal and terns (Nov–Mar); walking trails, butterfly watching, nature photography in mangroves/wetlands; guided boat or houseboat tours on Vembanad Lake for birds/scenic views; visit Pathirmanal, Narakathara, Thollairam Kayal.",
                    "image": "https://yourbucket.com/kumarakom-birding.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry cash for tickets, snacks, local shops; digital wallets limited."},
                {"tip": "Wear full-coverage clothes and insect repellent for wetland bugs."},
                {"tip": "Respect sanctuary timings/rules, do not litter/interact with wildlife."},
                {"tip": "Use authorized guides for boat tours and marked trails; avoid private land/undergrowth."},
                {"tip": "Best birding: November–March."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Vembanad Lake (houseboat/canoe experiences); Pathirmanal Island (migratory birds); Aruvikkuzhi Waterfalls (picnics/trails); Kottayam (temples, churches, museums); Kerala Backwaters (village/coir workshops, paddy fields, boats).",
                    "image": "https://yourbucket.com/vembanad-lake.jpg"
                }
            ]
        }
    ]
}


city_padmanabhaswamy_temple = {
    "state_id": kl_state_id,
    "name": "Padmanabhaswamy Temple",
    "popular_places": [
        {
            "name": "Padmanabhaswamy Temple",
            "history": {
                "text": "Padmanabhaswamy Temple in Thiruvananthapuram, Kerala, dedicated to Lord Vishnu, is among India’s most ancient shrines. References date to at least the 8th–9th centuries. It rose to prominence under Travancore kings, especially Marthanda Varma (18th century), who surrendered his kingdom to the deity, ruling as Padmanabha Dasa. The 18-foot Vishnu idol in 'Anantha Shayana' posture was rebuilt with 12,008 sacred stones in 1739. The temple and its vast hidden vaults are legendary for immense wealth and treasure.",
                "image": "https://yourbucket.com/padmanabhaswamy-history.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kerala sadya (vegetarian banana leaf feast), temple prasad (sweet payasam), appam/stew, puttu/kadala curry, idiyappam, banana chips, pazham pori, spicy snacks, filter coffee, coconut water from temple shops.",
                    "image": "https://yourbucket.com/kerala-sadya.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Temple darshan—viewing the reclining Vishnu idol through three doors; exploring the 100-ft gopuram, stone corridors, chuttambalam, sacred tank; experiencing Equinox solar alignment; visiting mural halls, shrines, joining rituals/festivals; touring the fort, shopping crafts, and enjoying local arts in Thiruvananthapuram.",
                    "image": "https://yourbucket.com/padmanabhaswamy-idol.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Only Hindus permitted inside inner temple; others may view exteriors/festivals."},
                {"tip": "Strict dress code: men in mundu (dhoti, no shirt); women in sari or full-length skirt/blouse."},
                {"tip": "No footwear, bags, cameras, or mobiles allowed inside."},
                {"tip": "Carry cash for tickets, shops, offerings—digital payment is limited."},
                {"tip": "Respect temple customs, photography bans, avoid heavy festival days for comfort."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Kuthira Malika Palace (royal wood-carved residence); Napier Museum (Kerala art/history); Shri Chitra Art Gallery (Ravi Varma art); Kovalam Beach (iconic seaside); Ponmudi Hills/Neyyar Sanctuary (nature excursions from city).",
                    "image": "https://yourbucket.com/kuthira-malika.jpg"
                }
            ]
        }
    ]
}


city_purmandal = {
    "state_id": jk_state_id,
    "name": "Purmandal",
    "hidden_gem_places": [
        {
            "name": "Purmandal",
            "history": {
                "text": "Purmandal, 'Chhota Kashi,' is a sacred village 30–40 km southeast of Jammu, known for its cluster of ancient Shiva and Parvati temples along the Devika River. Dating back 1400+ years, credited to Raja Veni Dutt of Kashmir, the temples feature Gupta, Maurya, and Dogra architectural elements. The Devika is regarded as the Ganges’ manifestation, said to cleanse sins like Haridwar/Kashi. The Umapati Shiva shrine is famed for its Svayambhuvalinga, local lore, wall frescoes, and historic visits by Guru Nanak and Maharaja Ranjit Singh.",
                "image": "https://tse1.mm.bing.net/th/id/OIP.f3u-kFs8uBUPxsTlb2_DUgHaFj?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Simple vegetarian fare—rajma chawal, sabzi, roti, curd from local dhabas; north Indian snacks (samosa, kachori, tea) in village/town; prasadam from temples, with sweets/dried fruits for festivals.",
                    "image": "https://tse4.mm.bing.net/th/id/OIP.st8jUn96FPmCUDczmjFA_QHaHa?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Exploring temple clusters (Shiva, Parvati, Nagdev) of stone architecture and frescoes; ritual bathing in Devika River ('Gupt Ganga'), believed to grant moksha; attending Purmandal Mela (Feb/March)—local crafts, music, festivals of Shiva-Parvati’s marriage; observing or joining Shivratri, Navratri, and other celebrations.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.fND6rtIFBg_8SSLHPUVtOQHaE6?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly; cover arms/legs; remove shoes in shrines/river banks."},
                {"tip": "Carry cash; digital payments rare outside Jammu city."},
                {"tip": "Respect customs at rituals; ask before photographing interiors/ceremonies."},
                {"tip": "Be cautious bathing in Devika—strong currents/monsoon and slippery banks."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Uttarbehni (river pilgrimage, peacocks, temples); Samba Fort (historic fort nearby); Surinsar/Mansar Lakes (picnics, boating, birdwatching); Peer Kho Cave Temple (ancient Shiva shrine, Jammu); Jammu city (Raghunath Temple, Mubarak Mandi Palace, markets).",
                    "image": "http://www.kashmirhills.com/wp-content/uploads/2015/02/surinsar-lake-2.jpg"
                }
            ]
        }
    ]
}


city_sinthan_top = {
    "state_id": jk_state_id,
    "name": "Sinthan Top",
    "hidden_gem_places": [
        {
            "name": "Sinthan Top",
            "history": {
                "text": "Sinthan Top is a remote, high-altitude mountain pass between Anantnag (Kashmir Valley) and Kishtwar (Jammu). For centuries a grazing ground for nomads and a route linking Kashmir to Chenab Valley, it is now a popular spot after development of the Anantnag–Kokernag–Kishtwar highway. Sinthan Top offers panoramic Himalayan views, adventure trekking, and stunning road trip scenery.",
                "image": "https://tse3.mm.bing.net/th/id/OIP.I4CPr5R9inKp6iGlEDpxCAHaEK?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Kashmiri staples—Rogan Josh, Dum Aloo, Girda bread in dhabas/eateries near the route; noon chai, kahwa, hot Maggi as trekking snacks; fresh trout from streams in guesthouses/villages.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.4GGXJWCQqfiiJjcgIXp3pAHaE-?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Trekking, hiking, road trips to the 12,500 ft summit (photography, 360° views, nature walks); snow activities (skiing, snow walks) in spring/summer—snow remains much of the year; bird watching, camping, picnics by mountain streams; scenic drives via Kokernag, Daksum, Achabal, onward to Margan Top.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.1vGTVAjnoJrypLmic8QibgHaE7?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Visit April–Sep for best access; winter snowblocks and extreme conditions."},
                {"tip": "Dress warmly in layers; snow/ice remain into June."},
                {"tip": "Carry cash—no shops, ATMs, or card options at summit."},
                {"tip": "Use registered guides/drivers; drive cautiously—roads winding/slippery."},
                {"tip": "Respect customs/grazing areas; ask before photographing locals/livestock."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Kokernag Spring (picnic spot); Daksum (health resort, pine woods/trout streams); Achabal Garden (Mughal park); Margan Top (trekking, dramatic pass); Kishtwar town (historic trade/culture hub via the pass).",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.D-XxicbhXEaUZMfIBVSR8QHaE7?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

city_doodhpatri = {
    "state_id": jk_state_id,
    "name": "Doodhpatri",
    "hidden_gem_places": [
        {
            "name": "Doodhpatri",
            "history": {
                "text": "Doodhpatri, the 'Valley of Milk,' is a tranquil hill station in Budgam, 42 km from Srinagar at 8,957 ft in the Pir Panjal mountains. Its legend: Nund Rishi struck earth seeking water for prayers—milk flowed, then turned to water for ablution, giving the meadows their name as streams appear white and cold year-round. Traditionally used as grazing pastures, the valley remained unexplored until recent tourism.",
                "image": "https://tse3.mm.bing.net/th/id/OIP.osW_75t9_VrAjDckDmoCCwHaE8?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Simple Kashmiri village cuisine—Rogan Josh (lamb curry), Dum Aloo, Yakhni from homestays/tea stalls; noon chai, kahwa, girda bread; fresh trout from streams/villages; hot Maggi at meadow huts.",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.9yJuvhr4FBRQF-Iaha9WyQHaJ4?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Trekking through meadows, pine forests, wildflowers, and milky streams; horse riding/guided walks to viewpoints; picnics, photography, migratory/Himalayan birdwatching; camping/village tours with shepherds; visiting Tosamaidan or Chang meadows for mountain views.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.KagKYe4KZeSW6l6cuz4xPAHaE7?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Visit May–Sep for green meadows/treks; winter brings snow, often blocking access."},
                {"tip": "Carry cash; shops/accommodation/food options are basic, card use rare."},
                {"tip": "Dress in layers; nights are cold even in summer, and rain is sudden."},
                {"tip": "Use authorized local guides for trekking, horse riding, village stays."},
                {"tip": "Respect rural/pastoral customs; always ask before photographing locals/livestock."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Tosamaidan (expansive pasture/former Mughal route); Khag village (historic shepherd/craft hub); Chang meadows (valleys, flowers, forest walks); Yousmarg (nearby alpine meadow for birding/hiking); Budgam (district HQ, markets, Sufi shrines).",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.SzPL2Qmyxy94W3LArChmsAHaE0?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}


city_gurez_valley = {
    "state_id": jk_state_id,
    "name": "Gurez Valley",
    "hidden_gem_places": [
        {
            "name": "Gurez Valley",
            "history": {
                "text": "Gurez Valley, at 2,400 meters in Bandipora district, was once part of ancient Dardistan and the Silk Route, connecting Kashmir to Central Asia via Gilgit. The capital Dawar features archaeological sites with Kharoshthi, Brahmi, and Tibetan inscriptions; Kanzalwan holds Buddhist relics and the last council of Buddhism in the region. Gurez’s Dardic/Shin communities retain unique customs and language. Closed to tourism for decades, it only opened in the 21st century, remaining vital to Kashmiri culture and military history.",
                "image": "https://tse4.mm.bing.net/th/id/OIP.KEcutj298jBm4ZPcmCSNigHaFj?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Local Kishanganga fish prepared by Dard families; Kashmiri Rogan Josh, Dum Aloo, Nadru Yakhni in Dawar/Gurez eateries; Dardic breads, rural dishes (lentils, rice, mountain vegetables); noon chai, kahwa, girda bread in homestays and tea shops.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.fIAYYNY5iKqk9vvKXLNtagHaEN?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Trekking, hiking, and camping along Kishanganga River with Habba Khatoon peak views; visiting shrines of local saints; exploring ancient ruins and archaeological sites; interacting with locals on Silk Route legends; birding, fishing, seasonal photography of raspberry/walnut groves and alpine wildlife.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.MHhx62vgbvdy6HcCpM_tFgHaEv?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Accessible June–Sep; Razdan Pass/roads close in winter (heavy snow)."},
                {"tip": "Carry cash; few ATMs and unreliable digital payments; homestays are basic but welcoming."},
                {"tip": "Respect security/army restrictions—carry ID, stay clear of military zones."},
                {"tip": "Dress in warm layers; nights freezing even in summer."},
                {"tip": "Use registered guides; avoid solo treks in remote areas."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Dawar (ancient capital, stone homes/shrines), Kanzalwan (Buddhist/Dardic archaeological sites), Habba Khatoon peak (trekking, folklore), Razdan Pass (gateway, Himalayan views), Sharda Peeth/Drass (via passes—old Silk Route/pilgrimage towns).",
                    "image": "https://curlytales.com/wp-content/uploads/2023/11/Travelling-To-Kashmir-Here-Are-4-Tourist-Things-To-Do-In-Dawar-Village.jpg"
                }
            ]
        }
    ]
}

city_yusmarg = {
    "state_id": jk_state_id,
    "name": "Yusmarg",
    "popular_places": [
        {
            "name": "Yusmarg",
            "history": {
                "text": "Yusmarg, the 'Meadow of Jesus,' is a peaceful alpine valley in Budgam district—formerly Roosmarg—once inhabited only by wildlife and herders. Its legend says Jesus Christ visited during his 'lost years.' With pristine meadows, forests, and Pir Panjal peaks, modern tourism only began in the 20th century, and it remains an offbeat wilderness gem.",
                "image": "https://tse3.mm.bing.net/th/id/OIP.N-Jxfr175cUhrNz1kSuhvQHaD4?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Kashmiri Rogan Josh, Dum Aloo, Modur Pulao (sweet rice), Gogji Raazma (turnip/beans), Wazwan specialties; café items like noon chai, kahwa, girda breads, cookies; Maggi, chai at trekking spots.",
                    "image": "http://pulses.org/images/com_yoorecipe/cropped-rajma-gogji.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trekking to Doodh Ganga River and Nilnag Lake for scenery, fishing, forest hikes; horse riding in meadows/pine woods; picnics, visiting Sang-e-Safed Valley; photography, camping, and digital detox amid quiet nature.",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.-JRjab1NEOVUzcGvzTU40wHaEe?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Visit May–Sep for mild weather/flowers or Nov–Feb for snow (down to −2°C)."},
                {"tip": "Dress in layers for chilly nights/weather shifts."},
                {"tip": "Use only authorized guides/pony owners for treks or off-trail rides."},
                {"tip": "Carry cash; card facilities and ATMs are rare."},
                {"tip": "Respect customs at Sufi shrines (Charar-e-Sharif); dress/act soberly."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Nilnag Lake (blue mountain lake by hike/pony), Doodh Ganga (milky stream for walks/fishing), Sang-e-Safed Valley (white stones, trekking), Charar-e-Sharif (Sufi shrine, 17km away), Tosa Maidan (remote meadow for adventure/backcountry camping).",
                    "image": "https://kashmirmountains.com/wp-content/uploads/KGL-63.jpg"
                }
            ]
        }
    ]
}


city_patnitop = {
    "state_id": jk_state_id,
    "name": "Patnitop",
    "popular_places": [
        {
            "name": "Patnitop",
            "history": {
                "text": "Patnitop is a tranquil hill station in the Lower Himalayas, surrounded by deodar forests and valleys. Historically it was a caravan rest stop on Kashmir–northern plains trading routes, becoming popular with Dogra rulers and British officers in colonial times. Tourism grew with Vaishno Devi pilgrimage and the Patnitop Tunnel in the 21st century made access easier.",
                "image": "https://www.tourmyindia.com/socialimg/patnitop-tour-packages.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rajma chawal (regional classic), kalaadi cheese (fried dairy specialty), north Indian meals (aloo paratha, dal, sabzi, curd at dhabas), street snacks, tea and sweets in Kud and Batote.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.T4LM-WzqELyvikRknrJbyAHaEK?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Trekking/nature walks in deodar forests (Natha Top, Sanasar Lake, Billoo Ki Powri steps); paragliding and gondola rides at Dawariyai/Sanget; skiing/sledding at Natha Top in winter; visiting Sudh Mahadev Temple, Naag Mandir, and folklore springs; horse riding and picnicking at Kud Park and meadows.",
                    "image": "https://c8.alamy.com/comp/2RRA89X/kinnaur-valleys-deodar-forest-amidst-deep-himalayan-valleys-himachal-pradesh-india-2RRA89X.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress in layers; summer is cool, winter brings snow and winds."},
                {"tip": "Carry cash; ATMs/digital payments unreliable in remote places."},
                {"tip": "Avoid trekking/travel at night, especially in winter/monsoon—trails can be slippery."},
                {"tip": "Use registered guides for sports; check safety gear before paragliding/sledding."},
                {"tip": "Respect spiritual sites—remove shoes, observe temple etiquette."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Natha Top (trekking, skiing, views); Sanasar (paragliding, climbing, tulip gardens); Sudh Mahadev Temple (ancient Shiva shrine/spring); Bhaderwah (lush hill town, temples); Baglihar Dam (hydroelectric dam along the Chenab River).",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.rGOeYkOQ4MCS4Z9zbHoWOwHaE8?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}


city_katra = {
    "state_id": jk_state_id,
    "name": "Katra",
    "popular_places": [
        {
            "name": "Katra Base & Pilgrimage Route",
            "history": {
                "text": "Katra, at the foothills of the Trikuta Mountains, is best known as the base camp for the revered Vaishno Devi Temple, India’s major pilgrimage destination. Town history reflects the shrine’s legend, attributed to Pandit Shridhar 700 years ago. 'Katra' comes from Arabic for 'caravan,' reflecting its past as a resting place for Kashmir–plains traders. British transport hubs and modern access have enabled millions of pilgrims to visit each year.",
                "image": "https://tse1.mm.bing.net/th/id/OIP.tWCqoMvJ2cnzNEw_xng2nQHaFj?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Rajma chawal and kalaadi cheese (regional specialties); north Indian vegetarian thalis (aloo paratha, dal, curd, sabzi); street snacks (samosas, kachoris, tea); traditional temple prasadam—dry fruits, sweets, nuts.",
                    "image": "http://eastindianrecipes.net/wp-content/uploads/2023/02/Chicken-Thali-Indian-Thali-Recipe7.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Pilgrimage trek (13km) to Vaishno Devi Temple on scenic mountain paths; visiting Ardh Kuwari Cave (spiritual stop); exploring Bhairavnath Temple and Banganga along the route; enjoying panoramic views and serene walks near Banganga River; shopping crafts/woolens/memorabilia in Katra’s markets.",
                    "image": "https://www.pilgrimagetour.in/blog/wp-content/uploads/2023/12/Best-Time-To-Visit-Mata-Vaishno-Devi-Temple.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Visit March–October for best weather; winter is cold, monsoon slippery."},
                {"tip": "Wear comfortable shoes and layered clothes; temperatures change along the climb."},
                {"tip": "Carry cash; digital payments/ATMs can be limited in busy pilgrimage times."},
                {"tip": "Prefer registered hotels/transport; crowds at festivals so secure valuables."},
                {"tip": "Follow temple customs: dress modestly, remove shoes at shrines, respect rituals/photography rules."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Ardh Kuwari Cave (spiritual cave en route), Bhairavnath Temple (ancient end-point site), Banganga River (sacred, tranquil walks), Shivkhori Cave Temple (famous shrine, 70km away), Patnitop (hill station, panoramic views, day trip).",
                    "image": "https://tse4.mm.bing.net/th/id/OIP.T9ESslHN2snVMhzajwyh5wHaFA?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

city_wular_lake = {
    "state_id": jk_state_id,
    "name": "Wular Lake",
    "popular_places": [
        {
            "name": "Wular Lake",
            "history": {
                "text": "Wular Lake in Bandipora, Kashmir, is India’s largest freshwater lake and Asia’s second largest, formed by tectonic activity. Known as Mahapadmasar or Ullola in Sanskrit, it’s tied to the mythical Satisar. Sultan Zain-ul-Abidin built Zaina Lank island on the lake in 1444. Wular has long played a role in trade, ritual, and Kashmiri legend; it was named a Ramsar Wetland of International Importance in 1990.",
                "image": "https://tse1.mm.bing.net/th/id/OIP.L47g_t7-dsEpPplkt5wLjwHaEc?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Freshwater fish (trout, carp) from local fishermen in villages/restaurants; Kashmiri Rogan Josh, Dum Aloo, Nadru Yakhni near the lake; noon chai and kahwa with girda bread; apples, cherries, lakeside snacks at markets (especially during bird migration/lotus bloom).",
                    "image": "https://tse4.mm.bing.net/th/id/OIP.uI8gWhOMxYHuE4BItyr6vQHaKG?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Shikara/boat rides to floating gardens (best in summer/autumn); birdwatching (migratory ducks, herons, kingfishers); visit and photograph Zaina Lank island with Himalaya views; nature walks in Garoora Park or wetlands; heritage/eco-tours; visit fishing villages, learn about lotus farming.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.JxiUGZsxAvaR7sUnzPQ7RQHaE8?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Best visit: May–Oct (lotus bloom); winter can be cold/partially frozen."},
                {"tip": "Use certified boats only; swimming is unsafe (currents/vegetation)."},
                {"tip": "Carry cash—few digital options in villages/markets."},
                {"tip": "Layered clothes/sunscreen; mountain weather can change quickly."},
                {"tip": "Respect customs, don't litter/disturb birds; see photo rules in religious/docked areas."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Bandipora town (markets, shrines, crafts); Garoora Wular Park (walks, birding); Manasbal Lake (sports, lotus); Dal Lake shikara/floating gardens (Srinagar); old shrines/temples in lakeside villages.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.K8zQW2iLvLAO6BrmzwWVZAHaE6?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}



city_jama_masjid = {
    "state_id": jk_state_id,
    "name": "Jama Masjid",
    "popular_places": [
        {
            "name": "jama Masjid",
            "history": {
                "text": "jama Masjid, in Nowhatta area of old Srinagar, was commissioned in 1394–1402 AD by Sultan Sikandar Shah and expanded by his son Zain-ul-Abidin. For 600+ years, it has been a spiritual and cultural hub with Persian and Indo-Saracenic architecture. The mosque was damaged by fire and reconstructed several times (1479, 1620, 1672). During the Sikh Era it faced closures, but remains a symbol of religious and community life in Kashmir.",
                "image": "https://cdn.siasat.com/wp-content/uploads/2019/12/Kashmir-Biggest-Mosque-Reopened-AFP1.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kashmiri Rogan Josh, Gustaba, Dum Aloo, Nadru Yakhni from nearby restaurants/markets; seekh kebabs, girda bread as street snacks; noon chai, kahwa from neighborhood tea stalls.",
                    "image": "https://tse4.mm.bing.net/th/id/OIP._sgoHR95e3Jokrw04bLpRAHaEU?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Exploring the mosque complex with 378 wooden deodar pillars and peaceful courtyard; photography of Kashmiri and Indo-Saracenic architecture; participating in Friday prayers and religious gatherings; shopping for handicrafts, spices, dry fruits in vibrant Nowhatta markets.",
                    "image": "https://c8.alamy.com/comp/2REKNEH/nowhatta-srinagar-jammu-and-kashmir-india-october-25-2022-man-walking-by-an-outdoor-clothing-market-2REKNEH.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly, covering arms/legs; headscarves appreciated for women inside."},
                {"tip": "Photography may be restricted during prayers—check rules and seek permission."},
                {"tip": "Remove shoes before prayer halls; avoid peak crowds for quiet visits."},
                {"tip": "Carry cash for old city markets; card acceptance is rare in this area."},
                {"tip": "Respect ongoing prayers and customs, especially during festivals/Friday gatherings."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Hari Parbat Fort (historic fort with panoramic views); Shah-e-Hamadan Mosque (ancient riverside mosque); Old Srinagar markets (spices, saffron, crafts); Shankaracharya Temple (hilltop temple with valley views); Dal Lake and Makhdoom Sahib Shrine (iconic spiritual/natural sites).",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.isqdnRQORhjXSJA0zSViiQHaEK?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}


city_sonamarg = {
    "state_id": jk_state_id,
    "name": "Sonamarg",
    "popular_places": [
        {
            "name": "Sonamarg",
            "history": {
                "text": "Sonamarg, the 'Meadow of Gold,' is an alpine hill station in Ganderbal, strategically on the ancient Silk Road connecting Kashmir, Tibet, and Central Asia. Historically used by nomadic shepherds, traders, and pilgrims for millennia. Sacred as an Amarnath Yatra starting point; ruled by Mauryas, Kushanas, Mughals, Sikhs, and vital in regional military and cultural history.",
                "image": "https://tse2.mm.bing.net/th/id/OIP.sIDYI_OTbQX80PtdGdJm4QHaEo?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Kashmiri Rogan Josh, Dum Aloo, Yakhni at resorts/huts; baqerkhani, sheermal breads, fresh trout from Sindh River; noon chai, kahwa, street snacks from highway stalls; simple vegetarian dhaba options during Amarnath Yatra.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.jy2B337RTydzjgMo0vKGLAHaEK?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Trekking to Thajiwas Glacier, Vishansar, Krishansar, Gangabal, Satsar Lakes; pony rides to glacier; white-water rafting on Sindh River; scenic drives via Zoji La Pass; camping, trout fishing, photography of Himalayan meadows and peaks.",
                    "image": "https://www.tourmyindia.com/socialimg/thajiwas-glacier-sonmarg.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Visit May–Sep; winter snow/avalanches block access."},
                {"tip": "Dress in layers; summer nights are chilly—waterproof gear for trekking."},
                {"tip": "Only use registered guides for treks/glacier walks/rafting."},
                {"tip": "Carry cash and medication—facilities rare outside Srinagar."},
                {"tip": "Respect local customs; follow instructions during pilgrimages; avoid isolated trails after dusk."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Thajiwas Glacier (pony/foot hikes, summer snow); Zoji La Pass (gateway to Ladakh, historic/scenic); Vishansar & Krishansar Lakes (trekking, angling); Nilagrad River (reddish sacred waters, picnic spots); Baltal Valley (Amarnath base camp, camping).",
                    "image": "https://thumbs.dreamstime.com/b/zojila-pass-most-beautiful-world-85176928.jpg"
                }
            ]
        }
    ]
}


city_pahalgam = {
    "state_id": jk_state_id,
    "name": "Pahalgam",
    "popular_places": [
        {
            "name": "Pahalgam",
            "history": {
                "text": "Pahalgam, the 'Valley of Shepherds,' lies at the confluence of the Lidder River and Sheshnag Lake. Its roots are in Hindu mythology and ancient saints, and it was ruled by Mughal and Hindu dynasties, with British and European visitors arriving in the colonial era. Today, it’s best known as the start point for the Amarnath Yatra and for spiritual sites like Mamleshwar Temple and the 8th-century Martand Sun Temple.",
                "image": "https://kashmirlife.net/wp-content/uploads/2023/06/BVP1.jpg"
            },
            "localCuisine": [
                {
                    "name": "Kashmiri Rogan Josh, Dum Aloo, Nadru Yakhni from restaurants and resorts; fresh trout from Lidder River (fried or grilled), Mughlai and vegetarian meals during pilgrimages, street snacks: seekh kebabs, kulfi, noon chai, kahwa, and South Indian fast food in the market.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.pmW0To-1Ckk7SHR-nn745AHaHa?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Trekking/walking to Baisaran, Aru, or Betaab Valleys; trout fishing; exploring Mamleshwar Temple, Martand Sun Temple, Sufi shrines; white-water rafting, golfing, snow-sledding, and skiing in winter.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.RqajicYdSllcVQZhHqO7tQHaEj?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Visit May–Oct for best weather; winters are harsh/snowy and close some trails."},
                {"tip": "Carry cash; digital payments and ATMs are limited in outlying areas."},
                {"tip": "Respect temple and shrine customs, dress modestly, and avoid unauthorized photography."},
                {"tip": "Use registered guides for trekking; heed all advisories."},
                {"tip": "Stay cautious during festivals or political events; large crowds and security issues have occurred."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Betaab Valley (scenery, Bollywood films, picnics), Aru Valley (meadows, starting treks), Baisaran Valley (forests, pony rides), Sheshnag and Tulian Lakes (glacial, trekking), Martand Sun Temple (8th-century marvel), Overa-Aru Wildlife Sanctuary (Himalayan fauna, birdwatching).",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.4J96P85X6hv8Vjd7q0wcCAAAAA?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

city_gulmarg = {
    "state_id": jk_state_id,
    "name": "Gulmarg",
    "popular_places": [
        {
            "name": "Gulmarg",
            "history": {
                "text": "Gulmarg, meaning 'meadow of flowers,' was renamed by Sultan Yusuf Shah Chak in the 16th century (previously Gaurimarg for Goddess Parvati). Mughal emperor Jahangir loved its wildflowers, while the British built golf courses and a ski club in the 19th–20th centuries. Since independence, it was a pivotal site in the 1947 Kashmir conflict and is now a famous ski resort and army training center.",
                "image": "https://tse4.mm.bing.net/th/id/OIP.A4L_s6r0OKgiwxr8BNbY9gHaE8?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Rogan Josh, Dum Aloo, Yakhni, Haak, Gushtaba, Rista, Noon Chai, Kahwa, Guchhi Pulao, lotus stem dishes, fresh trout, kebabs, and bakery treats—all classic Kashmiri mountain foods for chilly weather.",
                    "image": "https://images.squarespace-cdn.com/content/v1/578753d7d482e9c3a909de40/569a7114-71ec-4dc8-8130-bb119e74d17a/DSC03440.JPG"
                }
            ],
            "activities": [
                {
                    "name": "Skiing, snowboarding, and winter sports; riding the Gulmarg Gondola (one of the highest cable cars); trekking to Alpather Lake; golfing at the world's highest green golf course; biosphere reserve walks; Outer Circle Walk; visiting St. Mary's Church; handicraft shopping.",
                    "image": "https://tse4.mm.bing.net/th/id/OIP.Hc8A8Qz4kcd8n3ahx4AivQHaEK?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Carry layered, waterproof clothing—weather shifts quickly and winters can be extreme."},
                {"tip": "Use certified guides and ski instructors for winter sports."},
                {"tip": "Cash is best for small purchases; ATMs may be limited during peak times."},
                {"tip": "Be cautious off marked trails—respect local safety advisories."},
                {"tip": "Book stays in advance during ski season and holidays."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Alpather Lake (high-altitude, often frozen); Gulmarg Biosphere Reserve (endangered flora/fauna, wildlife walks); Tangmarg (apple orchards, scenic drives); Shrine of Baba Reshi (Sufi shrine in meadows); Khilanmarg (wildflowers, panoramic Himalayan views).",
                    "image": "https://indiachalk.com/wp-content/uploads/2022/05/Gulmarg-For-an-Adventurous-Trip-48.jpg"
                }
            ]
        }
    ]
}

city_srinagar = {
    "state_id": jk_state_id,
    "name": "Srinagar",
    "popular_places": [
        {
            "name": "Dal Lake",
            "history": {
                "text": "Dal Lake, the 'Jewel in the crown of Kashmir,' is Srinagar’s most celebrated freshwater lake. Mentioned as 'Mahasarit' in Sanskrit texts, it was revered by ancient civilizations and developed in the Mughal era with iconic gardens like Shalimar and Nishat for imperial retreats. Over centuries, Dal Lake has inspired poets, artists, and filmmakers—serving as a source for culture, sustenance, and trade.",
                "image": "https://i.pinimg.com/originals/f2/e3/22/f2e3224e082e1f9d5a6400fbce118f07.jpg"
            },
            "localCuisine": [
                {
                    "name": "Rogan Josh (lamb curry), Kashmiri Dum Aloo (potato dish), Nadru Yakhni (lotus stem curry), Tsaman (paneer), seekh kebabs, noon chai (salted tea), kulfi, fresh trout, rice dishes—all found in lakefront restaurants and houseboats.",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.jZbeWjw65Bb3_tAZjWeLPgHaFV?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Shikara rides through floating gardens, lotus farms, and markets; houseboat stays; exploring Mughal gardens (Shalimar, Nishat), Chashme Shahi, Hazratbal Shrine; summer watersports, winter ice skating and photography; bird watching and visiting Char Chinar island.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.CUP8GV60zNY7wLFrB3tQSwHaE8?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Visit May–Oct for best weather; winter brings freezing and ice cover."},
                {"tip": "Swimming discouraged due to currents and variable depth—use certified boat operators."},
                {"tip": "Carry cash; boat vendors and stalls may not accept cards."},
                {"tip": "Dress in layers, especially outside summer—mornings/evenings/boat rides get chilly."},
                {"tip": "Pollution is a concern—use only filtered water and take care with street food."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Shalimar Bagh and Nishat Bagh (Mughal gardens), Shankaracharya Temple (hilltop temple with city views), Hazratbal Shrine (white marble mosque), Hari Parbat Fort (historic fortress), Nigeen Lake (quieter houseboat area).",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.Mj2sgFATAPE85px33jQOLAHaEr?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

city_vizag = {
    "state_id": ap_state_id,
    "name": "Visakhapatnam",
    "popular_places": [
        {
            "name": "RK Beach",
            "history": {
                "text": "Ramakrishna Beach, commonly known as RK Beach, is a celebrated waterfront along the Bay of Bengal in Visakhapatnam. The beach is named after the nearby Ramakrishna Mission Ashram and has been a key tourist destination for decades, hosting cultural events like Navy Day and the Annual Coastal Festival, and contributing to the city's tourism and cultural identity.",
                "image": "https://www.yovizag.com/wp-content/uploads/2022/09/jpg_20220916_181009_0000.jpg"
            },
            "localCuisine": [
                {
                    "name": "Fresh seafood, especially prawn curry and fish fry, local specialties like Andhra-style biryani and spicy chaats from roadside eateries. The area is also famous for ice creams and fruit salad with ice cream.",
                    "image": "https://i.ytimg.com/vi/Ks_XLypaRdk/hqdefault.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Walking or relaxing on the sands and sunset views. Beach sports such as volleyball and kite flying. Camel and horse rides along the shore. Visiting museums like the INS Kurusura Submarine Museum, Visakha Museum, and Aquarium. Traditional boat rides operated by local fishermen. Exploring food stalls and various snacks.",
                    "image": "https://i.ytimg.com/vi/HfVfRfaHodA/maxresdefault.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Swimming can be dangerous due to strong currents; heed local advisories and lifeguards."},
                {"tip": "Stay clear of rocky areas and pay attention to red flag warnings on the beach."},
                {"tip": "Always keep an eye on personal belongings; crowded evenings require extra caution."},
                {"tip": "Prefer licensed eateries for food safety and avoid raw or street-sold seafood if you have a sensitive stomach."},
                {"tip": "Secure valuables and use registered transport to get around."}
            ],
            "nearbyAttractions": [
                {
                    "name": "INS Kurusura Submarine Museum (decommissioned submarine museum), Visakha Museum (regional history), Kali Temple (prominent temple architecture), TU 142 Aircraft Museum (naval aircraft museum), VUDA Park (gardens and entertainment zones).",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.r0zqzrxoclWXtKUqNIpi4QHaEv?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}
city_srisailam = {
    "state_id": ap_state_id,
    "name": "Srisailam",
    "popular_places": [
        {
            "name": "Mallikarjuna Swamy Temple",
            "history": {
                "text": "Srisailam is an ancient and revered pilgrimage town in the Nallamala Hills, famous for the Mallikarjuna Swamy Temple—one of the twelve Jyotirlingas of Shiva and a Shakti Peetha of Parvati (Bhramaramba). The temple's roots date back to at least the 2nd century CE, shaped by Satavahanas, Chalukyas, Pallavas, and Vijayanagara reigns. Srisailam's legends are tied to the Mahabharata and Ramayana, giving it major spiritual significance in Purana texts.",
                "image": "https://tse2.mm.bing.net/th/id/OIP.rAKvfskg6OfZ_Ncf01aVWQHaD2?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Andhra vegetarian thali (rice, lentils, sambar, spicy curries, pickles, chutneys), temple Pulihora (tamarind rice), Daddojanam (curd rice), sweet pongal, dhaba dishes like dosas, idlis, vada, poori. Region strictly vegetarian near temple.",
                    "image": "https://im.whatshot.in/content/2016/Aug/1472212329-yuktha-1-revised.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Visiting Mallikarjuna and Bhramaramba temples, ropeway to Pathala Ganga for boating, wildlife safari or jeep tour in Nagarjunsagar-Srisailam Tiger Reserve, trekking and nature walks in Nallamala forest, exploring Akka Mahadevi Caves by river boat.",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.ILMb5ihDp2vCiUq0JiQi7wHaEK?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Dress conservatively; dhoti/kurta for men, saree/salwar kameez for women near temple."},
                {"tip": "Photography restricted inside temple sanctums; always ask before clicking."},
                {"tip": "Beware of monkeys near temple and ghats; keep valuables secure."},
                {"tip": "Book accommodation in advance, especially during festivals/weekends."},
                {"tip": "Carry cash due to spotty network and limited digital payments."},
                {"tip": "Use only authorized guides and authorized jeeps for forest/wildlife activities."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Pathala Ganga (Krishna River ghat, ropeway/boat rides), Akka Mahadevi Caves (ancient caves, boat access), Nagarjunsagar-Srisailam Tiger Reserve (safaris, bird watching), Sakshi Ganapati Temple (Ganesh idol, en route), Hathakesvara Temple (ancient Shiva temple, spiritual site), Srisailam Dam (hydroelectric dam, scenic views).",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.RFHKE8B2tbROpuEdND5QjAHaFj?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

city_gandikota = {
    "state_id": ap_state_id,
    "name": "Gandikota",
    "popular_places": [
        {
            "name": "Gandikota Fort",
            "history": {
                "text": "Gandikota, often called the 'Grand Canyon of India,' is famed for its dramatic gorge on the Pennar River and its historic fort. The initial sand fort was established in 1123 CE by Kapa Raja of the Chalukya dynasty. Gandikota flourished as a fortified city under the Pemmasani Nayakas, with major additions by the Kakatiyas, Vijayanagara Empire, Golconda Sultanate, and British. Its fort complex features temples, a mosque, granaries, and a mix of Hindu and Islamic architecture from centuries of rule.",
                "image": "https://tse1.mm.bing.net/th/id/OIP.AHy1ke4NRvw4Qc8yrSgq4wHaFj?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Ragi sangati with natu kodi koora (finger millet balls with country chicken curry) is a Rayalaseema specialty found in local eateries. Andhra vegetarian thali serves spicy curries, pappu (dal), pickles, local vegetables, and bamboo chicken may be available in countryside camps. Most food is from stalls around the fort and nearby Jammalamadugu.",
                    "image": "https://i.pinimg.com/originals/28/4d/8a/284d8a2a7e4389661efa8a1725120b3f.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Exploring Gandikota Fort's temples, mosque, granaries, and ruins. Trekking and hiking along the gorge for views of the Pennar canyon. Camping at the canyon edge, rock climbing, rappelling, nature walks, and boating or coracle rides on the river during season.",
                    "image": "https://tse4.mm.bing.net/th/id/OIP._t57cyP1tMh5xCKrcpldpwHaDV?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Wear good trekking shoes; terrain is rocky and uneven around the fort."},
                {"tip": "Carry cash—network is patchy and most vendors do not accept cards."},
                {"tip": "Bring water, snacks, sunscreen, and hats—facilities at the fort are basic."},
                {"tip": "Avoid wandering close to canyon edges, especially in monsoons or high winds."},
                {"tip": "Respect local customs; dress modestly, covering shoulders and knees in village areas."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Belum Caves (India's largest underground caves, unique rock formations, 60 km away), Mylavaram Dam (scenic reservoir for bird watching and picnics), Ranganatha Swamy Temple (intricate architecture in Gandikota village), Owk Reservoir (tranquil water body for fishing/day trips), and Yaganti (ancient Shiva cave temple among hills, about 100 km east).",
                    "image": "https://tse4.mm.bing.net/th/id/OIP.pifspR3Jwwrf0QB2PpyJTgHaFj?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}
city_hamsaladeevi = {
    "state_id": ap_state_id,
    "name": "Hamsaladeevi",
    "popular_places": [
        {
            "name": "Venugopalaswamy Temple",
            "history": {
                "text": "Hamsaladeevi, meaning 'Swans Island,' is a historic village in Krishna District where the Krishna River meets the Bay of Bengal at Sagara Sangamam—a unique confluence with three water colors. It's famous for the ancient Venugopalaswamy Temple, built by the Chola dynasty 1,000+ years ago and one of the 108 sacred Vishnu temples. Local legends link its name to Gandharvas restored to swans after bathing here.",
                "image": "https://im.whatshot.in/img/2020/Feb/is-3-1581075200.jpg"
            },
            "localCuisine": [
                {
                    "name": "Simple vegetarian temple prasadam—pulihora (tamarind rice), sweet pongal during festivals; Andhra meals in local dhabas with spicy curries, fresh vegetables, lentils; homemade chutneys and pickles.",
                    "image": "https://yourbucket.com/hamsaladeevi-cuisine.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Exploring Venugopalaswamy Temple and its legends; bathing or walking at Sagara Sangamam, the river-sea confluence; relaxing at Hamsaladeevi Beach; participating in Magha Pournami festival for rituals and holy bathing.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.wVlHrKsoTyrbJZ0nYFp7uwHaJ4?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly for temple and beach; remove shoes at temple entrances."},
                {"tip": "Carry enough cash; digital payments and ATMs rare."},
                {"tip": "Avoid swimming in rough sea; stay near locals for guidance at the beach."},
                {"tip": "Respect customs, especially during festivals—photography may be restricted."},
                {"tip": "Basic medical services limited; keep emergency meds and contacts for Machilipatnam or Vijayawada."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Avanigadda (heritage town, near Puligadda, small temples/markets), Koduru (rural village, agricultural scenes), Machilipatnam (historic coastal town with forts, colonial heritage, markets, 40 km away), Diviseema region (lush delta landscapes, birdwatching, village tours).",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.fiM8Xt70H1m3876bABHM9AHaFj?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

city_belum_caves = {
    "state_id": ap_state_id,
    "name": "Belum Caves",
    "popular_places": [
        {
            "name": "Belum Caves",
            "history": {
                "text": "Belum Caves, in Nandyal District, are India's second largest cave system, formed by underground river flow over tens of thousands of years. Archaeological finds show use by Jain and Buddhist monks as early as the 3rd century BCE, with relics and inscriptions, and vessels dating back to around 4500 BCE, reflecting its importance across many eras.",
                "image": "https://tse2.mm.bing.net/th/id/OIP.kR3drwlemkAPwsSub3EEgwHaES?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Andhra vegetarian thali (rice, dal, pickles, spicy curries) at the canteen near the caves; pulihora (tamarind rice); simple snacks and refreshments at government facilities; more dining in nearby towns.",
                    "image": "https://yourbucket.com/belum-caves-thali.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Exploring long passages and unique rock formations: Simhadwaram, Kotilingalu Chamber, Patalaganga stream, Saptasvarala Musical Chamber, Meditation Hall; viewing stalactites, stone features like Thousand Hoods and Banyan Tree; learning cave geology in the museum and by the Buddha statue.",
                    "image": "https://4.bp.blogspot.com/-lFmZyz6TYOE/WYLDs58HZoI/AAAAAAAAMjg/rYWRtbj9bfQOlfzEOTHCl3ogxRY_tYyNwCLcBGAs/s1600/3.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry water and wear sturdy shoes—humidity and warmth persist inside caves."},
                {"tip": "Follow marked routes and use provided lighting; don’t wander off pathways."},
                {"tip": "Restrooms and a government canteen are near the entrance—carry cash for expenses."},
                {"tip": "Photography is allowed but avoid flash to protect cave features."},
                {"tip": "Visit with a guide if possible, and avoid faint lighting or slippery zones."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Yaganti (ancient cave temple, growing Nandi statue, 30 km away); Gandikota (historic fort and gorge, 60 km away); Owk Reservoir (bird watching and picnics); Oravakallu Rock Garden (hiking near Kurnool); Banaganapalle Fort (historical site).",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.SLxRnRyTxdGgiMWYE5AttgHaEK?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

# 3. Insert City: Tirupati
city_tirupati = {
    "state_id": ap_state_id,
    "name": "Tirupati",
    "popular_places": [
        {
            "name": "Sri Venkateswara Temple",
            "history": {
                "text": "Tirupati has ancient origins and is one of India's holiest pilgrimage towns, famed for the Sri Venkateswara Temple on the Tirumala hills. The city grew under the Pallava, Chola, and Vijayanagara Empires, each leaving marks on the temple's architecture and tradition, with the earliest inscriptions dating back to the Pallava dynasty between the 6th and 9th centuries CE. It became a major centre for Vaishnavism from the 11th century and received important contributions from numerous South Indian rulers.",
                "image": "https://www.holidify.com/images/cmsuploads/compressed/shutterstock_11162494701_20200130180527_20200130180558.png"
            },
            "localCuisine": [
                {
                    "name": "Srivari Laddu, pulihora (tamarind rice), chakkara pongal (sweet rice and lentil pudding), Andhra Thali, bisi bele bath, vada, appam, murukku, daddojanam (curd rice)",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.XpCfUHH3VmypuQWnNSR8xAHaG3?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Trekking to Tirumala hills, visiting BluLand Water Park, exploring the peaceful TTD Gardens, enjoying local food experiences and street snacks outside temple premises",
                    "image": "https://i0.wp.com/tirumalatirupationline.com/wp-content/uploads/2017/12/Route-Mapp-e1512113413784.jpg?w=982"
                }
            ],
            "safetyTips": [
                {"tip": "Traditional attire is mandatory for temple visits (men: dhoti & shirt, women: saree or salwar kameez)."},
                {"tip": "Do not wear footwear or headgear within temple premises."},
                {"tip": "Avoid bringing excess jewellery or cash, and stay clear of touts and unauthorized agents."},
                {"tip": "NRI/foreign visitors can book special darshan slots online for expedited entry."},
                {"tip": "Book accommodation in advance, and avoid peak festival days due to heavy crowds, when possible."},
                {"tip": "Follow only vegetarian dietary habits while in Tirupati."},
                {"tip": "Carry documentation for any prescription medication; avoid bringing weapons."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Chandragiri Fort (11th-century fort and former Vijayanagar capital, known for its Raja Mahal palace museum and panoramic hill views), Talakona Waterfalls (Andhra Pradesh's highest waterfall set within lush forests, popular for trekking and picnics), Kailasakona Waterfalls (scenic perennial waterfall and sacred site ideal for short hikes and nature photography), Horsley Hills (serene hill station famous for its cool climate and peaceful retreat), Kapila Theertham (ancient Shiva temple at the base of a natural waterfall)",
                    "image": "https://i.pinimg.com/originals/88/6b/2e/886b2e5e2119a082fdd7589d30768168.jpg"
                }
            ]
        }
    ]
}
city_coringa = {
    "state_id": ap_state_id,
    "name": "Coringa",
    "popular_places": [
        {
            "name": "Coringa Wildlife Sanctuary",
            "history": {
                "text": "Coringa is a coastal village near Kakinada, once a major British-era port and shipbuilding hub in the 18th–19th centuries, drawing traders from across Europe. Its role declined after devastating cyclones in 1789 and 1839. Today Coringa is best known for its vast mangrove forests and unique estuarine ecosystem.",
                "image": "https://media-cdn.tripadvisor.com/media/photo-s/19/71/95/9a/snapseed-01-largejpg.jpg"
            },
            "localCuisine": [
                {
                    "name": "Fresh seafood—prawns, crab, local fish with Andhra spices; vegetarian meals with spicy curries, rice, lentils served in modest eateries; street snacks like punugulu and mirchi bajji on routes to the sanctuary.",
                    "image": "https://www.nritravelogue.com/wp-content/uploads/2025/01/Crab-Meat-Curry.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Mangrove boat rides, guided nature walks in the sanctuary, bird watching for rare and endangered species (over 120 reported), fishing, speed boating, jet skiing, and nature photography at sunrise/sunset over the estuary.",
                    "image": "https://ik.imagekit.io/gondolatravel/digitalocean/strapi-uploads/The_Tropics_Boat_Tours_Clearwater_Beach_7a5b48376c.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Visit Nov–Mar for best weather and bird sightings; avoid summer and monsoon for safety."},
                {"tip": "Carry mosquito repellent and dress to deter bites in mangrove areas."},
                {"tip": "Bring cash; digital payments are rare."},
                {"tip": "Stay on marked trails and boardwalks; avoid soft mud areas."},
                {"tip": "Be cautious of wildlife; do not feed animals to protect the ecosystem."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Hope Island (sandbar buffer, calm beaches, turtle nesting), Kakinada Beach (port city beach and seafood), Yanam (town with French colonial architecture), Uppada Beach (fishing village, crafts, seafood), Draksharamam (ancient inland Shiva temple and heritage site).",
                    "image": "https://tse1.mm.bing.net/th/id/OIP.yU4qnQgzMgp_i1wBpVw7OAHaEO?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}
city_amaravati = {
    "state_id": ap_state_id,
    "name": "Amaravati",
    "popular_places": [
        {
            "name": "Amaravati Stupa (Mahachaitya)",
            "history": {
                "text": "The Amaravati Stupa, or Mahachaitya, was built during Emperor Ashoka’s reign (3rd century BCE) and expanded by Satavahanas and Ikshvakus through the 3rd–4th centuries CE. It was a major Buddhist center housing Buddha relics, renowned for elaborate limestone railings and gateways—hallmarks of the Amaravati School of Art. Its rediscovered ruins exemplify early Buddhist architectural sophistication, attracting pilgrims and scholars worldwide.",
                "image": "https://www.indianholiday.com/photo-gallery/andhra-pradesh/cities-in-andhra/amaravati/Amaravati-stupa-2031.jpg"
            },
            "localCuisine": [
                {
                    "name": "Traditional Andhra vegetarian thali (rice, spicy dal—pappu, sambar, pickles, vegetable curries, local sweets), pulihora, curd rice at festivals; snacks and refreshments from the bazaar, plus Guntur/Vijayawada dining.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.7Z34udYt0OlPlVdxxrDbvgHaFg?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Exploring the archaeological site and museum (Buddhist sculptures, art, relics); visiting ancient monuments and the Dhyana Buddha statue; enjoying heritage walks and guided tours about Buddhist history and legends; joining local festivals and storytelling events.",
                    "image": "https://hblimg.mmtcdn.com/content/hubble/img/amaravati/mmt/activities/m_activities_amaravati_dhyana_buddha_statue_l_480_640.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Visit Nov–Feb for comfortable climate."},
                {"tip": "Carry water, umbrella, sunscreen—site is open-air."},
                {"tip": "Follow site guidelines—do not touch ancient sculptures, photograph only where permitted."},
                {"tip": "Use registered local guides and keep valuables secure in crowds/festivals."},
                {"tip": "Guntur/Vijayawada have major facilities; keep emergency contacts handy."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Dhyana Buddha Park (giant Buddha statue, meditation); Undavalli Caves (rock-cut 4th–5th century caves with Hindu/Jain art); Kondapalli Fort (hilltop fort near Vijayawada); Prakasam Barrage (Krishna River bridge); Mangalagiri Temple (Vaishnava temple on Mangalagiri Hill).",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.J_ztK2LIYDzWRrndBq1nbAHaFj?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

city_lepakshi = {
    "state_id": ap_state_id,
    "name": "Lepakshi",
    "hidden_gem_places": [
        {
            "name": "Veerabhadra Temple",
            "history": {
                "text": "Lepakshi is a historic village in Anantapur renowned for the 16th-century Veerabhadra Temple, built under the Vijayanagara Empire. The temple showcases vibrant architecture, sculpted pillars, murals, and is linked to legends such as Jatayu’s final resting place from the Ramayana. ‘Lepakshi’ means ‘rise, bird’ in Telugu and the site features monolithic Nandi bull and Kannada inscriptions.",
                "image": "https://tse3.mm.bing.net/th/id/OIP.kgSqliuyolSg1g2OxYgyhQHaE7?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Andhra vegetarian thali (rice, spicy lentil stew, sambar, curries, pickles), pulihora (tamarind rice), dosas, fresh fruit from village vendors.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.tfrnWt4UFYJgcIcLhaEx9gHaEK?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Exploring ornate murals, the hanging pillar, photographing the Nandi statue, heritage walks about temple legends and engineering, shopping for handicrafts and textiles.",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.PDxess0fHpVthw19HeI2BAHaE8?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly and respect temple customs; removing footwear is mandatory at religious sites."},
                {"tip": "Carry cash; card payments and ATMs are limited in the village."},
                {"tip": "Visit during daylight and avoid isolated areas after dusk, especially in the temple complex."},
                {"tip": "Stay hydrated—carry water and sun protection, as the area can be very hot."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Hindupur (nearest town with accommodation), Penukonda Fort (historical ruins and views), Puttaparthi (pilgrimage center), Ghantasal Village (Buddhist relics, archaeological sites), Anantapur (temples, forts, heritage walks).",
                    "image": "https://www.hlimg.com/images/things2do/738X538/ttd_1522915097m1.gif"
                }
            ]
        }
    ]
}



city_yaganti = {
    "state_id": ap_state_id,
    "name": "Yaganti",
    "popular_places": [
        {
            "name": "Sri Yagantiswamy Temple",
            "history": {
                "text": "Yaganti is famous for the ancient Sri Yagantiswamy Temple, dedicated to Lord Shiva, with origins tracing back to the 5th–6th centuries and significant expansion by King Harihara Bukka Raya of the Vijayanagara Empire in the 15th century. This temple is unique for worshipping Shiva in idol form and is known for its mysterious, ever-growing Nandi (bull) statue and cave shrines reflecting legends and traditions.",
                "image": "https://tse1.mm.bing.net/th/id/OIP.IQh4ihvCvGatFWvRJ_xkwQHaEK?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Gongura pachadi (sorrel leaf chutney), pesarattu (green gram dosa), ulavacharu (horse gram stew), simple prasadam (temple meal) served to visitors, and homemade dhaba food.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.8J96vmIYqm0ExvnKXwwUEAHaFj?pid=Api&P=0&h=180"
                }
            ],
            "activities": [
                {
                    "name": "Exploring Sri Yagantiswamy Temple, observing the growing Nandi statue, visiting Agastya and Venkateswara natural caves, bathing at Pushkarini (sacred pond), attending temple rituals and festivals.",
                    "image": "https://tse2.mm.bing.net/th/id/OIP.3ndRgbOkXOhpWojxiBEUUgHaFf?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly and remove shoes before entering the temple."},
                {"tip": "Carry cash as digital payments and ATMs are limited."},
                {"tip": "Avoid isolated areas at night; visit with a group or during daylight."},
                {"tip": "Respect local customs; seek permission before taking photos, especially of people or rituals."},
                {"tip": "Basic medical and transport facilities exist; major emergencies require travel to Kurnool city."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Agastya Cave (meditation and scenic views), Pushkarini (year-round sacred tank), Belum Caves (India's longest caves, 70 km away), Gandikota Fort (13th-century fort, dramatic gorge views, 100 km away), Oravakallu Rock Garden (unique rock formations near Kurnool).",
                    "image": "https://2.bp.blogspot.com/-YribUOaL8Y8/U6Fsxxu8mfI/AAAAAAAAOEQ/Hb6YdadWZgY/s1600/DSC03140.JPG"
                }
            ]
        }
    ]
}

city_araku = {
    "state_id": ap_state_id,
    "name": "Araku Valley",
    "popular_places": [
        {
            "name": "Araku Valley",
            "history": {
                "text": "Araku Valley is a scenic hill station in the Eastern Ghats of Andhra Pradesh, historically inhabited by indigenous tribes for centuries. Tourism developed mainly in the 20th century, driven by its lush forests and cool climate, while the area is also renowned for its coffee plantations established after independence, now managed by local tribal cooperatives.",
                "image": "https://tse2.mm.bing.net/th/id/OIP.QdrtRqwTrAWSXRtAabEkEQHaE1?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Bamboo Chicken (meat cooked in bamboo shoots), famous Araku Coffee, traditional Andhra dishes like pappu, pulihora, spicy chicken curry, dosas, biryanis, millet-based meals; available at resorts and dhabas across the valley.",
                    "image": "https://i.ytimg.com/vi/5SmgZ7yDecM/maxresdefault.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trekking, hiking, rock climbing in hills and forests, exploring Borra Caves, visiting Padmapuram Botanical Gardens and its toy train, touring Tribal Museum, relaxing at Chaparai and Dumbriguda Waterfalls, watching tribal dance, bird watching, and nature camping at Tyda.",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.utPlQYlZvfwR43Apoh62jwHaE8?pid=Api&P=0&h=180"
                }
            ],
            "safetyTips": [
                {"tip": "Visit October-February for cool, safe weather; avoid monsoon season due to rough roads and landslides."},
                {"tip": "Travel to remote waterfalls or hill areas only with local jeep drivers, not private cars."},
                {"tip": "Carry cash; card payments are rare and few ATMs exist in the valley."},
                {"tip": "BSNL and selected Airtel SIMs provide better mobile coverage."},
                {"tip": "Book government-approved accommodations in advance; Haritha resorts are recommended."},
                {"tip": "Respect local tribal customs and wildlife; avoid littering or disturbing nature."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Borra Caves (limestone formations), Katiki Waterfalls (adventure-friendly, trekking), Padmapuram Botanical Gardens (exotic plants, toy train), Chaparai Waterfalls (unique cascade for picnicking), Dumbriguda Waterfalls (serene spot), Tyda Nature Camp (bird watching, camping, trekking near Araku).",
                    "image": "https://www.trawell.in/admin/images/upload/249844317KatikiFalls_Main.jpg"
                }
            ]
        }
    ]
}
tn_state_doc = {"name": "Tamil Nadu"}
tn_state_id = db.states.insert_one(tn_state_doc).inserted_id

city_ooty = {
    "state_id": tn_state_id,  # Replace with Tamil Nadu's state_id if you are using a separate states collection
    "name": "Ooty",
    "popular_places": [
        {
            "name": "Ooty Hill Station",
            "history": {
                "text": "Ooty, officially Udhagamandalam, is a historic hill station in the Nilgiri Hills. First popularized in 1819 by British collector John Sullivan, it became the 'Queen of Hill Stations' and the summer capital of the Madras Presidency, blending colonial and tribal culture.",
                "image": "https://hblimg.mmtcdn.com/content/hubble/img/destimg/mmt/destination/m_Ooty_main_tv_destination_img_1_l_764_1269.jpg"
            },
            "localCuisine": [
                {
                    "name": "Ooty Varkey (crisp biscuit), homemade chocolates and fudge, dosas, idlis, sambar, pongal, vada, Tamil-style biryanis, and Nilgiri tea.",
                    "image": "https://thestushkitchen.com/wp-content/uploads/2025/01/flaky-buttermilk-biscuits-scaled-e1736106373358.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Boating on Ooty Lake, strolling in the Botanical Gardens, riding the Nilgiri Mountain Railway, trekking Doddabetta Peak, visiting tea estates, nature-watching in Mudumalai National Park.",
                    "image": "https://asolivagantsshoes.com/wp-content/uploads/2022/05/2022_0504_17361200-2.jpg?w=1024"
                }
            ],
            "safetyTips": [
                {"tip": "Carry warm clothing even in summer, as temperatures are cool at night."},
                {"tip": "Only drink bottled/filtered water; be cautious with street food."},
                {"tip": "Book accommodation in advance during peak season."},
                {"tip": "Respect tribal customs in Toda settlements/temples."},
                {"tip": "Beware of pickpockets and always negotiate transport prices first."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Coonoor (Sim's Park, tea gardens, viewpoints), Doddabetta Peak, Avalanche Lake, Pykara Lake and Falls, Mudumalai National Park.",
                    "image": "https://yourbucket.com/coonoor-view.jpg"
                }
            ]
        }
    ]
}

city_ahobilam = {
    "state_id": ap_state_id,
    "name": "Ahobilam",
    "hidden_gem_places": [
        {
            "name": "Nava Narasimha Temples",
            "history": {
                "text": "Ahobilam is a revered pilgrimage site in the Nallamala Hills, known as the birthplace of Lord Narasimha, the fierce avatar of Vishnu. The complex dates back to the 9th century, expanded by Kakatiya and Vijayanagara rulers, and consists of nine shrines (Nava Narasimha) dedicated to different forms of the deity.",
                "image": "https://tse1.mm.bing.net/th/id/OIP.C1A5EpxhlnEcqoN8sVhM5gHaEM?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Andhra vegetarian meals (rice, sambar, dal, spicy curries, pickles); pulihora (tamarind rice) and curd rice (prasadam); fresh fruit and snacks from local markets.",
                    "image": "https://i.ytimg.com/vi/GLdLE_u13EY/maxresdefault.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trekking between nine Narasimha temples in lush forest, exploring shrines of Lower and Upper Ahobilam, learning legends and rituals, heritage walks, and enjoying natural streams and wildlife.",
                    "image": "https://1.bp.blogspot.com/-pNwzc5e_KxQ/WYV54R8uedI/AAAAAAAAAtw/WpDz1GZsvx8S0YTmA3562ybH9gFmASuCQCLcBGAs/s1600/ugra.PNG"
                }
            ],
            "safetyTips": [
                {"tip": "Wear comfortable clothes and sturdy shoes for forest treks; dress modestly for temples and remove footwear inside."},
                {"tip": "Carry cash—ATMs and digital payments are limited."},
                {"tip": "Visit with local guides for trekking and navigation; routes can be rugged and confusing."},
                {"tip": "Avoid trekking after dark as the region is hilly and home to wildlife."},
                {"tip": "Carry basic medicines and plenty of water, as facilities are limited outside the main village."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Oravakallu Rock Garden (unique rock formations), Yaganti (Shiva cave temple and growing Nandi bull), Belum Caves (India’s second longest caves), Mahanandi (Nandi temple and hot springs), Nallamala Forest (nature walks and wildlife spotting).",
                    "image": "https://tse3.mm.bing.net/th/id/OIP.ed-FMDVwZPu7m6-hK_HkiwHaD2?pid=Api&P=0&h=180"
                }
            ]
        }
    ]
}

city_lambasingi = {
    "state_id": ap_state_id,
    "name": "Lambasingi",
    "hidden_gem_places": [
        {
            "name": "Lambasingi Hill Station",
            "history": {
                "text": "Lambasingi is a scenic hill station in the Eastern Ghats, often called the 'Kashmir of Andhra Pradesh' due to its chilly climate and occasional frost. Dating to the 11th century, it features influences from Chola and Vijayanagara dynasties and colonial British coffee plantations. It was originally forested and settled by tribal communities, and nearby Buddhist relics highlight its ancient past.",
                "image": "https://tse1.mm.bing.net/th/id/OIP.8ca7BTl-zC8n-0yOBt6euwHaEo?pid=Api&P=0&h=180"
            },
            "localCuisine": [
                {
                    "name": "Freshly brewed Lambasingi coffee, Andhra-style vegetarian meals (rice, spicy curries, pickles), simple snacks and seasonal fruits directly from village farms.",
                    "image": "https://static.tnn.in/photo/msid-115488204/115488204.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trekking and nature walks in misty hills and plantations, bird watching and photography, visiting Kothapalli Waterfalls, strolling Susan Garden, camping, stargazing, and mountain biking.",
                    "image": "https://images.herzindagi.info/her-zindagi-english/images/2024/11/19/article/image/Lambasingi-Travel-Guide-1732020039019.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Visit November–January for best weather; bring warm clothes for possible freezing temperatures."},
                {"tip": "Roads may be foggy/slippery—drive carefully or hire a local driver."},
                {"tip": "Carry cash; card use may be limited."},
                {"tip": "Book accommodation early in peak season."},
                {"tip": "Respect local tribal customs, do not litter, keep nature clean."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Kothapalli Waterfalls (pristine cascades), Thajangi Reservoir (lake for photography), Susan Garden (flower fields), Bojjannakonda (Buddhist site), Kondakarla Bird Sanctuary (wetlands and birding).",
                    "image": "https://www.trawell.in/admin/images/upload/01943582Lambasingi_Kothapalli_Waterfalls_Main.jpg"
                }
            ]
        }
    ]
}



city_mahabalipuram = {
    "state_id": tn_state_id,  # Replace with Tamil Nadu's state_id if using a dedicated state
    "name": "Mahabalipuram",
    "popular_places": [
        {
            "name": "Mahabalipuram Monuments",
            "history": {
                "text": "Mahabalipuram, or Mamallapuram, was a thriving port city of the Pallava dynasty in the 7th–8th centuries CE. Its world-famous rock-cut temples, cave sanctuaries, monolithic rathas, and bas-reliefs like Arjuna's Penance and the Shore Temple are UNESCO World Heritage monuments, blending Hindu and Buddhist artistry.",
                "image": "https://www.mahabalipuram.org/wp-content/uploads/2023/11/F_MujZha8AAt96N.jpeg"
            },
            "localCuisine": [
                {
                    "name": "Fresh seafood (prawn curry, fried fish), dosas, idlis with coconut chutney, sweets with cashew and coconut, filter coffee, payasam.",
                    "image": "https://shwetainthekitchen.com/wp-content/uploads/2022/01/Idli-Sambar.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Exploring the Shore Temple, Pancha Rathas, Arjuna’s Penance, cycling/walking the beach, shopping for stone sculpture, attending the Mahabalipuram Dance Festival.",
                    "image": "https://media-cdn.tripadvisor.com/media/photo-s/10/9f/31/ec/pancha-rathas.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly in temples; remove shoes within shrines."},
                {"tip": "Carry enough cash for small shops; card acceptance is limited."},
                {"tip": "Be cautious of high waves along rocky coast; swim only in safe zones."},
                {"tip": "Book accommodation ahead during festivals/weekends."},
                {"tip": "Beware of pickpockets at tourist and temple sites."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Covelong Beach (water sports, resorts), Tiger Cave (rock-cut shrine), Vedanthangal Bird Sanctuary, Sadras Dutch Fort (colonial ruins), Thirukazhukundram Temple (hilltop views, sacred vultures).",
                    "image": "https://yourbucket.com/covelong-beach.jpg"
                }
            ]
        }
    ]
}
city_brihadeeswarar_temple = {
    "state_id": tn_state_id,
    "name": "Thanjavur (Brihadeeswarar Temple)",
    "popular_places": [
        {
            "name": "Brihadeeswarar Temple",
            "history": {
                "text": "Brihadeeswarar Temple, also called Thanjai Periya Kovil, is a UNESCO World Heritage Site and one of India’s largest temples, built by Chola emperor Raja Raja Chola I (1003–1010 CE). Its granite construction, monumental vimana, and rich murals showcase Chola power and artistry.",
                "image": "https://cdn.thedecorjournalindia.com/wp-content/uploads/2022/03/Brihadeshwara-Temple-A-structure-conceived-with-grace-and-Magnificence-1.jpg"
            },
            "localCuisine": [
                {
                    "name": "Tamil vegetarian thali (rice, sambar, rasam, kootu, poriyal, appalam, payasam), filter coffee, onion uthappam, vadai, dosai, temple prasadam (sweet pongal, laddu).",
                    "image": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjC9m3G6VQ8EwYheMVP6w1mycq6eJaSAHhcQYo3nW0kuh9vIwT5x85PwX2tPzoDcukhGBPnWjaDjriqB2KRIEvUStJtrcYRLI0mkA8Ivil3He-0I_ksH2iOEIwkNlj9VhahHaO6RKr3OFgF/s1600/IMG_4044.JPG"
                }
            ],
            "activities": [
                {
                    "name": "Explore architecture and murals, giant Nandi statue, attend Mahashivaratri and cultural festivals, visit Thanjavur Palace and art gallery, watch dance performances in temple festivals.",
                    "image": "https://mediaim.expedia.com/destination/2/d7bbc288c5a681dcd14e52233c7d3b22.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly; remove shoes when entering temple premises."},
                {"tip": "No photography inside sanctum—check camera rules."},
                {"tip": "Carry cash; card acceptance limited."},
                {"tip": "Visit early/late for cooler weather—avoid hot afternoons."},
                {"tip": "Use only official guides; entry is free."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Thanjavur Palace (Saraswathi Mahal Library, Schwartz Church, Sangeetha Mahal), Rajaraja Manimandapam, Punnainallur Mariamman Temple.",
                    "image": "https://yourbucket.com/thanjavur-palace.jpg"
                }
            ]
        }
    ]
}

city_kodaikanal = {
    "state_id": tn_state_id,
    "name": "Kodaikanal",
    "popular_places": [
        {
            "name": "Kodaikanal Hill Station",
            "history": {
                "text": "Kodaikanal, 'The Gift of the Forest', is a famed Palani Hills hill station first inhabited by the Palaiyar tribe and referenced in Tamil Sangam literature. Founded as a colonial retreat in 1845 by missionaries and British officials, it developed with churches, colonial buildings and the artificial Kodai Lake.",
                "image": "https://static.toiimg.com/photo/123945980.cms"
            },
            "localCuisine": [
                {
                    "name": "Homemade chocolate & fudge, dosas, idlis, pongal, sambar, Tamil thali, Ooty Varkey, Nilgiri tea, seasonal fruits (plums, pears, peaches).",
                    "image": "https://kodaiherbal.com/public/uploads/all/Ebcuerl1eXMhGsuzWnxcsuITU2ZYK91pys7PMZ52.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Boating on Kodai Lake, cycling its perimeter, trekking to Pillar Rocks, Dolphin’s Nose, or Coaker’s Walk, visiting Bryant Park, Silver Cascade Waterfall, colonial-era buildings, Solar Observatory, and shopping for chocolate and local goods.",
                    "image": "https://d26dp53kz39178.cloudfront.net/media/uploads/products/5_3_VNC3mgL.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry warm clothing (night temperatures drop)."},
                {"tip": "Drink bottled/filtered water; check food hygiene."},
                {"tip": "Book stays in advance for peak tourist season."},
                {"tip": "Negotiate local transport fares in advance."},
                {"tip": "Do not litter; respect nature and local customs."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Pillar Rocks (picnic & views), Silver Cascade Waterfall (quick stop), Coaker’s Walk (cliffside path), Berijam Lake (forest lake, birding & picnics), Guna Caves (adventure hiking).",
                    "image": "https://yourbucket.com/pillar-rocks.jpg"
                }
            ]
        }
    ]
}

city_srirangam = {
    "state_id": tn_state_id,
    "name": "Srirangam",
    "popular_places": [
        {
            "name": "Ranganathaswamy Temple",
            "history": {
                "text": "Srirangam's Ranganathaswamy Temple is among India's oldest and most significant Vaishnava shrines, with roots in the Ramayana and centuries of expansion from the early Chola period through to the Vijayanagara era. It features a vast 156-acre, seven-enclosure sacred complex and monumental towers.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Aerial_view_of_Sri_Rangam_temple_near_Tiruchirapalli_1.jpg"
            },
            "localCuisine": [
                {
                    "name": "Temple prasadam padaiyal (puliyodarai, curd rice, sweet pongal), South Indian thali (sambar, rasam, poriyal, sweets), filter coffee, local snacks (murukku, adhirasam), simple vegetarian meals.",
                    "image": "https://x9s2d6a3.delivery.rocketcdn.me/wp-content/uploads/2015/05/Aravanai-Srirangam-14.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Explore Ranganathaswamy Temple's towers and halls, witness rituals and Vaikunta Ekadasi festival, walk through the temple’s seven enclosures, shop in temple markets, visit shrines and tanks.",
                    "image": "https://th-i.thgim.com/public/news/cities/Tiruchirapalli/article17012206.ece/alternates/FREE_1200/TY09_VAIKUNTA"
                }
            ],
            "safetyTips": [
                {"tip": "Wear modest clothing (cover shoulders and knees); remove shoes in temple."},
                {"tip": "Photograph only where permitted; avoid in the sanctum or during select rituals."},
                {"tip": "Carry cash for markets and donations."},
                {"tip": "Take care of belongings in festival crowds."},
                {"tip": "Use only authorized temple guides."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Rockfort Temple (panoramic hilltop shrine), Jambukeswarar Temple (water shrine), Erumbeeswarar Temple (hilltop views), St. Lourdes Church (Trichy), Kallanai (Grand Anicut) on Kaveri River.",
                    "image": "https://yourbucket.com/rockfort-temple.jpg"
                }
            ]
        }
    ]
}

city_meenakshi_temple = {
    "state_id": tn_state_id,
    "name": "Madurai (Meenakshi Temple)",
    "popular_places": [
        {
            "name": "Meenakshi Temple",
            "history": {
                "text": "Madurai’s Meenakshi Temple, dedicated to Goddess Meenakshi and Lord Sundareswarar (Shiva), dates back over 1400 years, with earliest construction attributed to Pandyan kings. It was expanded by Pandya, Chola, and Nayaka dynasties, and rebuilt after invasions, serving as the religious and cultural heart of Madurai.",
                "image": "https://media-cdn.tripadvisor.com/media/photo-s/11/71/bf/0e/madurai-meenakshi-temple.jpg"
            },
            "localCuisine": [
                {
                    "name": "Temple prasadam (puliyodarai, curd rice, sweet pongal), Madurai street food (jigarthanda, idlis, dosas, Chettinad curries, snacks), filter coffee from Tamil cafés.",
                    "image": "https://www.famousjigarthanda.com/assets/images/services/category/large/product1.png"
                }
            ],
            "activities": [
                {
                    "name": "Explore the temple’s 14 gopurams, 1,000-pillared hall, Golden Lotus pond, stone carvings; watch daily rituals and festivals (Chithirai Thiruvizha); shop for handicrafts; heritage walks to learn temple legends and city history.",
                    "image": "https://images.indianexpress.com/2022/04/madurai.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly; remove shoes inside temple areas."},
                {"tip": "Follow photo rules—no photos in sanctum/private rituals."},
                {"tip": "Carry cash for donations/purchases; cards not always accepted."},
                {"tip": "Beware of pickpockets during festivals; use authorized guides."},
                {"tip": "Respect customs; ask before taking photos of people/rituals."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Tirumalai Nayak Palace, Koodal Azhagar Temple, Gandhi Memorial Museum, Alagar Kovil (in Alagar Hills), Samanar Hills (Jain caves and views).",
                    "image": "https://yourbucket.com/tirumalai-nayak-palace.jpg"
                }
            ]
        }
    ]
}

city_kanyakumari = {
    "state_id": tn_state_id,
    "name": "Kanyakumari",
    "popular_places": [
        {
            "name": "Kanyakumari Coastal Town",
            "history": {
                "text": "Kanyakumari, formerly Cape Comorin, stands at India's southernmost tip at the confluence of three seas. Its history spans ancient Sangam-era kingdoms, maritime trade with Rome and Egypt, colonial influences, and deep Hindu mythology, most notably the Kumari Amman Temple and Vivekananda Rock.",
                "image": "https://footloosedev.com/wp-content/uploads/2016/04/kanyakumari-e1736840394191.jpg"
            },
            "localCuisine": [
                {
                    "name": "Fresh seafood (fish fry, prawn curry, crab), South Indian thali (dosas, idlis, appam, gravies), banana chips, coconut ladoos, filter coffee.",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtE47XwYNeJKJ5NpDGcEBgA7A0kCG74q1_BA&s"
                }
            ],
            "activities": [
                {
                    "name": "Watching sunrise and sunset at the beach, ferry ride to Vivekananda Rock Memorial, climb Thiruvalluvar Statue, visit Kumari Amman Temple, tour Padmanabhapuram Palace and Vattakottai Fort, shop for seashell souvenirs and handicrafts.",
                    "image": "https://afreentravelbug.wordpress.com/wp-content/uploads/2015/01/sea-shells-shopping-in-kanyakumari.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly at temples and festivals; remove shoes for entry."},
                {"tip": "Be wary of high tides and rough seas; heed swimming warnings."},
                {"tip": "Carry cash for small purchases; limited ATMs."},
                {"tip": "Respect photography rules at sanctums; ask before photographing people."},
                {"tip": "Beware of touts and unsolicited guides."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Vivekananda Rock Memorial (meditation site), Thiruvalluvar Statue (monument), Padmanabhapuram Palace (teakwood heritage), Vattakottai Fort (coastal views), Thanumalayan Temple (Suchindram, gopuram and pillar festival).",
                    "image": "https://yourbucket.com/thiruvalluvar-statue.jpg"
                }
            ]
        }
    ]
}

city_marina_beach = {
    "state_id": tn_state_id,
    "name": "Chennai (Marina Beach)",
    "popular_places": [
        {
            "name": "Marina Beach",
            "history": {
                "text": "Marina Beach, one of the world’s longest urban beaches, was officially developed and named in 1884 by Governor Mountstuart Grant Duff. Once muddy, it grew into a recreation hub in colonial times, hosting social movements and now commemorates national leaders with statues and memorials, central to Chennai’s social life.",
                "image": "https://res.cloudinary.com/chasset/c_fill,e_improve,f_webp,h_480,w_720/hbimages/desktop/1500880207631-Marina%20Beach.jpg"
            },
            "localCuisine": [
                {
                    "name": "Sundal, murukku, roasted corn (milagai masala corn), raw mango with chili-salt, idli, dosa, vadai, coconut chutney, fresh coconut water, and filter coffee.",
                    "image": "https://vspiceroute.com/wp-content/uploads/2023/04/A7B1EFD5-EC78-4299-87B9-F7C24D674CF2-500x500.jpeg"
                }
            ],
            "activities": [
                {
                    "name": "Strolling the beach, sunrise and sunset viewing, kite flying, beach volleyball, horse riding, visiting statues and memorials, Chennai Lighthouse, Annie Besant Park, and Aquarium.",
                    "image": "https://sc0.blr1.digitaloceanspaces.com/large/879483-eedntshjbq-1526649264.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Swimming discouraged due to strong undercurrents and few lifeguards."},
                {"tip": "Visit early morning/evening; avoid midday sun, use sunscreen, stay hydrated."},
                {"tip": "Beware of pickpockets; carry cash for food stalls."},
                {"tip": "Respect customs at memorials, use bins to avoid littering."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Vivekananda House (Swami Vivekananda museum), Chepauk Palace and Stadium, University of Madras and Senate House, San Thome Basilica, Kapaleeshwarar Temple.",
                    "image": "https://yourbucket.com/vivekananda-house.jpg"
                }
            ]
        }
    ]
}

city_rameshwaram = {
    "state_id": tn_state_id,
    "name": "Rameshwaram",
    "popular_places": [
        {
            "name": "Ramanathaswamy Temple & Rameshwaram Town",
            "history": {
                "text": "Rameshwaram, on Pamban Island, is famed for the Ramanathaswamy Temple—one of India's twelve Jyotirlingas and a major Char Dham site. Its origins are tied to Lord Rama and the Ramayana, with temple construction spanning centuries and culminating in grand 17th-century Dravidian halls and corridors, reflecting deep religious and maritime history.",
                "image": "https://blogs.pathbeat.in/wp-content/uploads/2024/05/rameswaram-temple-1656167436_f2c551193bb7d4bc6f70.webp"
            },
            "localCuisine": [
                {
                    "name": "Temple prasadam (puliyodarai, curd rice, sweet pongal, laddus), South Indian vegetarian staples (dosas, idlis, sambar, coconut chutney), fresh seafood (fish curry, prawn fry, crab), filter coffee, street snacks (sundal, vadai).",
                    "image": "https://images.timesnownews.com/thumb/msid-151360422,thumbsize-67556,width-1280,height-720,resizemode-75/151360422.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Explore Ramanathaswamy Temple, its corridors and teerthams; take a dip at Agni Theertham beach; visit Pamban Bridge, Kothandaramaswamy Temple, Gandhamadhana Parvatham, Abdul Kalam Memorial; enjoy local beaches, water sports and eco-tours.",
                    "image": "https://www.hotelrameswaramgrand.com/wp-content/uploads/2018/09/Pamban-Bridge.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly in temples; remove shoes at shrines."},
                {"tip": "Take care at Agni Theertham—watch for currents and follow safety flags."},
                {"tip": "Carry cash as cards/digital payments have limited acceptance in small shops."},
                {"tip": "Beware touts; hire authorized guides only."},
                {"tip": "Respect customs and photography bans in sanctum areas."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Agni Theertham, Pamban Bridge, Kothandaramaswamy Temple, Gandhamadhana Parvatham, Abdul Kalam Memorial, Dhanushkodi (mythic Ram Setu, dramatic landscape).",
                    "image": "https://yourbucket.com/dhanushkodi.jpg"
                }
            ]
        }
    ]
}

city_coonoor = {
    "state_id": tn_state_id,
    "name": "Coonoor",
    "popular_places": [
        {
            "name": "Coonoor Hill Station",
            "history": {
                "text": "Coonoor, a scenic Nilgiri hill station first settled by the Todas and Kurumbas, became a colonial retreat after British officials arrived in the 19th century. The Wellington Cantonment, tea industry, and Nilgiri Mountain Railway transformed it into a renowned tea, trade, and tourism hub.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmp3cIlNgDOq8hgBOOyJfhBevE30Puhx6KJg&s"
            },
            "localCuisine": [
                {
                    "name": "Bakery treats (breads, cakes, varkey biscuits), South Indian staples (dosas, idlis, sambar, Chettinad gravies), Nilgiri tea, homemade chocolates and fudge.",
                    "image": "https://i.pinimg.com/236x/25/4e/19/254e1923b16cdf9240c452dfc8cf7bc2.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Ride Nilgiri Mountain Railway to Ooty, explore Sim’s Park, trek to Lamb’s Rock/Dolphin’s Nose/Lady Canning’s Seat, visit tea estates, stroll colonial streets, and see heritage churches.",
                    "image": "https://ootytourism.co.in/images/headers/dolphins-nose-coonoor-entry-fee-timings-holidays-reviews-header.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Carry a jacket—weather is chilly, frequent rain."},
                {"tip": "Stick to bottled water, and check food hygiene at roadside stalls."},
                {"tip": "Book ahead in busy season (May–June, Sep–Oct)."},
                {"tip": "Watch for leeches and slippery paths if trekking after rain."},
                {"tip": "Respect privacy/customs in tribal hamlets and temple areas."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Ooty (nearby by train/road), Kotagiri (hill town), Doddabetta Peak (highest point), Catherine Falls (twin waterfalls), Wellington Cantonment (scenic drives, golf).",
                    "image": "https://yourbucket.com/catherine-falls.jpg"
                }
            ]
        }
    ]
}



city_pichavaram = {
    "state_id": tn_state_id,
    "name": "Pichavaram",
    "hidden_gem_places": [
        {
            "name": "Pichavaram Mangrove Forest",
            "history": {
                "text": "Pichavaram is a coastal village near Chidambaram, home to one of the world’s largest ancient mangrove forests. These wetlands have long aided fishing and farming, guarding the coast against storms and tides. The mangroves are locally sacred and closely tied to the historic Chidambaram Nataraja Temple.",
                "image": "https://madrascourier.com/wp-content/uploads/2017/09/Pichavaram-Madras-Courier-03.jpg"
            },
            "localCuisine": [
                {
                    "name": "Fresh seafood (crab, prawn, fish) with local spices, traditional Tamil vegetarian meals (rice, rasam, sambar, kootu), and snacks like sundal and roasted corn.",
                    "image": "https://images.jdmagicbox.com/quickquotes/images_main/-18rm114j.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Boating and kayaking in the canals, bird watching (200+ species), nature walks and eco-tours, mangrove photography, peak from Nov–Feb.",
                    "image": "https://images.exoticamp.com/vendors/images/profile/Xmas%20&%20NY%20Thumbnail%20New%20Website%20(1746%20x%20776%20px)%20(28)_20250705T102254265Z.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Visit Nov–Feb for best weather; avoid hot summers and monsoon flooding."},
                {"tip": "Use only authorized boats and wear life jackets—some canals are deep."},
                {"tip": "Bring insect repellent and wear covered clothing in the forest."},
                {"tip": "Carry cash; basic amenities only, nearest major town is Chidambaram."},
                {"tip": "Respect village customs, especially at temple festivals."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Chidambaram Nataraja Temple (historic Shiva temple), Porto Novo Beach, Vilgam Bird Sanctuary, Veeranam Lake, Parangipettai (historic port/market town).",
                    "image": "https://yourbucket.com/chidambaram-temple.jpg"
                }
            ]
        }
    ]
}

city_kolli_hills = {
    "state_id": tn_state_id,
    "name": "Kolli Hills",
    "hidden_gem_places": [
        {
            "name": "Kolli Hills Region",
            "history": {
                "text": "Kolli Hills in Namakkal are famous in ancient Tamil literature and ruled by the legendary Valvil Ori around 200 CE. The guardian goddess Kollipavai, said to protect sages, is honored with a temple in the hills.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThWUSBIrxIuMNCou-nHTHBlKbKLfW3l3kGtA&s"
            },
            "localCuisine": [
                {
                    "name": "Jackfruit and pineapple with honey, rice and millets (ragi, saamai), sambar, vegetable curries, Naatu Kozhi Varuval (country chicken roast), herbal soups, snacks (Kuzhi Paniyaram).",
                    "image": "https://th-i.thgim.com/public/migration_catalog/article10239799.ece/alternates/FREE_1200/04sa-jack-fruitSA04_TRIBAL_SHANDY..jpg"
                }
            ],
            "activities": [
                {
                    "name": "Trek to Agaya Gangai Falls, Masila Falls, Mini Falls; visit Arapaleeswarar Temple; explore Siddhar Caves; nature walks to Sikku Parai, Pulian Cholai, Botanical Gardens; enjoy fruits and markets.",
                    "image": "https://imgtemple.dinamalar.com/kovilimages/T_500_1023.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Road has 70+ sharp hairpin bends—hire skilled drivers, avoid night travel."},
                {"tip": "Few lodges—book ahead, limited amenities outside Semmedu."},
                {"tip": "Carry cash; ATMs/network limited in rural hills."},
                {"tip": "Watch for slippery steps or steep drops near falls, especially after rain."},
                {"tip": "Respect tribal customs and temple practices."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Arapaleeswarar Temple (Shiva shrine), Agaya Gangai Falls (famous waterfall), Pulian Cholai (eco-park/views), Botanical Gardens, Ettukkai Amman Temple (guardian goddess).",
                    "image": "https://yourbucket.com/arappaleeswarar-temple.jpg"
                }
            ]
        }
    ]
}

city_chettinad = {
    "state_id": tn_state_id,
    "name": "Chettinad",
    "hidden_gem_places": [
        {
            "name": "Chettinad Region",
            "history": {
                "text": "Chettinad, 74 villages in Sivaganga and Pudukottai, is historically home to the Nattukottai Chettiar merchant-bankers. The community moved inland after a 6th-century tsunami and flourished from the 19th century as global traders, building grand mansions blending Dravidian and Western influences.",
                "image": "https://avathioutdoors.gumlet.io/travelGuide/dev/chettinad_P8820.jpg"
            },
            "localCuisine": [
                {
                    "name": "Chettinad Chicken Curry, seafood dishes with pepper and aromatic masalas, vegetarian classics (brinjal curry, drumstick sambar, paal paniyaram, payasam, ghee rice), spicy chutneys.",
                    "image": "https://rakskitchen.net/wp-content/uploads/2017/10/Paal-paniyaram-recipe.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Explore palatial mansions, visit clan temples (Vairavan Kovil, Karpaga Vinayakar), tour Chettinad Museum, learn tile-making in Athangudi, shop for handlooms and crafts.",
                    "image": "https://www.theparkhotels.com/images/site-specific/the-lotus-palace-chettinad/home/banner-1.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Dress modestly, especially in temples and ancestral homes."},
                {"tip": "Use cash for small transactions; cards not always accepted."},
                {"tip": "Ask permission before photography in temples, mansions, and markets."},
                {"tip": "Guided tours are best for mansions/temples for context."},
                {"tip": "Carry water; summers can be hot and dry."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Karaikudi (markets, restaurants, railway station), Athangudi (handmade tiles), Pillaiyarpatti Temple (rock-cut Ganesha temple), Kanadukathan Chettinad Palace, Karpaga Vinayakar Temple.",
                    "image": "https://yourbucket.com/athangudi-tiles.jpg"
                }
            ]
        }
    ]
}

city_hogenakkal_falls = {
    "state_id": tn_state_id,
    "name": "Hogenakkal Falls",
    "hidden_gem_places": [
        {
            "name": "Hogenakkal Falls",
            "history": {
                "text": "Hogenakkal Falls, on the Kaveri river at the Tamil Nadu–Karnataka border, are famed as 'smoky rocks' due to the mist over ancient carbonatite stones. Steeped in Sangam-era legend, local folklore, and the worship of the Kaveri, these cascades have inspired art and history for centuries.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/5/52/Hogenakkal_Falls_Close.jpg"
            },
            "localCuisine": [
                {
                    "name": "Fried river fish from Cauvery, Tamil-style sambar rice, lemon rice, spicy chutneys from local dhabas, roasted peanuts and corn, riverside snacks.",
                    "image": "https://media-cdn.tripadvisor.com/media/photo-s/06/94/1a/9d/hogenakkal-falls.jpg"
                }
            ],
            "activities": [
                {
                    "name": "Ride coracle boats under the falls, enjoy herbal oil massages, trek/view/scenic photography, and bathe only in safe designated river zones.",
                    "image": "https://media-cdn.tripadvisor.com/media/photo-s/0d/56/38/3c/hogenakkal-falls-parisal.jpg"
                }
            ],
            "safetyTips": [
                {"tip": "Do not swim in strong currents; use only official bathing and boat areas."},
                {"tip": "Life jackets are mandatory—choose only authorized boat operators."},
                {"tip": "Visit Oct–Feb for the best water levels; avoid summer and monsoon."},
                {"tip": "Carry cash; digital payments rare—watch belongings in crowds."}
            ],
            "nearbyAttractions": [
                {
                    "name": "Pennagaram Village (markets, local culture), Theerthamalai Temple (hilltop shrine), Dharmapuri (heritage temples), Mutharaiyar Palace (historic site), Melagiri Hills (treks, birding, nature).",
                    "image": "https://yourbucket.com/theerthamalai-temple.jpg"
                }
            ]
        }
    ]
}



# 5. Insert ALL cities into database
#db.cities.insert_many([city_vizag, city_tirupati, city_araku,city_yaganti,city_srisailam, city_gandikota, city_hamsaladeevi, city_belum_caves, city_coringa,city_ahobilam,city_dhanushkodi, city_amaravati, city_ooty,city_mahabalipuram,city_rameshwaram,city_hogenakkal_falls,city_lepakshi,city_lambasingi,city_brihadeeswarar_temple,city_kodaikanal,city_srirangam,city_meenakshi_temple,city_kanyakumari,city_marina_beach,city_coonoor,city_pichavaram,city_kolli_hills,city_chettinad,city_gulmarg,city_srinagar,city_pahalgam,city_sonamarg,city_mughal_garden,city_jama_masjid,city_katra,city_patnitop,city_yusmarg,city_gurez_valley,city_doodhpatri,city_sinthan_top,city_,city_padmanabhaswamy_temple,city_kumarakom_bird_sanctuary,city_sabarimala,city_periyar, city_alleppey,city_kovalam,city_kozhikode,city_munnar,city_silent_valley,city_athirappilly,city_kolukkumalai,city_marayoor,city_gavi,city_kasi, city_taj_mahal, city_mathura, city_sarnath, city_fatehpur_sikri, city_ayodhya , city_prayagraj#, city_dudhwa_national_park, city_agra_fort, city_lucknow, city_chitrakoot, city_chunar_fort, city_ramnagar, city_rani_mahal, city_katarniaghat,city_narlai, city_khuri_dunes, city_mandawa, city_wayanad,city_osian, city_khimsar, city_chittorgarh_fort , city_mount_abu, city_ajmer_dargah, city_junagarh_fort, city_pushkar, city_ranthambore_national_park, city_jaisalmer_fort,city_kochi city_mehrangarh_fort, city_udaipur_city_palace, city_hawa_mahal, city_chamundi_hills, city_kudremukh, city_apsara_konda, city_st_marys_islands,city_wular_lake,city_agumbe, city_srirangapatna, city_chikmagalur, city_nandi_hills, city_kabini_wildlife, city_belur, city_badami, city_coorg, city_gokarna, city_mysore_palace,  city_hampi, city_kamakhya_temple,city_manas,city_haflong,city_guwahati,city_jorhat,city_kaziranga,city_tezpur, city_majuli, city_sualkuchi,city_tinsukia, city_pabitora,city_digboi, city_panimur, city_dibru_saikhowa,city_sivasagar])
#print("Database created and all city information inserted.")

db.cities.insert_many([
    city_vizag, city_tirupati, city_araku, city_yaganti, city_srisailam, city_gandikota, city_hamsaladeevi,
    city_belum_caves, city_coringa, city_ahobilam, city_amaravati, city_ooty, city_mahabalipuram,
    city_rameshwaram, city_hogenakkal_falls, city_lepakshi, city_lambasingi, city_brihadeeswarar_temple,
    city_kodaikanal, city_srirangam, city_meenakshi_temple, city_kanyakumari, city_marina_beach, city_coonoor,
    city_pichavaram, city_kolli_hills, city_chettinad, city_gulmarg, city_srinagar, city_pahalgam, city_sonamarg,
    city_mughal_garden, city_jama_masjid, city_katra, city_patnitop, city_yusmarg, city_gurez_valley,
    city_doodhpatri, city_sinthan_top, city_purmandal, city_padmanabhaswamy_temple, city_kumarakom_bird_sanctuary,
    city_sabarimala, city_periyar, city_alleppey, city_kovalam, city_kozhikode, city_munnar, city_silent_valley,
    city_athirappilly, city_kolukkumalai, city_marayoor, city_gavi, city_kasi, city_taj_mahal, city_mathura,
    city_sarnath, city_fatehpur_sikri, city_ayodhya, city_prayagraj, city_dudhwa_national_park, city_agra_fort,
    city_lucknow, city_chitrakoot, city_chunar_fort, city_ramnagar, city_rani_mahal, city_katarniaghat,
    city_narlai, city_khuri_dunes, city_mandawa, city_wayanad, city_osian, city_khimsar, city_chittorgarh_fort,
    city_mount_abu, city_ajmer_dargah, city_junagarh_fort, city_pushkar, city_ranthambore_national_park,
    city_jaisalmer_fort, city_kochi, city_mehrangarh_fort, city_udaipur_city_palace, city_hawa_mahal,
    city_chamundi_hills, city_kudremukh, city_apsara_konda, city_st_marys_islands,
    city_wular_lake, city_agumbe, city_srirangapatna, city_chikmagalur, city_nandi_hills, city_kabini_wildlife,
    city_belur, city_badami, city_coorg, city_gokarna, city_mysore_palace, city_hampi, city_kamakhya_temple,
    city_manas, city_haflong, city_guwahati, city_jorhat, city_kaziranga, city_tezpur, city_majuli, city_sualkuchi,
    city_tinsukia, city_pabitora, city_digboi, city_panimur, city_dibru_saikhowa, city_sivasagar
])
print("Database created and all city information inserted.")
