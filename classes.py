OBJECT_CATEGORIES = {

    "Electronics": [
        "laptop", "desktop computer", "keyboard", "mouse",
        "monitor", "mobile phone", "tablet", "television",
        "camera", "headphones", "speaker", "printer",
        "router", "remote control", "smartwatch"
    ],

    "Home Appliances": [
        "refrigerator", "washing machine", "microwave oven",
        "electric kettle", "toaster", "blender", "mixer grinder",
        "vacuum cleaner", "air conditioner", "ceiling fan",
        "table fan", "water purifier", "rice cooker",
        "iron box", "dishwasher"
    ],

    "Vehicles": [
        "car", "motorcycle", "scooter", "bicycle", "bus",
        "truck", "train", "airplane", "helicopter", "boat",
        "ship", "van", "ambulance", "fire truck", "tractor"
    ],

    "Animals": [
        "dog", "cat", "cow", "buffalo", "elephant",
        "horse", "sheep", "goat", "lion", "tiger",
        "bear", "monkey", "deer", "zebra", "giraffe",
        "rabbit", "fox", "wolf", "pig", "camel"
    ],

    "Office and Stationery": [
        "pen", "pencil", "eraser", "notebook", "book",
        "scissors", "stapler", "paper clip", "marker",
        "highlighter", "ruler", "calculator", "folder",
        "envelope", "glue stick"
    ],

    "Food and Groceries": [
        "apple", "banana", "orange", "mango", "grapes",
        "watermelon", "pineapple", "strawberry", "bread",
        "egg", "milk bottle", "cheese", "pizza", "burger",
        "sandwich", "rice", "tomato", "potato", "onion",
        "carrot"
    ],

    "Tools": [
        "hammer", "screwdriver", "wrench", "pliers",
        "drill machine", "saw", "spanner", "axe",
        "measuring tape", "toolbox", "chisel", "file",
        "clamp", "bolt cutter", "paint brush"
    ],

    "Sports": [
        "football", "basketball", "cricket bat", "cricket ball",
        "tennis racket", "badminton racket", "shuttlecock",
        "golf club", "baseball bat", "volleyball",
        "hockey stick", "boxing gloves", "helmet",
        "skateboard", "surfboard"
    ],

    "Personal Accessories": [
        "watch", "sunglasses", "handbag", "backpack",
        "wallet", "belt", "hat", "cap", "shoes",
        "sandals", "umbrella", "necklace", "ring",
        "bracelet", "tie"
    ],

    "Household": [
        "chair", "table", "sofa", "bed", "pillow",
        "blanket", "lamp", "clock", "mirror", "cup",
        "plate", "bowl", "spoon", "fork", "bottle"
    ],

    "Toys and Games": [
        "teddy bear", "doll", "toy car", "toy truck",
        "toy bus", "toy train", "toy airplane", "toy helicopter",
        "toy boat", "toy robot", "toy dinosaur", "toy animal",
        "action figure", "toy soldier", "toy gun",
        "building blocks", "toy bricks", "toy house",
        "toy kitchen set", "toy phone", "toy camera",
        "toy ball", "yo-yo", "spinning top", "rubik's cube",
        "jigsaw puzzle", "chess board", "board game",
        "playing cards", "remote control toy car"
    ],

    "Musical Instruments": [
        "guitar", "electric guitar", "acoustic guitar", "piano",
        "keyboard", "drum", "drum set", "violin", "cello",
        "flute", "trumpet", "saxophone", "trombone", "clarinet",
        "harmonica", "accordion", "ukulele", "harp", "xylophone",
        "tambourine"
    ],

    "Medical Equipment": [
        "stethoscope", "thermometer", "blood pressure monitor",
        "medical syringe", "surgical mask", "medical gloves",
        "wheelchair", "hospital bed", "crutches", "walking stick",
        "first aid kit", "bandage", "oxygen cylinder",
        "pulse oximeter", "IV stand", "medical scissors",
        "otoscope", "ECG machine", "defibrillator", "medical scale"
    ],

    "Construction Objects": [
        "hammer", "screwdriver", "wrench", "drill machine",
        "electric saw", "circular saw", "measuring tape",
        "spirit level", "ladder", "wheelbarrow", "cement bag",
        "brick", "concrete block", "wooden plank", "steel rod",
        "paint bucket", "paint roller", "safety helmet",
        "construction vest", "shovel", "spade", "pickaxe",
        "pliers", "bolt", "nut"
    ],

    "Plants and Gardening": [
        "potted plant", "flower pot", "rose", "sunflower",
        "tulip", "hibiscus", "orchid", "cactus", "bonsai tree",
        "fern", "bamboo plant", "palm tree", "banana plant",
        "mango tree", "coconut tree", "watering can",
        "garden hose", "garden shovel", "plant sprayer",
        "lawn mower"
    ],

    "Insects": [
        "butterfly", "honey bee", "house fly", "mosquito",
        "ant", "ladybug", "dragonfly", "grasshopper", "cricket",
        "cockroach", "spider", "scorpion", "caterpillar",
        "moth", "wasp", "termite", "beetle", "firefly",
        "praying mantis", "centipede"
    ],

    "Industrial and Workshop Objects": [
        "welding machine", "air compressor", "generator",
        "industrial fan", "water pump", "electric motor",
        "hydraulic jack", "toolbox", "vice clamp",
        "metal pipe", "industrial valve", "pressure gauge",
        "gas cylinder", "conveyor belt", "industrial robot"
    ]
}

# Combine all category prompts into one list
ALL_CLASSES = [
    item
    for category in OBJECT_CATEGORIES.values()
    for item in category
]

print("Total categories:", len(OBJECT_CATEGORIES))
print("Total prompts:", len(ALL_CLASSES))